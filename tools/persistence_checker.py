#!/usr/bin/env python3
"""Deterministic offline checker for the supervised ADW persistence boundary."""

import datetime as _datetime
import hashlib
import json
import math
import os
import re
import stat
import sys
from pathlib import Path, PurePosixPath


SCHEMA_VERSION = "adw.persistence-checker.case.v1"
REPORT_VERSION = "adw.persistence-checker.report.v1"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
UTC_SECOND = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
VALID_MODES = {"100644", "100755", "120000", "160000"}
RESULT_EXIT = {"PASS": 0, "FAIL": 1, "UNEVALUABLE": 2}


class InputError(Exception):
    """Required input is absent, malformed, ambiguous, or unreadable."""


class DuplicateKey(InputError):
    pass


class DirectoryConsistencyError(InputError):
    def __init__(self, reason, path=None, expected=None, observed=None):
        super().__init__(reason)
        self.path = path
        self.expected = expected
        self.observed = observed


def _object_no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKey("duplicate JSON key: %s" % key)
        result[key] = value
    return result


def _reject_json_constant(value):
    raise InputError("non-standard JSON constant is forbidden: %s" % value)


def _validate_unicode_scalars(value, label):
    if isinstance(value, float) and not math.isfinite(value):
        raise InputError("%s contains a non-finite JSON number" % label)
    if isinstance(value, str):
        if any(0xD800 <= ord(character) <= 0xDFFF for character in value):
            raise InputError("%s contains an unpaired UTF-16 surrogate" % label)
        return
    if isinstance(value, list):
        for item in value:
            _validate_unicode_scalars(item, label)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            _validate_unicode_scalars(key, label + " object key")
            _validate_unicode_scalars(item, label)


def _sanitize_unicode(value):
    if isinstance(value, str):
        if any(0xD800 <= ord(character) <= 0xDFFF for character in value):
            return "<invalid-unicode-scalar>"
        return value
    if isinstance(value, list):
        return [_sanitize_unicode(item) for item in value]
    if isinstance(value, dict):
        clean = {}
        invalid_key = 0
        for key, item in value.items():
            safe_key = _sanitize_unicode(key)
            if safe_key in clean:
                invalid_key += 1
                safe_key = "<invalid-object-key-%d>" % invalid_key
            clean[safe_key] = _sanitize_unicode(item)
        return clean
    return value


def _sanitize_nonfinite(value):
    if isinstance(value, float) and not math.isfinite(value):
        return "<invalid-non-finite-number>"
    if isinstance(value, list):
        return [_sanitize_nonfinite(item) for item in value]
    if isinstance(value, dict):
        return {key: _sanitize_nonfinite(item) for key, item in value.items()}
    return value


def _bounded_diagnostic(error):
    text = _sanitize_unicode(str(error))
    try:
        text.encode("utf-8", "strict")
    except UnicodeEncodeError:
        text = "unsafe diagnostic suppressed"
    return text[:500]


def _json_bytes(data, evidence, validate_scalars=True):
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise InputError("%s is not strict UTF-8: %s" % (evidence, exc))
    try:
        value = json.loads(
            text,
            object_pairs_hook=_object_no_duplicates,
            parse_constant=_reject_json_constant,
        )
    except DuplicateKey:
        raise
    except (json.JSONDecodeError, ValueError) as exc:
        raise InputError("%s is not valid JSON: %s" % (evidence, exc))
    if validate_scalars:
        _validate_unicode_scalars(value, evidence)
    return value


def byte_identity(data):
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return {
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "git_blob": hashlib.sha1(header + data).hexdigest(),
    }


def _is_exact_keys(value, keys):
    return isinstance(value, dict) and set(value) == set(keys)


def _is_str_list(value, nonempty=False):
    return (
        isinstance(value, list)
        and (not nonempty or bool(value))
        and all(isinstance(item, str) and item for item in value)
    )


def _safe_rel(value, label):
    if not isinstance(value, str) or not value:
        raise InputError("%s must be a non-empty relative POSIX path" % label)
    _validate_unicode_scalars(value, label)
    if "\\" in value or "\0" in value or value.startswith("/"):
        raise InputError("%s is not a canonical relative POSIX path" % label)
    path = PurePosixPath(value)
    if str(path) != value or any(part in ("", ".", "..") for part in path.parts):
        raise InputError("%s contains traversal or an unsafe alias" % label)
    return value


def _assert_no_symlink(path, label, require_directory=False):
    if not isinstance(path, str):
        raise InputError("%s must be a string path" % label)
    _validate_unicode_scalars(path, label)
    if "\0" in path or not os.path.isabs(path):
        raise InputError("%s must be an absolute canonical path" % label)
    root_form = os.path.abspath(os.sep)
    if path != root_form:
        parts = path.split(os.sep)
        if (
            path.endswith(os.sep)
            or any(part in ("", ".", "..") for part in parts[1:])
            or os.path.abspath(path) != path
            or os.path.normpath(path) != path
        ):
            raise InputError("%s must be an absolute canonical path" % label)
    path = Path(path)
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current = current / part
        try:
            info = os.lstat(str(current))
        except OSError as exc:
            raise InputError("%s is unavailable: %s" % (label, exc))
        if stat.S_ISLNK(info.st_mode):
            raise InputError("%s contains a symlink" % label)
    info = os.stat(str(path))
    if require_directory and not stat.S_ISDIR(info.st_mode):
        raise InputError("%s is not a directory" % label)
    return path


def _under(path, root):
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _read_regular(path, label):
    try:
        before = os.lstat(str(path))
        if stat.S_ISLNK(before.st_mode) or not stat.S_ISREG(before.st_mode):
            raise InputError("%s is not a regular non-symlink file" % label)
        flags = os.O_RDONLY
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        fd = os.open(str(path), flags)
        try:
            chunks = []
            while True:
                chunk = os.read(fd, 1024 * 1024)
                if not chunk:
                    break
                chunks.append(chunk)
            after = os.fstat(fd)
        finally:
            os.close(fd)
    except InputError:
        raise
    except OSError as exc:
        raise InputError("%s cannot be read: %s" % (label, exc))
    if (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
        raise InputError("%s changed identity while being read" % label)
    return b"".join(chunks), (after.st_dev, after.st_ino)


def _parse_time(value, label):
    if not isinstance(value, str) or not UTC_SECOND.match(value):
        raise InputError("%s must be UTC in YYYY-MM-DDTHH:MM:SSZ form" % label)
    try:
        return _datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=_datetime.timezone.utc
        )
    except ValueError as exc:
        raise InputError("%s is invalid: %s" % (label, exc))


def _git_tree(entries):
    root = {}
    for path, entry in entries.items():
        node = root
        parts = path.split("/")
        for part in parts[:-1]:
            existing = node.get(part)
            if existing is None:
                existing = {}
                node[part] = existing
            if not isinstance(existing, dict) or "mode" in existing:
                raise InputError("inventory has a file/directory path conflict at %s" % path)
            node = existing
        if parts[-1] in node:
            raise InputError("inventory path conflict at %s" % path)
        node[parts[-1]] = entry

    def digest(node):
        records = []
        for name, value in node.items():
            is_dir = isinstance(value, dict) and "mode" not in value
            order_key = (name + ("/" if is_dir else "")).encode("utf-8")
            if is_dir:
                mode = "40000"
                object_id = digest(value)
            else:
                mode = value["mode"]
                object_id = value["blob"]
            body = mode.encode("ascii") + b" " + name.encode("utf-8") + b"\0"
            body += bytes.fromhex(object_id)
            records.append((order_key, body))
        payload = b"".join(body for _, body in sorted(records, key=lambda item: item[0]))
        header = b"tree " + str(len(payload)).encode("ascii") + b"\0"
        return hashlib.sha1(header + payload).hexdigest()

    return digest(root)


class Checker:
    def __init__(self, case_path, case_bytes, case):
        self.case_path = Path(case_path)
        self.case_bytes = case_bytes
        self.case = case
        self.predicates = []
        self.files = {}
        self.file_inodes = {}
        self.roots = []
        self.base_entries = {}
        self.target_entries = {}
        self.base_inventory_valid = False
        self.target_inventory_valid = False
        self.actual_delta = None

    def record(self, predicate, result, reason, evidence, expected=None, observed=None):
        self.predicates.append(
            {
                "predicate": predicate,
                "result": result,
                "reason": reason,
                "evidence": evidence,
                "expected": expected,
                "observed": observed,
            }
        )

    def require(self, condition, predicate, reason, evidence, expected=None, observed=None,
                inability=False):
        self.record(
            predicate,
            "PASS" if condition else ("UNEVALUABLE" if inability else "FAIL"),
            "satisfied" if condition else reason,
            evidence,
            expected,
            observed,
        )

    def schema(self):
        top = {
            "schema_version", "task_reference", "phase", "verification_scope",
            "repository", "paths", "authority", "identities", "inventories",
            "allowed_delta", "byte_files", "register", "pending_external_gates",
        }
        if not _is_exact_keys(self.case, top):
            self.record("case.schema", "UNEVALUABLE", "top-level fields are missing or unknown",
                        "case-file", sorted(top), sorted(self.case) if isinstance(self.case, dict) else None)
            return False
        checks = [
            (self.case["schema_version"] == SCHEMA_VERSION, "schema_version"),
            (isinstance(self.case["task_reference"], str) and bool(self.case["task_reference"]), "task_reference"),
            (self.case["phase"] in ("preflight", "readback"), "phase"),
            (_is_str_list(self.case["verification_scope"], True), "verification_scope"),
            (_is_str_list(self.case["pending_external_gates"]), "pending_external_gates"),
            (_is_exact_keys(self.case["repository"], {"name", "ref"}), "repository"),
            (_is_exact_keys(self.case["paths"], {"read_roots", "report_root", "report_destination"}), "paths"),
            (_is_exact_keys(self.case["authority"], {
                "source", "branch_request_reference", "tree_request_reference",
                "caller_identity", "provenance_claims",
                "observation_time", "evaluation_time", "freshness_cutoff", "available",
                "branch_response_file", "tree_response_file", "live_ref_commit",
                "expected_protected", "expected_protection_enabled",
                "expected_status_check_enforcement",
            }), "authority"),
            (isinstance(self.case["identities"], dict), "identities"),
            (_is_exact_keys(self.case["inventories"], {"base", "target"}), "inventories"),
            (_is_exact_keys(self.case["allowed_delta"], {"additions", "deletions", "modifications"}), "allowed_delta"),
            (isinstance(self.case["byte_files"], list), "byte_files"),
            (_is_exact_keys(self.case["register"], {
                "path", "authorized_before_file", "observed_before_file",
                "authorized_after_file", "observed_after_file",
            }), "register"),
        ]
        bad = [name for ok, name in checks if not ok]
        if bad:
            self.record("case.schema", "UNEVALUABLE", "invalid required structures",
                        "case-file", "all required structures", bad)
            return False
        repo = self.case["repository"]
        paths = self.case["paths"]
        authority = self.case["authority"]
        identities = self.case["identities"]
        inventories = self.case["inventories"]
        allowed_delta = self.case["allowed_delta"]
        register = self.case["register"]
        phase = self.case["phase"]
        base_keys = {"expected_commit", "observed_commit", "expected_tree", "observed_tree"}
        if phase == "preflight":
            identity_shape_ok = (
                _is_exact_keys(identities, {"base", "working"})
                and _is_exact_keys(identities.get("base"), base_keys)
                and _is_exact_keys(identities.get("working"), {"expected_tree"})
            )
        elif phase == "readback":
            identity_shape_ok = (
                _is_exact_keys(identities, {"base", "candidate"})
                and _is_exact_keys(identities.get("base"), base_keys)
                and _is_exact_keys(identities.get("candidate"), {
                    "expected_commit", "observed_commit", "expected_parents", "observed_parents",
                    "expected_tree", "observed_tree",
                })
            )
        else:
            identity_shape_ok = False
        inventory_shape_ok = all(
            _is_exact_keys(inventories.get(name), {"complete", "truncated", "entries"})
            and type(inventories[name].get("complete")) is bool
            and type(inventories[name].get("truncated")) is bool
            and isinstance(inventories[name].get("entries"), list)
            for name in ("base", "target")
        )
        scalar_ok = (
            all(isinstance(repo[key], str) and repo[key] for key in ("name", "ref"))
            and repo["ref"].startswith("refs/heads/") and len(repo["ref"]) > len("refs/heads/")
            and _is_str_list(paths["read_roots"], True)
            and isinstance(paths["report_root"], str)
            and isinstance(paths["report_destination"], str)
            and all(isinstance(authority[key], str) and authority[key] for key in (
                "source", "branch_request_reference", "tree_request_reference", "caller_identity",
                "observation_time", "evaluation_time", "freshness_cutoff", "live_ref_commit",
                "expected_status_check_enforcement"))
            and _is_str_list(authority["provenance_claims"])
            and type(authority["available"]) is bool
            and all(authority[name] is None or isinstance(authority[name], str)
                    for name in ("branch_response_file", "tree_response_file"))
            and (authority["branch_response_file"] is None
                 or authority["tree_response_file"] is None
                 or authority["branch_response_file"] != authority["tree_response_file"])
            and type(authority["expected_protected"]) is bool
            and type(authority["expected_protection_enabled"]) is bool
            and identity_shape_ok
            and inventory_shape_ok
            and all(isinstance(allowed_delta[name], list)
                    for name in ("additions", "deletions", "modifications"))
            and all(isinstance(register[name], str) and register[name]
                    for name in ("path", "authorized_before_file", "observed_before_file",
                                 "authorized_after_file", "observed_after_file"))
        )
        if not scalar_ok:
            self.record("case.schema", "UNEVALUABLE", "invalid scalar field types",
                        "case-file", "strict v1 field types", None)
            return False
        self.record("case.schema", "PASS", "satisfied", "case-file", SCHEMA_VERSION,
                    self.case["schema_version"])
        return True

    def paths_and_files(self):
        try:
            root_paths = []
            for index, value in enumerate(self.case["paths"]["read_roots"]):
                root_paths.append(_assert_no_symlink(value, "read_roots[%d]" % index, True))
            for index, root in enumerate(root_paths):
                for other in root_paths[index + 1:]:
                    if root == other or _under(root, other) or _under(other, root):
                        raise InputError("read roots overlap or alias")
            case_matches = [root for root in root_paths if _under(self.case_path, root)]
            if len(case_matches) != 1:
                raise InputError("case file is not contained by exactly one read root")
            _assert_no_symlink(str(self.case_path), "case-file")
            self.roots = root_paths
            self.record("paths.read_boundary", "PASS", "satisfied", "case-file and read_roots")
        except (InputError, OSError) as exc:
            self.record("paths.read_boundary", "UNEVALUABLE", str(exc), "case-file and read_roots")
            return

        seen_ids = set()
        seen_spec_paths = set()
        for index, spec in enumerate(self.case["byte_files"]):
            evidence = "byte_files[%d]" % index
            keys = {"id", "root", "path", "governed_text", "expected_size", "expected_sha256",
                    "expected_git_blob", "bind_path"}
            if not _is_exact_keys(spec, keys):
                self.record("file.%d.schema" % index, "UNEVALUABLE", "missing or unknown file fields",
                            evidence, sorted(keys), sorted(spec) if isinstance(spec, dict) else None)
                continue
            valid = (
                isinstance(spec["id"], str) and bool(spec["id"])
                and type(spec["root"]) is int and 0 <= spec["root"] < len(self.roots)
                and type(spec["governed_text"]) is bool
                and type(spec["expected_size"]) is int and spec["expected_size"] >= 0
                and isinstance(spec["expected_sha256"], str) and bool(HEX64.match(spec["expected_sha256"]))
                and isinstance(spec["expected_git_blob"], str) and bool(HEX40.match(spec["expected_git_blob"]))
                and (spec["bind_path"] is None or isinstance(spec["bind_path"], str))
            )
            try:
                rel = _safe_rel(spec["path"], evidence + ".path")
                if spec["bind_path"] is not None:
                    _safe_rel(spec["bind_path"], evidence + ".bind_path")
            except InputError as exc:
                valid = False
                rel = None
                invalid_reason = str(exc)
            else:
                invalid_reason = "invalid field type or identity"
            if not valid:
                self.record("file.%d.schema" % index, "UNEVALUABLE", invalid_reason, evidence)
                continue
            key = (spec["root"], rel)
            if spec["id"] in seen_ids or key in seen_spec_paths:
                self.record("file.%d.unique" % index, "UNEVALUABLE", "duplicate id or designated path",
                            evidence, "unique", {"id": spec["id"], "path": list(key)})
                continue
            seen_ids.add(spec["id"])
            seen_spec_paths.add(key)
            full_path = self.roots[spec["root"]] / Path(*PurePosixPath(rel).parts)
            try:
                _assert_no_symlink(str(full_path), evidence)
                data, inode = _read_regular(full_path, evidence)
                if inode in self.file_inodes:
                    raise InputError("unsafe filesystem alias with %s" % self.file_inodes[inode])
                self.file_inodes[inode] = spec["id"]
                self.files[spec["id"]] = {"spec": spec, "bytes": data, "path": str(full_path)}
                identity = byte_identity(data)
                self.record("file.%s.read" % spec["id"], "PASS", "satisfied", evidence,
                            str(full_path), str(full_path))
                for field, predicate in (("bytes", "size"), ("sha256", "sha256"),
                                         ("git_blob", "git_blob")):
                    expected_field = "expected_size" if field == "bytes" else "expected_" + field
                    self.require(identity[field] == spec[expected_field],
                                 "file.%s.%s" % (spec["id"], predicate),
                                 "byte identity mismatch", evidence, spec[expected_field], identity[field])
                if spec["governed_text"]:
                    checks = {
                        "utf8": self._strict_utf8(data),
                        "bom": not data.startswith(b"\xef\xbb\xbf"),
                        "cr": b"\r" not in data,
                        "one_final_lf": data.endswith(b"\n") and not data.endswith(b"\n\n"),
                    }
                    reasons = {
                        "utf8": "not strict UTF-8", "bom": "UTF-8 BOM present",
                        "cr": "CR byte present", "one_final_lf": "not exactly one final LF",
                    }
                    for name in ("utf8", "bom", "cr", "one_final_lf"):
                        self.require(checks[name], "file.%s.text.%s" % (spec["id"], name),
                                     reasons[name], evidence, True, checks[name])
            except InputError as exc:
                self.record("file.%s.read" % spec["id"], "UNEVALUABLE", str(exc), evidence)

    @staticmethod
    def _strict_utf8(data):
        try:
            data.decode("utf-8", "strict")
            return True
        except UnicodeDecodeError:
            return False

    def identities_and_time(self):
        ids = self.case["identities"]
        base = ids["base"]
        phase = self.case["phase"]
        base_values = [base[name] for name in (
            "expected_commit", "observed_commit", "expected_tree", "observed_tree")]
        format_values = list(base_values)
        if phase == "preflight":
            format_values.append(ids["working"]["expected_tree"])
            parents_ok = True
        else:
            candidate = ids["candidate"]
            format_values.extend(candidate[name] for name in (
                "expected_commit", "observed_commit", "expected_tree", "observed_tree"))
            parents_ok = (
                _is_str_list(candidate["expected_parents"], True)
                and _is_str_list(candidate["observed_parents"], True)
                and all(isinstance(value, str) and HEX40.match(value)
                        for value in candidate["expected_parents"] + candidate["observed_parents"])
            )
        formats_ok = all(isinstance(value, str) and bool(HEX40.match(value))
                         for value in format_values)
        if not formats_ok or not parents_ok:
            self.record("identity.format", "UNEVALUABLE", "malformed commit/tree/parent identity",
                        "identities", "complete lowercase 40-hex", ids)
        else:
            self.record("identity.format", "PASS", "satisfied", "identities")
            for name in ("commit", "tree"):
                self.require(base["expected_" + name] == base["observed_" + name],
                             "identity.base.%s" % name, "base identity mismatch", "identities.base",
                             base["expected_" + name], base["observed_" + name])
            if phase == "preflight":
                self.record("identity.working.no_publication_identity", "PASS",
                            "preflight represents W without C commit, parent, or ref identity",
                            "identities.working", "tree identity only", ids["working"])
            else:
                candidate = ids["candidate"]
                for name in ("commit", "tree"):
                    self.require(candidate["expected_" + name] == candidate["observed_" + name],
                                 "identity.candidate.%s" % name, "published candidate identity mismatch",
                                 "identities.candidate", candidate["expected_" + name],
                                 candidate["observed_" + name])
                self.require(candidate["expected_parents"] == [base["expected_commit"]],
                             "identity.candidate.expected_parent",
                             "published C does not have sole expected parent B",
                             "identities.candidate", [base["expected_commit"]],
                             candidate["expected_parents"])
                self.require(candidate["observed_parents"] == candidate["expected_parents"],
                             "identity.candidate.observed_parents", "ordered parent identity mismatch",
                             "identities.candidate", candidate["expected_parents"],
                             candidate["observed_parents"])
        auth = self.case["authority"]
        try:
            observed = _parse_time(auth["observation_time"], "authority.observation_time")
            evaluated = _parse_time(auth["evaluation_time"], "authority.evaluation_time")
            cutoff = _parse_time(auth["freshness_cutoff"], "authority.freshness_cutoff")
            self.require(cutoff <= observed <= evaluated, "authority.freshness",
                         "observation is stale or after evaluation instant", "authority",
                         "freshness_cutoff <= observation_time <= evaluation_time",
                         {"freshness_cutoff": auth["freshness_cutoff"],
                          "observation_time": auth["observation_time"],
                          "evaluation_time": auth["evaluation_time"]}, inability=True)
        except InputError as exc:
            self.record("authority.time_format", "UNEVALUABLE", str(exc), "authority")
        self.require(auth["available"], "authority.available", "required live verification is unavailable",
                     "authority.available", True, auth["available"], inability=True)

    def _inventory(self, name):
        value = self.case["inventories"][name]
        evidence = "inventories.%s" % name
        if not _is_exact_keys(value, {"complete", "truncated", "entries"}):
            self.record("inventory.%s.schema" % name, "UNEVALUABLE",
                        "missing or unknown inventory fields", evidence)
            return None
        if type(value["complete"]) is not bool or type(value["truncated"]) is not bool or not isinstance(value["entries"], list):
            self.record("inventory.%s.schema" % name, "UNEVALUABLE", "invalid inventory field types", evidence)
            return None
        self.require(value["complete"] and not value["truncated"], "inventory.%s.complete" % name,
                     "inventory is incomplete or truncated", evidence, {"complete": True, "truncated": False},
                     {"complete": value["complete"], "truncated": value["truncated"]}, inability=True)
        if not value["complete"] or value["truncated"]:
            return None
        entries = {}
        bad = False
        for index, entry in enumerate(value["entries"]):
            if not _is_exact_keys(entry, {"path", "mode", "blob"}):
                bad = True
                continue
            try:
                path = _safe_rel(entry["path"], "%s.entries[%d].path" % (evidence, index))
            except InputError:
                bad = True
                continue
            if path in entries or entry["mode"] not in VALID_MODES or not isinstance(entry["blob"], str) or not HEX40.match(entry["blob"]):
                bad = True
                continue
            entries[path] = {"mode": entry["mode"], "blob": entry["blob"]}
        if bad or len(entries) != len(value["entries"]):
            self.record("inventory.%s.entries" % name, "UNEVALUABLE",
                        "duplicate, unsafe, malformed, or incomplete entries", evidence)
            return None
        else:
            self.record("inventory.%s.entries" % name, "PASS", "satisfied", evidence,
                        len(value["entries"]), len(entries))
        return entries

    def inventories_and_delta(self):
        base_entries = self._inventory("base")
        target_entries = self._inventory("target")
        self.base_inventory_valid = base_entries is not None
        self.target_inventory_valid = target_entries is not None
        self.base_entries = base_entries if base_entries is not None else {}
        self.target_entries = target_entries if target_entries is not None else {}
        if base_entries is None or target_entries is None:
            return
        ids = self.case["identities"]
        try:
            base_tree = _git_tree(self.base_entries)
            target_tree = _git_tree(self.target_entries)
            self.require(base_tree == ids["base"]["observed_tree"],
                         "inventory.base.tree_binding",
                         "base leaf inventory conflicts with observed tree",
                         "inventories.base+identities.base.observed_tree",
                         ids["base"]["observed_tree"], base_tree, inability=True)
            if self.case["phase"] == "preflight":
                self.require(target_tree == ids["working"]["expected_tree"],
                             "inventory.working.tree_binding",
                             "computed W tree differs from the intended working tree",
                             "inventories.target+identities.working",
                             ids["working"]["expected_tree"], target_tree)
            else:
                self.require(target_tree == ids["candidate"]["observed_tree"],
                             "inventory.candidate.tree_binding",
                             "target inventory conflicts with observed candidate tree",
                             "inventories.target+identities.candidate.observed_tree",
                             ids["candidate"]["observed_tree"], target_tree, inability=True)
        except (InputError, KeyError, TypeError) as exc:
            self.record("inventory.tree_binding", "UNEVALUABLE", str(exc), "inventories")
        actual = {
            "additions": sorted(set(self.target_entries) - set(self.base_entries)),
            "deletions": sorted(set(self.base_entries) - set(self.target_entries)),
            "modifications": sorted(
                path for path in set(self.base_entries) & set(self.target_entries)
                if self.base_entries[path] != self.target_entries[path]
            ),
        }
        self.actual_delta = actual
        expected = {}
        delta_ok = True
        for name in ("additions", "deletions", "modifications"):
            values = self.case["allowed_delta"][name]
            try:
                if not isinstance(values, list):
                    raise InputError("delta list required")
                checked = [_safe_rel(value, "allowed_delta.%s" % name) for value in values]
                if len(set(checked)) != len(checked) or checked != sorted(checked):
                    raise InputError("delta paths must be unique and sorted")
                expected[name] = checked
            except InputError as exc:
                delta_ok = False
                self.record("delta.%s.schema" % name, "UNEVALUABLE", str(exc), "allowed_delta.%s" % name)
        if delta_ok:
            for name in ("additions", "deletions", "modifications"):
                self.require(actual[name] == expected[name], "delta.%s" % name,
                             "complete inventory delta differs from authorization", "inventories+allowed_delta",
                             expected[name], actual[name])
            unchanged = sorted(set(self.base_entries) & set(self.target_entries) - set(actual["modifications"]))
            self.require(all(self.base_entries[p] == self.target_entries[p] for p in unchanged),
                         "delta.unchanged_entries", "an unchanged entry differs", "inventories",
                         "identical mode/blob for every unchanged path", unchanged)

    def file_bindings_and_register(self):
        changed = set(self.case["allowed_delta"].get("additions", [])) | set(
            self.case["allowed_delta"].get("modifications", []))
        bindings = {}
        for file_id, item in self.files.items():
            bind = item["spec"]["bind_path"]
            if bind is not None:
                if bind in bindings:
                    self.record("binding.%s.unique" % bind, "UNEVALUABLE",
                                "multiple byte files bind one repository path", "byte_files")
                else:
                    bindings[bind] = file_id
                    target = self.target_entries.get(bind)
                    if target is None:
                        self.record("binding.%s.target" % bind, "UNEVALUABLE",
                                    "bound path is absent from target inventory", "byte_files+inventories.target")
                    else:
                        actual_blob = byte_identity(item["bytes"])["git_blob"]
                        self.require(actual_blob == target["blob"], "binding.%s.blob" % bind,
                                     "bound bytes do not match target blob", "byte_files+inventories.target",
                                     target["blob"], actual_blob)
        self.require(set(bindings) == changed, "binding.complete", "changed-path byte bindings are incomplete or extra",
                     "byte_files+allowed_delta", sorted(changed), sorted(bindings), inability=True)
        reg = self.case["register"]
        try:
            reg_path = _safe_rel(reg["path"], "register.path")
            ids = [reg[name] for name in ("authorized_before_file", "observed_before_file",
                                          "authorized_after_file", "observed_after_file")]
            if not all(isinstance(file_id, str) and file_id in self.files for file_id in ids):
                raise InputError("Register references an unavailable byte file")
            before_auth, before_observed, after_auth, after_observed = [self.files[file_id]["bytes"] for file_id in ids]
            self.require(before_auth == before_observed, "register.before_exact",
                         "authorized and observed Register-before bytes differ", "register+byte_files",
                         byte_identity(before_auth), byte_identity(before_observed))
            self.require(after_auth == after_observed, "register.after_exact",
                         "authorized and observed Register-after bytes differ", "register+byte_files",
                         byte_identity(after_auth), byte_identity(after_observed))
            self.require(reg_path in self.case["allowed_delta"]["modifications"], "register.delta",
                         "Register is not exactly an authorized modification", "register+allowed_delta",
                         "authorized modification", reg_path)
            if self.base_inventory_valid:
                base_register = self.base_entries.get(reg_path)
                self.require(base_register is not None,
                             "register.base_inventory_membership",
                             "Register path is absent from the complete base inventory",
                             "register+inventories.base", "present", reg_path in self.base_entries)
                self.require(
                    base_register is not None
                    and byte_identity(before_observed)["git_blob"] == base_register["blob"],
                    "register.before_blob",
                    "Register-before bytes do not bind the base inventory entry",
                    "register+inventories.base",
                    base_register["blob"] if base_register is not None else "Register base entry",
                    byte_identity(before_observed)["git_blob"],
                )
            else:
                self.record("register.base_inventory_membership", "UNEVALUABLE",
                            "base inventory is invalid or unavailable",
                            "register+inventories.base", "present", None)
                self.record("register.before_blob", "UNEVALUABLE",
                            "base inventory is invalid or unavailable",
                            "register+inventories.base", "Register base blob", None)
            if self.target_inventory_valid:
                target_register = self.target_entries.get(reg_path)
                self.require(target_register is not None,
                             "register.target_inventory_membership",
                             "Register path is absent from the complete target inventory",
                             "register+inventories.target", "present", reg_path in self.target_entries)
                self.require(
                    target_register is not None
                    and byte_identity(after_observed)["git_blob"] == target_register["blob"],
                    "register.after_blob",
                    "Register-after bytes do not bind the target inventory entry",
                    "register+inventories.target",
                    target_register["blob"] if target_register is not None else "Register target entry",
                    byte_identity(after_observed)["git_blob"],
                )
                self.require(bindings.get(reg_path) == reg["observed_after_file"], "register.after_binding",
                             "target Register binding is not the observed after file", "register+byte_files",
                             reg["observed_after_file"], bindings.get(reg_path), inability=True)
            else:
                self.record("register.target_inventory_membership", "UNEVALUABLE",
                            "target inventory is invalid or unavailable",
                            "register+inventories.target", "present", None)
                self.record("register.after_blob", "UNEVALUABLE",
                            "target inventory is invalid or unavailable",
                            "register+inventories.target", "Register target blob", None)
            if self.actual_delta is None:
                self.record("register.delta_classification", "UNEVALUABLE",
                            "complete inventory delta is unavailable",
                            "register+inventories+allowed_delta",
                            "modification", None)
            else:
                classifications = [
                    name for name in ("additions", "deletions", "modifications")
                    if reg_path in self.actual_delta[name]
                ]
                self.require(classifications == ["modifications"],
                             "register.delta_classification",
                             "computed delta does not classify the Register as a modification",
                             "register+inventories+allowed_delta",
                             ["modifications"], classifications)
        except (InputError, KeyError, TypeError) as exc:
            self.record("register.schema", "UNEVALUABLE", str(exc), "register")

    def observation(self):
        auth = self.case["authority"]
        if not auth["available"]:
            return
        branch_id = auth["branch_response_file"]
        tree_id = auth["tree_response_file"]
        if not all(isinstance(file_id, str) and file_id in self.files
                   for file_id in (branch_id, tree_id)):
            self.record("authority.raw_response_files", "UNEVALUABLE",
                        "required raw branch or recursive-tree response is unavailable",
                        "authority.branch_response_file+authority.tree_response_file")
            return
        try:
            branch = _json_bytes(self.files[branch_id]["bytes"], "raw GitHub branch response")
            tree = _json_bytes(self.files[tree_id]["bytes"], "raw GitHub recursive-tree response")
            branch_values = self._raw_branch(branch)
            tree_sha, payload_entries, directory_evidence, empty_directories = self._raw_tree(tree)
            self.record("authority.raw_branch_schema", "PASS", "required GitHub REST fields parsed",
                        "raw branch response", None, byte_identity(self.files[branch_id]["bytes"]))
            self.record("authority.raw_tree_schema", "PASS", "required GitHub REST fields parsed",
                        "raw recursive-tree response", None, byte_identity(self.files[tree_id]["bytes"]))
            self.record("authority.raw_tree.directory_consistency", "PASS",
                        "every supplied directory and the reconstructed root match canonical Git tree hashes",
                        "raw recursive-tree response", "all directory SHAs consistent",
                        directory_evidence)
            self.require(not empty_directories,
                         "authority.raw_tree.empty_directories_unrepresentable",
                         "explicit empty Git-tree entries cannot be represented by the v1 leaf inventory",
                         "raw recursive-tree response",
                         [], empty_directories, inability=True)
            expected_branch_name = self.case["repository"]["ref"].removeprefix("refs/heads/")
            self.require(branch_values["name"] == expected_branch_name,
                         "authority.ref_consistency", "raw branch name conflicts with governed ref",
                         "raw branch response+case", expected_branch_name, branch_values["name"], inability=True)
            self.require(branch_values["commit"] == auth["live_ref_commit"],
                         "authority.live_ref_consistency", "raw branch response conflicts with declared live ref commit",
                         "raw branch response+authority", auth["live_ref_commit"],
                         branch_values["commit"], inability=True)
            self.require(branch_values["tree"] == tree_sha,
                         "authority.branch_tree_consistency",
                         "branch commit tree conflicts with recursive-tree response",
                         "raw branch response+raw recursive-tree response",
                         branch_values["tree"], tree_sha, inability=True)
            self.require(branch_values["protected"] == auth["expected_protected"],
                         "authority.branch_protected", "branch protection flag mismatch",
                         "raw branch response+authority", auth["expected_protected"],
                         branch_values["protected"])
            self.require(branch_values["protection_enabled"] == auth["expected_protection_enabled"],
                         "authority.protection_enabled", "protection enabled flag mismatch",
                         "raw branch response+authority", auth["expected_protection_enabled"],
                         branch_values["protection_enabled"])
            self.require(branch_values["status_check_enforcement"] == auth["expected_status_check_enforcement"],
                         "authority.status_check_enforcement", "status-check enforcement mismatch",
                         "raw branch response+authority", auth["expected_status_check_enforcement"],
                         branch_values["status_check_enforcement"])
            phase = self.case["phase"]
            ids = self.case["identities"]
            if phase == "preflight":
                expected_ref = ids["base"]["expected_commit"]
                observed_commit = ids["base"]["observed_commit"]
                observed_tree = ids["base"]["observed_tree"]
                observed_parents = None
                selected_entries = self.base_entries
            else:
                expected_ref = ids["candidate"]["expected_commit"]
                observed_commit = ids["candidate"]["observed_commit"]
                observed_tree = ids["candidate"]["observed_tree"]
                observed_parents = ids["candidate"]["observed_parents"]
                selected_entries = self.target_entries
            self.require(auth["live_ref_commit"] == expected_ref, "authority.phase_ref",
                         "%s ref does not equal required identity" % phase, "authority+identities",
                         expected_ref, auth["live_ref_commit"])
            self.require(branch_values["commit"] == observed_commit, "authority.commit_consistency",
                         "raw branch response conflicts with declared observed commit",
                         "raw branch response+identities", observed_commit,
                         branch_values["commit"], inability=True)
            self.require(tree_sha == observed_tree, "authority.tree_consistency",
                         "raw tree response conflicts with declared observed tree",
                         "raw recursive-tree response+identities", observed_tree, tree_sha, inability=True)
            if observed_parents is not None:
                self.require(branch_values["parents"] == observed_parents, "authority.parents_consistency",
                             "raw branch response conflicts with declared ordered parents",
                             "raw branch response+identities", observed_parents,
                             branch_values["parents"], inability=True)
            self.require(payload_entries == selected_entries, "authority.inventory_consistency",
                         "raw tree response conflicts with selected complete inventory",
                         "raw recursive-tree response+inventories",
                         selected_entries, payload_entries, inability=True)
        except DirectoryConsistencyError as exc:
            self.record("authority.raw_tree.directory_consistency", "UNEVALUABLE", str(exc),
                        "raw recursive-tree response",
                        {"path": exc.path, "sha": exc.expected},
                        {"path": exc.path, "sha": exc.observed})
        except InputError as exc:
            self.record("authority.raw_response_schema", "UNEVALUABLE", str(exc),
                        "raw branch/tree responses")

    @staticmethod
    def _raw_branch(payload):
        if not isinstance(payload, dict):
            raise InputError("raw branch response must be an object")
        name = payload.get("name")
        commit = payload.get("commit")
        protected = payload.get("protected")
        protection = payload.get("protection")
        if not isinstance(name, str) or not isinstance(commit, dict):
            raise InputError("raw branch response lacks name or commit object")
        if type(protected) is not bool or not isinstance(protection, dict):
            raise InputError("raw branch response lacks protection fields")
        commit_sha = commit.get("sha")
        inner = commit.get("commit")
        parents = commit.get("parents")
        if not isinstance(commit_sha, str) or not HEX40.match(commit_sha):
            raise InputError("raw branch commit sha is malformed")
        if not isinstance(inner, dict) or not isinstance(inner.get("tree"), dict):
            raise InputError("raw branch commit tree is missing")
        tree_sha = inner["tree"].get("sha")
        if not isinstance(tree_sha, str) or not HEX40.match(tree_sha):
            raise InputError("raw branch tree sha is malformed")
        if not isinstance(parents, list):
            raise InputError("raw branch ordered parents are missing")
        parent_shas = []
        for parent in parents:
            if not isinstance(parent, dict) or not isinstance(parent.get("sha"), str) or not HEX40.match(parent["sha"]):
                raise InputError("raw branch parent sha is malformed")
            parent_shas.append(parent["sha"])
        enabled = protection.get("enabled")
        checks = protection.get("required_status_checks")
        if type(enabled) is not bool or not isinstance(checks, dict):
            raise InputError("raw branch protection details are incomplete")
        enforcement = checks.get("enforcement_level")
        if not isinstance(enforcement, str) or not enforcement:
            raise InputError("raw branch status-check enforcement is missing")
        return {
            "name": name, "commit": commit_sha, "tree": tree_sha, "parents": parent_shas,
            "protected": protected, "protection_enabled": enabled,
            "status_check_enforcement": enforcement,
        }

    @staticmethod
    def _raw_tree(payload):
        if not isinstance(payload, dict):
            raise InputError("raw recursive-tree response must be an object")
        tree_sha = payload.get("sha")
        entries = payload.get("tree")
        truncated = payload.get("truncated")
        if not isinstance(tree_sha, str) or not HEX40.match(tree_sha):
            raise InputError("raw recursive-tree sha is malformed")
        if not isinstance(entries, list):
            raise InputError("raw recursive-tree entries are missing")
        if type(truncated) is not bool:
            raise InputError("raw recursive-tree truncated flag is missing")
        if truncated:
            raise InputError("raw recursive-tree response is truncated")
        result = {}
        directories = {}
        seen_paths = set()
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                raise InputError("raw recursive-tree entry %d is malformed" % index)
            path = _safe_rel(entry.get("path"), "raw recursive-tree entry path")
            mode = entry.get("mode")
            entry_type = entry.get("type")
            object_id = entry.get("sha")
            if path in seen_paths:
                raise DirectoryConsistencyError("raw recursive-tree path is duplicated", path)
            seen_paths.add(path)
            if not isinstance(object_id, str) or not HEX40.match(object_id):
                raise InputError("raw recursive-tree object sha is malformed")
            if entry_type == "tree":
                if mode != "040000":
                    raise InputError("raw recursive-tree directory mode is malformed")
                directories[path] = object_id
                continue
            if entry_type not in ("blob", "commit") or mode not in VALID_MODES:
                raise InputError("raw recursive-tree leaf type or mode is malformed")
            if (entry_type == "commit") != (mode == "160000"):
                raise InputError("raw recursive-tree leaf type conflicts with mode")
            result[path] = {"mode": mode, "blob": object_id}

        implied = set()
        for path in list(result) + list(directories):
            parts = path.split("/")
            for depth in range(1, len(parts)):
                implied.add("/".join(parts[:depth]))
        missing = sorted(implied - set(directories))
        if missing:
            raise DirectoryConsistencyError("raw recursive-tree directory evidence is missing",
                                            missing[0])
        conflicts = sorted(set(result) & implied)
        if conflicts:
            raise DirectoryConsistencyError("raw recursive-tree file/directory evidence conflicts",
                                            conflicts[0])

        computed = {}

        def parent(path):
            return path.rpartition("/")[0]

        def basename(path):
            return path.rpartition("/")[2]

        def compute(directory):
            records = []
            child_directories = sorted(
                path for path in directories if parent(path) == directory
            )
            child_leaves = sorted(path for path in result if parent(path) == directory)
            for child in child_directories:
                child_sha = compute(child)
                name = basename(child)
                body = b"40000 " + name.encode("utf-8") + b"\0" + bytes.fromhex(child_sha)
                records.append(((name + "/").encode("utf-8"), body))
            for child in child_leaves:
                name = basename(child)
                leaf = result[child]
                body = leaf["mode"].encode("ascii") + b" " + name.encode("utf-8") + b"\0"
                body += bytes.fromhex(leaf["blob"])
                records.append((name.encode("utf-8"), body))
            content = b"".join(body for _, body in sorted(records, key=lambda item: item[0]))
            framed = b"tree " + str(len(content)).encode("ascii") + b"\0" + content
            actual = hashlib.sha1(framed).hexdigest()
            computed[directory or "<root>"] = actual
            if directory and directories[directory] != actual:
                raise DirectoryConsistencyError("supplied directory SHA conflicts with descendants",
                                                directory, directories[directory], actual)
            return actual

        root_sha = compute("")
        if root_sha != tree_sha:
            raise DirectoryConsistencyError("top-level tree SHA conflicts with reconstructed entries",
                                            "<root>", tree_sha, root_sha)
        occupied_directories = set()
        for path in list(result) + list(directories):
            current = parent(path)
            while current:
                occupied_directories.add(current)
                current = parent(current)
        empty_directories = sorted(set(directories) - occupied_directories)
        return tree_sha, result, computed, empty_directories

    def overall(self):
        results = [item["result"] for item in self.predicates]
        if "UNEVALUABLE" in results:
            return "UNEVALUABLE"
        if "FAIL" in results:
            return "FAIL"
        return "PASS"

    def report(self):
        try:
            checker_bytes = Path(__file__).read_bytes()
            checker_identity = byte_identity(checker_bytes)
        except OSError as exc:
            checker_identity = {"error": str(exc)}
            self.record("checker.identity", "UNEVALUABLE", str(exc), "checker source")
        authority = self.case.get("authority")
        if not isinstance(authority, dict):
            authority = {}
        return {
            "report_version": REPORT_VERSION,
            "overall_result": self.overall(),
            "checker_identity": checker_identity,
            "runtime_identity": {
                "implementation": sys.implementation.name,
                "version": ".".join(str(part) for part in sys.version_info[:3]),
            },
            "input_identity": byte_identity(self.case_bytes),
            "task_reference": self.case.get("task_reference"),
            "phase": self.case.get("phase"),
            "phase_identity_model": (
                "B plus working candidate W tree/inventory; no publication identity C"
                if self.case.get("phase") == "preflight"
                else "B plus exact published candidate C commit/sole-parent/tree/ref"
                if self.case.get("phase") == "readback" else None
            ),
            "verification_scope": self.case.get("verification_scope"),
            "caller_provenance_claims": {
                "source": authority.get("source"),
                "branch_request_reference": authority.get("branch_request_reference"),
                "tree_request_reference": authority.get("tree_request_reference"),
                "caller_identity": authority.get("caller_identity"),
                "claims": authority.get("provenance_claims"),
            },
            "freshness": {
                "observation_time": authority.get("observation_time"),
                "evaluation_time": authority.get("evaluation_time"),
                "freshness_cutoff": authority.get("freshness_cutoff"),
                "limitations": [
                    "Caller-exported snapshots are not authenticated by this checker.",
                    "No supplied snapshot proves current live GitHub state or later ref stability.",
                    "The evaluation instant is caller-supplied; the checker does not consult a clock.",
                ],
            },
            "predicates": self.predicates,
            "pending_external_gates": self.case.get("pending_external_gates"),
            "non_authority": [
                "No provenance authentication, writer-exclusivity, permission, review, acceptance, push authorization, or operational readiness is established.",
                "Filesystem containment checks cannot eliminate check/use races against concurrent mutation.",
            ],
        }


def _load_case(case_path):
    path = _assert_no_symlink(case_path, "case-file")
    data, _ = _read_regular(path, "case-file")
    case = _json_bytes(data, "case-file", validate_scalars=False)
    if not isinstance(case, dict):
        raise InputError("case-file top level must be an object")
    value_error = None
    try:
        _validate_unicode_scalars(case, "case-file")
    except InputError as exc:
        value_error = exc
    return path, data, case, value_error


def _report_target(case):
    paths = case.get("paths")
    if not _is_exact_keys(paths, {"read_roots", "report_root", "report_destination"}):
        raise InputError("report destination cannot be determined from malformed paths")
    if not isinstance(paths["report_root"], str) or not isinstance(paths["report_destination"], str):
        raise InputError("report root and destination must be strings")
    root = _assert_no_symlink(paths["report_root"], "report_root", True)
    relative = _safe_rel(paths["report_destination"], "report_destination")
    target = root / Path(*PurePosixPath(relative).parts)
    if not _under(target, root):
        raise InputError("report destination is outside report_root")
    parent = _assert_no_symlink(str(target.parent), "report destination parent", True)
    if not _under(parent, root):
        raise InputError("report destination parent escapes report_root")
    try:
        os.lstat(str(target))
    except FileNotFoundError:
        return target
    except OSError as exc:
        raise InputError("report destination cannot be inspected: %s" % exc)
    raise InputError("report destination already exists")


def _exclusive_write(target, data):
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    fd = os.open(str(target), flags, 0o600)
    try:
        offset = 0
        while offset < len(data):
            written = os.write(fd, data[offset:])
            if written <= 0:
                raise OSError("short report write")
            offset += written
        os.fsync(fd)
    finally:
        os.close(fd)


def execute(case_path):
    """Evaluate one case and exclusively write its report.

    Returns (exit_code, report_or_none, report_written, diagnostic).
    """
    try:
        path, case_bytes, case, value_error = _load_case(case_path)
    except Exception as exc:
        return 2, None, False, _bounded_diagnostic(exc)
    checker = Checker(path, case_bytes, case)
    try:
        if value_error is not None:
            checker.record("case.json_values", "UNEVALUABLE", str(value_error), "case-file")
        elif checker.schema():
            checker.paths_and_files()
            checker.identities_and_time()
            checker.inventories_and_delta()
            checker.file_bindings_and_register()
            checker.observation()
    except Exception as exc:
        checker.record("input.fail_closed", "UNEVALUABLE",
                       "malformed or unreadable input: %s: %s" %
                       (type(exc).__name__, _bounded_diagnostic(exc)),
                       "case and designated inputs")
    try:
        target = _report_target(case)
        checker.record("report.destination", "PASS", "satisfied", "paths",
                       "new file inside report_root", str(target))
    except Exception as exc:
        diagnostic = _bounded_diagnostic(exc)
        checker.record("report.destination", "UNEVALUABLE", diagnostic, "paths")
        report = checker.report()
        return 2, report, False, diagnostic
    report = _sanitize_unicode(checker.report())
    try:
        report_bytes = (json.dumps(report, sort_keys=True, indent=2, ensure_ascii=False,
                                   allow_nan=False) + "\n").encode(
            "utf-8", "strict")
    except (UnicodeEncodeError, TypeError, ValueError) as exc:
        checker.record("report.serialization", "UNEVALUABLE",
                       "report serialization failed safely", "report")
        report = _sanitize_nonfinite(_sanitize_unicode(checker.report()))
        try:
            report_bytes = (json.dumps(report, sort_keys=True, indent=2, ensure_ascii=True,
                                       allow_nan=False) + "\n").encode(
                "ascii", "strict")
        except (UnicodeEncodeError, TypeError, ValueError):
            return 2, report, False, "report serialization failed safely"
    try:
        _exclusive_write(target, report_bytes)
    except OSError as exc:
        report["overall_result"] = "UNEVALUABLE"
        report["predicates"].append({
            "predicate": "report.write", "result": "UNEVALUABLE",
            "reason": "report creation failed: %s" % exc, "evidence": "report destination",
            "expected": "exclusive complete write", "observed": "I/O failure",
        })
        return 2, report, False, "report creation failed: %s" % _bounded_diagnostic(exc)
    return RESULT_EXIT[report["overall_result"]], report, True, None


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print("usage: persistence_checker.py /absolute/path/to/case.json", file=sys.stderr)
        return 2
    code, report, written, diagnostic = execute(argv[0])
    if written:
        print(report["overall_result"])
    else:
        print("UNEVALUABLE: %s" % (diagnostic or "report was not created"), file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())

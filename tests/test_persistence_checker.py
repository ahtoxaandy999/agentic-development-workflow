"""Focused synthetic tests for persistence_checker.py (standard library only)."""

import copy
import hashlib
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


CHECKER_PATH = Path(__file__).resolve().parents[1] / "tools" / "persistence_checker.py"
SPEC = importlib.util.spec_from_file_location("persistence_checker_under_test", str(CHECKER_PATH))
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


BASE_COMMIT = "a" * 40
SUBJECT_COMMIT = "b" * 40
BASE_PARENT = "9" * 40
STABLE = b"stable\n"
REGISTER_BEFORE = b"next_gate: old\n"
REGISTER_AFTER = b"next_gate: new\n"
ARTIFACT = b"candidate\n"

# Independent native-oracle constants (wc, shasum -a 256, git hash-object --stdin).
KNOWN = {
    "stable": (7, "2b92ea252be0fbc26f70317cdaa7b6411ea634b50d55338cd8c495e4dbf25d1d",
               "2bf5ad0447d3370461c6f32a0a5bc8a3177376aa"),
    "register_before": (15, "90e03ae727e172844bbc535e6ac146447674b059d7e1f84307437c82a04c48be",
                        "f14b35af4d415c9c352a0a8b94f9fe1e8c17f244"),
    "register_after": (15, "1d93b1899942a4db39e31b9348528c64fec49eedecdd3d12cd1b9e50de1fd714",
                       "d586d7ef3bbce42505cc55a592002d51e2759d02"),
    "artifact": (10, "1e81270f1a47dce22a2e4985250c74b2e3374443734f1492b03ea2cd2af4ec48",
                 "02e8acdcc44da4d68465994d590e44bcab3296b2"),
}


def oracle_identity(data):
    """Separately coded test oracle; it does not call checker helpers."""
    size = len(data)
    sha256 = hashlib.new("sha256", data).hexdigest()
    framed = b"blob " + ("%d" % size).encode("ascii") + bytes([0]) + data
    git_blob = hashlib.new("sha1", framed).hexdigest()
    return size, sha256, git_blob


def oracle_tree_details(entry_list, empty_directories=()):
    """Independent recursive Git-tree oracle returning root and directory SHAs."""
    root = {}
    for entry in entry_list:
        node = root
        parts = entry["path"].split("/")
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = (entry["mode"], entry["blob"])
    for directory in empty_directories:
        node = root
        for part in directory.split("/"):
            node = node.setdefault(part, {})

    directories = {}

    def tree_id(node, prefix=""):
        pieces = []
        for name, value in node.items():
            if isinstance(value, dict):
                child_path = prefix + "/" + name if prefix else name
                mode, object_id, key = "40000", tree_id(value, child_path), name + "/"
            else:
                mode, object_id, key = value[0], value[1], name
            record = mode.encode("ascii") + b" " + name.encode("utf-8") + bytes([0])
            record += bytes.fromhex(object_id)
            pieces.append((key.encode("utf-8"), record))
        payload = b"".join(record for _, record in sorted(pieces))
        framed = b"tree " + str(len(payload)).encode("ascii") + bytes([0]) + payload
        object_id = hashlib.sha1(framed).hexdigest()
        if prefix:
            directories[prefix] = object_id
        return object_id

    return tree_id(root), directories


def oracle_tree(entry_list):
    """Independent recursive Git-tree root oracle for synthetic inventories."""
    return oracle_tree_details(entry_list)[0]


def file_spec(file_id, rel_path, content, bind_path=None, governed_text=True):
    size, sha256, git_blob = oracle_identity(content)
    return {
        "id": file_id,
        "root": 0,
        "path": rel_path,
        "governed_text": governed_text,
        "expected_size": size,
        "expected_sha256": sha256,
        "expected_git_blob": git_blob,
        "bind_path": bind_path,
    }


class SyntheticCase:
    def __init__(self, phase="preflight"):
        self.temp = tempfile.TemporaryDirectory(prefix="adw-checker-test-")
        self.root = Path(self.temp.name).resolve()
        self.inputs = self.root / "inputs"
        self.reports = self.root / "reports"
        self.inputs.mkdir()
        self.reports.mkdir()
        base_entries = [
            {"path": "docs/research/research-register.md", "mode": "100644",
             "blob": KNOWN["register_before"][2]},
            {"path": "src/unchanged.txt", "mode": "100644", "blob": KNOWN["stable"][2]},
        ]
        target_entries = [
            {"path": "artifacts/checker.md", "mode": "100644", "blob": KNOWN["artifact"][2]},
            {"path": "docs/research/research-register.md", "mode": "100644",
             "blob": KNOWN["register_after"][2]},
            {"path": "src/unchanged.txt", "mode": "100644", "blob": KNOWN["stable"][2]},
        ]
        self.contents = {
            "stable": STABLE,
            "register-before-authorized": REGISTER_BEFORE,
            "register-before-observed": REGISTER_BEFORE,
            "register-after-authorized": REGISTER_AFTER,
            "register-after-observed": REGISTER_AFTER,
            "artifact": ARTIFACT,
        }
        self.case = {
            "schema_version": "adw.persistence-checker.case.v1",
            "task_reference": "SYNTHETIC-NON-OPERATIONAL-CASE-001",
            "phase": phase,
            "verification_scope": ["synthetic two-file persistence", "producer test only"],
            "repository": {"name": "synthetic/example", "ref": "refs/heads/main"},
            "paths": {
                "read_roots": [str(self.root)],
                "report_root": str(self.reports),
                "report_destination": "report-001.json",
            },
            "authority": {
                "source": "synthetic exact-byte GitHub REST fixtures",
                "branch_request_reference": "synthetic-branch-request-001",
                "tree_request_reference": "synthetic-tree-request-001",
                "caller_identity": "synthetic-test-caller",
                "provenance_claims": ["synthetic", "not authenticated", "not operational"],
                "observation_time": "2026-09-04T12:00:00Z",
                "evaluation_time": "2026-09-04T12:05:00Z",
                "freshness_cutoff": "2026-09-04T11:55:00Z",
                "available": True,
                "branch_response_file": "github-branch-response",
                "tree_response_file": "github-tree-response",
                "live_ref_commit": BASE_COMMIT if phase == "preflight" else SUBJECT_COMMIT,
                "expected_protected": False,
                "expected_protection_enabled": False,
                "expected_status_check_enforcement": "off",
            },
            "identities": {},
            "inventories": {
                "base": {"complete": True, "truncated": False, "entries": base_entries},
                "target": {"complete": True, "truncated": False, "entries": target_entries},
            },
            "allowed_delta": {
                "additions": ["artifacts/checker.md"],
                "deletions": [],
                "modifications": ["docs/research/research-register.md"],
            },
            "byte_files": [
                file_spec("stable", "inputs/stable.txt", STABLE),
                file_spec("register-before-authorized", "inputs/register-before-authorized.md", REGISTER_BEFORE),
                file_spec("register-before-observed", "inputs/register-before-observed.md", REGISTER_BEFORE),
                file_spec("register-after-authorized", "inputs/register-after-authorized.md", REGISTER_AFTER),
                file_spec("register-after-observed", "inputs/register-after-observed.md", REGISTER_AFTER,
                          "docs/research/research-register.md"),
                file_spec("artifact", "inputs/artifact.md", ARTIFACT, "artifacts/checker.md"),
            ],
            "register": {
                "path": "docs/research/research-register.md",
                "authorized_before_file": "register-before-authorized",
                "observed_before_file": "register-before-observed",
                "authorized_after_file": "register-after-authorized",
                "observed_after_file": "register-after-observed",
            },
            "pending_external_gates": ["independent review", "coordinator disposition", "persistence authorization"],
        }
        base_identity = {
            "expected_commit": BASE_COMMIT, "observed_commit": BASE_COMMIT,
            "expected_tree": oracle_tree(base_entries), "observed_tree": oracle_tree(base_entries),
        }
        if phase == "preflight":
            self.case["identities"] = {
                "base": base_identity,
                "working": {"expected_tree": oracle_tree(target_entries)},
            }
        else:
            self.case["identities"] = {
                "base": base_identity,
                "candidate": {
                    "expected_commit": SUBJECT_COMMIT, "observed_commit": SUBJECT_COMMIT,
                    "expected_parents": [BASE_COMMIT], "observed_parents": [BASE_COMMIT],
                    "expected_tree": oracle_tree(target_entries), "observed_tree": oracle_tree(target_entries),
                },
            }
        self.case_path = self.root / "case.json"
        self.counter = 1
        self.materialize()

    def observed_values(self):
        if self.case["phase"] == "preflight":
            commit = self.case["identities"]["base"]["observed_commit"]
            tree = self.case["identities"]["base"]["observed_tree"]
            parents = [BASE_PARENT]
            inventory = self.case["inventories"]["base"]
        else:
            commit = self.case["identities"]["candidate"]["observed_commit"]
            tree = self.case["identities"]["candidate"]["observed_tree"]
            parents = self.case["identities"]["candidate"]["observed_parents"]
            inventory = self.case["inventories"]["target"]
        return commit, tree, parents, inventory

    def branch_response_bytes(self):
        commit, tree, parents, _ = self.observed_values()
        payload = {
            "name": "main",
            "commit": {
                "sha": commit,
                "commit": {"tree": {"sha": tree, "url": "https://example.invalid/tree"},
                           "message": "synthetic only"},
                "parents": [{"sha": parent, "url": "https://example.invalid/parent"}
                            for parent in parents],
                "url": "https://example.invalid/commit",
            },
            "protected": False,
            "protection": {
                "enabled": False,
                "required_status_checks": {
                    "enforcement_level": "off", "contexts": [], "checks": []
                },
                "unrelated_future_field": {"accepted": True},
            },
            "url": "https://example.invalid/branch",
            "synthetic_fixture": True,
        }
        return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")

    def tree_response_bytes(self, empty_directories=()):
        _, tree, _, inventory = self.observed_values()
        entries = []
        computed_tree, directories = oracle_tree_details(inventory["entries"], empty_directories)
        self.assert_oracle_tree(tree, computed_tree)
        for directory, directory_sha in sorted(directories.items()):
            entries.append({"path": directory, "mode": "040000", "type": "tree",
                            "sha": directory_sha, "url": "https://example.invalid/tree-entry"})
        for entry in inventory["entries"]:
            entries.append({"path": entry["path"], "mode": entry["mode"],
                            "type": "commit" if entry["mode"] == "160000" else "blob",
                            "sha": entry["blob"], "size": 1,
                            "url": "https://example.invalid/object"})
        payload = {
            "sha": tree,
            "url": "https://example.invalid/recursive-tree",
            "tree": entries,
            "truncated": False,
            "synthetic_fixture": True,
        }
        return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")

    @staticmethod
    def assert_oracle_tree(expected, observed):
        if expected != observed:
            raise AssertionError("synthetic fixture tree does not match independent oracle")

    def refresh_observation(self):
        payloads = {
            "github-branch-response": ("inputs/github-branch-response.json", self.branch_response_bytes()),
            "github-tree-response": ("inputs/github-tree-response.json", self.tree_response_bytes()),
        }
        specs = self.case["byte_files"]
        for file_id, (path, data) in payloads.items():
            self.contents[file_id] = data
            replacement = file_spec(file_id, path, data)
            for index, spec in enumerate(specs):
                if spec["id"] == file_id:
                    specs[index] = replacement
                    break
            else:
                specs.append(replacement)

    def rebind_trees(self):
        base_tree = oracle_tree(self.case["inventories"]["base"]["entries"])
        target_tree = oracle_tree(self.case["inventories"]["target"]["entries"])
        for key in ("expected_tree", "observed_tree"):
            self.case["identities"]["base"][key] = base_tree
        if self.case["phase"] == "preflight":
            self.case["identities"]["working"]["expected_tree"] = target_tree
        else:
            for key in ("expected_tree", "observed_tree"):
                self.case["identities"]["candidate"][key] = target_tree
        self.refresh_observation()

    def materialize(self, raw_case=None):
        self.refresh_observation()
        for spec in self.case["byte_files"]:
            data = self.contents[spec["id"]]
            target = self.root / spec["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        if raw_case is None:
            raw_case = (json.dumps(self.case, sort_keys=True, indent=2) + "\n").encode("utf-8")
        self.case_path.write_bytes(raw_case)

    def execute(self):
        self.counter += 1
        self.case["paths"]["report_destination"] = "report-%03d.json" % self.counter
        self.materialize()
        return CHECKER.execute(str(self.case_path))

    def execute_with_raw(self, file_id, data):
        return self.execute_with_raws({file_id: data})

    def execute_with_raws(self, payloads):
        for file_id, data in payloads.items():
            self.contents[file_id] = data
            for spec in self.case["byte_files"]:
                if spec["id"] == file_id:
                    spec.update(file_spec(file_id, spec["path"], data))
                    break
        self.counter += 1
        self.case["paths"]["report_destination"] = "report-raw-%03d.json" % self.counter
        for spec in self.case["byte_files"]:
            target = self.root / spec["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(self.contents[spec["id"]])
        self.case_path.write_bytes((json.dumps(self.case, sort_keys=True, indent=2) + "\n").encode("utf-8"))
        return CHECKER.execute(str(self.case_path))

    def execute_case_only(self):
        self.counter += 1
        if isinstance(self.case.get("paths"), dict):
            self.case["paths"]["report_destination"] = "report-case-%03d.json" % self.counter
        self.case_path.write_bytes((json.dumps(self.case, sort_keys=True, indent=2) + "\n").encode("utf-8"))
        return CHECKER.execute(str(self.case_path))

    def close(self):
        self.temp.cleanup()


class PersistenceCheckerTests(unittest.TestCase):
    def setUp(self):
        self.fx = SyntheticCase()

    def tearDown(self):
        self.fx.close()

    def assert_result(self, expected, outcome):
        code, report, written, diagnostic = outcome
        self.assertEqual(expected, report["overall_result"])
        self.assertEqual({"PASS": 0, "FAIL": 1, "UNEVALUABLE": 2}[expected], code)
        self.assertTrue(written)
        self.assertIsNone(diagnostic)
        return report

    def configure_pcr006_empty_base(self, truthful_register_addition=False):
        self.fx.case["inventories"]["base"]["entries"] = []
        next(spec for spec in self.fx.case["byte_files"]
             if spec["id"] == "stable")["bind_path"] = "src/unchanged.txt"
        additions = ["artifacts/checker.md", "src/unchanged.txt"]
        modifications = ["docs/research/research-register.md"]
        if truthful_register_addition:
            additions.append("docs/research/research-register.md")
            modifications = []
        self.fx.case["allowed_delta"] = {
            "additions": sorted(additions),
            "deletions": [],
            "modifications": modifications,
        }
        self.fx.rebind_trees()

    def test_valid_preflight_pass(self):
        report = self.assert_result("PASS", self.fx.execute())
        self.assertEqual("preflight", report["phase"])
        self.assertEqual({"base", "working"}, set(self.fx.case["identities"]))
        self.assertNotIn("candidate", self.fx.case["identities"])
        self.assertIn("no publication identity C", report["phase_identity_model"])
        self.assertTrue(all(item["result"] == "PASS" for item in report["predicates"]))

    def test_preflight_rejects_fabricated_publication_identity(self):
        self.fx.case["identities"]["candidate"] = {
            "expected_commit": SUBJECT_COMMIT, "observed_commit": SUBJECT_COMMIT,
            "expected_parents": [BASE_COMMIT], "observed_parents": [BASE_COMMIT],
            "expected_tree": "c" * 40, "observed_tree": "c" * 40,
        }
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertEqual("case.schema", report["predicates"][0]["predicate"])

    def test_valid_readback_pass(self):
        self.fx.close()
        self.fx = SyntheticCase("readback")
        report = self.assert_result("PASS", self.fx.execute())
        self.assertEqual("readback", report["phase"])
        self.assertEqual({"base", "candidate"}, set(self.fx.case["identities"]))
        self.assertIn("published candidate C", report["phase_identity_model"])
        self.assertIn("authority.parents_consistency", [p["predicate"] for p in report["predicates"]])

    def test_raw_github_branch_and_recursive_tree_responses_accept_extra_fields(self):
        report = self.assert_result("PASS", self.fx.execute())
        predicates = {p["predicate"]: p for p in report["predicates"]}
        self.assertEqual("PASS", predicates["authority.raw_branch_schema"]["result"])
        self.assertEqual("PASS", predicates["authority.raw_tree_schema"]["result"])
        self.assertEqual(oracle_identity(self.fx.contents["github-branch-response"])[2],
                         predicates["authority.raw_branch_schema"]["observed"]["git_blob"])
        self.assertEqual(oracle_identity(self.fx.contents["github-tree-response"])[2],
                         predicates["authority.raw_tree_schema"]["observed"]["git_blob"])

    def test_raw_tree_directory_sha_conflict_is_unevaluable_with_specific_predicate(self):
        payload = json.loads(self.fx.tree_response_bytes().decode("utf-8"))
        directory = next(entry for entry in payload["tree"] if entry["type"] == "tree")
        directory["sha"] = "e" * 40
        data = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        report = self.assert_result("UNEVALUABLE",
                                    self.fx.execute_with_raw("github-tree-response", data))
        predicate = next(item for item in report["predicates"]
                         if item["predicate"] == "authority.raw_tree.directory_consistency")
        self.assertEqual("UNEVALUABLE", predicate["result"])
        self.assertIn("directory SHA", predicate["reason"])

    def test_pcr001_preflight_explicit_empty_directory_is_unevaluable(self):
        entries = self.fx.case["inventories"]["base"]["entries"]
        root_sha, directories = oracle_tree_details(entries, ("empty",))
        self.assertEqual("4b825dc642cb6eb9a060e54bf8d69288fbee4904", directories["empty"])
        self.fx.case["identities"]["base"]["expected_tree"] = root_sha
        self.fx.case["identities"]["base"]["observed_tree"] = root_sha
        branch_data = self.fx.branch_response_bytes()
        tree_data = self.fx.tree_response_bytes(("empty",))
        report = self.assert_result("UNEVALUABLE", self.fx.execute_with_raws({
            "github-branch-response": branch_data,
            "github-tree-response": tree_data,
        }))
        unable = {item["predicate"] for item in report["predicates"]
                  if item["result"] == "UNEVALUABLE"}
        self.assertIn("authority.raw_tree.empty_directories_unrepresentable", unable)
        self.assertIn("inventory.base.tree_binding", unable)

    def test_pcr001_readback_explicit_empty_directory_is_unevaluable(self):
        self.fx.close()
        self.fx = SyntheticCase("readback")
        entries = self.fx.case["inventories"]["target"]["entries"]
        root_sha, _ = oracle_tree_details(entries, ("empty",))
        for field in ("expected_tree", "observed_tree"):
            self.fx.case["identities"]["candidate"][field] = root_sha
        branch_data = self.fx.branch_response_bytes()
        tree_data = self.fx.tree_response_bytes(("empty",))
        report = self.assert_result("UNEVALUABLE", self.fx.execute_with_raws({
            "github-branch-response": branch_data,
            "github-tree-response": tree_data,
        }))
        unable = {item["predicate"] for item in report["predicates"]
                  if item["result"] == "UNEVALUABLE"}
        self.assertIn("authority.raw_tree.empty_directories_unrepresentable", unable)
        self.assertIn("inventory.candidate.tree_binding", unable)

    def test_pcr001_base_leaf_inventory_binds_to_observed_tree_in_both_phases(self):
        for phase in ("preflight", "readback"):
            with self.subTest(phase=phase):
                fx = SyntheticCase(phase)
                try:
                    root_sha, _ = oracle_tree_details(
                        fx.case["inventories"]["base"]["entries"], ("empty",))
                    for field in ("expected_tree", "observed_tree"):
                        fx.case["identities"]["base"][field] = root_sha
                    if phase == "preflight":
                        report = self.assert_result("UNEVALUABLE", fx.execute_with_raws({
                            "github-branch-response": fx.branch_response_bytes(),
                            "github-tree-response": fx.tree_response_bytes(("empty",)),
                        }))
                    else:
                        report = self.assert_result("UNEVALUABLE", fx.execute())
                    predicate = next(item for item in report["predicates"]
                                     if item["predicate"] == "inventory.base.tree_binding")
                    self.assertEqual("UNEVALUABLE", predicate["result"])
                finally:
                    fx.close()

    def test_pcr001_silent_empty_directory_deletion_cannot_pass(self):
        entries = self.fx.case["inventories"]["base"]["entries"]
        root_sha, _ = oracle_tree_details(entries, ("empty",))
        for field in ("expected_tree", "observed_tree"):
            self.fx.case["identities"]["base"][field] = root_sha
        report = self.assert_result("UNEVALUABLE", self.fx.execute_with_raws({
            "github-branch-response": self.fx.branch_response_bytes(),
            "github-tree-response": self.fx.tree_response_bytes(("empty",)),
        }))
        self.assertEqual([], self.fx.case["allowed_delta"]["deletions"])
        self.assertIn("authority.raw_tree.empty_directories_unrepresentable",
                      {item["predicate"] for item in report["predicates"]
                       if item["result"] == "UNEVALUABLE"})

    def test_pcr001_ordinary_nonempty_nested_directories_pass_both_phases(self):
        for phase in ("preflight", "readback"):
            with self.subTest(phase=phase):
                fx = SyntheticCase(phase)
                try:
                    report = self.assert_result("PASS", fx.execute())
                    predicate = next(item for item in report["predicates"] if
                                     item["predicate"] ==
                                     "authority.raw_tree.empty_directories_unrepresentable")
                    self.assertEqual("PASS", predicate["result"])
                finally:
                    fx.close()

    def test_raw_tree_missing_implied_directory_is_unevaluable(self):
        payload = json.loads(self.fx.tree_response_bytes().decode("utf-8"))
        payload["tree"] = [entry for entry in payload["tree"]
                           if not (entry["type"] == "tree" and entry["path"] == "docs/research")]
        data = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        report = self.assert_result("UNEVALUABLE",
                                    self.fx.execute_with_raw("github-tree-response", data))
        predicate = next(item for item in report["predicates"]
                         if item["predicate"] == "authority.raw_tree.directory_consistency")
        self.assertIn("missing", predicate["reason"])

    def test_pcr005_raw_directory_mode_040000_passes(self):
        payload = json.loads(self.fx.tree_response_bytes().decode("utf-8"))
        directory_modes = [entry["mode"] for entry in payload["tree"]
                           if entry["type"] == "tree"]
        self.assertTrue(directory_modes)
        self.assertEqual({"040000"}, set(directory_modes))
        self.assert_result("PASS", self.fx.execute())

    def test_pcr005_raw_directory_mode_40000_is_unevaluable(self):
        payload = json.loads(self.fx.tree_response_bytes().decode("utf-8"))
        for entry in payload["tree"]:
            if entry["type"] == "tree":
                entry["mode"] = "40000"
        data = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        report = self.assert_result("UNEVALUABLE",
                                    self.fx.execute_with_raw("github-tree-response", data))
        self.assertTrue(any("directory mode" in item["reason"] for item in report["predicates"]
                            if item["result"] == "UNEVALUABLE"))

    def test_unpaired_surrogate_in_task_reference_is_reported_unevaluable(self):
        self.fx.case["task_reference"] = "\ud800"
        code, report, written, diagnostic = self.fx.execute_case_only()
        self.assertEqual(2, code)
        self.assertEqual("UNEVALUABLE", report["overall_result"])
        self.assertTrue(written)
        self.assertIsNone(diagnostic)
        report_path = self.fx.reports / self.fx.case["paths"]["report_destination"]
        report_path.read_bytes().decode("utf-8", "strict")

    def test_unpaired_surrogate_in_repository_path_is_reported_unevaluable(self):
        self.fx.case["inventories"]["base"]["entries"][0]["path"] = "\ud800"
        code, report, written, diagnostic = self.fx.execute_case_only()
        self.assertEqual((2, "UNEVALUABLE", True, None),
                         (code, report["overall_result"], written, diagnostic))

    def test_unpaired_surrogate_in_raw_github_field_is_reported_unevaluable(self):
        payload = json.loads(self.fx.branch_response_bytes().decode("utf-8"))
        payload["name"] = "\ud800"
        data = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        report = self.assert_result("UNEVALUABLE",
                                    self.fx.execute_with_raw("github-branch-response", data))
        self.assertTrue(any("unpaired UTF-16 surrogate" in item["reason"]
                            for item in report["predicates"] if item["result"] == "UNEVALUABLE"))

    def test_unpaired_surrogate_in_json_object_key_is_reported_unevaluable(self):
        self.fx.case["\ud800"] = "unsafe"
        code, report, written, diagnostic = self.fx.execute_case_only()
        self.assertEqual((2, "UNEVALUABLE", True, None),
                         (code, report["overall_result"], written, diagnostic))

    def test_valid_non_ascii_unicode_remains_supported(self):
        self.fx.case["task_reference"] = "Синтетична-перевірка-✓"
        report = self.assert_result("PASS", self.fx.execute())
        self.assertEqual("Синтетична-перевірка-✓", report["task_reference"])
        report_path = self.fx.reports / self.fx.case["paths"]["report_destination"]
        self.assertIn("Синтетична-перевірка-✓", report_path.read_text("utf-8"))

    def test_independent_known_size_sha256_and_git_blob_constants(self):
        for name, data in (("stable", STABLE), ("register_before", REGISTER_BEFORE),
                           ("register_after", REGISTER_AFTER), ("artifact", ARTIFACT)):
            self.assertEqual(KNOWN[name], oracle_identity(data))
            self.assertEqual(KNOWN[name][0], CHECKER.byte_identity(data)["bytes"])
            self.assertEqual(KNOWN[name][1], CHECKER.byte_identity(data)["sha256"])
            self.assertEqual(KNOWN[name][2], CHECKER.byte_identity(data)["git_blob"])

    def test_wrong_bytes_size_digest_and_blob_fail(self):
        self.fx.contents["artifact"] = b"wrong\n"
        report = self.assert_result("FAIL", self.fx.execute())
        failed = {p["predicate"] for p in report["predicates"] if p["result"] == "FAIL"}
        self.assertTrue({"file.artifact.size", "file.artifact.sha256", "file.artifact.git_blob"} <= failed)
        self.assertIn("binding.artifacts/checker.md.blob", failed)

    def test_each_text_serialization_violation_fails(self):
        bad_values = [b"\xef\xbb\xbfcandidate\n", b"\xff\n", b"candidate\r\n",
                      b"candidate", b"candidate\n\n"]
        expected_predicates = ["bom", "utf8", "cr", "one_final_lf", "one_final_lf"]
        for data, suffix in zip(bad_values, expected_predicates):
            with self.subTest(data=data):
                fx = SyntheticCase()
                try:
                    fx.contents["artifact"] = data
                    report = self.assert_result("FAIL", fx.execute())
                    self.assertIn("file.artifact.text.%s" % suffix,
                                  {p["predicate"] for p in report["predicates"] if p["result"] == "FAIL"})
                finally:
                    fx.close()

    def test_malformed_identity_is_unevaluable(self):
        self.fx.case["identities"]["base"]["observed_commit"] = "short"
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertIn("identity.format", {p["predicate"] for p in report["predicates"]})

    def test_malformed_digest_identity_is_unevaluable(self):
        self.fx.case["byte_files"][0]["expected_sha256"] = "not-a-sha256"
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertTrue(any(p["predicate"] == "file.0.schema" and p["result"] == "UNEVALUABLE"
                            for p in report["predicates"]))

    def test_wrong_base_candidate_parent_tree_and_ref_fail(self):
        variants = ("base", "candidate", "parent", "tree", "ref")
        for variant in variants:
            with self.subTest(variant=variant):
                fx = SyntheticCase("readback" if variant in ("candidate", "parent", "tree") else "preflight")
                try:
                    if variant == "base":
                        fx.case["identities"]["base"]["expected_commit"] = "c" * 40
                    elif variant == "candidate":
                        fx.case["identities"]["candidate"]["expected_commit"] = "c" * 40
                    elif variant == "parent":
                        fx.case["identities"]["candidate"]["observed_parents"] = ["c" * 40]
                    elif variant == "tree":
                        fx.case["identities"]["candidate"]["expected_tree"] = "c" * 40
                    else:
                        fx.case["authority"]["live_ref_commit"] = "c" * 40
                    report = self.assert_result("FAIL" if variant != "ref" else "UNEVALUABLE", fx.execute())
                    self.assertTrue(any(p["result"] in ("FAIL", "UNEVALUABLE") for p in report["predicates"]))
                finally:
                    fx.close()

    def test_unexpected_addition_deletion_modification_and_mode_fail(self):
        variants = ("addition", "deletion", "modification", "mode")
        for variant in variants:
            with self.subTest(variant=variant):
                fx = SyntheticCase()
                try:
                    target = fx.case["inventories"]["target"]["entries"]
                    if variant == "addition":
                        target.append({"path": "unexpected.txt", "mode": "100644", "blob": KNOWN["stable"][2]})
                    elif variant == "deletion":
                        target[:] = [e for e in target if e["path"] != "src/unchanged.txt"]
                    elif variant == "modification":
                        next(e for e in target if e["path"] == "src/unchanged.txt")["blob"] = KNOWN["artifact"][2]
                    else:
                        next(e for e in target if e["path"] == "src/unchanged.txt")["mode"] = "100755"
                    fx.rebind_trees()
                    report = self.assert_result("FAIL", fx.execute())
                    self.assertTrue(any(p["predicate"].startswith("delta.") and p["result"] == "FAIL"
                                        for p in report["predicates"]))
                finally:
                    fx.close()

    def test_changed_supposedly_untouched_entry_fails(self):
        entry = next(e for e in self.fx.case["inventories"]["target"]["entries"]
                     if e["path"] == "src/unchanged.txt")
        entry["blob"] = KNOWN["artifact"][2]
        self.fx.rebind_trees()
        report = self.assert_result("FAIL", self.fx.execute())
        self.assertIn("delta.modifications", {p["predicate"] for p in report["predicates"] if p["result"] == "FAIL"})

    def test_pcr006_inventory_parser_distinguishes_invalid_and_valid_empty(self):
        valid_checker = CHECKER.Checker(
            self.fx.case_path, self.fx.case_path.read_bytes(), self.fx.case)
        self.fx.case["inventories"]["base"]["entries"] = []
        self.assertEqual({}, valid_checker._inventory("base"))

        invalid_case = copy.deepcopy(self.fx.case)
        invalid_case["inventories"]["base"]["complete"] = False
        invalid_checker = CHECKER.Checker(
            self.fx.case_path, self.fx.case_path.read_bytes(), invalid_case)
        self.assertIsNone(invalid_checker._inventory("base"))

    def test_pcr006_empty_base_checks_canonical_empty_tree(self):
        self.configure_pcr006_empty_base()
        report = self.assert_result("FAIL", self.fx.execute())
        predicate = next(item for item in report["predicates"]
                         if item["predicate"] == "inventory.base.tree_binding")
        self.assertEqual("PASS", predicate["result"])
        self.assertEqual("4b825dc642cb6eb9a060e54bf8d69288fbee4904",
                         predicate["expected"])
        self.assertEqual("4b825dc642cb6eb9a060e54bf8d69288fbee4904",
                         predicate["observed"])

    def test_pcr006_empty_base_evaluates_complete_additions(self):
        self.configure_pcr006_empty_base(truthful_register_addition=True)
        report = self.assert_result("FAIL", self.fx.execute())
        predicate = next(item for item in report["predicates"]
                         if item["predicate"] == "delta.additions")
        expected = [
            "artifacts/checker.md",
            "docs/research/research-register.md",
            "src/unchanged.txt",
        ]
        self.assertEqual("PASS", predicate["result"])
        self.assertEqual(expected, predicate["expected"])
        self.assertEqual(expected, predicate["observed"])

    def test_pcr006_review002_reproduction_false_modification_cannot_pass(self):
        self.configure_pcr006_empty_base()
        report = self.assert_result("FAIL", self.fx.execute())
        failed = {item["predicate"] for item in report["predicates"]
                  if item["result"] == "FAIL"}
        self.assertIn("delta.additions", failed)
        self.assertIn("delta.modifications", failed)
        self.assertIn("register.base_inventory_membership", failed)
        self.assertIn("register.delta_classification", failed)

    def test_pcr006_truthful_register_addition_cannot_satisfy_modification_contract(self):
        self.configure_pcr006_empty_base(truthful_register_addition=True)
        report = self.assert_result("FAIL", self.fx.execute())
        predicates = {item["predicate"]: item for item in report["predicates"]}
        self.assertEqual("PASS", predicates["delta.additions"]["result"])
        self.assertEqual("FAIL", predicates["register.delta"]["result"])
        self.assertEqual("FAIL", predicates["register.delta_classification"]["result"])
        self.assertEqual(["additions"],
                         predicates["register.delta_classification"]["observed"])

    def test_pcr006_missing_register_in_target_cannot_pass(self):
        target = self.fx.case["inventories"]["target"]["entries"]
        target[:] = [entry for entry in target
                     if entry["path"] != "docs/research/research-register.md"]
        self.fx.case["allowed_delta"] = {
            "additions": ["artifacts/checker.md"],
            "deletions": ["docs/research/research-register.md"],
            "modifications": [],
        }
        self.fx.rebind_trees()
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        predicate = next(item for item in report["predicates"]
                         if item["predicate"] == "register.target_inventory_membership")
        self.assertEqual("FAIL", predicate["result"])

    def test_pcr006_empty_target_evaluates_complete_deletions(self):
        self.fx.case["inventories"]["target"]["entries"] = []
        self.fx.case["allowed_delta"] = {
            "additions": [],
            "deletions": ["docs/research/research-register.md", "src/unchanged.txt"],
            "modifications": [],
        }
        self.fx.rebind_trees()
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        predicates = {item["predicate"]: item for item in report["predicates"]}
        self.assertEqual("PASS", predicates["inventory.working.tree_binding"]["result"])
        self.assertEqual("4b825dc642cb6eb9a060e54bf8d69288fbee4904",
                         predicates["inventory.working.tree_binding"]["observed"])
        self.assertEqual("PASS", predicates["delta.deletions"]["result"])
        self.assertEqual(["docs/research/research-register.md", "src/unchanged.txt"],
                         predicates["delta.deletions"]["observed"])

    def test_pcr006_invalid_inventory_is_unevaluable_without_crash(self):
        self.fx.case["inventories"]["base"]["complete"] = False
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertIn("inventory.base.complete",
                      {item["predicate"] for item in report["predicates"]
                       if item["result"] == "UNEVALUABLE"})
        self.assertFalse(any("Traceback" in str(value) for value in report.values()))

    def test_pcr006_empty_inventory_cases_emit_mandatory_tree_and_delta_predicates(self):
        self.configure_pcr006_empty_base()
        report = self.assert_result("FAIL", self.fx.execute())
        present = {item["predicate"] for item in report["predicates"]}
        mandatory = {
            "inventory.base.tree_binding",
            "inventory.working.tree_binding",
            "delta.additions",
            "delta.deletions",
            "delta.modifications",
            "delta.unchanged_entries",
        }
        self.assertTrue(mandatory <= present)

    def test_pcr006_ordinary_nonempty_preflight_and_readback_still_pass(self):
        for phase in ("preflight", "readback"):
            with self.subTest(phase=phase):
                fx = SyntheticCase(phase)
                try:
                    self.assert_result("PASS", fx.execute())
                finally:
                    fx.close()

    def test_incomplete_unchanged_inventory_is_not_pass(self):
        self.fx.case["inventories"]["target"]["complete"] = False
        self.fx.refresh_observation()
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertIn("inventory.target.complete",
                      {p["predicate"] for p in report["predicates"] if p["result"] == "UNEVALUABLE"})

    def test_incorrect_register_before_and_after_bytes_fail(self):
        for file_id in ("register-before-observed", "register-after-observed"):
            with self.subTest(file_id=file_id):
                fx = SyntheticCase()
                try:
                    fx.contents[file_id] = b"not authorized\n"
                    report = self.assert_result("FAIL", fx.execute())
                    self.assertTrue(any(p["predicate"].startswith("register.") and p["result"] == "FAIL"
                                        for p in report["predicates"]))
                finally:
                    fx.close()

    def test_missing_field_and_incomplete_evidence_are_unevaluable(self):
        del self.fx.case["authority"]["branch_request_reference"]
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertEqual("case.schema", report["predicates"][0]["predicate"])

    def test_duplicate_case_json_key_is_unevaluable_without_report(self):
        raw = b'{"schema_version":"x","schema_version":"y"}\n'
        self.fx.case_path.write_bytes(raw)
        code, report, written, diagnostic = CHECKER.execute(str(self.fx.case_path))
        self.assertEqual(2, code)
        self.assertIsNone(report)
        self.assertFalse(written)
        self.assertIn("duplicate JSON key", diagnostic)

    def test_pcr002_nonstandard_constants_in_case_are_rejected(self):
        for constant in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(constant=constant):
                fx = SyntheticCase()
                try:
                    raw = fx.case_path.read_bytes().replace(
                        b'"task_reference": "SYNTHETIC-NON-OPERATIONAL-CASE-001"',
                        ('"task_reference": %s' % constant).encode("ascii"),
                        1,
                    )
                    fx.case_path.write_bytes(raw)
                    code, report, written, diagnostic = CHECKER.execute(str(fx.case_path))
                    self.assertEqual(2, code)
                    self.assertIsNone(report)
                    self.assertFalse(written)
                    self.assertIn("non-standard JSON constant", diagnostic)
                finally:
                    fx.close()

    def test_pcr002_nonstandard_constants_in_raw_branch_are_unevaluable(self):
        for constant in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(constant=constant):
                fx = SyntheticCase()
                try:
                    data = fx.branch_response_bytes().replace(
                        b"{", ('{"nonfinite":%s,' % constant).encode("ascii"), 1)
                    report = self.assert_result(
                        "UNEVALUABLE", fx.execute_with_raw("github-branch-response", data))
                    self.assertIn("non-standard JSON constant",
                                  " ".join(item["reason"] for item in report["predicates"]))
                    report_path = fx.reports / fx.case["paths"]["report_destination"]

                    def reject(value):
                        raise AssertionError("non-standard JSON constant written: %s" % value)

                    json.loads(report_path.read_text("utf-8"), parse_constant=reject)
                finally:
                    fx.close()

    def test_pcr002_nonstandard_constants_in_raw_tree_are_unevaluable(self):
        for constant in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(constant=constant):
                fx = SyntheticCase()
                try:
                    data = fx.tree_response_bytes().replace(
                        b"{", ('{"nonfinite":%s,' % constant).encode("ascii"), 1)
                    report = self.assert_result(
                        "UNEVALUABLE", fx.execute_with_raw("github-tree-response", data))
                    self.assertIn("non-standard JSON constant",
                                  " ".join(item["reason"] for item in report["predicates"]))
                    report_path = fx.reports / fx.case["paths"]["report_destination"]

                    def reject(value):
                        raise AssertionError("non-standard JSON constant written: %s" % value)

                    json.loads(report_path.read_text("utf-8"), parse_constant=reject)
                finally:
                    fx.close()

    def test_pcr002_nonfinite_report_values_use_strict_bounded_fallback(self):
        original_report = CHECKER.Checker.report
        for value in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(value=value):
                fx = SyntheticCase()
                try:
                    def report_with_nonfinite(checker):
                        report = original_report(checker)
                        report["synthetic_nonfinite"] = value
                        return report

                    with mock.patch.object(CHECKER.Checker, "report", report_with_nonfinite):
                        report = self.assert_result("UNEVALUABLE", fx.execute())
                    self.assertEqual("<invalid-non-finite-number>", report["synthetic_nonfinite"])
                    self.assertIn("report.serialization",
                                  {item["predicate"] for item in report["predicates"]
                                   if item["result"] == "UNEVALUABLE"})
                    report_path = fx.reports / fx.case["paths"]["report_destination"]

                    def reject(constant):
                        raise AssertionError("non-standard JSON constant written: %s" % constant)

                    loaded = json.loads(report_path.read_text("utf-8"), parse_constant=reject)
                    self.assertEqual("UNEVALUABLE", loaded["overall_result"])
                finally:
                    fx.close()

    def test_pcr002_numeric_overflow_is_recursively_rejected(self):
        with self.assertRaisesRegex(CHECKER.InputError, "non-finite JSON number"):
            CHECKER._json_bytes(b'{"nested":{"values":[1e999]}}\n', "synthetic JSON")

    def test_duplicate_inventory_path_is_unevaluable(self):
        duplicate = copy.deepcopy(self.fx.case["inventories"]["base"]["entries"][0])
        self.fx.case["inventories"]["base"]["entries"].append(duplicate)
        self.fx.refresh_observation()
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertIn("inventory.base.entries",
                      {p["predicate"] for p in report["predicates"] if p["result"] == "UNEVALUABLE"})

    def test_duplicate_key_in_each_raw_github_response_is_unevaluable(self):
        for file_id, original in (("github-branch-response", self.fx.branch_response_bytes()),
                                  ("github-tree-response", self.fx.tree_response_bytes())):
            with self.subTest(file_id=file_id):
                fx = SyntheticCase()
                try:
                    if file_id == "github-branch-response":
                        conflicted = original.replace(b'{"commit":', b'{"commit":{},"commit":', 1)
                    else:
                        conflicted = original.replace(b'{"sha":', b'{"sha":"' + ("e" * 40).encode() + b'","sha":', 1)
                    report = self.assert_result("UNEVALUABLE", fx.execute_with_raw(file_id, conflicted))
                    self.assertIn("authority.raw_response_schema",
                                  {p["predicate"] for p in report["predicates"]
                                   if p["result"] == "UNEVALUABLE"})
                finally:
                    fx.close()

    def test_duplicate_file_path_is_unevaluable(self):
        duplicate = copy.deepcopy(self.fx.case["byte_files"][0])
        duplicate["id"] = "another-id"
        self.fx.case["byte_files"].append(duplicate)
        self.fx.contents["another-id"] = STABLE
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertTrue(any(p["predicate"].endswith(".unique") and p["result"] == "UNEVALUABLE"
                            for p in report["predicates"]))

    def test_conflicting_branch_and_tree_responses_are_unevaluable(self):
        payload = json.loads(self.fx.branch_response_bytes().decode("utf-8"))
        payload["commit"]["commit"]["tree"]["sha"] = "c" * 40
        data = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        report = self.assert_result("UNEVALUABLE",
                                    self.fx.execute_with_raw("github-branch-response", data))
        self.assertIn("authority.branch_tree_consistency",
                      {p["predicate"] for p in report["predicates"] if p["result"] == "UNEVALUABLE"})

    def test_missing_required_raw_field_is_unevaluable(self):
        payload = json.loads(self.fx.branch_response_bytes().decode("utf-8"))
        del payload["commit"]["commit"]["tree"]
        data = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        report = self.assert_result("UNEVALUABLE",
                                    self.fx.execute_with_raw("github-branch-response", data))
        self.assertIn("authority.raw_response_schema",
                      {p["predicate"] for p in report["predicates"] if p["result"] == "UNEVALUABLE"})

    def test_truncated_recursive_tree_response_is_unevaluable(self):
        payload = json.loads(self.fx.tree_response_bytes().decode("utf-8"))
        payload["truncated"] = True
        data = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        report = self.assert_result("UNEVALUABLE",
                                    self.fx.execute_with_raw("github-tree-response", data))
        self.assertTrue(any("truncated" in p["reason"] for p in report["predicates"]
                            if p["result"] == "UNEVALUABLE"))

    def test_stale_observation_is_unevaluable(self):
        self.fx.case["authority"]["observation_time"] = "2026-09-04T11:00:00Z"
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertIn("authority.freshness", {p["predicate"] for p in report["predicates"]
                                               if p["result"] == "UNEVALUABLE"})

    def test_future_observation_is_unevaluable(self):
        self.fx.case["authority"]["observation_time"] = "2026-09-04T12:06:00Z"
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertIn("authority.freshness", {p["predicate"] for p in report["predicates"]
                                               if p["result"] == "UNEVALUABLE"})

    def test_stale_observation_retains_independent_failure_with_unevaluable_precedence(self):
        self.fx.case["authority"]["observation_time"] = "2026-09-04T11:00:00Z"
        self.fx.case["identities"]["working"]["expected_tree"] = "c" * 40
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertIn("authority.freshness", {p["predicate"] for p in report["predicates"]
                                               if p["result"] == "UNEVALUABLE"})
        self.assertIn("inventory.working.tree_binding",
                      {p["predicate"] for p in report["predicates"] if p["result"] == "FAIL"})

    def test_unavailable_live_verification_is_unevaluable(self):
        self.fx.case["authority"]["available"] = False
        self.fx.case["authority"]["branch_response_file"] = None
        self.fx.case["authority"]["tree_response_file"] = None
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertIn("authority.available",
                      {p["predicate"] for p in report["predicates"] if p["result"] == "UNEVALUABLE"})

    def test_unsafe_traversal_read_path_is_unevaluable(self):
        self.fx.case["byte_files"][0]["path"] = "../escape"
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertTrue(any(p["predicate"].startswith("file.0.schema") for p in report["predicates"]))

    def test_symlink_escape_is_unevaluable(self):
        outside = self.fx.root / "outside.txt"
        outside.write_bytes(STABLE)
        link = self.fx.inputs / "link.txt"
        link.symlink_to(outside)
        self.fx.case["byte_files"][0]["path"] = "inputs/link.txt"
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertTrue(any("symlink" in p["reason"] for p in report["predicates"]
                            if p["result"] == "UNEVALUABLE"))

    def test_case_outside_declared_read_root_is_unevaluable(self):
        other = self.fx.root / "other"
        other.mkdir()
        self.fx.case["paths"]["read_roots"] = [str(other)]
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        self.assertIn("paths.read_boundary",
                      {p["predicate"] for p in report["predicates"] if p["result"] == "UNEVALUABLE"})

    def test_pcr004_case_path_normalization_aliases_are_rejected(self):
        aliases = [
            str(self.fx.root) + "/./case.json",
            str(self.fx.root) + "//case.json",
            str(self.fx.case_path) + "/",
            str(self.fx.root) + "/inputs/../case.json",
        ]
        for alias in aliases:
            with self.subTest(alias=alias):
                code, report, written, diagnostic = CHECKER.execute(alias)
                self.assertEqual(2, code)
                self.assertIsNone(report)
                self.assertFalse(written)
                self.assertIn("absolute canonical path", diagnostic)

    def test_pcr004_read_root_normalization_aliases_are_rejected(self):
        aliases = [
            str(self.fx.root) + "/.",
            str(self.fx.root) + "//",
            str(self.fx.root) + "/",
            str(self.fx.root) + "/inputs/..",
        ]
        for alias in aliases:
            with self.subTest(alias=alias):
                fx = SyntheticCase()
                try:
                    fx.case["paths"]["read_roots"] = [alias.replace(str(self.fx.root), str(fx.root), 1)]
                    report = self.assert_result("UNEVALUABLE", fx.execute())
                    self.assertIn("paths.read_boundary",
                                  {p["predicate"] for p in report["predicates"]
                                   if p["result"] == "UNEVALUABLE"})
                finally:
                    fx.close()

    def test_pcr004_report_root_normalization_aliases_are_rejected(self):
        aliases = [
            str(self.fx.reports) + "/.",
            str(self.fx.reports) + "//",
            str(self.fx.reports) + "/",
            str(self.fx.root) + "/inputs/../reports",
        ]
        for alias in aliases:
            with self.subTest(alias=alias):
                fx = SyntheticCase()
                try:
                    fx.case["paths"]["report_root"] = alias.replace(str(self.fx.root), str(fx.root), 1)
                    code, report, written, diagnostic = fx.execute_case_only()
                    self.assertEqual(2, code)
                    self.assertFalse(written)
                    self.assertIn("absolute canonical path", diagnostic)
                finally:
                    fx.close()

    def test_existing_report_destination_is_unevaluable_without_overwrite(self):
        destination = self.fx.reports / "exists.json"
        destination.write_bytes(b"keep\n")
        self.fx.case["paths"]["report_destination"] = "exists.json"
        self.fx.materialize()
        code, report, written, diagnostic = CHECKER.execute(str(self.fx.case_path))
        self.assertEqual(2, code)
        self.assertEqual("UNEVALUABLE", report["overall_result"])
        self.assertFalse(written)
        self.assertIn("already exists", diagnostic)
        self.assertEqual(b"keep\n", destination.read_bytes())

    def test_out_of_scope_report_destination_is_unevaluable(self):
        self.fx.case["paths"]["report_destination"] = "../escape.json"
        self.fx.materialize()
        code, report, written, diagnostic = CHECKER.execute(str(self.fx.case_path))
        self.assertEqual(2, code)
        self.assertFalse(written)
        self.assertIn("unsafe alias", diagnostic)

    def test_report_write_failure_returns_nonzero_diagnostic(self):
        self.fx.case["paths"]["report_destination"] = "write-failure.json"
        self.fx.materialize()
        with mock.patch.object(CHECKER, "_exclusive_write", side_effect=PermissionError("synthetic denial")):
            code, report, written, diagnostic = CHECKER.execute(str(self.fx.case_path))
        self.assertEqual(2, code)
        self.assertEqual("UNEVALUABLE", report["overall_result"])
        self.assertFalse(written)
        self.assertIn("synthetic denial", diagnostic)

    def test_reproduced_missing_nested_identity_is_fail_closed(self):
        del self.fx.case["identities"]["base"]["expected_commit"]
        code, report, written, diagnostic = self.fx.execute_case_only()
        self.assertEqual(2, code)
        self.assertEqual("UNEVALUABLE", report["overall_result"])
        self.assertTrue(written)
        self.assertIsNone(diagnostic)

    def test_reproduced_wrong_allowed_delta_type_is_fail_closed(self):
        self.fx.case["allowed_delta"]["additions"] = 7
        code, report, written, diagnostic = self.fx.execute_case_only()
        self.assertEqual(2, code)
        self.assertEqual("UNEVALUABLE", report["overall_result"])
        self.assertTrue(written)
        self.assertIsNone(diagnostic)

    def test_reproduced_null_report_root_is_bounded_diagnostic(self):
        self.fx.case["paths"]["report_root"] = None
        code, report, written, diagnostic = self.fx.execute_case_only()
        self.assertEqual(2, code)
        self.assertEqual("UNEVALUABLE", report["overall_result"])
        self.assertFalse(written)
        self.assertIn("must be strings", diagnostic)

    def test_wrong_types_or_missing_fields_in_each_major_nested_object_fail_closed(self):
        mutations = {
            "repository": lambda case: case.update(repository=None),
            "paths": lambda case: case.update(paths=None),
            "authority": lambda case: case.update(authority=None),
            "identities": lambda case: case.update(identities=None),
            "inventories": lambda case: case.update(inventories=None),
            "allowed_delta": lambda case: case.update(allowed_delta=None),
            "byte_files": lambda case: case.update(byte_files={}),
            "register": lambda case: case.update(register=None),
            "repository-missing": lambda case: case["repository"].pop("name"),
            "paths-missing": lambda case: case["paths"].pop("report_root"),
            "authority-missing": lambda case: case["authority"].pop("source"),
            "identities-missing": lambda case: case["identities"].pop("base"),
            "inventories-missing": lambda case: case["inventories"].pop("base"),
            "allowed_delta-missing": lambda case: case["allowed_delta"].pop("additions"),
            "byte_files-missing": lambda case: case["byte_files"][0].pop("id"),
            "register-missing": lambda case: case["register"].pop("path"),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                fx = SyntheticCase()
                try:
                    mutate(fx.case)
                    code, report, written, diagnostic = fx.execute_case_only()
                    self.assertEqual(2, code)
                    self.assertNotEqual("PASS", report["overall_result"])
                    self.assertFalse(any("Traceback" in str(value)
                                         for value in (diagnostic, report)))
                finally:
                    fx.close()

    def test_mismatch_plus_inability_precedence_retains_both(self):
        self.fx.case["identities"]["working"]["expected_tree"] = "c" * 40
        self.fx.case["authority"]["available"] = False
        self.fx.case["authority"]["branch_response_file"] = None
        self.fx.case["authority"]["tree_response_file"] = None
        report = self.assert_result("UNEVALUABLE", self.fx.execute())
        results = {p["result"] for p in report["predicates"]}
        self.assertIn("FAIL", results)
        self.assertIn("UNEVALUABLE", results)

    def test_report_contains_required_identity_provenance_limits_and_gates(self):
        report = self.assert_result("PASS", self.fx.execute())
        self.assertEqual("adw.persistence-checker.report.v1", report["report_version"])
        self.assertEqual("cpython", report["runtime_identity"]["implementation"])
        self.assertEqual("synthetic-test-caller", report["caller_provenance_claims"]["caller_identity"])
        self.assertEqual(3, len(report["pending_external_gates"]))
        self.assertTrue(report["non_authority"])
        serialized = (json.dumps(report, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
        written = (self.fx.reports / self.fx.case["paths"]["report_destination"]).read_bytes()
        self.assertEqual(serialized, written)


if __name__ == "__main__":
    unittest.main()

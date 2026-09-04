# Supervised persistence checker

This document defines the narrow first-version input interface for the
manually invoked ADW persistence checker. It is not a Workflow v1 task schema,
an operational workflow, or an authorization mechanism.

The checker uses Python 3.9.6-compatible standard-library code. It performs one
offline evaluation over caller-designated immutable byte files and two raw,
caller-exported GitHub REST response files. It invokes no network, Git,
subprocess, credential, repair, retry, scheduling, or mutation facility. Its
only permitted effect is exclusive creation of the case-designated report.

## Invocation

Keep the case file and every designated input below one of the case's absolute
`read_roots`. Create the report root and destination parent directories in
advance. Then run:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 tools/persistence_checker.py /absolute/path/to/case.json
```

The case path must be absolute and canonical. The checker reads it to learn
the declared roots, then requires it to be inside exactly one read root.
Inputs are opened read-only. The report destination is relative to an existing
absolute `report_root`, must not exist, and is opened with exclusive creation.

## Strict case interface

JSON objects reject duplicate keys. Every case object has exactly the listed
keys; unknown and missing case keys make the case unevaluable. Raw GitHub REST
objects are different: required fields are validated, while ordinary unrelated
fields are retained in the exact payload bytes and accepted.

Repository paths and report destinations are canonical relative POSIX paths:
no absolute form, empty segment, `.`, `..`, backslash, traversal, or
normalization alias. Filesystem roots are absolute canonical directories.
Read roots may not overlap. Symlinks and duplicate filesystem aliases are
rejected.

The top-level case object is:

```json
{
  "schema_version": "adw.persistence-checker.case.v1",
  "task_reference": "caller-owned reference",
  "phase": "preflight",
  "verification_scope": ["bounded statement"],
  "repository": {"name": "owner/repository", "ref": "refs/heads/main"},
  "paths": {
    "read_roots": ["/absolute/existing/root"],
    "report_root": "/absolute/existing/report-root",
    "report_destination": "new-report.json"
  },
  "authority": {},
  "identities": {},
  "inventories": {},
  "allowed_delta": {},
  "byte_files": [],
  "register": {},
  "pending_external_gates": ["independent review"]
}
```

`phase` is exactly `preflight` or `readback`. `verification_scope` and
`pending_external_gates` are caller statements and confer no authority.

## Phase-specific identity model

The two phases intentionally have different strict `identities` shapes.

Preflight checks immutable base `B` and proposed working candidate `W`. `W`
has a complete proposed target inventory and a computed intended tree, but no
publication commit, parent, or ref identity:

```json
{
  "base": {
    "expected_commit": "B-40-hex",
    "observed_commit": "B-40-hex",
    "expected_tree": "40-hex",
    "observed_tree": "40-hex"
  },
  "working": {
    "expected_tree": "computed-W-tree-40-hex"
  }
}
```

A preflight case containing `candidate`, a predicted commit, a placeholder
SHA, publication parents, or a publication ref is rejected as an unknown
identity shape. No branch name or fabricated hash represents future `C`.

Readback checks base `B` and exact published candidate `C`:

```json
{
  "base": {
    "expected_commit": "B-40-hex",
    "observed_commit": "B-40-hex",
    "expected_tree": "40-hex",
    "observed_tree": "40-hex"
  },
  "candidate": {
    "expected_commit": "C-40-hex",
    "observed_commit": "C-40-hex",
    "expected_parents": ["B-40-hex"],
    "observed_parents": ["B-40-hex"],
    "expected_tree": "published-tree-40-hex",
    "observed_tree": "published-tree-40-hex"
  }
}
```

Readback requires `C` to have sole ordered parent `B`, and the governed live
ref, raw branch response, raw tree response, candidate identity, and published
inventory must agree. Reports state whether they evaluated `B + W` or
`B + C`.

## Caller-exported raw GitHub evidence

`authority` has exactly:

```json
{
  "source": "caller claim about export source",
  "branch_request_reference": "request reference",
  "tree_request_reference": "request reference",
  "caller_identity": "caller-asserted identity",
  "provenance_claims": ["synthetic or operational qualification"],
  "observation_time": "2026-09-04T12:00:00Z",
  "evaluation_time": "2026-09-04T12:05:00Z",
  "freshness_cutoff": "2026-09-04T11:55:00Z",
  "available": true,
  "branch_response_file": "github-branch-response",
  "tree_response_file": "github-tree-response",
  "live_ref_commit": "40-lowercase-hex",
  "expected_protected": false,
  "expected_protection_enabled": false,
  "expected_status_check_enforcement": "off"
}
```

Times use exact UTC-second form. Freshness requires
`freshness_cutoff <= observation_time <= evaluation_time`; the checker never
consults the current clock. Unavailable required authority evidence makes the
result `UNEVALUABLE`.

`branch_response_file` designates the exact bytes returned by the GitHub REST
branch endpoint. The checker parses the real response structure and requires:

- top-level `name`, `protected`, and `protection`;
- `commit.sha`, `commit.commit.tree.sha`, and ordered `commit.parents[].sha`;
- `protection.enabled` and
  `protection.required_status_checks.enforcement_level`.

`tree_response_file` designates exact bytes from the GitHub recursive Git-tree
endpoint. The checker requires top-level `sha`, `tree`, and `truncated`; each
tree entry must provide `path`, `mode`, `type`, and `sha`. Directory entries
use Git tree modes and remain first-class evidence; blob and submodule entries
become leaf `path`/`mode`/`blob` values. `truncated` must be exactly `false`.

Every directory implied by a leaf or nested directory path must have its own
raw tree entry. The checker recursively rebuilds each supplied subtree from
its immediate leaf and directory children using canonical Git tree framing and
ordering. Every supplied directory SHA must equal that computed subtree SHA,
and the reconstructed root must equal the response's top-level `sha`. An extra
empty directory is accepted only when its object identity is the canonical
empty Git tree `4b825dc642cb6eb9a060e54bf8d69288fbee4904` and the root identity includes
that entry. Missing, duplicated, or internally conflicting directory evidence
makes the result `UNEVALUABLE` with a directory-consistency predicate.

Extra REST fields such as URLs, sizes, commit metadata, or later unrelated
response additions are allowed without caller rewriting. The exact raw bytes
remain bound through their byte count, SHA-256, and Git blob identity in the
report. Duplicate JSON keys are rejected independently in each response. The
branch commit tree must equal the recursive response's top-level tree SHA.

For preflight, both raw responses bind live `B` and its complete base tree;
`W` is bound only by proposed files, the target inventory, and its computed
tree. For readback, the responses bind live `C`, sole parent `B`, published
tree, and complete target inventory. There is no normalized operational
wrapper and no network or connector client inside the checker. Tests use
synthetic fixtures that follow these REST structures and explicitly mark
themselves non-operational.

## Inventories, delta, and byte files

`inventories` contains exactly `base` and `target`. Each has `complete`,
`truncated`, and `entries`; each entry has exactly `path`, `mode`, and `blob`.
Allowed leaf modes are `100644`, `100755`, `120000`, and `160000`. Paths must
be unique. The checker recomputes each complete Git tree and compares all
entries. In preflight, target is proposed `W`; in readback, it is published
`C`.

`allowed_delta` contains sorted, unique arrays named `additions`, `deletions`,
and `modifications`. The complete computed delta must equal them. Every
supposedly unchanged `mode`/`blob` pair must remain identical.

Each `byte_files` entry has exactly:

```json
{
  "id": "unique-id",
  "root": 0,
  "path": "relative/input.txt",
  "governed_text": true,
  "expected_size": 123,
  "expected_sha256": "64-lowercase-hex",
  "expected_git_blob": "40-lowercase-hex",
  "bind_path": "repository/path-or-null"
}
```

`root` indexes `read_roots`. The checker recomputes byte count, SHA-256, and
canonical Git blob SHA-1 over `blob SP decimal-size NUL bytes`. Governed text
must be strict UTF-8 with no BOM or CR and exactly one final LF. Every added or
modified repository path has exactly one binding to bytes reproducing its
target blob; no other binding is allowed. Raw REST files are designated byte
files with `bind_path: null`.

`register` has exactly:

```json
{
  "path": "docs/research/research-register.md",
  "authorized_before_file": "byte-file-id",
  "observed_before_file": "byte-file-id",
  "authorized_after_file": "byte-file-id",
  "observed_after_file": "byte-file-id"
}
```

Complete authorized and observed before bytes must match exactly, as must the
after bytes. Their blobs bind to base and target inventory entries. The
Register path must be an authorized modification, and its target binding must
name `observed_after_file`.

## Results, fail-closed handling, and report

- `PASS`, exit `0`: every required predicate passed.
- `FAIL`, exit `1`: at least one definite mismatch exists and no inability
  prevents evaluation.
- `UNEVALUABLE`, exit `2`: input is missing, malformed, incorrectly typed,
  ambiguous, conflicting, unavailable, unsafe, or unreadable. It takes
  aggregate precedence while detected `FAIL` predicates remain visible.

Nested structures are validated before semantic use. A normal malformed-input
exception is converted to an `input.fail_closed` predicate when needed;
`KeyboardInterrupt`, `SystemExit`, and other `BaseException` signals are not
caught. When a safe new destination can be established, malformed input gets a
deterministic `UNEVALUABLE` report. If the case cannot safely establish that
destination, the CLI emits one bounded diagnostic without a traceback. It
never overwrites an existing file.

After each JSON document is decoded, the checker recursively validates every
object key and string value as Unicode scalar text. Escaped or literal
unpaired UTF-16 surrogate code points are rejected before semantic use and are
never copied into diagnostics. A safe destination still receives a sanitized,
deterministic `UNEVALUABLE` report. Report serialization has a second bounded
sanitization/fallback boundary so an ordinary `UnicodeEncodeError` cannot
escape. Valid non-ASCII Unicode remains supported and is emitted as UTF-8.

The sorted JSON report records checker/runtime/case identities, phase-specific
`W` or `C` semantics, task/scope, raw payload identities, expected and observed
values, every predicate with reason and evidence reference, provenance claims,
freshness boundaries, limitations, non-authority statements, and pending
gates. Report creation failure is nonzero; an operating-system write failure
may leave a partial new report, which must not be relied upon.

## Limits and non-authority

The checker compares bounded caller-supplied snapshots. Hashes establish byte
identity, not truth, provenance, approval, or authority. Caller names, request
references, timestamps, and payloads are claims it cannot authenticate. It
cannot establish current live GitHub state, later ref stability, writer
exclusivity, human availability, permissions, custody, independent review,
acceptance, push authorization, or operational readiness.

Canonical-path, component-symlink, regular-file, inode-alias, and
exclusive-create checks reduce common traversal hazards but cannot isolate the
filesystem from a concurrent actor; check/use races remain possible. The
supervised procedure owns isolation, fresh live observation, custody, review,
authorization, cancellation, and stopping decisions.

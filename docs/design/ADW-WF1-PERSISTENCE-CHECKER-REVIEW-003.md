---
id: ADW-WF1-PERSISTENCE-CHECKER-REVIEW-003
artifact: independent-candidate-review
artifact_status: active
owner: independent-review
subject_commit: d17af996803ae91253f11308e92f1b3601e04aa8
subject_parent: d9a449235e93942450f789a2c8ee8c9c611869a9
subject_tree: be8308ad4470b0f717fb113557282796d5a07667
predecessor_review_ref: docs/design/ADW-WF1-PERSISTENCE-CHECKER-REVIEW-002.md
reviewed_on: 2026-09-05
normative_effect: none
supersedes: null
---

# ADW-WF1-PERSISTENCE-CHECKER-REVIEW-003

Task: `ADW-WF1-PERSISTENCE-CHECKER-REVIEW-003`.
Mode: fresh targeted independent candidate review.
Repository: `ahtoxaandy999/agentic-development-workflow`.

## Review result

**Verdict:** `accept-second-corrected-candidate-for-checker-disposition`

**Findings:** 0 BLOCKER / 0 MAJOR / 0 MINOR.

This is an independent review recommendation bound only to the exact three-file checker candidate at commit `d17af996803ae91253f11308e92f1b3601e04aa8`. It is not candidate acceptance, coordinator disposition, persistence authorization, operational authorization, Workflow v1 adoption, baseline establishment, or acceptance of the publication commit or Research Register as a whole.

Proposed next gate: `Workflow v1 supervised persistence checker second corrected candidate review persistence`.

## Exact live and immutable basis

Connected `@GitHub` was used read-only for every live repository claim.

At entry and again at point of reliance:

- live `main`: `d17af996803ae91253f11308e92f1b3601e04aa8`;
- sole ordered parent: `d9a449235e93942450f789a2c8ee8c9c611869a9`;
- subject tree: `be8308ad4470b0f717fb113557282796d5a07667`;
- branch `protected`: `false`;
- protection `enabled`: `false`;
- required-status-check enforcement: `off`;
- recursive subject tree: complete, `truncated:false`;
- parent-to-subject comparison: `ahead_by:1`, `behind_by:0`, one commit;
- complete changed-path set exactly:
  - `docs/research/research-register.md`;
  - `docs/tooling/persistence-checker.md`;
  - `tests/test_persistence_checker.py`;
  - `tools/persistence_checker.py`.

Compare statistics were 8 Register changes, 15 usage-note changes, 136 test additions, and 90 implementation changes. No other path changed.

The accessible branch collection contains only `main`; the open PR collection is empty. The authoritative Register has `Superseded: None`, points to the second corrected checker candidate task, retains REVIEW-002 as the current persisted checker review, and contains no later checker disposition. Repository searches found no persisted `ADW-WF1-PERSISTENCE-CHECKER-REVIEW-003` and no occurrence of the prospective recommendation string. No competing or superseding current checker candidate or decision was found in the inspected repository owners and live collections.

### Register identity and current gate

`docs/research/research-register.md` at the exact subject independently reproduces:

- Git blob: `11300593a05a9af0949d949c12b715bce77d4187`;
- bytes: `51061`;
- SHA-256: `449b039a494bc8c88a3133e61a878a43796a91e535652eed4dc70a4d24f6fa64`;
- UTF-8 without BOM;
- LF-only;
- exactly one final LF.

Both current next-gate fields are exactly:

`Workflow v1 supervised persistence checker second corrected candidate independent review gate`

REVIEW-001 remains blob `807f34b9f3618255a5a8e58337c0ef83be056997`. REVIEW-002 remains blob `ca33acc578d631661bb72252231ceba4c8007b1d` and remains the predecessor review against subject `8b9feaed2fc3edd955e41a682dd7fc3b013535cc` with verdict `request-another-corrected-checker-candidate` and finding count 0 BLOCKER / 1 MAJOR / 0 MINOR.

The accepted tooling-design disposition remains `docs/design/ADW-WF1-TOOLING-DESIGN-DISPOSITION-001.md` at blob `d029e25406442ff5a44768c06e88333f6e1cd779`, decision `accept-initial-tooling-enforcement-design`, with accepted design subject commit `dc881f2a01ad0e5bfe173bad7be19b66b7fea51d` and blob `2e0c640e8cab61b0bf165712c27e02ff9a455ec6`.

The DR-005 disposition remains `docs/research/ADW-DR-005-DISPOSITION-001.md` at blob `70cea63938bf4a8b908904d2b9c7b0c9aec1b401`, decision `accept-scoped-dr-005-tooling-recommendations-for-design`, evidence target commit `38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958`, and evidence blob `615692060c7bf9d7372d5469550176f22caca9be`. Neither disposition was reopened substantively.

## Reviewer eligibility and independence

This Independent Review environment did not produce or persist the subject candidate, did not author the PCR-006 correction, and did not make a coordinator disposition for this candidate. No material reviewer conflict was identified.

This is procedural separation only. It does not establish platform-enforced reviewer identity. RG4 remains unresolved.

## Exact candidate identities

The three candidate files were reconstructed from exact subject blobs and independently hashed before execution and again after all synthetic tests/probes. All modes in the subject tree are `100644`.

| Path | Bytes | SHA-256 | Git blob | Serialization |
|---|---:|---|---|---|
| `tools/persistence_checker.py` | 62875 | `c0ad28a8e59d3e4d161c74b0f832682ed590836229b35f45527c645d9030d723` | `655cf2e8c2809b299e53f6e585a5d9bce0dc9c34` | UTF-8, no BOM, LF-only, exactly one final LF |
| `tests/test_persistence_checker.py` | 62065 | `f58273a337019da436af1d65d4f590e008773c72bf00566ebb9011a5c0d7a970` | `f975ced081a736e9b156411a303bb8675deb8bb3` | UTF-8, no BOM, LF-only, exactly one final LF |
| `docs/tooling/persistence-checker.md` | 14173 | `cec48b49f7496c3869b5a10eefd43db266e384d9aa3f816b22f1cda1da0c3814` | `405f8222b4d6f7b48b9332a758ab6d1c3c945f0f` | UTF-8, no BOM, LF-only, exactly one final LF |

The exact candidate bytes remained unchanged by review execution.

## Required reading and targeted method

The following exact-subject repository artifacts were read completely:

- `AGENTS.md`;
- `PROJECT-CHARTER.md`;
- `docs/research/research-register.md`;
- `docs/design/ADW-WF1-PERSISTENCE-CHECKER-GATE-001.md`;
- `docs/design/ADW-WF1-PERSISTENCE-CHECKER-REVIEW-001.md`;
- `docs/design/ADW-WF1-PERSISTENCE-CHECKER-REVIEW-002.md`;
- `tools/persistence_checker.py`;
- `tests/test_persistence_checker.py`;
- `docs/tooling/persistence-checker.md`.

The accepted tooling-design and DR-005 disposition identities were checked without reopening their complete substantive design. The parent implementation around the PCR-006 defect was also read to independently establish the corrected semantic delta rather than relying on producer conclusions.

The review was targeted to PCR-006 plus representative regression guards for PCR-001 through PCR-005, changed-code inspection, exact suite execution, independent synthetic probes, and effect/authority boundaries. No operational checker case was executed.

## PCR-006 assessment

**Result: resolved.**

The subject removes the REVIEW-002 truthiness/sentinel ambiguity:

- invalid, malformed, incomplete, or truncated inventory returns the invalid sentinel `None` and records `UNEVALUABLE` evidence;
- a valid complete zero-entry inventory returns `{}` and remains valid;
- validity is tested with `is not None`, not mapping truthiness;
- invalid inventories are replaced by empty internal placeholders only after their invalid status is retained, and tree/delta evaluation is skipped in that invalid-evidence case;
- valid empty inventories proceed through the complete tree and delta path.

For every valid base/target inventory, including zero-entry inventories, the implementation computes both Git trees, binds base to `base.observed_tree`, binds the phase-appropriate target tree, computes additions/deletions/modifications, evaluates unchanged entries, and emits the required tree/delta predicates.

The independently computed canonical empty Git-tree identity is:

`4b825dc642cb6eb9a060e54bf8d69288fbee4904`

Both valid-empty base and valid-empty target probes bound to that identity.

Register enforcement is no longer conditional on path presence:

- `register.path` must be present in every valid complete base inventory;
- it must be present in every valid complete target inventory;
- before bytes must bind the base Register blob;
- after bytes must bind the target Register blob;
- the actual computed delta is retained and separately classified;
- `register.delta_classification` requires exactly `modifications`;
- actual addition or deletion cannot satisfy the Register contract;
- invalid inventory evidence yields `UNEVALUABLE` Register membership/blob/classification evidence rather than PASS;
- valid contradictory evidence cannot produce PASS.

### Independent REVIEW-002 false-PASS reproduction

The exact semantic reproduction was rebuilt independently:

- valid complete empty base inventory;
- canonical empty base tree;
- non-empty target inventory;
- Register is an actual addition;
- allowed delta falsely declares the Register as a modification;
- all other synthetic evidence is internally valid.

Subject result: `FAIL`, nonzero.

The report included the applicable mandatory tree/delta predicates and exposed definite failures in:

- `delta.additions`;
- `delta.modifications`;
- `register.base_inventory_membership`;
- `register.delta_classification`.

The observed Register classification was `additions`. The REVIEW-002 false PASS is therefore not reproducible on this subject.

## PCR-001 through PCR-005 regression guard

**Result: all five accepted corrections preserved in focused independent probes.**

- **PCR-001:** explicit empty Git-tree entries remain `UNEVALUABLE` through `authority.raw_tree.empty_directories_unrepresentable`; leaf inventory/tree binding cannot silently delete them.
- **PCR-002:** `NaN`, `Infinity`, `-Infinity`, and non-finite numeric overflow are rejected and cannot produce non-standard PASS/report JSON.
- **PCR-003:** stale or post-evaluation authority remains `UNEVALUABLE`; a separately induced tree mismatch remains independently recorded as `FAIL` while aggregate precedence stays `UNEVALUABLE`.
- **PCR-004:** non-canonical filesystem aliases are rejected in original string form before `Path` normalization.
- **PCR-005:** REST recursive-tree directory mode accepts exactly `040000` and rejects `40000`; internal canonical Git tree framing continues to use `40000`.

No regression or material contradiction was found that required reopening unrelated accepted semantic/tooling-design work.

## Exact suite execution

Command:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_persistence_checker.py' -v
```

Execution environment: CPython 3.13.5 on Linux.

Result:

- tests: `70`;
- failures: `0`;
- errors: `0`;
- unittest runtime: `0.456 s`;
- external measured wall time: `1.11 s`;
- exit: `0`;
- result: `OK`.

No `__pycache__`, `.pyc`, or `.pyo` review artifact was retained.

Passing producer tests were treated only as supporting evidence.

## Independent temporary probes

A separate temporary harness used independent assertions and an independently coded native Git-tree oracle where relevant. It executed only synthetic non-operational cases, then was deleted.

| Required probe | Result |
|---|---|
| 1. REVIEW-002 reproduction | PASS: candidate returned `FAIL`, not PASS |
| 2. Valid empty base tree | PASS: canonical empty tree computed and bound |
| 3. Valid empty target tree | PASS: canonical empty tree computed and bound |
| 4. Invalid vs valid-empty inventory | PASS: `None` vs `{}` distinguished |
| 5. Truthful Register addition | PASS: addition delta may be truthful, but Register contract rejects it |
| 6. Missing Register from base | PASS: membership/blob predicates fail, no PASS |
| 7. Missing Register from target | PASS: membership/blob/classification prevent PASS |
| 8. Empty-inventory mandatory predicate coverage | PASS: all six required tree/delta predicates present |
| 9. Ordinary valid non-empty preflight | PASS / exit 0 |
| 10. Ordinary valid non-empty readback | PASS / exit 0 |
| 11. Representative PCR-001 through PCR-005 cases | PASS: all five regression groups preserved |

Independent probe total: `11/11` groups, `56` assertions, all passed.

## Changed-code, tests, and usage-contract inspection

The parent implementation used `{}` for both invalid and valid-empty inventory outcomes and then tested `if not self.base_entries or not self.target_entries`, directly reproducing the REVIEW-002 false-PASS root cause.

The subject replaces that coupling with an explicit invalid sentinel and validity flags, retains actual delta state for Register classification, adds mandatory Register membership/blob/classification predicates, and leaves the ordinary non-empty path intact.

No new skipped mandatory predicate, truthiness/sentinel confusion, partial-invalid inventory reuse, `None`/empty-map crash, false PASS, or material false FAIL was found in the changed implementation.

The 136 test-line additions cover PCR-006 cases including invalid/valid-empty distinction, canonical empty tree, complete additions/deletions, REVIEW-002 reproduction, truthful Register addition rejection, missing Register, mandatory predicate coverage, and ordinary preflight/readback. Test expectations also use independent native-oracle constants/tree construction rather than using the production tree helper as the sole oracle.

The usage note matches the implementation: it documents zero-leaf inventories as valid and evaluated, the canonical empty-tree identity, mandatory tree/delta coverage, invalid evidence as `UNEVALUABLE`, and the requirement that the Register exist in both inventories and be an actual modification with before/after blob bindings.

## Effect and authority review

Static source inspection and AST-based surface checks found only standard-library imports: `datetime`, `hashlib`, `json`, `math`, `os`, `pathlib`, `re`, `stat`, and `sys`.

The candidate remains:

- manually invoked;
- deterministic with respect to supplied bytes and runtime, with no clock/random/network acquisition;
- offline;
- input-read-only;
- limited to exclusive creation of one case-designated report;
- fail-closed on an existing/unsafe report destination;
- free of subprocess, network, credential, Git-write, installation, repair, retry, scheduling, and orchestration behavior.

The sole write path uses `O_CREAT | O_EXCL` and does not use `O_TRUNC`. No operational case was executed. This review makes no claim of measured usefulness or operational readiness.

## RG, DI, and non-authority boundaries

RG1 through RG12 remain unresolved. This candidate and this review create none of the missing controls.

In particular, no branch protection, writer fencing, permission proof, reviewer-identity enforcement, custody guarantee, provenance authentication, AFK authority, unattended authority, routine-write authority, or operational readiness is created.

`DI-1` remains preserved.

`DI-2` remains preserved.

The observed branch remains unprotected. That observation is not an authorization to weaken or bypass controls.

Workflow v1 remains unadopted and non-normative. The narrow D3 checker-development exception is not expanded by this review recommendation.

## Findings

No candidate defect meeting BLOCKER, MAJOR, or MINOR classification was found.

Counts:

- BLOCKER: `0`;
- MAJOR: `0`;
- MINOR: `0`.

There is therefore no finding requiring a corrected immutable candidate or renewed review. RG1-RG12 are pre-existing unresolved governance/tooling gaps, not candidate defects introduced by this subject.

## Verdict and next gate

`accept-second-corrected-candidate-for-checker-disposition`

The acceptance recommendation conditions for this review gate are met for the exact three-file candidate at commit `d17af996803ae91253f11308e92f1b3601e04aa8`: PCR-006 is substantively resolved; PCR-001 through PCR-005 remain resolved in focused regression probes; no BLOCKER, MAJOR, or MINOR finding remains; implementation, tests, and usage documentation agree; and the candidate remains within the narrow non-operational D3 boundary.

This recommendation applies only to that exact immutable three-file candidate. It does not accept the entire publication commit or Register, does not authorize operational checker use, does not resolve RG gaps, does not adopt Workflow v1, and does not perform the separate coordinator checker disposition.

Proposed next gate:

`Workflow v1 supervised persistence checker second corrected candidate review persistence`

## Explicit non-actions

This review did not:

- modify GitHub, the repository, the Register, or candidate files;
- correct a finding;
- persist this review into the repository;
- accept or disposition the candidate;
- execute an operational checker case;
- install or configure tooling;
- create hooks, Actions, automation, PRs, Issues, comments, tags, branches, or releases;
- change branch protection;
- authorize routine, parallel, automated, unattended, or AFK execution;
- adopt Workflow v1;
- resolve RG1 through RG12;
- establish a baseline.

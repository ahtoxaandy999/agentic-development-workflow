---
id: ADW-WF1-PERSISTENCE-CHECKER-REVIEW-002
artifact: independent-candidate-review
artifact_status: active
owner: independent-review
subject_commit: 8b9feaed2fc3edd955e41a682dd7fc3b013535cc
subject_parent: a275d348652d0e9349d1a355127b5f26e6996028
subject_tree: ee4e11db2d6c6589ac2685672a30ca005e9b80db
predecessor_review_ref: docs/design/ADW-WF1-PERSISTENCE-CHECKER-REVIEW-001.md
reviewed_on: 2026-09-04
normative_effect: none
supersedes: null
---

# Corrected supervised persistence checker independent review

## Result

**CORRECTED CHECKER INDEPENDENT REVIEW COMPLETE**

Verdict: **request-another-corrected-checker-candidate**.

PCR-001 through PCR-005 from REVIEW-001 are substantively resolved in the
exact corrected three-file candidate at commit
`8b9feaed2fc3edd955e41a682dd7fc3b013535cc`. No correction-induced regression
was found. One separate inherited MAJOR defect remains: a schema-valid empty
base leaf inventory causes the checker to skip every tree-binding and delta
predicate, permitting a semantically inconsistent case to return PASS. The
candidate therefore is not suitable to advance to checker disposition.

Counts: **0 BLOCKER / 1 MAJOR / 0 MINOR**.

Proposed next gate: **Workflow v1 supervised persistence checker correction
gate**.

This recommendation is bound only to the exact three-file candidate at the
subject commit. It does not accept or reject the entire publication commit,
accept the Register, authorize operational use, resolve any RG gap, adopt
Workflow v1, establish a baseline, or make a coordinator disposition.

## Exact live and immutable basis

The connected **@GitHub** surface was invoked explicitly and read-only. Initial
live reads and the final point-of-reliance recheck at `2026-09-04T21:09:05Z`
agreed:

- repository: `ahtoxaandy999/agentic-development-workflow`;
- live `refs/heads/main`:
  `8b9feaed2fc3edd955e41a682dd7fc3b013535cc`;
- subject sole ordered parent:
  `a275d348652d0e9349d1a355127b5f26e6996028`;
- subject tree: `ee4e11db2d6c6589ac2685672a30ca005e9b80db`;
- parent-to-subject comparison: status `ahead`, one commit ahead, zero behind,
  one total commit;
- complete changed-path set: `docs/research/research-register.md`,
  `docs/tooling/persistence-checker.md`, `tests/test_persistence_checker.py`,
  and `tools/persistence_checker.py`, with no other path;
- recursive tree: 38 entries, `truncated: false`;
- refs collection: only `refs/heads/main`, at the subject;
- all-state collections: one closed bootstrap-acceptance Issue with zero
  comments, no pull requests, and no releases.

The live branch response reported `protected: false`,
`protection.enabled: false`, and
`required_status_checks.enforcement_level: off`. The dedicated protection
endpoint returned HTTP 403 to the integration, and ruleset enumeration returned
the private-plan HTTP 403. No protection state was inferred from those
unavailable endpoints; the branch response itself supplied the expected
observation.

The complete tree, sole ref, current Register, and all-state collections expose
no competing or superseding current checker candidate or decision. The
Register's Superseded section is `None`. This is a bounded repository finding;
it does not establish writer inactivity or knowledge of unseen local work.

The current Register is mode `100644`, 50,839 bytes, Git blob
`3c3bdd5f0b264f217ab38573c26a4d573764b62c`, and SHA-256
`e14fca6acfc0430c70c202fd7eb5be8a42e1d2b2aefa45e9d1ba8359efd30352`.
Both current fields—the Current bootstrap gate field and the DR-005 field—say
exactly `Workflow v1 supervised persistence checker corrected candidate
independent review gate`. The Register records the predecessor review verdict
`request-corrected-checker-candidate`, binds that review to predecessor commit
`c3a133174ec8187849870c83947dcfc5c7bab7f3`, and states that the corrected
candidate remains unreviewed, unaccepted, and unauthorized for operational
reliance.

Repository-state prerequisites PASS. This review is not blocked by drift.

## Exact subject identities

| Path | Mode | Bytes | Git blob | SHA-256 |
|---|---:|---:|---|---|
| `tools/persistence_checker.py` | `100644` | 59,474 | `7a92561c497a732b80c55c8484ba641c5364a56b` | `9815f48a785ab7b4dc9550cd15f900e530cd6e7e0ad49a3125cecd9145fb6df3` |
| `tests/test_persistence_checker.py` | `100644` | 55,094 | `e8f3095f7d39bdd0aa3df1f4aa7635d361cb1870` | `f394e62a6c981a6214632932dc09ee5cf5d928780482bf2db6eac5716429eb0b` |
| `docs/tooling/persistence-checker.md` | `100644` | 13,431 | `10a99f41c9ffde377f8c3bd85ba7497a1ccbf348` | `6a312aafecce43a5276c691df7b0053091b183444c5fae9cf8c73cd1f1d8bfc2` |

Each identity was independently recomputed from the exact bytes returned by
@GitHub. All three files decode as strict UTF-8 without BOM, contain no CR byte,
use LF only, and have exactly one final LF. Git tree modes and byte counts match
the recursive subject tree.

The predecessor remains commit
`c3a133174ec8187849870c83947dcfc5c7bab7f3`, tree
`7ef3788c84d1e10015e083f03964bb15592278ae`. REVIEW-001 remains blob
`807f34b9f3618255a5a8e58337c0ef83be056997`, verdict
`request-corrected-checker-candidate`, with 0 BLOCKER / 3 MAJOR / 2 MINOR.
It was used only to identify predecessor findings and reproduce PCR-001; it was
not treated as proof about this corrected subject.

## Reviewer eligibility

This is a fresh Independent Review task. The reviewer did not produce the
original checker or corrected checker, did not perform either candidate
persistence, did not author the correction, and did not make a prior
coordinator disposition for this candidate. No material conflict is present in
the available context.

This is procedural eligibility only. A fresh chat, role label, project boundary,
or matching digest is not platform-enforced identity separation. RG4 remains
unresolved.

## Review method and authoritative inputs

The following artifacts were retrieved and read completely at the exact subject
or their controlling immutable identities: `AGENTS.md`, `PROJECT-CHARTER.md`,
the current `docs/research/research-register.md`,
`docs/design/ADW-WF1-PERSISTENCE-CHECKER-GATE-001.md`, REVIEW-001,
`docs/design/ADW-WF1-TOOLING-DESIGN-001.md`,
`docs/design/ADW-WF1-TOOLING-DESIGN-DISPOSITION-001.md`,
`docs/research/ADW-DR-005-DISPOSITION-001.md`, and all three candidate files.
The non-truncated tree binds those paths to their expected blobs.

Review work combined line-by-line code and documentation inspection, exact
predecessor-to-corrected diff inspection, native byte/Git-object calculations,
the candidate's exact immutable unit suite, 33 independent synthetic probe
assertions for PCR-001 through PCR-005 and the newly identified edge case,
static effect/import review, and separate checks of exclusive creation and
BaseException propagation. Producer conclusions and producer PASS labels were
not used as an oracle. No operational checker case was executed.

## Exact test execution

Command:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_persistence_checker.py' -v
```

Runtime: CPython 3.9.6 (`cpython`), executable
`/Library/Developer/CommandLineTools/usr/bin/python3`, Darwin 25.6.0 arm64.

Result: **60 tests run; 60 passed; 0 failures; 0 errors; 0.811 s**.

No `__pycache__`, `.pyc`, or `.pyo` artifact was retained in the immutable
candidate reconstruction. Post-run byte, SHA-256, Git blob, serialization, and
mode checks remained identical to the subject table. The green suite is
supporting evidence only and does not cover the MAJOR empty-inventory defect.

## PCR-001 through PCR-005

### PCR-001 — PASS — empty Git-tree entries

The predecessor defect was independently reproduced against the old immutable
implementation: base tree `18ba2b7249af4e9809956d51eb4c47550e856a79`
contained canonical empty tree
`4b825dc642cb6eb9a060e54bf8d69288fbee4904`; W omitted it; allowed deletions
were empty; the predecessor returned PASS/0.

Against the corrected subject, preflight binds the base leaf inventory to
`base.observed_tree`, readback binds both the base inventory and selected target
inventory to their observed trees, and an explicit empty directory returns
UNEVALUABLE through the stable
`authority.raw_tree.empty_directories_unrepresentable` predicate. The
phase-appropriate inventory tree-binding predicate is also UNEVALUABLE. Silent
empty-directory deletion cannot pass. Ordinary non-empty nested directories
PASS in both phases. Independent native Git hashing confirmed canonical empty
tree identity and mixed-mode nested tree calculations.

### PCR-002 — PASS — non-standard and non-finite JSON numbers

Independent probes covered `NaN`, `Infinity`, `-Infinity`, and `1e9999`
overflow in the case file, raw branch response, and raw recursive-tree response.
All were bounded and non-passing. Raw-response and representable case-overflow
paths produced UNEVALUABLE reports; every written report reparsed with a
rejecting `parse_constant` hook as strict JSON. Case-level non-standard constants
that prevented unambiguous case parsing returned exit 2 with a bounded
diagnostic and no report destination claim.

Report serialization was independently injected with each non-finite float,
including an overflow-produced infinity. Every case used the bounded fallback,
recorded UNEVALUABLE, serialized the safe fixed token
`<invalid-non-finite-number>`, and wrote strict JSON. No unsafe value or
unbounded diagnostic was emitted.

### PCR-003 — PASS — stale authority

An observation before `freshness_cutoff` and one after `evaluation_time` each
returned `authority.freshness: UNEVALUABLE` with aggregate UNEVALUABLE. A stale
case with an independently wrong W tree retained
`inventory.working.tree_binding: FAIL` while aggregate UNEVALUABLE retained
precedence. Freshness alone did not become definite FAIL. This preserves the
stale-evidence denial and recovery meaning required by DI-2.

### PCR-004 — PASS — canonical absolute paths

Four original-string aliases were independently exercised for each of the case
path, read root, and report root: `/./`, `/../`, redundant separators, and a
disallowed trailing separator. All were rejected before normalization. Separate
probes confirmed traversal, component-symlink, and hard-link inode-alias
rejection. Containment and existing-destination protections remained intact.

### PCR-005 — PASS — REST directory modes

Raw REST directory mode `040000` succeeds in valid cases; replacing it with
`40000` makes the raw response malformed and UNEVALUABLE. Independent native
Git hashing confirmed that internal recursive tree framing still uses `40000`:
the candidate and native Git both produced mixed-mode nested tree
`24ba4145369064e8da01079cddd978149f9e577c`. External REST and internal Git
representations are not conflated.

Independent PCR probe result: **33 assertions completed, 0 probe assertion
failures**. Thirty-two assertions establish the five correction groups and
their supporting path/result behavior; the remaining assertion positively
reproduces PCR-006 below.

## Broader regression assessment

The following behaviors conformed in inspection, the exact suite, and targeted
independent probes: valid preflight B+W and readback B+C; rejection of fabricated
preflight C identity; exact candidate commit/sole-parent/tree/ref binding;
non-empty complete inventory and delta comparison; byte count, SHA-256, Git blob,
and full Register before/after byte binding; raw branch/tree conflict and
truncation rejection; duplicate and malformed JSON rejection; Unicode scalar
rejection with valid non-ASCII preservation; FAIL/UNEVALUABLE precedence; safe
exclusive report creation; existing-destination refusal without overwrite;
nonzero report-write failure; and absence of traceback for ordinary malformed
inputs.

Independent monkey-patched probes confirmed that `KeyboardInterrupt`,
`SystemExit`, and a direct `BaseException` subclass propagate rather than being
caught. A second write to an existing report destination returned exit 2,
created no replacement, left the first report byte-identical, and exposed no
traceback.

One complete-inventory edge case fails, as PCR-006 records. No other false PASS,
false FAIL, crash, unsafe path behavior, nondeterminism, or implementation/test/
documentation mismatch was established.

## Findings

### PCR-006 — MAJOR — empty complete base inventory skips tree and delta evaluation

- **Exact location:** `tools/persistence_checker.py` lines 625-629, with the
  skipped checks at lines 630-683 and conditional Register presence checks at
  lines 725-737. Missing edge coverage is adjacent to the non-empty delta tests
  in `tests/test_persistence_checker.py` lines 629-657. The contradicted usage
  claims are `docs/tooling/persistence-checker.md` lines 200-213.
- **Observed defect:** `_inventory` validly returns `{}` for a complete,
  non-truncated inventory whose `entries` list is empty. `inventories_and_delta`
  treats that valid empty mapping like an invalid result and returns at line
  629. It therefore records no base/target tree binding, no computed additions,
  deletions, or modifications, and no unchanged-entry predicate. Later Register
  checks are conditional on path presence and do not restore the omitted base
  binding.
- **Independent reproduction:** a synthetic preflight case used a complete
  empty base inventory bound to canonical empty tree
  `4b825dc642cb6eb9a060e54bf8d69288fbee4904`. The non-empty target added the
  Register, artifact, and stable file, while `allowed_delta` falsely described
  the Register as a modification and described the other two paths as
  additions. All raw branch/tree, byte, freshness, protection, and target
  bindings were otherwise internally valid. The checker returned PASS/0 with
  no predicate containing `tree_binding` and no `delta.*` predicate. The
  Register was in fact an addition, so the complete computed delta did not equal
  authorization.
- **Violated requirement:** the gate's bounded development contract requires
  complete base and target leaf inventories, comparison of the entire
  path/mode/blob delta including untouched entries, and exact Register
  before/after binding. The usage note promises every complete tree is
  recomputed and the complete computed delta equals `allowed_delta`. PASS/0 is
  permitted only when every required enumerated predicate passed; omitted
  mandatory predicates cannot count as pass.
- **Consequence:** a structurally valid but semantically inconsistent case can
  obtain PASS/0 while tree and complete-delta evaluation never occurred. A
  consumer can receive false evidence that an addition was an authorized
  modification. This is material even though the present ADW repository base is
  non-empty.
- **Required correction:** distinguish invalid inventory parsing from a valid
  empty mapping; never skip tree and delta evaluation solely because a complete
  inventory has zero leaves. Always compute/bind the canonical empty tree and
  compare the full delta. Explicitly require the Register path and before/after
  blob bindings in both base and target when the case claims the required
  Register modification. Add positive/negative tests for valid empty inventories
  and for a Register addition mislabeled as a modification.
- **New immutable candidate and renewed review required:** **yes**.
- **Origin classification:** candidate defect inherited from the predecessor and
  newly discovered by this review. It is not introduced by the PCR-001 through
  PCR-005 correction diff, repository drift, or later external-state change.

## Effect and authority review

Static AST and call-site inspection found only standard-library imports:
`datetime`, `hashlib`, `json`, `math`, `os`, `pathlib`, `re`, `stat`, and `sys`.
No subprocess, network, credential, Git write, installation, repair, retry,
scheduling, hook, Action, plugin, skill, or orchestration behavior exists. The
checker remains manually invoked, deterministic for fixed bytes/runtime,
offline, input-read-only, and limited to exclusive creation of one designated
report with mode `0600`. Its documented check/use race and possible partial new
file after an operating-system write failure remain explicit limitations.

The candidate remains inside the narrow D3 development exception as a
non-operational helper. This review does not claim measured usefulness,
preparation-cost benefit, runtime deployment readiness, or operational
correctness. The MAJOR finding prevents checker disposition regardless.

## RG and DI boundaries

RG1-RG12 all remain unresolved. In particular, the helper creates no effective
branch protection, technical writer fencing, permission proof, publication
provenance, platform-enforced reviewer identity, cancellation/containment,
durable recovery, retention/integrity guarantee, installed-capability proof,
optional-integration justification, documentation resolution, or AFK authority.
Canonical path checks, supervision, and exclusive report creation are
procedural containment only.

DI-1 remains preserved: the checker owns no mutable workflow state and does not
convert a branch name, PASS, green test, report, or provider status into review,
disposition, normativity, baseline acceptance, terminal success, or workflow
adoption. Required evidence, mismatch, inability, and external gates remain
distinct.

DI-2 remains preserved: stale or future authority cannot PASS; independent
mismatches remain visible under UNEVALUABLE precedence; the checker performs no
automatic retry, reopening, recovery, compensation, containment claim, history
rewrite, resource release, or terminal transition. PCR-006 is an inventory/delta
omission and does not alter these stale-evidence and recovery boundaries.

## Explicit non-actions and stop boundary

No GitHub mutation, repository mutation, Register update, candidate correction,
review persistence, coordinator acceptance/disposition, operational checker
case, operational reliance, dependency/tool installation, hook, Action,
automation, pull request, Issue, comment, tag, branch, protection change,
routine/parallel/automated/unattended/AFK authorization, Workflow v1 adoption,
RG resolution, or baseline establishment occurred. The immutable candidate and
synced Project source files were not modified. Temporary files contained only
read-only @GitHub reconstructions and synthetic probes under `/tmp`.

This local record is the sole durable output of the review task. It has no
normative effect and is not persisted to the repository. Stop here.

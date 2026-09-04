---
id: ADW-WF1-PERSISTENCE-CHECKER-REVIEW-001
artifact: independent-candidate-review
artifact_status: active
owner: independent-review
subject_commit: c3a133174ec8187849870c83947dcfc5c7bab7f3
subject_parent: 10101a5665026c9b5b9c50b5e51794473df74d21
subject_tree: 7ef3788c84d1e10015e083f03964bb15592278ae
gate_ref: docs/design/ADW-WF1-PERSISTENCE-CHECKER-GATE-001.md
reviewed_on: 2026-09-04
normative_effect: none
supersedes: null
---

# Supervised persistence checker independent review

## Result

**CHECKER INDEPENDENT REVIEW COMPLETE**

Verdict: **request-corrected-checker-candidate**.

The exact three-file candidate at commit
`c3a133174ec8187849870c83947dcfc5c7bab7f3` is not suitable to advance to a
coordinator checker disposition. Three MAJOR defects permit an unlisted empty
Git-tree change or malformed raw JSON to pass, and classify stale evidence as
a definite mismatch rather than an inability. Two MINOR strict-interface
defects also remain.

This verdict does not reject or accept the whole commit, authorize operational
reliance, resolve an RG gap, adopt Workflow v1, establish a baseline, or make a
coordinator disposition.

Proposed next gate: **Workflow v1 supervised persistence checker correction
gate**.

## Exact live and immutable basis

All repository facts below were independently retrieved read-only through the
connected @GitHub surface. Local bytes were used only after their Git blob IDs
were reproduced against the immutable @GitHub objects.

Final live-identity recheck: `2026-09-04T19:57:02Z`.

- Repository: `ahtoxaandy999/agentic-development-workflow`.
- Live `refs/heads/main`: `c3a133174ec8187849870c83947dcfc5c7bab7f3`.
- Subject sole ordered parent:
  `10101a5665026c9b5b9c50b5e51794473df74d21`.
- Subject tree: `7ef3788c84d1e10015e083f03964bb15592278ae`.
- Parent-to-subject comparison: status `ahead`, one commit ahead, zero behind,
  one total commit.
- Complete changed-path set: `docs/research/research-register.md`,
  `docs/tooling/persistence-checker.md`, `tests/test_persistence_checker.py`,
  and `tools/persistence_checker.py`; no other path appeared in the comparison.
- Recursive subject tree: 37 entries, `truncated: false`.
- Sole repository ref returned by the ref collection: `refs/heads/main` at the
  subject commit.
- All-state repository collections returned one closed bootstrap-acceptance
  Issue with zero comments, no pull requests, and no releases.
- Live branch response: `protected: false`, `protection.enabled: false`, and
  `required_status_checks.enforcement_level: off`. The separate protection
  endpoint was unavailable to the installed integration with HTTP 403; the
  branch endpoint itself supplied the expected protection fields. Repository
  ruleset enumeration returned the plan-level 403 documented by GitHub for
  this private repository. No enabled protection or required-check state was
  inferred from those unavailable sub-endpoints.

Exact expected path identities all matched:

| Path | Mode | Bytes | Git blob | SHA-256 |
|---|---:|---:|---|---|
| `docs/design/ADW-WF1-PERSISTENCE-CHECKER-GATE-001.md` | `100644` | 11949 | `0f21b3d4ab45748200545cddbae7963e81f1a229` | `386383e1adba328841075811b3c79515771b7a1bed1ae94d687a40301e16a731` |
| `tools/persistence_checker.py` | `100644` | 57384 | `f4af724cfd8ab108835575ba728fd37eb33b00ec` | `2711015b5b5c815467988fff0616b2baddd2f8e48b2fbb5b9d54fb89f6c0c3d2` |
| `tests/test_persistence_checker.py` | `100644` | 42032 | `4c9686e98400403a3363038f20fd2f783a8a6889` | `898b1f689f3857af5a85107fb7dcd59fbc884cd83df0323a764d40376bd02a79` |
| `docs/tooling/persistence-checker.md` | `100644` | 11990 | `e71988fe405b40f8b1381ca2eecbb4f13544dadd` | `682807291ceef66bc57c697fa72615561a6dbc87576745de907f8b6679d6c128` |
| `docs/research/research-register.md` | `100644` | 50111 | `6c2f67ade7320b7a95988cac2692191a8c58036a` | `d7dce779948f625cd13944facf5a4903039b9a53983a8cf79764fea9f230b122` |

The gate, AGENTS, Charter, accepted tooling design, tooling-design disposition,
and DR-005 disposition blobs match their controlling identities and are absent
from the parent-to-subject diff. The Register contains the one gate pointer,
three candidate pointers, candidate task ID, and the exact next gate
`Workflow v1 supervised persistence checker independent review gate` in both
the Current bootstrap gate and DR-005 mutable locations. Its Superseded section
is `None`. The complete live tree exposes no second checker implementation,
usage record, checker decision, or superseding candidate. Under the Register's
sole-owner rule, no competing current checker decision was found.

Repository-state prerequisites therefore PASS. This review was not blocked by
repository drift.

## Reviewer independence

No known producer/executor conflict exists in this fresh task. The reviewer did
not produce, correct, persist, or previously disposition the subject candidate,
and performed no candidate modification during this review. The available
context does not disclose material participation in candidate production or
persistence.

This is procedural conflict assessment only. RG4 platform-enforced reviewer
identity remains unresolved; a fresh chat, separate project, role label, or
matching digest does not technically enforce independence.

## Findings

Counts: **0 BLOCKER, 3 MAJOR, 2 MINOR**.

### PCR-001 — MAJOR — empty Git-tree entries can be silently removed in preflight

- Exact location: `tools/persistence_checker.py` lines 594-615, 704-786 and
  839-931; codified by `tests/test_persistence_checker.py` lines 415-426.
- Observed defect: `_raw_tree` validates and returns directory evidence, but
  `observation` compares only the leaf map to the selected base inventory.
  Preflight computes W solely from target leaves. A canonical empty directory
  in B changes B's root tree but is absent from both leaf inventories and all
  delta arrays. The candidate's own empty-directory test makes B contain the
  canonical empty tree while W omits it and nevertheless asserts PASS.
- Independent reproduction: B root
  `18ba2b7249af4e9809956d51eb4c47550e856a79` contained empty tree
  `4b825dc642cb6eb9a060e54bf8d69288fbee4904`; W root
  `cc969798129db87d2a2d9d11d3e87114fac1bbf7` omitted it. With otherwise valid
  evidence and no directory deletion in `allowed_delta`, the checker returned
  PASS/0.
- Violated requirement: gate section “Bounded development contract” requires
  the complete delta, including untouched entries, to be compared; accepted
  tooling design section 6.1 requires every untouched tree entry to match B;
  this review contract requires correct canonical empty-directory handling.
- Concrete consequence: a preflight report can authorize a W tree that deletes
  an existing empty Git-tree entry without naming that change. The promised
  exact B-to-W delta is false even though every emitted predicate passes.
- Required correction: either model complete directory inventories for B and W
  and compare/preserve their identities, or reject any base tree containing an
  explicit empty directory when W cannot represent it. Add a negative test for
  unlisted empty-directory deletion and positive tests for explicitly preserved
  directory evidence across both phases.
- New immutable candidate and renewed independent review required: **yes**.

### PCR-002 — MAJOR — non-standard JSON constants can pass as raw GitHub evidence

- Exact location: `tools/persistence_checker.py` lines 92-105 and 1086-1098;
  missing adversarial coverage near `tests/test_persistence_checker.py` lines
  393-401 and 590-628.
- Observed defect: Python's `json.loads` is called without a rejecting
  `parse_constant`, so the non-JSON tokens `NaN`, `Infinity`, and `-Infinity`
  are accepted. `json.dumps` is also called without `allow_nan=False`.
- Independent reproduction: adding `"unrelated_future_field": NaN` to an
  otherwise valid raw branch payload produced PASS/0. Putting NaN in a required
  identity produced UNEVALUABLE/2 but the created report itself contained a
  bare `NaN` token and was not strict JSON.
- Violated requirement: the gate requires a small strict JSON case, malformed
  input to be UNEVALUABLE, and a deterministic JSON report; the review contract
  specifically requires malformed raw evidence not to pass.
- Concrete consequence: bytes that cannot be a conforming GitHub REST JSON
  response can receive a PASS report, and malformed case values can escape into
  a non-portable report serialization.
- Required correction: reject all non-finite parse constants in every JSON
  document, reject non-finite numeric values recursively if necessary, and
  serialize reports with `allow_nan=False` inside the bounded fallback. Add
  direct case, branch-response, tree-response, and report tests for all three
  non-finite constants.
- New immutable candidate and renewed independent review required: **yes**.

### PCR-003 — MAJOR — stale authority evidence is reported as FAIL rather than UNEVALUABLE

- Exact location: `tools/persistence_checker.py` lines 543-552;
  `tests/test_persistence_checker.py` lines 665-669.
- Observed defect: the freshness predicate uses the default definite-mismatch
  result. An observation before `freshness_cutoff` returns FAIL/1, and the test
  explicitly requires that classification.
- Violated requirement: this review contract defines stale evidence as
  UNEVALUABLE/2 and reserves FAIL/1 for definite mismatch without inability.
  AGENTS and the accepted DI-2 boundary require stale authority to block
  reliance and be escalated rather than treated as current evidence about a
  mismatching subject.
- Concrete consequence: a consumer can be directed toward candidate correction
  for what is actually an evidence reacquisition problem. The nonzero exit still
  blocks PASS, but the result plane and recovery meaning are wrong.
- Required correction: classify a stale or post-evaluation observation as
  UNEVALUABLE while retaining any independently detected FAIL predicates; update
  stale/unavailable/simultaneous tests to assert the distinct result meanings.
- New immutable candidate and renewed independent review required: **yes**.

### PCR-004 — MINOR — absolute root normalization aliases are accepted

- Exact location: `tools/persistence_checker.py` lines 141-160; contrary usage
  statement at `docs/tooling/persistence-checker.md` lines 35-39.
- Observed defect: `_assert_no_symlink` converts the supplied string to `Path`
  before comparing it with `os.path.abspath`. That conversion removes `./`,
  redundant interior separators, and a trailing separator. A case with both
  read and report roots written using `/./` returned PASS/0.
- Violated requirement: canonical absolute roots and rejection of normalization
  aliases.
- Concrete consequence: the strict interface accepts multiple textual names for
  one root. No containment escape was reproduced, but strict identity and alias
  diagnostics are weaker than documented.
- Required correction: compare the original string with its canonical absolute
  form before constructing `Path`, and test dot, redundant-separator, and
  trailing-separator aliases.
- New immutable candidate and renewed independent review required: **yes** if
  corrected with the required candidate changes.

### PCR-005 — MINOR — raw recursive-tree mode validation accepts a non-API spelling

- Exact location: `tools/persistence_checker.py` lines 868-871.
- Observed defect: a raw directory entry accepts both `040000` and `40000`.
  GitHub's REST tree mode enumeration names `040000` for a tree; `40000` is the
  internal canonical Git tree framing spelling, not the documented REST field
  spelling. Replacing every raw directory mode with `40000` still returned
  PASS/0.
- Violated requirement: validate exact-byte raw GitHub recursive-tree response
  semantics while permitting only unrelated ordinary REST fields.
- Concrete consequence: a normalized or fabricated load-bearing directory field
  can pass as though it were an exported GitHub response. Root hashing itself
  remained correct.
- Required correction: require `040000` at the REST parsing boundary and keep
  `40000` only for the reconstructed Git tree frame; add a negative test.
- New immutable candidate and renewed independent review required: **yes** if
  corrected with the required candidate changes.

## Scenario and semantic results

1. Valid preflight B+W: PASS in the candidate suite; phase schema excludes C.
2. Valid readback B+C: PASS; C commit/tree/ref and sole ordered parent B are
   transitively bound to the raw branch and target tree evidence.
3. Fabricated C in preflight: UNEVALUABLE through strict identity shape.
4. Wrong base/candidate/tree/parent/ref: detected as FAIL or UNEVALUABLE for a
   malformed/conflicting identity; branch name or generic completion state is
   not used as an identity substitute.
5. Wrong bytes/size/SHA-256/Git blob: FAIL with the expected independent
   predicates.
6. Invalid UTF-8, BOM, CR, and final-LF state: FAIL; strict UTF-8 and valid
   non-ASCII are distinguished.
7. Unexpected additions, deletions, modifications, and modes: FAIL for leaf
   inventory deltas.
8. Changed supposedly unchanged leaf: FAIL.
9. Incorrect full Register before/after bytes: FAIL; both inventory blobs and
   the observed-after binding are checked.
10. Missing fields, duplicate keys/paths, wrong types, and ordinary structural
    conflicts: UNEVALUABLE, except the non-finite JSON defect PCR-002.
11. Raw branch/tree conflict and `truncated: true`: UNEVALUABLE; required branch
    commit/tree/parent/ref relationships are cross-checked.
12. Missing or wrong implied directory evidence: UNEVALUABLE; canonical empty
    tree hashing is correct in isolation, but cross-phase preservation fails as
    PCR-001.
13. Unavailable authority: UNEVALUABLE. Stale authority is incorrectly FAIL as
    PCR-003.
14. Traversal, component symlink, case outside roots, existing/out-of-scope
    destination, and synthetic report-write failure: safely nonzero with no
    overwrite. Canonical-root spelling is incomplete as PCR-004. The documented
    check/use race remains external and is not technical writer fencing.
15. Escaped unpaired UTF-16 surrogate: UNEVALUABLE with sanitized report; valid
    non-ASCII Unicode: PASS.
16. Simultaneous mismatch and authority inability: overall UNEVALUABLE while the
    tested FAIL predicate remains present.
17. Report order and identity: deterministic for fixed bytes/runtime; required
    provenance limitations, non-authority statements, phase model, and pending
    gates are present, subject to PCR-002's non-finite serialization defect.
18. Prohibited behavior: static inspection found no network, Git, subprocess,
    credential, repair/retry, hook, Action, schedule, orchestration, workflow
    transition, repository mutation, or acceptance/operational-authority path.
    The only write path is exclusive report creation.

Independent hash review reproduced the expected candidate/test/usage identities
and matched the checker tree computation for `100644`, `100755`, `120000`, and
`160000` leaves against native Git hashing. Nested ordering, UTF-8 path bytes,
Git blob framing, and canonical empty-tree identity were otherwise correct.

## Test execution and quality

The exact immutable candidate suite ran under the contract's minimum runtime:

- runtime: CPython 3.9.6;
- command boundary: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v
  tests/test_persistence_checker.py` in an isolated local reconstruction of the
  two exact @GitHub blobs;
- result: 44 tests run, 44 passed, 0 failures, 0 errors, approximately 0.624 s;
- retained bytecode: none.

The tests are meaningful for the principal positive/negative leaf, identity,
Register, Unicode, result-precedence, raw-conflict, and filesystem cases. Blob
constants are fixed external-native vectors; tree logic is separately coded and
checks the canonical empty-tree constant, although it largely mirrors the
implementation and lacks a fixed non-empty mixed-mode Git vector. More
importantly, the suite positively codifies PCR-001 and omits the adversarial
inputs in PCR-002, PCR-004, and PCR-005; it also codifies the wrong stale-result
semantics in PCR-003. The green suite is therefore insufficient evidence of
contract conformance.

This execution was synthetic review evidence only. No operational persistence
case was run.

## Usefulness and proportionality

The candidate remains manually invoked, deterministic, offline, standard-library
Python, read-only with respect to inputs, and an exclusive report creator. Its
effects remain a narrow D3 exception, not an automation or operational system.

It consolidates many error-prone byte, identity, inventory, and raw-response
checks into one report. However, the three-file package is 111,406 bytes before
the Register update, the implementation is 57,384 bytes, and preparation still
requires complete inventories, multiple Register byte copies, two raw payloads,
and independent expected identities. That is substantial preparation and
maintenance for a “small” helper. No measured time/error reduction is available.
This does not create a separate correctness finding, but proportional benefit,
case-preparation cost, removal/maintenance cost, and runtime deployment remain
explicit later validation items. Operational reliance remains unauthorized.

## RG and DI boundary result

No RG1-RG12 gap is resolved.

- RG1: live unprotected main continues to block routine, parallel, automated,
  product-dogfooding, and AFK writes; this review grants no write authority.
- RG2-RG5: the checker proves no technical writer fence, permission boundary,
  publication provenance, or platform-enforced reviewer identity. Canonical and
  exclusive-create checks are procedural containment only.
- RG6-RG9: cancellation, cross-domain containment, recovery, custody/retention,
  and installed/runtime capability remain external later evidence. This review
  verifies only CPython 3.9.6 execution of the synthetic suite.
- RG10-RG11: value and optional-integration/documentation questions remain in
  their existing scopes; no integration was selected.
- RG12: no unattended or AFK eligibility is created.

DI-1 is preserved: the checker owns no mutable workflow state, does not turn a
branch name/green status/PASS into review, disposition, normativity, acceptance,
or terminal success, and keeps pending external gates explicit. DI-2's
no-reliance-on-stale effect is preserved because stale input cannot PASS, but
PCR-003 misclassifies that inability as a definite mismatch and must be corrected
before checker disposition. No automatic retry, reopening, recovery, containment,
history rewrite, resource release, or terminal transition is implemented.

## Explicit non-actions

No GitHub mutation, commit, push, branch/ref update, pull request, Issue/comment,
release, Register update, protection/ruleset change, candidate edit, correction
candidate, coordinator disposition, operational checker run, operational
reliance authorization, dependency/tool installation, hook, Action, schedule,
automation, delegation, parallel execution, AFK enablement, Workflow v1 adoption,
or baseline acceptance occurred. Repository access was read-only. Synced project
source files were not modified.

This local record is the only durable review output of this task and has no
normative effect.

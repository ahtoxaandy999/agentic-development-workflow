---
id: ADW-WF1-DESIGN-REVIEW-002
artifact_status: active
authority: evidence
review_type: independent-design-review
review_target_commit: bca878ea3a2576ef2c354bac00e0049041d616e1
review_target_parent: c8db8c04ec8843f0cbe6e3b05a93d8962e47d08e
review_target_path: docs/design/ADW-WF1-DESIGN-001.md
review_target_blob: f76c7df6686b3c338d261860e9c4aa3f72da5480
review_target_bytes: 94494
review_target_sha256: c092af2f72cffd7d022dfce8712ea729c744b541f9d731e12b5683c2b1ceb203
verdict: require-new-design-candidate
reviewed_on: 2026-09-03
owner: agentic-development-independent-review
supersedes: null
---

# Workflow v1 Corrected Design Independent Review

All live repository facts in this review were independently verified through GitHub. The final `main` reread still resolved to candidate-002.

## A. Exact reviewed identity

| Field | Independently verified value |
|---|---|
| Repository | `ahtoxaandy999/agentic-development-workflow` |
| Live `main` | `bca878ea3a2576ef2c354bac00e0049041d616e1` |
| Candidate-002 | `bca878ea3a2576ef2c354bac00e0049041d616e1` |
| Sole parent | `c8db8c04ec8843f0cbe6e3b05a93d8962e47d08e` |
| Candidate artifact | `docs/design/ADW-WF1-DESIGN-001.md` |
| Artifact blob | `f76c7df6686b3c338d261860e9c4aa3f72da5480` |
| Raw bytes | `94494` |
| Independently computed SHA-256 | `c092af2f72cffd7d022dfce8712ea729c744b541f9d731e12b5683c2b1ceb203` |
| Research Register blob | `b9b4a7b7f4edb302014bbcb498a619155cb23161` |
| Correction-basis review blob | `f2df1186f72374f8386d531117b13a80bc42b1bb` |

Front matter was verified as:

- `design_stage: initial-design-complete`
- `artifact_status: draft`
- `normative_effect: none`

The Research Register records:

- `next_gate: Workflow v1 corrected design independent review gate`
- Workflow v1 remains unadopted.
- DR-005 is deferred with its dependency unsatisfied.

The prior review record remains bound to candidate-001 `24b378832f4edc8ec55d7f3063114dc536d7e24e`, target blob `d164c7f9c4461572f26707fd747ed886e6b0ed93`; it does not review candidate-002.

Review-subject verification result: **PASS — exact subject established.**

## B. Correction resolution

### ADW-WF1-DR-MAJ-001: RESOLVED

The join rules are now consistent:

- A join may pass only after current required integrated verification succeeds, or after legitimate non-applicability is recorded with its governing rule and rationale.
- Pending, failed, stale, missing, conflicted, or silently omitted required verification prevents pass.
- Required integrated-verification failure produces `join=failed`.
- Candidate formation and task completion expressly reject a relied-upon non-passing join.
- Disposition requires all applicable gates to be effective.
- Material change or stale load-bearing evidence invalidates an earlier pass and returns the join to pending.
- Required and optional branches remain separately accounted.

No materially divergent compliant join implementation remains.

### ADW-WF1-DR-MAJ-002: REGRESSION INTRODUCED

The original duplicated containment states and missing cancellation/abandonment transitions are corrected. Containment now resides in the cancellation plane, and request, acknowledgement, containment, terminal cancellation, and abandonment have distinct mutations, owners, predicates, and evidence.

However, the newly expanded recovery state machine introduces two material transition defects:

1. `task control=recovering; recovery=intervention-required` can be entered but has no defined exit.
2. Successful non-cancellation recovery resumes without resetting `recovery=recovered`, preventing a later recovery cycle under the declared source predicates.

Thus the corrected area still does not have one implementable recovery/resumption interpretation. These defects are represented by ADW-WF1-DR-MAJ-003 and ADW-WF1-DR-MAJ-004.

## C. Overall verdict

REQUIRE NEW DESIGN CANDIDATE

## D. Findings

Finding counts:

- BLOCKER: 0
- MAJOR: 2
- MINOR: 0

### ADW-WF1-DR-MAJ-003

- Severity: **MAJOR**
- Location: recovery transition rows, lines 750–754, particularly lines 751–753; protocol line 983.
- Ambiguity/contradiction: The authorization and action-recording transitions may produce `task control=recovering; recovery=intervention-required`. The recovery-conclusion transition excludes `intervention-required` from its source set, while all other exit transitions require `active` or `blocked`. This makes the permitted state a transition sink, despite the protocol saying unsuccessful recovery returns to `blocked; intervention-required`.
- Smallest counterexample: A blocked task begins recovery. During recovery authorization, unresolved ambiguity requires intervention. A literal implementation records `recovering/intervention-required` and can never exit. Another implementation infers an unlisted transition to `blocked/intervention-required` so escalation or renewed recovery can occur.
- Impact: Implementations diverge on whether intervention, cancellation closure, abandonment, or renewed recovery remains reachable.
- Another candidate required: **Yes.**

### ADW-WF1-DR-MAJ-004

- Severity: **MAJOR**
- Location: unmentioned-plane retention and ordinary resume at lines 735 and 742; recovery source, conclusion, and reset rules at lines 750–754.
- Ambiguity/contradiction: Non-cancellation recovery concludes as `task control=blocked; cancellation=none; recovery=recovered`. Ordinary resume modifies only task control and cancellation, so the explicit retention rule leaves recovery as `recovered`. A later recovery may begin only from `not-applicable` or `intervention-required`. Only cancellation-specific resume explicitly resets recovery.
- Smallest counterexample: A task completes one non-cancellation recovery and resumes. It later experiences another recoverable failure. A literal implementation retains `recovery=recovered` and must deny the new recovery transition; another resets recovery implicitly to `not-applicable` and permits it.
- Impact: Repeated recovery behavior materially differs, and a long-running task can become irrecoverably stuck after its first successful recovery.
- Another candidate required: **Yes.**

No BLOCKER or MINOR findings.

## E. Regression assessment

| Area | Assessment | Reason |
|---|---|---|
| Lifecycle | **FAIL** | Recovery introduces an entered-but-unexitable state and a missing non-cancellation reset. |
| Ownership | **PASS** | Decision authority, evidence suppliers, and the sole mutable execution-state recorder are distinguishable; aggregation ownership remains separate. |
| Join/integrated verification | **PASS** | Ordering, non-applicability, failure, staleness, candidate reliance, and invalidation are coherent. |
| Cancellation/containment | **PASS** | Generic stop, request, acknowledgement, verified containment, residual effects, and resource restrictions are separated and fail closed. |
| Recovery/resumption | **FAIL** | Findings MAJ-003 and MAJ-004 produce material transition divergence. |
| Completion/cancelled/abandoned terminal semantics | **PASS WITH QUALIFICATION** | Their direct predicates, authority, evidence, and durable effects are clear, but recovery-generated sink states can make legitimate terminal paths unreachable. |
| Candidate/review lifecycle | **PASS** | Immutable identity, impact analysis, affected reverification, renewed review, disposition, adoption, and baseline acceptance remain distinct. |
| Accepted-input preservation | **FAIL** | DR-001 and DR-002 remain preserved; DR-003 PR10 is not fully operationalized by the recovery graph. |

Generic stopping, blocked-state cancellation requests, cancellation recovery, residual-effect ownership, resource retention under containment uncertainty, and abandonment safeguards otherwise remain fail closed.

## F. Implementer-consistency test

**YES.**

Two competent implementers could still produce materially different required behavior while honestly claiming compliance:

- one deadlocks at `recovering/intervention-required`, while another invents a transition to `blocked/intervention-required`;
- one retains `recovery=recovered` after ordinary resumption and rejects a second recovery cycle, while another implicitly resets it to `not-applicable`.

These are required workflow-state differences, not interchangeable mechanism choices.

## G. Conformance scenarios

“Operative” means the scenario supplies a discriminating state or denial outcome suitable as a conformance oracle.

| Scenario | Assessment |
|---|---|
| Legitimately omitted conditional gate | **PASS — operative** |
| Falsely claimed gate pass | **PASS — operative** |
| Stale state before transition | **PASS — operative** |
| Missing required parallel result | **PASS — operative** for the material non-passing invariant; `partial` versus `failed` remains contextual but neither permits reliance. |
| Required integrated-verification failure | **PASS — operative** |
| Required integrated-verification success | **PASS — operative** |
| Legitimate integrated-verification non-applicability | **PASS — operative** |
| Material candidate correction | **PASS — operative** |
| Generic stop without cancellation | **PASS — operative** |
| Cancellation requested but not acknowledged | **PASS — operative** |
| Acknowledged but containment unverified | **PASS — operative** |
| Verified containment and clean cancellation closure | **PASS — operative** |
| Residual effects delaying cancellation | **PASS — operative**, but it does not exercise the intervention-required sink. |
| Explicit abandonment | **PASS — operative** |
| Fresh-context rehydration | **PASS — operative** |
| Unattended denial with incomplete evidence | **PASS — operative** |
| Optional parallel result omitted | **PASS — operative** |
| Ambiguous retry | **PASS — operative** |
| Executor proposes scope expansion | **PASS — operative** |
| Carried-forward evidence after correction | **PASS — operative** |

The supplied scenarios do not cover either failed recovery entering `intervention-required` or a second non-cancellation recovery cycle. Consequently, they do not expose ADW-WF1-DR-MAJ-003 or ADW-WF1-DR-MAJ-004.

## H. Accepted-input boundary

Not fully preserved operationally.

- **DR-001:** Preserved, including state separation, single ownership, immutable identity, freshness, durability, contextual review, and proportionality qualifications.
- **DR-002:** Preserved, including contextual readiness, executability/verifiability, qualified decomposition, conditional vertical slicing, feedback separation, and mechanism neutrality.
- **DR-003:** Delegation, parallelism, joins, rehydration, evidence, candidate correction, cancellation separation, least privilege, unattended denial, and mechanism deferral are preserved. PR10’s operation-aware recovery requirement is not fully implemented because the recovery graph cannot deterministically exit or repeat.
- Qualifications against universal schemas, thresholds, reviewer counts, concurrency values, autonomy, and mechanism selection remain intact.

## I. DR-005 boundary

**PASS.**

Mechanism selection remains deferred. DR-005 is still planned, deferred, and dependency-unsatisfied; no tooling, storage, tracker, orchestration, identity, logging, isolation, or automation mechanism is selected.

## J. Authority boundary

Confirmed:

- Candidate-002 remains non-normative.
- Workflow v1 remains unadopted.
- This rereview neither accepts nor adopts the candidate or workflow.
- DR-005 remains blocked.
- No routine repository-write authority is created.
- No parallel direct-main write authority is created.
- No automated, unattended, or AFK write authority is created.

## K. Repository write status

No GitHub write performed.

## L. Next gate

Workflow v1 design correction gate

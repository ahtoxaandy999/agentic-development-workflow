---
id: ADW-D13-PREREQUISITE-DESIGN-CORRECTION-001
artifact: d13-prerequisite-design-correction
artifact_status: proposed
authority: design-correction
owner: architecture-design-producer
normative_effect: none
produced_on: 2026-09-16
repository: ahtoxaandy999/agentic-development-workflow
applies_to_path: docs/design/ADW-D13-PREREQUISITE-DESIGN-001.md
applies_to_blob: 52cb46ee84634e7e7948b12e16a4cc7b4af5a34c
applies_to_sha256: bf14dc409aa9f34460917564493f63cfd2b268e3b35c918301aaeef42efb6d0a
replaces_section: "5.4 Exhaustive restart/reconciliation projection"
correction_scope: F-04R-only
supersedes: null
---

# ADW-D13-PREREQUISITE-DESIGN-CORRECTION-001

## Purpose and scope

This is a bounded producer correction to the exact proposed design identified above.

For candidate review, the complete Section 5.4 of `ADW-D13-PREREQUISITE-DESIGN-001.md` at blob `52cb46ee84634e7e7948b12e16a4cc7b4af5a34c` is replaced by the section below. No other section, authority boundary, mechanism disposition, conformance layer, writer-fencing rule, side-effect rule, or non-authority is changed by this correction.

The correction closes only the remaining restart-projection ambiguity identified as `F-04R`: awaiting-candidate states without fresh reviewer-dispatch authority and recovery from pre-crash `BLOCKED` must still resolve to one deterministic projection result.

This artifact is a candidate correction delta, not an independent review record and not a second normative design owner. It must be normalized into the primary design artifact before protected publication. Until normalization, the exact review subject is the frozen Git candidate containing both the primary design blob and this exact correction artifact.

It does not authorize implementation, conformance execution, mechanism selection, D5/D13 reconsideration, PoC execution, repository publication, ready/merge, parallel writers, reviewer-to-GitHub mutation, unattended/AFK operation, or Workflow v1 amendment.

## Replacement Section 5.4

### 5.4 Exhaustive restart/reconciliation projection

Every controller restart first enters `RECONCILING` as an **internal evaluation phase only**. `RECONCILING` is not itself a projection result. The controller must evaluate this tuple:

```text
pre-crash runtime phase
+ current authoritative semantic state
+ journal evidence
+ live worker/reviewer state
+ authoritative writer claim/generation
+ workspace/Git state
+ outstanding external effects
```

The evaluation must terminate in exactly one of these result classes:

1. `RESUME_SAME_IDENTITY`: resume the same exact worker/reviewer/operation identity and preserve the same current writer generation where applicable;
2. `RECOGNIZE_COMPLETED`: establish by exact readback that the pre-crash operation already completed and project to the exact next runtime phase without repeating it;
3. `REPLACE_AFTER_CONTAINMENT`: start a replacement identity only after predecessor containment, effect reconciliation, fresh authority and, for writers, successful acquisition of a strictly newer fencing generation;
4. `BLOCKED`: continuation requires intervention, authority or evidence that is not currently sufficient;
5. `TERMINATED`: current authoritative semantic state ends the episode or the one-correction ceiling produces a defined non-continuable result, and all consequential effects are reconciled/contained.

No implementation may choose between these result classes by preference. A recognized fact such as “candidate C1 already exists” may be retained as evaluation evidence, but the final restart projection still resolves to exactly one result class above.

#### Universal guards

The following rules apply before phase-specific projection:

* If current authoritative task/cancellation/recovery state denies further execution and all live effects are proven contained/reconciled, result is `TERMINATED`.
* If current authority denies continuation but a worker/effect may still be live or ambiguous, result is `BLOCKED` until containment/reconciliation proves a terminal projection.
* If authority is stale, conflicting or cannot resolve the designated execution-state owner/recorder, result is `BLOCKED`.
* If the journal is missing/corrupt and live evidence cannot prove writer/effect safety, result is `BLOCKED`.
* If an outstanding consequential effect has ambiguous completion, result is `BLOCKED` until Section 11 reconciliation establishes non-occurrence, exact completion or intervention.
* A stale writer generation is never resumed. It must be denied at write boundaries and contained before any replacement generation can exist.
* A reviewer bound to a different candidate, inherited executor history or effective candidate-write authority is not resumable as an independent reviewer.
* If an awaiting-candidate phase already has an exact candidate/readiness bundle but the fresh semantic permission required for reviewer dispatch is absent, the candidate/readiness completion is retained as exact evidence and the final restart projection is `BLOCKED`; readiness never implies dispatch permission.
* If a pre-crash `BLOCKED` episode becomes recoverable, the controller may re-enter `RECONCILING` only as an internal evaluation step using the durably retained predecessor phase/operation identity. That evaluation must immediately terminate in one of the five result classes. If the predecessor continuation target cannot be uniquely reconstructed, result is `BLOCKED`.

#### Phase-specific projection

| Pre-crash phase | Deterministic projection |
| --- | --- |
| `EXECUTOR_ACTIVE` | If the exact executor is live, current authority still permits the same operation, its writer claim/generation remains current, and no ambiguous effect exists: `RESUME_SAME_IDENTITY` to `EXECUTOR_ACTIVE`. If exact readback proves the executor operation completed and no live writer remains: `RECOGNIZE_COMPLETED` to `AWAITING_AUTHORITATIVE_CANDIDATE`. If the predecessor is proven contained, workspace/Git/effects are reconciled, current authority permits replacement, and a new generation is atomically acquired: `REPLACE_AFTER_CONTAINMENT` to `EXECUTOR_ACTIVE`. Otherwise: `BLOCKED`. |
| `AWAITING_AUTHORITATIVE_CANDIDATE` | If current authority ends the episode and all effects are reconciled/contained: `TERMINATED`. If the C1/readiness bundle is incomplete or candidate/effect state is ambiguous: `BLOCKED`. If no live writer/effect remains and exact C1 plus required verification/readiness evidence is established, the prior candidate-production operation is recognized as completed and C1 is not recreated. From that exact recognized state: if fresh authoritative review-dispatch permission is present, result is `RECOGNIZE_COMPLETED` to one new fresh R1 in `REVIEWER_ACTIVE`; if that permission is absent, result is `BLOCKED` with C1/readiness retained as established evidence. No other result is permitted. |
| `REVIEWER_ACTIVE` | If the same exact R1 is live, still independent, still bound to unchanged C1 and current authority permits continuation: `RESUME_SAME_IDENTITY` to `REVIEWER_ACTIVE`. If exact review evidence proves R1 already completed: `RECOGNIZE_COMPLETED`; PASS projects to `STOPPED_BEFORE_ACCEPTANCE`; correction-required may enter `CORRECTION_ACTIVE` only after fresh authoritative correction permission and valid writer fencing, otherwise the final result is `BLOCKED` with the verdict retained. If R1 failed/stopped without verdict and is proven contained, a replacement must be a new fresh reviewer identity under fresh review-dispatch authority: `REPLACE_AFTER_CONTAINMENT` to `REVIEWER_ACTIVE`; if that authority is absent, result is `BLOCKED`. Ambiguity gives `BLOCKED`. |
| `CORRECTION_ACTIVE` | If the same authorized executor is live, its current writer generation is valid, current authority still permits the one correction and no ambiguous effect exists: `RESUME_SAME_IDENTITY` to `CORRECTION_ACTIVE`. If correction activity is proven complete and predecessor cannot write further: `RECOGNIZE_COMPLETED` to `AWAITING_NEW_AUTHORITATIVE_CANDIDATE`. If the executor must be replaced, replacement requires predecessor containment/reconciliation, fresh correction authority and a strictly newer fencing generation: `REPLACE_AFTER_CONTAINMENT` to `CORRECTION_ACTIVE`. Otherwise: `BLOCKED`. |
| `AWAITING_NEW_AUTHORITATIVE_CANDIDATE` | If current authority ends the episode and all effects are reconciled/contained: `TERMINATED`. If the C2/readiness bundle is incomplete or candidate/effect state is ambiguous: `BLOCKED`. If no live writer/effect remains and exact C2, `C2 != C1`, plus affected verification/readiness evidence is established, the prior correction/candidate-production operation is recognized as completed and C2 is not recreated. From that exact recognized state: if fresh authoritative re-review permission is present, result is `RECOGNIZE_COMPLETED` to one new fresh R2 in `FRESH_REVIEWER_ACTIVE`; if that permission is absent, result is `BLOCKED` with C2/readiness retained as established evidence. No other result is permitted. |
| `FRESH_REVIEWER_ACTIVE` | If the same exact R2 is live, still independent and bound to unchanged C2 and current authority permits continuation: `RESUME_SAME_IDENTITY` to `FRESH_REVIEWER_ACTIVE`. If exact review evidence proves PASS: `RECOGNIZE_COMPLETED` to `STOPPED_BEFORE_ACCEPTANCE`. If exact valid R2 verdict requires another content correction, the one-correction ceiling is exhausted: `TERMINATED`. If R2 failed/stopped without verdict and is proven contained, a replacement may be a new fresh reviewer under fresh re-review authority: `REPLACE_AFTER_CONTAINMENT` to `FRESH_REVIEWER_ACTIVE`; if that authority is absent, result is `BLOCKED`. Ambiguity gives `BLOCKED`. |
| `BLOCKED` | If current authority explicitly ends the episode and all effects are reconciled/contained: `TERMINATED`. If no fresh recovery/resumption authority exists, any blocking predicate remains unresolved, or the predecessor phase/operation identity cannot be uniquely reconstructed: `BLOCKED`. Otherwise the controller uses the durably retained predecessor phase/operation identity and current evidence to run an internal `RECONCILING` evaluation, then applies that predecessor phase's row above. The final result must be exactly `RESUME_SAME_IDENTITY`, `RECOGNIZE_COMPLETED`, `REPLACE_AFTER_CONTAINMENT`, `BLOCKED`, or `TERMINATED`; `RECONCILING` is never the returned projection result. Silence or elapsed time never clears the block. |

A phase not listed above cannot be inferred from a nearby phase. `STOPPED_BEFORE_ACCEPTANCE` and `TERMINATED` remain terminal after restart and permit no new controller effect.

## Candidate semantics and normalization requirement

For this candidate only, the replacement section above is the effective proposed Section 5.4 and supersedes Section 5.4 in the exact target design blob named in front matter. All other sections remain exactly those of the target design blob.

A fresh independent reviewer must review the complete composite candidate and explicitly determine whether this delta closes `F-04R` without regression. This correction artifact itself is not review evidence.

Before any coordinator-accepted design is protected-published, the accepted composite semantics must be normalized back into `docs/design/ADW-D13-PREREQUISITE-DESIGN-001.md`; that normalization creates a new immutable publication candidate and requires exact affected verification/review of equivalence before publication.

## Review subject status

This correction record and the primary design blob it names jointly define the proposed candidate semantics for independent review. Producer-context assessments after this correction are correction input only and do not satisfy the independent-review gate.

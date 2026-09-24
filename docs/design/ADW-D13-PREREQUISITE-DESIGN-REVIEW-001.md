---
id: ADW-D13-PREREQUISITE-DESIGN-REVIEW-001
artifact_status: active
authority: evidence
review_type: independent-design-review
review_scope_status: predecessor-only
reviewed_on: 2026-09-16
owner: agentic-development-independent-review
review_target_kind: external-exact-bytes
review_target_bytes: 65733
review_target_sha256: eb06edc9b27c2c3a01210e8340f85a89723594f719b5c380fd75b76cd04fc9f8
review_target_git_blob_if_materialized_verbatim: 320214335252f8dcca7194b3ae442ff0e18e4c83
live_basis_commit: 796fef15a7ba3b78b57c1f06f5911c6a3f85dad5
live_basis_tree: 9c582a9cd004030bc7d0f10a58e6c77243997097
verdict: requires-correction
finding_counts:
  blocker: 2
  major: 3
  minor: 0
  note: 2
source_review_record_sha256: 8df8cc56e20fe8599d0e8fd750a0c10f18677d6d900dbcba39336990af7792ad
source_review_record_bytes: 37888
source_review_verbatim_persistence_commit: d64c2aebfd202e2ca58ea63930ed874a130df07a
source_review_verbatim_blob: b4891a60c9e2837b9966bbbdd618653f913168ba
supersedes: null
---

# ADW-D13-PREREQUISITE-DESIGN-REVIEW-001

## Review status

**REQUIRES CORRECTION**

This record preserves the independent adversarial review of the predecessor, pre-correction `ADW-D13-PREREQUISITE-DESIGN-001` subject identified above.

It does **not** review or approve the corrected repository candidate now present at `docs/design/ADW-D13-PREREQUISITE-DESIGN-001.md`. Material correction created a new review subject, so a fresh independent affected review is still required.

The original independent review text was persisted verbatim at commit `d64c2aebfd202e2ca58ea63930ed874a130df07a`, blob `b4891a60c9e2837b9966bbbdd618653f913168ba`. This normalized record replaces chat-local citation tokens with durable repository identities while preserving the verdict, findings, failure modes, and required corrections.

## Controlling basis

The review verified live repository state at:

- `main`: `796fef15a7ba3b78b57c1f06f5911c6a3f85dad5`
- tree: `9c582a9cd004030bc7d0f10a58e6c77243997097`

Applicable authority:

- [`AGENTS.md`](../../AGENTS.md)
- [`PROJECT-CHARTER.md`](../../PROJECT-CHARTER.md)
- [`WORKFLOW-V1.md`](../../WORKFLOW-V1.md)
- [`docs/research/research-register.md`](../research/research-register.md)
- [`docs/research/ADW-DR-005-DISPOSITION-001.md`](../research/ADW-DR-005-DISPOSITION-001.md)
- [`docs/research/ADW-DR-006.md`](../research/ADW-DR-006.md)
- [`docs/research/ADW-DR-006-SOURCE-REVIEW-001.md`](../research/ADW-DR-006-SOURCE-REVIEW-001.md)
- [`docs/research/ADW-DR-006-DISPOSITION-001.md`](../research/ADW-DR-006-DISPOSITION-001.md)
- [`docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md`](ADW-WF1-TASK-CONTROL-REFERENCE-001.md)
- [`docs/design/ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-OPERATIONAL-USE-SCOPING-001.md`](ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-OPERATIONAL-USE-SCOPING-001.md)

The controlling DR-006 disposition preserved:

- D5: `CONFIRM DEFER`
- D13: `CONFIRM DEFER`
- X3: `CONFIRM REJECT`
- exactly one bounded D13 prerequisite design/propose gate
- no PoC, mechanism-selection, implementation, conformance-execution, reviewer-to-GitHub, unattended/AFK, ready, merge, or Workflow v1 amendment authority.

## Finding summary

| ID | Severity | Predecessor design area | Finding |
|---|---|---|---|
| F-01 | BLOCKER | Conformance Stage 2 / evidence contract | Fixture/test-double evidence was not sufficiently separated from actual D13 conformance evidence. |
| F-02 | BLOCKER | Writer exclusivity / claim model | The active writer claim was bookkeeping/invariant, not an enforceable semantic fence against stale/concurrent writers. |
| F-03 | MAJOR | Authority model / controller boundary | The exact designated Workflow execution-state owner and recorder boundary was ambiguous. |
| F-04 | MAJOR | Runtime restart/reconciliation | Restart projection was not deterministic for every active/awaiting runtime phase. |
| F-05 | MAJOR | Consequential side effects | Effect semantics were too generic for objective operation-aware conformance and safe retry/reconciliation. |

## F-01 — conformance taxonomy was insufficient

### Failure mode

A completely green suite against fake transport, fake journal, fake process liveness, fake Git, and fake side effects could have been presented as satisfying the D13 conformance prerequisite even though actual fencing, crash durability, containment, Git/ref semantics, and transport lifecycle behavior had never been exercised.

### Required correction

The design had to distinguish at minimum:

1. `abstract-controller conformance`;
2. `transport conformance`;
3. `target-environment conformance`.

Deterministic doubles may support only claims whose truth is confined to controller logic. Fixture-only evidence must never by itself satisfy the accepted D13 conformance prerequisite. Real substrate behavior is required where durability, writer fencing, process containment, Git semantics, or operation-aware reconciliation is claimed.

## F-02 — writer claim was not an enforceable fence

### Failure mode

Controller A could retain a stale writer capable of effects while Controller B reconstructed state and issued a new generation. If write-capable boundaries did not validate the current generation, both writers could mutate concurrently even though the journal reported one active claim.

### Required correction

The design had to define a technology-neutral semantic fencing contract:

`single authoritative current-claim owner/store -> atomic compare-and-acquire -> monotonic generation/fencing token -> mandatory current-generation validation at write-capable boundaries -> stale-generation denial -> successor only after predecessor containment and reconciliation`.

A claim record, heartbeat, workspace name, or journal entry without enforcement is not fencing.

## F-03 — semantic execution-state ownership was ambiguous

### Failure mode

An implementation could interpret controller-owned dispatch ordering or transition recording as authority to write `active`, `blocked`, cancellation, or recovery semantic state, creating a second mutable owner and violating DI-1.

### Required correction

The authority resolver had to identify the exact designated run/task execution-state owner and, where distinct, the sole recorder. The runtime controller may supply facts and transition requests only. It may continue consequential execution only after fresh authoritative readback of the required semantic transition. Its journal is never the semantic transition record.

## F-04 — restart projection was incomplete

### Failure mode

After restart during reviewer or correction phases, multiple implementations could make incompatible but superficially compliant choices: resume the old reviewer, start a replacement, return to executor activity, block, or terminate.

### Required correction

Restart/reconciliation had to deterministically map:

`pre-crash phase + authoritative semantic state + journal evidence + live worker/reviewer state + workspace/Git state + outstanding effects`

to exactly one permitted result under explicit guards:

- resume the same exact identity;
- recognize an already completed exact operation;
- replace only after containment/reconciliation;
- `BLOCKED`;
- `TERMINATED`.

No unguarded implementation choice such as `BLOCKED or TERMINATED` is acceptable.

## F-05 — consequential-effect semantics were too generic

### Failure mode

Different implementations could treat an ambiguous Git ref update, candidate-object creation, workspace mutation, or other effect differently: retry, block, or duplicate the operation, with no objective conformance rule identifying the correct behavior.

### Required correction

Every allowed consequential effect had to carry an exact descriptor containing at least:

- effect class;
- operation ID;
- authority reference;
- exact target identity;
- expected/precondition state;
- writer generation when applicable;
- repeatability/idempotency classification;
- intended/result identity binding;
- observed outcome;
- reconciliation/readback rule;
- safe retry predicate.

Effects outside the future minimum PoC should have denial conformance only rather than speculative positive mutation design.

## Review-positive areas retained

The independent review did **not** require redesign of these areas:

- authority resolver -> deterministic controller -> replaceable transport architecture;
- separation of runtime state from Workflow semantic state in principle;
- fresh reviewer identity/context;
- immutable candidate binding;
- correction produces a new candidate and fresh affected review;
- D5 independence from D13;
- transport-neutral comparison of Native Threads and App Server;
- future PoC ceiling stopping before human acceptance;
- no hidden mechanism-selection, implementation, PoC, or Workflow v1 amendment authority.

The review specifically assessed reviewer independence and D5 separation as sound at the design-semantics level, subject to later transport-specific evidence.

## Evidence-layer conclusion

The predecessor review concluded:

- deterministic fixtures can legitimately test controller-only logic;
- they cannot prove global writer exclusivity, real crash durability, real process containment, real Git/ref semantics, real transport reviewer freshness, or target credentials/sandbox behavior;
- D13 prerequisite evidence must keep abstract-controller, transport, and target-environment claims distinct;
- abstract-controller evidence must use real substrates for properties whose semantics depend on real persistence/process/Git behavior;
- actual transport behavior must be validated separately for any transport later proposed for D13 reconsideration;
- target-environment claims belong to later bounded PoC/operational validation unless separately required earlier.

## Historical verdict

**VERDICT: REQUIRES_CORRECTION**

Finding counts:

- BLOCKER: 2
- MAJOR: 3
- MINOR: 0
- NOTE: 2

The predecessor subject was **NOT READY FOR COORDINATOR DISPOSITION**.

## Successor review boundary

The corrected design now persisted at [`ADW-D13-PREREQUISITE-DESIGN-001.md`](ADW-D13-PREREQUISITE-DESIGN-001.md) is a materially different subject and must receive a fresh independent affected review.

That review should primarily re-evaluate closure of F-01 through F-05 and scan for regressions in DI-1, DI-2, D5 separation, reviewer independence, transport neutrality, and explicit non-authorities.

Passing that future review would make the corrected design eligible for coordinator disposition only. It would not itself authorize implementation, conformance execution, D13 reconsideration, D5 selection, PoC, ready transition, or merge.

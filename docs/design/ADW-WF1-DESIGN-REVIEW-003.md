---
id: ADW-WF1-DESIGN-REVIEW-003
artifact_status: active
authority: evidence
review_type: independent-design-review
review_target_commit: fd047c7563a9c44be5b3a4bde7d12f9e88d27414
review_target_parent: 8969335926967af14d0b05b94e34708cfa41a4d6
review_target_path: docs/design/ADW-WF1-DESIGN-001.md
review_target_blob: 229a5a16cd93e41c9bdf19da47a488947e8dbb29
review_target_bytes: 104018
review_target_sha256: a83a4ec393008b352971599c5975e826932f2e83fc0c064db3da5dc25a03e461
verdict: require-new-design-candidate
reviewed_on: 2026-09-03
owner: agentic-development-independent-review
supersedes: null
---

### A. Exact reviewed identity

Verified directly through @GitHub. Initial and final `main` reads both resolved to candidate-003.

| Field | Verified value |
|---|---|
| Repository | `ahtoxaandy999/agentic-development-workflow` |
| Candidate-003 | `fd047c7563a9c44be5b3a4bde7d12f9e88d27414` |
| Sole parent | `8969335926967af14d0b05b94e34708cfa41a4d6` |
| Artifact | `docs/design/ADW-WF1-DESIGN-001.md` |
| Artifact Git blob | `229a5a16cd93e41c9bdf19da47a488947e8dbb29` |
| Independently computed bytes | `104018` |
| Independently computed SHA-256 | `a83a4ec393008b352971599c5975e826932f2e83fc0c064db3da5dc25a03e461` |
| Research Register blob | `e6bce292c33666092cfa4a0b4f1627fa69bee401` |
| Review-002 blob | `b18aeaa0e86c3cf2ce02afaf36106e19a8e7de78` |

The retrieved artifact bytes also reproduce the expected Git blob hash. [Commit](https://github.com/ahtoxaandy999/agentic-development-workflow/commit/fd047c7563a9c44be5b3a4bde7d12f9e88d27414)

Verified front matter: `design_stage: initial-design-complete`, `artifact_status: draft`, `normative_effect: none`. The Register’s current gate remains **Workflow v1 corrected design independent review gate**, and its review pointer still identifies review-002. Workflow v1 remains unadopted; DR-005 remains deferred and dependency-unsatisfied. [Design](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/design/ADW-WF1-DESIGN-001.md#L1-L15), [Register](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/research/research-register.md#L30-L58)

**Exact-subject verification: PASS.**

### B. Correction resolution

**ADW-WF1-DR-MAJ-003: RESOLVED**

The sole intervention transition explicitly produces `blocked / cancellation-unchanged / intervention-required` from every active recovery phase. It prohibits `recovering/intervention-required`, requires no unavailable approval merely to record the block, and distinguishes recorder, domain evidence provider, decision authority, and escalation destination. Renewed recovery, continued blocking, and separately authorized cancellation have explicit routes; successful recovery and terminal outcomes cannot be inferred. [Lines 752–787](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/design/ADW-WF1-DESIGN-001.md#L752-L787)

**ADW-WF1-DR-MAJ-004: RESOLVED**

Both resumption paths explicitly set `active/none/not-applicable`. The common rule preserves durable episode evidence and residual obligations, prohibits resetting incomplete recovery or intervention, and permits the requested second recovery cycle after resumption. The separate finding below concerns cancellation **before** that reset. [Ordinary resumption](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/design/ADW-WF1-DESIGN-001.md#L744), [Common reset](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/design/ADW-WF1-DESIGN-001.md#L789)

### C. Overall verdict

**REQUIRE NEW DESIGN CANDIDATE**

### D. Findings

**ADW-WF1-DR-MAJ-005 — Cancellation after recovered, before resumption, can prevent required new recovery**

- **Severity:** MAJOR.
- **Exact location:** `docs/design/ADW-WF1-DESIGN-001.md`, lines **737, 749–757, 770–789**, and residual-effects scenario **1110**.
- **Ambiguity/contradiction:** Cancellation request, acknowledgement, and containment retain `recovery=recovered`. If cancellation introduces a new required compensation or reconciliation action, **begin recovery** excludes `recovered`; **require accountable intervention** accepts only `task control=recovering`. Resumption cannot reset the plane while required recovery remains incomplete. The residual-effects scenario nevertheless requires recovery/reconciliation. [Transition predicates](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/design/ADW-WF1-DESIGN-001.md#L737-L789), [Scenario](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/design/ADW-WF1-DESIGN-001.md#L1110)
- **Smallest counterexample:** A recovery successfully repairs a published result against its authorized target. Before resumption, the authorized owner cancels; the task’s cancellation obligations require a separately authorized compensating withdrawal. Further effects are contained, but withdrawal remains outstanding:

  ```text
  blocked/none/recovered
    → request cancellation
  blocked/requested/recovered
    → acknowledge cancellation
  blocked/acknowledged/recovered
    → verify containment; published effect requires withdrawal
  blocked/residual-effects/recovered
  ```

  Fresh evidence, ownership, and withdrawal authority can all be available. Nevertheless, neither recovery entry nor intervention accepts this tuple. Resumption, terminal cancellation, and abandonment remain denied because required handling is incomplete. General invalidation or escalation language supplies no explicit replacement recovery value or transition.

- **Impact:** A literal implementation cannot perform the required recovery through the declared workflow. Another must invent a reopening/reset transition. This is an operational closure defect, not merely unavailable intervention: supplying the accountable decision does not unlock an existing route.
- **Provenance:** Newly identified gap involving retained predicates; not claimed to have been introduced by candidate-003.
- **Another candidate required:** **Yes.**

Finding counts: **0 BLOCKER, 1 MAJOR, 0 MINOR.**

### E. Recovery-graph assessment

I independently enumerated **28 reachable nonterminal tuples** in the task-control/cancellation/recovery projection: one active, fifteen blocked, and twelve recovering. This excludes framing/authorization and other planes. All declared recovery values are reachable; `recovering/intervention-required` is excluded. Applying evidence and authority guards exposes MAJ-005 despite tuple-level connectivity.

| Area | Assessment | Decisive result |
|---|---|---|
| Intervention path | **PASS** | All four active phases reach blocked intervention for each eligible cancellation value; renewal and authorized cancellation are explicit. |
| Successful recovery | **PASS** | Validated conclusion produces blocked/recovered; no automatic resumption or termination. |
| Ordinary resumption/reset | **PASS** | Explicit reset and durable historical evidence. |
| Repeated recovery | **PASS WITH QUALIFICATION** | Requested post-resumption sequence passes; a new recovery obligation before reset exposes MAJ-005. |
| Cancellation recovery | **PASS WITH QUALIFICATION** | Contained cancellation → recovery → resumption or terminal cancellation works from eligible recovery values. Prior `recovered` can prevent a new episode. |
| Residual-effects recovery | **FAIL** | Entry and intervention work from eligible values, but the MAJ-005 residual-effects state cannot begin required new handling. |
| Terminal paths | **PASS WITH QUALIFICATION** | Independent guards and history retention remain correct; MAJ-005 can prevent satisfying those guards. |

The requested repeated-recovery sequence executes using listed transitions:

```text
active/none/not-applicable
→ generic stop → blocked/none/not-applicable
→ begin recovery → recovering/none/assessment
→ authorize action → recovering/none/retry-authorized
→ record action → recovering/none/reconciling
→ conclude recovery → blocked/none/recovered
→ ordinary resume/reset → active/none/not-applicable
→ later failure / generic stop → blocked/none/not-applicable
→ begin recovery → recovering/none/assessment
```

I also exercised assessment-to-reconciling, intervention from every active phase, intervention-to-cancellation-to-renewal, both contained-cancellation outcomes, residual-effects intervention, and independently legal abandonment after recovery. These satisfy the fourteen minimum route classes under their stated guards; they do not eliminate MAJ-005.

### F. Regression assessment

| Area | Assessment |
|---|---|
| Join/integrated verification | **PASS.** Effective integrated verification remains necessary. Failed, stale, pending, missing, conflicted, or silently omitted required verification prevents pass. Legitimate non-applicability remains distinct. Candidate formation and completion reject non-passing relied-upon joins. |
| Cancellation/containment | **PASS WITH QUALIFICATION.** Generic stop, request, acknowledgement, containment, residual effects, and terminal authorization remain distinct and fail closed. The additional recovery interaction fails as reported. |
| Ownership | **PASS.** One execution-state recorder; domain owners provide evidence and recovery decisions; task/risk decisions do not create competing workflow-state writers. |
| Candidate/review lifecycle | **PASS.** Identity, producer verification, independent review, correction, disposition, adoption, and baseline acceptance remain separate. |
| Authority boundary | **PASS.** No new write, unattended, AFK, or mechanism-selection authority. |
| Accepted-input preservation | **FAIL overall.** DR-001 and DR-002 are preserved. DR-003 PR09 remains preserved; PR10 remains incompletely operationalized because required cancellation compensation can lack a recovery entry. Other accepted DR-003 constraints and qualifications remain intact. |

These conclusions derive from the candidate text and comparison with the parent artifact, independently retrieved as blob `f76c7df6686b3c338d261860e9c4aa3f72da5480`. Relevant controls remain in [join rules](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/design/ADW-WF1-DESIGN-001.md#L954-L969), [ownership](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/design/ADW-WF1-DESIGN-001.md#L708), and [candidate lifecycle](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/design/ADW-WF1-DESIGN-001.md#L888-L911).

### G. Implementer-consistency test

**YES.**

One implementer follows the source predicates and remains blocked at `blocked/residual-effects/recovered`. Another interprets the required residual-effects recovery as reopening or resetting recovery, but must invent that transition. The required behavior remains materially underdetermined in MAJ-005.

### H. Conformance-scenario assessment

All existing scenarios remain present as explicit conformance obligations. Their assessment is:

| Scenarios | Assessment |
|---|---|
| Intervention-required exit | **PASS.** Exact state, blocking reason, accountable decision owner, continued escalation, and explicit renewal are discriminated. |
| Repeated non-cancellation recovery | **PASS.** Explicit successful close, resumption reset, later failure, and second assessment. |
| Residual effects delaying cancellation | **PASS WITH QUALIFICATION.** Correct denial oracle, but no recovery entry when inherited recovery is already `recovered`. |
| Generic stop; request without acknowledgement; unverified containment; clean cancellation closure | **PASS.** Distinct states and forbidden outcomes remain operative. |
| Legitimate gate omission; false pass; stale state; missing required branch; integrated verification failure, success, and non-applicability; optional omission | **PASS.** Discriminating outcomes preserved. |
| Material correction; carried-forward evidence | **PASS.** New identity and supported reverification/re-review remain required. |
| Abandonment; ambiguous retry; scope expansion | **PASS.** Independent guards, retry denial, and escalation remain operative. |
| Fresh-context rehydration; unattended denial | **PASS.** Authoritative rereads and incomplete-evidence denial remain operative. |

The scenarios do not cover recovery conclusion followed by cancellation requiring a new recovery action before resumption. [Scenario set](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/design/ADW-WF1-DESIGN-001.md#L1094-L1121)

### I. DR-005 boundary

**PASS.** Mechanism selection remains deferred. DR-005 is planned, deferred, and dependency-unsatisfied; design disposition and an explicit research gate remain prerequisites. [Register boundary](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/fd047c7563a9c44be5b3a4bde7d12f9e88d27414/docs/research/research-register.md#L962-L974)

### J. Authority boundary

Confirmed:

- Candidate-003 remains non-normative.
- Workflow v1 remains unadopted.
- This review neither dispositions nor adopts Workflow v1.
- DR-005 remains blocked.
- No routine, parallel direct-main, automated, unattended, or AFK authority is created.

### K. Repository write status

No GitHub write performed.

### L. Next gate

Workflow v1 design correction gate.

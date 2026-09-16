---

id: ADW-D13-PREREQUISITE-DESIGN-001
artifact: d13-prerequisite-design-proposal
artifact_status: proposed
authority: design-proposal
owner: architecture-design-producer
normative_effect: none
produced_on: 2026-09-15
repository: ahtoxaandy999/agentic-development-workflow
basis_main: 796fef15a7ba3b78b57c1f06f5911c6a3f85dad5
basis_tree: 9c582a9cd004030bc7d0f10a58e6c77243997097
supersedes: null
authorized_by: docs/research/ADW-DR-006-DISPOSITION-001.md
----------------------------------------------------------

# ADW-D13-PREREQUISITE-DESIGN-001

## 1. Live-state verification

### Preflight result

**PASS. No stop condition triggered.**

Live `main` is exactly:

* commit: `796fef15a7ba3b78b57c1f06f5911c6a3f85dad5`
* tree: `9c582a9cd004030bc7d0f10a58e6c77243997097`

That commit is the merge commit of merged PR #10. Therefore the live branch has not advanced beyond the published DR-006 state identified by this task. No newer authority on live `main` supersedes the published disposition. This statement is limited to the authoritative live repository state inspected here and makes no claim about unpublished local/private drafts.

The live Research Register records DR-006 as:

* `research_status: reviewed`
* `current_decision_status: accepted`
* decision: `accept-dr-006-evidence-and-authorize-bounded-d13-prerequisite-design`
* `D5: CONFIRM DEFER`
* `D13: CONFIRM DEFER`
* `X3: CONFIRM REJECT`
* `next_gate: D13 prerequisite-scoping/design gate`

The repository-wide gate remains independently unchanged.

### Controlling disposition confirmation

**D5 = CONFIRM DEFER**

**D13 = CONFIRM DEFER**

**X3 = CONFIRM REJECT**

DR-005 owns those mechanism boundaries. D13 may be reconsidered only after an accepted adapter/ownership design and conformance evidence preserving DI-1 and DI-2. D5 separately remains deferred. X3 continues to reject unmodified Symphony/custom-harness retry, stale-input, cleanup, and related defaults as evidence of ADW conformance.

The current DR-006 coordinator disposition authorizes exactly one bounded D13 prerequisite design gate, `DESIGN AND PROPOSE` only. It explicitly states that a design or test plan does not itself satisfy the D13 conformance prerequisite and grants no PoC or mechanism-selection authority.

---

## 2. Exact authoritative artifacts used

| Artifact                                                                 | Exact basis used                                                                                                                                              | Role in this proposal                                                               |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `AGENTS.md`                                                              | live main `796fef15...`, blob `18d9b694de020f93c90a69940b21b2800c4a9297`                                                                                      | Read order, authority, exact-candidate and escalation rules                         |
| `PROJECT-CHARTER.md`                                                     | live main, blob `c521f6869662f39106bcac0365426eb0e9bdb327`                                                                                                    | Repository scope, authority hierarchy, roles, no duplicate owner                    |
| `WORKFLOW-V1.md`                                                         | live main, blob `3195789595f6ebbe063bb4b48bb1f63930d96eb8`                                                                                                    | Sole normative Workflow v1 owner                                                    |
| Workflow v1 incorporated semantics                                       | commit `2b9532682ae77bf5037f1b2fa45b720e5865d0ad`, `docs/design/ADW-WF1-DESIGN-001.md`, blob `afed983e7632caf3169dcbac7a80f8da8226d86d`, line 632 through EOF | Orthogonal planes, owner, freshness, correction, recovery and conformance semantics |
| `docs/policies/research-evidence.md`                                     | live main, blob `90572c47463f2d2adc493f9978c1c720fd8f8275`                                                                                                    | Evidence, freshness and adoption separation                                         |
| `docs/research/research-register.md`                                     | live main `796fef15...`                                                                                                                                       | Current DR-006 state and next gate                                                  |
| `ADW-DR-005-DISPOSITION-001.md`                                          | live main                                                                                                                                                     | D5, D13, X3, DI-1 and DI-2 boundaries                                               |
| `ADW-DR-006.md`                                                          | reviewed subject commit `b244385d5a84d6db66b34b897182e138f3e325ba`, blob `c29547c1174831140f97ad8c1f7aa1c9af8f16a6`                                           | Source-reviewed orchestration evidence                                              |
| `ADW-DR-006-SOURCE-REVIEW-001.md`                                        | blob `65ce80777fdbf5858106b2d8400cf8e031a0ee2d`                                                                                                               | Independent source-review acceptance                                                |
| `ADW-DR-006-DISPOSITION-001.md`                                          | blob `85610d35b126bc49f68d814b5f47c7fcc41a2530`                                                                                                               | Authority for this exact bounded design gate                                        |
| `ADW-WF1-TASK-CONTROL-REFERENCE-001.md`                                  | live main                                                                                                                                                     | Explanatory owner and B/W/C/I separation reference                                  |
| `ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-OPERATIONAL-USE-SCOPING-001.md` | live main, blob `88caf8aacf95030f16858a18279298c4b4d7f837`                                                                                                    | Existing protected publication and one-writer boundaries                            |

The Charter establishes that current repository authority outranks summaries or runtime state, exact candidate identity is a full commit SHA, and review and coordinator acceptance are separate gates.  Workflow v1 further requires orthogonal state planes, one mutable owner, fresh relied-upon identities, new candidate identity after material correction, reliance-based durability, and operation-aware recovery.

### Targeted current platform re-verification

DR-006 source review explicitly requires unstable App Server/Codex behavior to be reverified at a dependent design gate.  This proposal therefore performed only a targeted current check, not a new Symphony/App Server research cycle.

Current primary source inspected:

* `openai/codex@b1f3c2f77e7cb802af0d8ef1c325cb6e9d39d8d9` on 2026-09-15.
* current protocol contains `thread/start`, `thread/resume`, `thread/read`, `turn/start`, explicit `turn/started` and `turn/completed` lifecycle events.
* current `thread/resume` supports normal persisted-thread resumption by thread ID while marking alternate history/path behavior experimental.
* `experimentalApi` remains an explicit opt-in and defaults to false.
* current stable `TurnStartParams` surface includes `outputSchema`, along with thread, cwd, sandbox, model and reasoning controls.

These facts only support the transport comparison below. They do not reopen D5 or select App Server.

---

# 3. Executive decision summary

## Design conclusion

A coherent D13 prerequisite architecture can be defined without selecting Symphony, App Server, Native Threads, or another execution mechanism.

The smallest acceptable architecture has four logical boundaries:

```text
authoritative Workflow v1 + project/task policy
                    |
          read-only authority resolution
                    |
                    v
        deterministic runtime controller
          |                     |
          |                     +--> side-effect/reconciliation boundary
          |
          v
     replaceable execution transport
          |
     executor / reviewer
```

The runtime coordinator is **not a workflow engine in the normative sense**. It is an execution controller whose authority is derived from current external owners on every consequential transition.

Its sole authoritative domain is execution-local lifecycle and recovery state.

It does not own:

* task authorization;
* Workflow v1 semantics;
* project/product state;
* research state;
* verification truth;
* candidate correctness;
* review verdict;
* coordinator acceptance;
* publication authorization;
* normative adoption;
* repository baseline acceptance.

This preserves Workflow v1's orthogonal state model and the DR-005 DI-1 boundary.

A **minimal durable recovery journal is required**. Without it, controller restart, observed writer-fence history, ambiguous effects and recovery history cannot be deterministically reconstructed. The authoritative current writer claim remains owned by the separate fencing contract in Section 8; the journal is an execution/recovery record only and cannot become a second task tracker or claim owner.

The transport remains replaceable. Native Codex threads and App Server are evaluated against one adapter contract rather than defining different Workflow v1 semantics.

---

# 4. Authority model

## 4.1 Existing authoritative owners remain unchanged

| State or decision | Authoritative owner | Runtime coordinator relationship |
| --- | --- | --- |
| Repository mission, scope, authority hierarchy | `PROJECT-CHARTER.md` | Read only |
| Workflow semantics | `WORKFLOW-V1.md` | Read and enforce transition preconditions, never reinterpret |
| ADW research state/current gate | Research Register | Read only |
| D5/D13/X3 disposition | Existing coordinator disposition chain | Read only |
| Product/project policy | Applicable project repository owner | Read only |
| Task objective, scope, readiness and authorization | Accepted task-contract authority | Read only |
| Execution and task-control semantic state | Exact designated run/task execution-state owner resolved from current task authority; exact sole recorder resolved separately where applicable | Supplies runtime facts and transition requests; consumes authoritative transitions; never records the semantic transition itself |
| Cancellation semantic state | Applicable authorized requester plus designated execution-state owner/recorder under Workflow v1 task control | Supplies runtime containment facts only; never authoritatively records cancellation state |
| Recovery semantic state | Applicable state/side-effect owner and required risk authority, recorded by the designated sole recorder where applicable | Supplies reconciliation evidence and requests; never authoritatively records recovery state |
| Working implementation bytes | Authorized executor within its writable boundary | Controller fences access but does not own product content |
| Current writer claim | One authoritative current-claim owner/store for the exact fenced domain | Controller acquires, validates and releases only through the fencing contract in Section 8 |
| Candidate identity | Exact immutable Git object promoted under project/persistence authority | Controller may persist/cache the SHA as a pointer |
| Verification verdict | Assigned verifier/project verification owner | Controller consumes exact evidence |
| Review verdict | Conflict-free independent reviewer/review owner | Controller routes and consumes exact evidence |
| Coordinator acceptance | Coordinator/accountable human | Controller has no write authority |
| Publication authorization | Applicable coordinator/human write authority | Controller has no implicit authority |
| Actual GitHub/external system state | Live external system | Controller observes or invokes only separately authorized effects |

Workflow v1 requires one current authoritative owner for every mutable state class and treats caches, evidence and runtime representations as non-owners.

## 4.2 Deterministic semantic execution-state owner resolution

Before dispatch, resumption, correction, reviewer dispatch or any other consequential continuation, the authority resolver must resolve an immutable current authority bundle that identifies at minimum:

* exact task/run identity;
* exact task-contract and authorization references;
* exact designated run/task execution-state owner for task-control transitions;
* exact sole recorder, if the applicable task-control representation separates decision authority from recording authority;
* exact current semantic task-control/cancellation/recovery transition relied upon for the requested continuation;
* exact authoritative revision or immutable pointer from which those identities and transitions were observed.

If the current authority does not designate a unique execution-state owner, or if two credible sources claim the same mutable semantic domain, the dependent transition fails closed. Time, journal recency, process liveness and controller preference do not choose the owner.

The runtime controller may:

* supply attributable runtime facts;
* request or propose a semantic transition to the designated owner;
* provide evidence needed by the owner or sole recorder;
* consume the resulting authoritative transition after fresh readback.

The runtime controller may not authoritatively write task-control, cancellation, recovery, verification, review, acceptance, publication or other Workflow semantic state.

Where an owner and recorder are distinct, the owner decides and the recorder alone updates the authoritative current projection. Recording does not transfer decision authority.

Before a consequential dispatch or resumption, the controller must freshly observe the required authoritative transition from the resolved owner/recorder. A controller request, worker exit, transport event, local journal entry or cached prior transition is not sufficient.

## 4.3 What the runtime coordinator may own persistently

The runtime coordinator may be the sole mutable owner of:

* orchestration run identity;
* runtime controller state;
* attempt and operation identities;
* transport worker/thread identities;
* workspace/worktree association;
* the controller's reference to the authoritative current writer claim and fencing generation;
* controller-local interruption/termination request state;
* external-effect operation identifiers and observed outcomes;
* reconciliation checkpoint;
* runtime recovery episode history;
* pointers to exact candidate, verification and review evidence.

These are execution-local facts, not Workflow v1 semantic verdicts.

The authoritative current writer claim itself is not owned by the recovery journal merely because the journal records it. Section 8 defines the separate current-claim owner/store.

## 4.4 What it may cache only

It may cache, with authoritative source pointer and observed version:

* task authorization state;
* current task-control plane;
* cancellation and recovery semantic state;
* project policy;
* current baseline;
* candidate SHA;
* verification state;
* review state/verdict;
* coordinator disposition;
* publication state;
* current branch/PR status;
* current writer claim observation.

A cached observation is never sufficient for a later state-dependent transition without the freshness requirement applicable to that transition.

## 4.5 What it must never become authoritative for

It must never decide or own:

* that a task is authorized;
* the current Workflow task-control transition;
* semantic cancellation or recovery state;
* that a candidate is valid;
* that verification passed;
* that review passed;
* that a project requirement was satisfied;
* that coordinator acceptance occurred;
* that a branch or PR represents accepted work;
* that publication is authorized;
* that a research or normative state changed;
* that a workflow exception exists;
* that a task is successfully complete solely because a worker exited.

The runtime journal is never the semantic transition record for any of those claims.

## 4.6 What must be reconstructed after restart

Before any post-restart effect, the controller must reconstruct:

1. current authority and task contract from authoritative owners;
2. exact designated execution-state owner and sole recorder where applicable;
3. current authoritative semantic task-control, cancellation and recovery transitions required for continuation;
4. current runtime journal state;
5. live transport worker/reviewer state;
6. workspace/worktree and local Git state;
7. exact candidate identity, if one exists;
8. remote branch/PR/candidate state, if relevant;
9. outstanding effect operations and their exact descriptors;
10. authoritative current writer-claim state and fencing generation;
11. current verification/review evidence pointers;
12. unresolved recovery, containment or intervention obligations.

A journal/live-state mismatch causes reconciliation or blocking. The journal never wins merely because it is newer. A post-restart continuation is permitted only through the deterministic projection in Section 5.4.

---

# 5. Runtime state model

## 5.1 Principle

Runtime process state is deliberately smaller than Workflow v1 semantic state.

For example:

* `REVIEWER_ACTIVE` does not mean `review=required-pending`;
* worker exit does not mean `task_control=completed`;
* `STOPPED_BEFORE_ACCEPTANCE` does not mean accepted, passed or complete;
* transport `turn/completed` means only that a transport turn completed.

This separation implements DI-1. Workflow v1 explicitly prohibits platform/runtime statuses from substituting for task, verification, review, disposition or acceptance planes.

## 5.2 Minimum runtime states

| Runtime state | Meaning |
| --- | --- |
| `RECONCILING` | Controller has not yet established enough current evidence to initiate another effect |
| `EXECUTOR_ACTIVE` | One executor identity is active under the current authoritative writer claim and fencing generation |
| `AWAITING_AUTHORITATIVE_CANDIDATE` | Executor activity ended or paused, but the exact candidate/readiness bundle needed for review dispatch has not yet been authoritatively established |
| `REVIEWER_ACTIVE` | Fresh independent reviewer R1 is examining one immutable candidate C1 |
| `CORRECTION_ACTIVE` | Same authorized writer is performing the one permitted review-directed correction under the current writer claim |
| `AWAITING_NEW_AUTHORITATIVE_CANDIDATE` | Correction activity ended or paused, but the exact C2/readiness bundle needed for affected re-review has not yet been authoritatively established |
| `FRESH_REVIEWER_ACTIVE` | Fresh independent reviewer R2 is examining corrected immutable candidate C2 |
| `BLOCKED` | Continuation is denied because authority, identity, fencing, containment, reconciliation, evidence or intervention requirements are unresolved |
| `STOPPED_BEFORE_ACCEPTANCE` | Intended bounded orchestration path has ended after the permitted review path and no further automated/controller action is permitted |
| `TERMINATED` | Runtime episode has ended because applicable authority ended/abandoned/cancelled it, or because the bounded path reached a defined non-continuable terminal condition |

`BLOCKED` is non-terminal. `TERMINATED` and `STOPPED_BEFORE_ACCEPTANCE` are terminal for that runtime episode.

## 5.3 Principal transitions

```text
start or restart
    |
    v
RECONCILING
    |
    +-- unresolved/stale/ambiguous --------------------> BLOCKED
    +-- authority ended and residual effects resolved -> TERMINATED
    |
    v
EXECUTOR_ACTIVE
    |
    v
AWAITING_AUTHORITATIVE_CANDIDATE
    |
    | exact C1 + required verification + fresh authoritative review-dispatch transition
    v
REVIEWER_ACTIVE
    |
    +-- valid PASS ------------------------------------> STOPPED_BEFORE_ACCEPTANCE
    |
    +-- valid correction-required verdict + fresh authoritative correction transition
            |
            v
      CORRECTION_ACTIVE
            |
            v
      AWAITING_NEW_AUTHORITATIVE_CANDIDATE
            |
            | exact C2 + affected verification + fresh authoritative re-review transition
            v
      FRESH_REVIEWER_ACTIVE
            |
            +-- valid PASS ----------------------------> STOPPED_BEFORE_ACCEPTANCE
            +-- valid finding requiring another content correction
            |                                           -> TERMINATED
            +-- failed reviewer/no valid verdict ------> replacement only under Section 5.4 guards
```

`BLOCKED` may transition only to `RECONCILING` after fresh recovery/resumption authority and resolution of the blocking predicate, or to `TERMINATED` after explicit authority ends the episode and every consequential effect is reconciled.

There is no runtime transition to `ACCEPTED`, `MERGED`, `ADOPTED`, `PUBLISHED`, or an equivalent value.

## 5.4 Exhaustive restart/reconciliation projection

Every controller restart first enters `RECONCILING`. The controller must evaluate this tuple:

```text
pre-crash runtime phase
+ current authoritative semantic state
+ journal evidence
+ live worker/reviewer state
+ authoritative writer claim/generation
+ workspace/Git state
+ outstanding external effects
```

The projection must resolve to exactly one of these result classes:

1. `RESUME_SAME_IDENTITY`: resume the same exact worker/reviewer/operation identity and preserve the same current writer generation where applicable;
2. `RECOGNIZE_COMPLETED`: establish by exact readback that the pre-crash operation already completed and project to the next deterministic runtime phase without repeating it;
3. `REPLACE_AFTER_CONTAINMENT`: start a replacement identity only after predecessor containment, effect reconciliation, fresh authority and, for writers, successful acquisition of a strictly newer fencing generation;
4. `BLOCKED`: continuation requires intervention or evidence that is not currently sufficient;
5. `TERMINATED`: current authoritative semantic state ends the episode or the one-correction ceiling produces a defined non-continuable result, and all consequential effects are reconciled/contained.

No implementation may choose between these result classes by preference. The guards below determine the result.

### Universal guards

The following rules apply before phase-specific projection:

* If current authoritative task/cancellation/recovery state denies further execution and all live effects are proven contained/reconciled, result is `TERMINATED`.
* If current authority denies continuation but a worker/effect may still be live or ambiguous, result is `BLOCKED` until containment/reconciliation proves a terminal projection.
* If authority is stale, conflicting or cannot resolve the designated execution-state owner/recorder, result is `BLOCKED`.
* If the journal is missing/corrupt and live evidence cannot prove writer/effect safety, result is `BLOCKED`.
* If an outstanding consequential effect has ambiguous completion, result is `BLOCKED` until Section 11 reconciliation establishes non-occurrence, exact completion or intervention.
* A stale writer generation is never resumed. It must be denied at write boundaries and contained before any replacement generation can exist.
* A reviewer bound to a different candidate, inherited executor history or effective candidate-write authority is not resumable as an independent reviewer.

### Phase-specific projection

| Pre-crash phase | Deterministic projection |
| --- | --- |
| `EXECUTOR_ACTIVE` | If the exact executor is live, current authority still permits the same operation, its writer claim/generation remains current, and no ambiguous effect exists: `RESUME_SAME_IDENTITY` to `EXECUTOR_ACTIVE`. If exact readback proves the executor operation completed and no live writer remains: `RECOGNIZE_COMPLETED` to `AWAITING_AUTHORITATIVE_CANDIDATE`. If the predecessor is proven contained, workspace/Git/effects are reconciled, current authority permits replacement, and a new generation is atomically acquired: `REPLACE_AFTER_CONTAINMENT` to `EXECUTOR_ACTIVE`. Otherwise: `BLOCKED`. |
| `AWAITING_AUTHORITATIVE_CANDIDATE` | If no live writer/effect remains and exact C1 plus required verification/readiness evidence is already established, recognize that fact and do not recreate C1. Reviewer dispatch occurs only after fresh authoritative review-dispatch permission; if present, start one new fresh R1 and enter `REVIEWER_ACTIVE`. If the readiness bundle is incomplete but no unsafe live effect exists, remain `BLOCKED` pending the authoritative transition/evidence rather than infer completion. If current authority ends the episode: `TERMINATED`. |
| `REVIEWER_ACTIVE` | If the same exact R1 is live, still independent, still bound to unchanged C1 and current authority permits continuation: `RESUME_SAME_IDENTITY` to `REVIEWER_ACTIVE`. If exact review evidence proves R1 already completed: `RECOGNIZE_COMPLETED`; PASS projects to `STOPPED_BEFORE_ACCEPTANCE`; correction-required may enter `CORRECTION_ACTIVE` only after fresh authoritative correction permission and valid writer fencing. If R1 failed/stopped without verdict and is proven contained, a replacement must be a new fresh reviewer identity under fresh review-dispatch authority: `REPLACE_AFTER_CONTAINMENT` to `REVIEWER_ACTIVE`. Ambiguity gives `BLOCKED`. |
| `CORRECTION_ACTIVE` | If the same authorized executor is live, its current writer generation is valid, current authority still permits the one correction and no ambiguous effect exists: `RESUME_SAME_IDENTITY` to `CORRECTION_ACTIVE`. If correction activity is proven complete and predecessor cannot write further: `RECOGNIZE_COMPLETED` to `AWAITING_NEW_AUTHORITATIVE_CANDIDATE`. If the executor must be replaced, replacement requires predecessor containment/reconciliation, fresh correction authority and a strictly newer fencing generation: `REPLACE_AFTER_CONTAINMENT` to `CORRECTION_ACTIVE`. Otherwise: `BLOCKED`. |
| `AWAITING_NEW_AUTHORITATIVE_CANDIDATE` | If no live writer/effect remains and exact C2, `C2 != C1`, plus affected verification/readiness evidence is established, recognize it without recreating C2. R2 dispatch occurs only after fresh authoritative re-review permission; if present, start one new fresh R2 and enter `FRESH_REVIEWER_ACTIVE`. Incomplete or ambiguous candidate/effect state gives `BLOCKED`. If current authority ends the episode: `TERMINATED`. |
| `FRESH_REVIEWER_ACTIVE` | If the same exact R2 is live, still independent and bound to unchanged C2: `RESUME_SAME_IDENTITY`. If exact review evidence proves PASS: `RECOGNIZE_COMPLETED` to `STOPPED_BEFORE_ACCEPTANCE`. If exact valid R2 verdict requires another content correction, the one-correction ceiling is exhausted: `TERMINATED`. If R2 failed/stopped without verdict and is proven contained, a replacement may be a new fresh reviewer under fresh re-review authority: `REPLACE_AFTER_CONTAINMENT` to `FRESH_REVIEWER_ACTIVE`. Ambiguity gives `BLOCKED`. |
| `BLOCKED` | Restart preserves `BLOCKED` unless fresh recovery/resumption authority exists and every blocking predicate has enough new evidence to re-enter `RECONCILING`. If current authority explicitly ends the episode and all effects are reconciled/contained: `TERMINATED`. Silence or elapsed time never clears the block. |

A phase not listed above cannot be inferred from a nearby phase. `STOPPED_BEFORE_ACCEPTANCE` and `TERMINATED` remain terminal after restart and permit no new controller effect.

---

# 6. Minimal adapter architecture

## 6.1 Boundary A: Authority and policy resolver

Conceptual responsibility:

* resolve exact task authorization;
* resolve current Workflow v1 and applicable project policy;
* resolve the exact designated run/task execution-state owner;
* resolve the exact sole recorder where the semantic owner and recorder are distinct;
* resolve the current authoritative task-control/cancellation/recovery transition required for the contemplated action;
* resolve current baseline and relied-upon identities;
* verify freshness before state-dependent transitions;
* return an immutable observation bundle to the controller.

It is read-only.

It must not copy Workflow v1 into a new mutable policy file or runtime database.

### Required conceptual operations

* `resolveTaskAuthority(taskRef)`
* `resolveCurrentPolicy(taskRef)`
* `resolveExecutionStateOwner(taskRef)`
* `resolveExecutionBoundary(taskRef)`
* `resolveRequiredSemanticTransition(taskRef, contemplatedAction)`
* `revalidateAuthority(observationBundle)`

The names are illustrative, not implementation API.

A resolution that does not identify one current semantic owner and, where applicable, one sole recorder is invalid and fails closed.

## 6.2 Boundary B: Deterministic orchestration controller

Owns only:

* runtime state;
* claim acquisition/validation requests against the authoritative current-claim owner/store;
* dispatch ordering after fresh semantic permission exists;
* transport association;
* runtime journal;
* operation-aware retry decisions;
* reconciliation sequencing;
* fail-closed transition guards.

It may submit runtime facts and proposed semantic transitions to the designated execution-state owner. It may not write the authoritative task-control, cancellation or recovery transition itself.

Every consequential dispatch/resumption must be preceded by fresh readback of the required semantic transition from the resolved owner/recorder.

It must not use LLM interpretation to determine whether an authority, candidate, verification, review or acceptance gate passed when the authoritative result is machine-addressable.

Model reasoning may assist implementation work or review. It does not own controller transitions.

## 6.3 Boundary C: Replaceable execution transport

A transport must support the following abstract contract sufficiently for the selected bounded use.

### Executor operations

* start a fresh executor under a supplied bounded grant;
* bind the executor to the current writer claim/generation where it can write;
* observe whether the executor is active, completed, failed or unreachable;
* identify the transport/session used;
* resume the same executor context for an authorized correction when supported;
* request interruption/termination;
* reconcile worker identity after controller restart;
* provide evidence sufficient to determine whether a predecessor remains capable of effects.

### Reviewer operations

* start a new fresh reviewer;
* bind it to an immutable candidate SHA and review criteria;
* ensure it does not inherit executor conversation/history;
* prevent or withhold candidate-write authority;
* obtain a structured review result;
* reconcile reviewer lifecycle after controller restart.

### Transport rule

The transport reports execution facts. It does not decide Workflow v1 transitions.

Transport liveness, completion, resume, cancellation and reviewer-isolation claims remain transport-conformance claims under Section 14. They are not proven by the abstract adapter contract itself.

## 6.4 Boundary D: Side-effect and reconciliation port

External or consequential mutations require a separate control boundary because transport isolation alone cannot control workspace, Git/GitHub or other external effects.

Every allowed consequential effect must be presented with the mandatory effect descriptor in Section 10.1.

Conceptually the boundary must:

* observe current effect target;
* validate explicit authority;
* validate current writer generation where the effect is writer-scoped;
* enforce exact expected-state/version preconditions;
* execute at most the authorized operation identified by its operation ID;
* perform read-only reconciliation after ambiguous outcomes;
* return exact resulting identity and observed outcome;
* permit retry only when the descriptor's safe-retry predicate is proven true.

This port is subordinate to authorization. It is not an external-effect scheduler, task owner, semantic transition recorder or generic write authority.

An effect denied by the minimum future PoC has no positive execution contract here. For those classes, only denial conformance is defined.

---

# 7. Native Threads versus App Server

This comparison is **not a mechanism-selection verdict**.

Current App Server primary-source re-verification confirms explicit thread/turn lifecycle primitives, resumability/readback primitives, final completion notifications and structured `outputSchema`. Experimental API functionality remains separately opt-in.

| Criterion                         | Native thread orchestration                                                                                                       | App Server transport                                                                                                   |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Implementation surface            | Lowest additional software surface                                                                                                | Larger explicit client/protocol surface                                                                                |
| Lifecycle observability           | Can coordinate executor/reviewer roles, but more transition interpretation may remain model-driven                                | Explicit thread/turn lifecycle events available                                                                        |
| Executor continuity               | Existing model/thread context can support correction                                                                              | Explicit thread resume/read primitives available                                                                       |
| Cross-controller restart evidence | Deterministic inspect/resume behavior for the proposed controller remains an evidence gap                                         | Better documented primitives, but target process/thread retention still requires real validation                       |
| Fresh reviewer                    | Can start a separate new thread                                                                                                   | Can start a separate new thread                                                                                        |
| Forked reviewer acceptable?       | No                                                                                                                                | No. Forking/inheriting executor history does not satisfy independence                                                  |
| Structured final result           | Can request structured prose/JSON, but the current D13 evidence does not establish an equivalent deterministic protocol guarantee | Current `turn/start` exposes `outputSchema`                                                                            |
| Controller determinism            | More lifecycle interpretation may remain with a parent model                                                                      | External deterministic state machine can consume explicit events                                                       |
| Git/effect reconciliation         | Must be implemented outside the model/thread                                                                                      | Must still be implemented outside App Server                                                                           |
| Stable/experimental boundary      | Depends on native product surface used                                                                                            | Core methods may be used without experimental opt-in; experimental fields/methods require separate current evidence    |
| D5 consequence                    | Does not itself select the deferred App Server client                                                                             | Actual use requires an applicable D5 selection/reconsideration                                                         |
| Current conclusion                | Abstractly compatible, with evidence gaps around deterministic restart/control semantics                                          | Abstractly compatible, with stronger lifecycle primitives but separate D5 authority and target-validation requirements |

**Design conclusion:** both may target the same adapter contract. Neither changes Workflow v1 semantics. No transport is selected here.

---

# 8. Writer exclusivity and semantic fencing

Workspace isolation is necessary but insufficient. DR-005 explicitly rejects treating worktree separation as writer fencing. The existing protected write path also retains sole-writer requirements and fails closed on competing writers.

## 8.1 Fenced writer domain

A writer fence applies to one bounded mutation domain identified by at least:

```text
task/run identity
+ repository
+ writable workspace/worktree
+ authorized mutation scope
+ branch/ref or external effect domain when applicable
```

Two domains may be concurrent only if a later explicit design and authority prove they do not permit conflicting effects. This proposal authorizes no parallel writers.

## 8.2 One authoritative current-claim owner/store

For each fenced domain there must be exactly one authoritative owner/store of the current writer claim.

The current-claim store owns only writer-fencing state. It does not own task authorization, Workflow task-control state, review, acceptance, publication or other semantic planes.

The recovery journal may mirror the current claim for reconstruction, but the journal record is not the authoritative claim and does not itself fence anything.

The storage/locking technology is deliberately unspecified.

## 8.3 Atomic unique acquisition and monotonic generation

Claim acquisition must be atomic for the fenced domain.

The semantic operation is:

```text
observe authoritative fencing state `(generation=N, current_claim=none)`
+ prove all predecessor containment/reconciliation guards
+ atomic compare-and-acquire against that exact state
= authoritative fencing state `(generation=N+1, current_claim=new_claim)`
```

Required properties:

* two competing acquisitions cannot both succeed for the same fenced domain;
* generation/fencing tokens increase monotonically and are never reused;
* claim identity binds task/run, writer identity, transport/session identity, repository/base, workspace, mutation scope and generation;
* an acquisition failure does not imply ownership and cannot be retried as success without a fresh observation;
* claim history remains durable and prior generations are never rewritten as though they did not exist.

## 8.4 Mandatory current-generation validation

Every controller-visible write-capable boundary must validate immediately before granting or performing the write that:

1. the supplied claim ID is the current claim for the fenced domain;
2. the supplied generation equals the authoritative current generation;
3. the requested path/effect lies inside the claim scope;
4. current task authority still permits the operation;
5. the exact operation descriptor, where required, is current and valid.

A stale generation is denied even if its executor is still alive, still has cached authority or previously held the current claim.

Validation is required for:

* the boundary that grants writable workspace/process capability, and any mediated workspace mutation boundary;
* Git object or index/worktree mutation boundaries;
* Git ref mutation boundaries;
* any allowed external side-effect boundary.

If raw workspace writes cannot carry a fencing token per filesystem operation, generation validation at the capability-grant boundary is necessary but not sufficient for successor safety. Section 8.5 then requires physical containment/revocation before any newer generation is issued.

## 8.5 Logical or physical prevention of stale writes

A generation token is useful only if stale writers cannot bypass it.

Therefore every writable surface must satisfy one of these technology-neutral conditions:

* **logical fencing:** all mutations to that surface are mediated by a boundary that validates the authoritative current generation immediately before mutation; or
* **physical containment:** before a new generation can be issued, the predecessor is positively proven unable to mutate that surface through process termination, access revocation, workspace isolation or another evidenced containment mechanism.

If a surface cannot enforce current-generation validation and predecessor inability to write cannot be proven, replacement is forbidden and the runtime remains `BLOCKED`.

A claim record, heartbeat, workspace name, thread ID or journal row without one of these enforcement properties is bookkeeping, not fencing.

## 8.6 No timeout-based ownership transfer

Silence, heartbeat timeout, UI inactivity or an apparently idle worker does not release a writer claim.

A replacement writer requires positive evidence that:

1. the previous executor can no longer produce workspace, Git or allowed external effects;
2. relevant process/transport activity is stopped or contained;
3. local workspace/Git state is reconciled;
4. every outstanding remote/external effect is reconciled;
5. current task authority permits replacement;
6. atomic acquisition of a strictly newer generation succeeds.

Only then may a replacement writer become current.

## 8.7 Release and transfer guards

A claim may be released as current only when:

* the current holder is proven unable to produce further in-scope effects, or the bounded operation has reached a controller state in which the holder has no remaining write capability;
* all issued consequential effect operations for that generation are reconciled;
* workspace/Git state is reconciled to exact observed identities;
* the release itself is durably attributable to the current generation.

Transfer is not an in-place identity rewrite. A replacement always receives a new claim ID or successor claim plus a strictly newer generation after the guards above pass.

## 8.8 Duplicate executor dispatch

If a current writable claim exists:

* a second writer dispatch is denied;
* a second workspace does not make the second writer safe by itself;
* the denied attempt is recorded in runtime/recovery evidence;
* a competing controller instance cannot mint another valid generation without atomic acquisition from the same authoritative current-claim store.

## 8.9 Correction cycle

The normal correction path retains the same authorized writer and current claim/generation where the executor remains valid and current authority permits the correction.

The review verdict does not grant new write scope.

If the correction requires replacement of the executor, Section 8.6 containment and a strictly newer generation are mandatory. Replacement does not broaden the correction scope or create a second correction cycle.

## 8.10 Durable fencing evidence

Later conformance evidence must make reconstructable:

* authoritative current-claim owner/store identity;
* acquisition operation identity;
* competing acquisition outcomes;
* every issued generation;
* writer identity and bounded scope per generation;
* stale-generation denial evidence;
* predecessor containment evidence before successor generation;
* release/transfer evidence;
* outstanding effect reconciliation per generation;
* duplicate dispatch denial;
* retained historical claims and recovery episodes.

This design selects no database, lock service, filesystem primitive, process manager or transport implementation.

---

# 9. Reviewer independence

Workflow v1 requires an independent reviewer to be conflict-free for the exact reviewed subject, and review never substitutes for acceptance. A corrected candidate creates a new immutable identity and affected review must be renewed.

For this design, an independent reviewer requires all of the following:

1. a new reviewer execution identity;
2. a new reviewer conversation/thread context;
3. no executor conversation/history inheritance;
4. exact immutable candidate SHA;
5. exact base/baseline identity where relevant;
6. explicit review criteria;
7. no candidate-write claim;
8. no candidate mutation authority;
9. no coordinator-acceptance authority;
10. an attributable structured result.

A transport-level fork of executor history does not count as fresh review merely because it has a new thread ID.

A minimum review envelope conceptually contains:

```text
reviewer identity
review assignment identity
reviewed candidate full SHA
reviewed base/baseline
verdict
findings
evidence pointers
review completion identity/time
```

If correction changes candidate content:

```text
C1 + review R1
    |
    | correction
    v
C2
```

then:

* `C1` remains historical;
* `R1` remains bound to `C1`;
* `C2 != C1`;
* affected verification is renewed;
* a fresh independent reviewer identity reviews `C2`.

---

# 10. Consequential side-effect contract

Default rule: deny every effect not already authorized by the applicable task and existing protected write-path authority.

## 10.1 Mandatory effect descriptor

Every allowed consequential effect must have one immutable operation descriptor before execution containing:

```text
effect class
operation ID
authority reference
exact target identity
expected/precondition state
writer claim ID and generation, where writer-scoped
repeatability/idempotency classification
intended result identity or result-binding rule
observed outcome
reconciliation/readback rule
safe retry predicate
```

The descriptor is operation evidence, not semantic task authority.

The controller/side-effect boundary must reject an effect when any required descriptor field is absent, stale, contradictory or outside the current authority.

An ambiguous effect is never blindly repeated. Retry is permitted only when the exact descriptor's safe-retry predicate has been established from readback.

## 10.2 Effect classes permitted only when a later bounded PoC explicitly grants them

The future minimum PoC may need only the effect classes below. Their inclusion here defines conformance semantics, not current authority.

| Effect class | Minimum semantic contract | Repeatability / safe retry |
| --- | --- | --- |
| Local workspace file mutation | Target is exact workspace + path set; writer generation must be current; precondition binds expected prior existence/content/digest where material; observed result binds exact paths and content identities. | Repeat only if descriptor classifies the mutation as idempotent against exact desired bytes/state and readback confirms no conflicting intermediate state. Otherwise reconcile and block. |
| Git/index/worktree mutation used to prepare a candidate | Target is exact repository/worktree and authorized base; writer generation current; expected index/worktree state and allowed path scope are bound; result is read back by exact Git/content identities. | Repeat only when the specific Git/worktree operation is classified safe after exact readback. No generic retry rule applies. |
| Git object creation for immutable candidate persistence | Target repository and exact intended object class/content basis are bound; authority explicitly permits candidate persistence; result identity is exact object SHA plus required parent/tree/content binding. | Content-addressed blob/tree creation may be repeatable when exact bytes are predetermined. Commit/object creation that can produce a different identity is not assumed idempotent; ambiguity requires readback or intervention before another candidate object is accepted. |
| Branch/ref mutation, if a later PoC explicitly requires it | Target is exact ref; precondition names exact expected old value or non-existence; writer generation current; mutation is non-force; resulting ref target is exact full SHA. | Retry only after readback proves the intended update did not occur and the expected old value still matches. If the ref moved or occurrence is ambiguous, block/reframe. |

These contracts do not require a particular command, library, database or Git hosting mechanism.

## 10.3 Process containment as a consequential control

Starting, resuming, interrupting or terminating a writer/reviewer is a transport lifecycle action rather than a repository mutation, but it is consequential to fencing and recovery.

Later conformance must bind those actions to exact worker/session identities and prove that a predecessor described as contained cannot continue producing in-scope effects. A transport's `completed`, `cancelled` or disconnected status is not by itself proof of process/effect containment unless transport conformance establishes that property.

## 10.4 Effect classes outside the future minimum PoC

The minimum future D13 PoC does not require:

* draft PR creation/update;
* reviewer GitHub review/comment publication;
* PR ready transition;
* merge;
* branch cleanup;
* external tracker/issue mutation;
* production multi-project external effects.

For these classes this design defines denial conformance only:

* no positive mutation path is required;
* no retry implementation is designed here;
* an attempted unauthorized operation must be rejected before mutation and recorded as denial evidence.

Any later positive use requires its own authority and effect-specific design/evidence.

## 10.5 Current effect authority table

| Effect class | Owner / mutation authority | Future minimum PoC status |
| --- | --- | --- |
| Local workspace file mutation | Authorized executor under current writer fence | Conditionally permitted only if later PoC authorization grants it |
| Git/index/worktree mutation | Authorized executor/candidate-persistence authority under current writer fence | Conditionally permitted only if later PoC authorization grants it |
| Git object creation | Candidate-persistence authority | Conditionally permitted only if later PoC authorization grants it |
| Branch/ref mutation | Authorized writer + repository write authority | Optional, only if the later PoC explicitly requires it |
| Draft PR creation/update | Separate publication authority | Denied by minimum PoC |
| Reviewer GitHub review/comment publication | Separate reviewer-publication authority | Denied by minimum PoC |
| PR ready transition | Coordinator/human publication authority | Denied by minimum PoC |
| Merge | Coordinator/human exact publication authority | Denied by minimum PoC |
| External tracker/issue mutation | Applicable external state owner | Denied by minimum PoC |

A read-only reviewer filesystem does not prove absence of remote mutation authority. Reviewer transport permissions and credentials remain separately bounded and are target-environment claims under Section 14.

---

# 11. Reconciliation contract

Reconciliation always compares four domains:

```text
1. authoritative semantic state
2. runtime/journal and writer-fence state
3. workspace and Git state
4. transport and remote/external effect state
```

## 11.1 Precedence rules

* Workflow/project/task authority controls semantic permission.
* The resolved designated execution-state owner/recorder controls the relied-upon semantic transition.
* The authoritative current-claim owner/store controls which writer generation is current.
* Live Git/GitHub controls actual repository state.
* Live transport/process inspection controls actual worker/reviewer state only to the extent proven by transport/substrate evidence.
* Journal state controls only controller-local history.
* Cached observations control nothing when current evidence disagrees.

## 11.2 Mandatory reconciliation points

Reconciliation is required:

* after controller restart;
* after transport disconnect;
* after an ambiguous mutation response;
* before replacement writer dispatch;
* before reviewer replacement;
* before review dispatch;
* before correction dispatch;
* before relying on a persisted candidate;
* before release/transfer of a writer claim;
* before retry of any non-trivially repeatable consequential effect.

## 11.3 Candidate reconciliation

A candidate is identified only by exact immutable identity.

A moving branch cannot alter the identity of the candidate already under review.

If branch head changes from `C1` to `C2`:

* review of `C1` remains review of `C1`;
* `C2` is not reviewed by implication;
* the controller cannot retarget the existing reviewer silently;
* any intended use of `C2` enters new candidate/review handling.

## 11.4 Ambiguous effect rule

When an effect may have succeeded but acknowledgement is missing:

1. stop new effects in the affected domain;
2. preserve the original operation descriptor unchanged;
3. perform read-only inspection using the descriptor's exact target and reconciliation rule;
4. establish whether the intended effect did not occur, occurred exactly once with the intended identity, or remains ambiguous/conflicting;
5. reconcile journal and writer-fence observations against actual state;
6. if exact intended completion is proved, record `RECOGNIZE_COMPLETED` and do not repeat;
7. retry only if non-occurrence is proved and the descriptor's expected state still holds, or if a stable idempotency/deduplication rule proves repetition safe;
8. otherwise enter `BLOCKED` and require accountable recovery/intervention.

This preserves DI-2's operation-aware recovery requirement.

## 11.5 Writer reconciliation

Writer reconciliation is separate from journal reconstruction.

It must establish:

* authoritative current claim ID/generation;
* whether the predecessor process/session can still produce effects;
* whether any effect issued under that generation remains unresolved;
* exact workspace/Git state produced so far;
* whether release/transfer guards are satisfied.

A newer journal entry cannot supersede a still-capable predecessor. A successor generation cannot be acquired until Section 8 containment/reconciliation guards pass.

---

# 12. Failure and recovery contract

DR-006 identified load-bearing classes that later conformance must exercise, including quiet workers, partial publication, moving candidates, reviewer failure, restart, duplicate writer attempts and unauthorized merge.

| Case | Observed runtime fact | Engineering/workflow semantic state | Permitted recovery | Required evidence | Fail-closed condition |
| --- | --- | --- | --- | --- | --- |
| 1. Worker appears quiet | No recent observable output | No semantic failure inferred | Inspect transport/process/liveness | worker/thread/process identity and activity | No release/replacement from silence |
| 2. Executor exits without candidate | Executor no longer running | Candidate not established | Reconcile working output and authoritative task state | workspace state, output, transport result | Reviewer dispatch denied |
| 3. Verification failure | Verification owner reports fail | Verification remains failed for exact subject | Return only to separately authorized correction/reframe path | exact subject + verification evidence | No review/pass promotion |
| 4. Partial Git/publication effect | Mutation result uncertain or partial | External effect unresolved | Apply original effect descriptor readback; recognize exact completion or block | exact operation ID, refs/objects/target state | Blind repetition denied |
| 5. Moving candidate branch | Mutable branch differs from reviewed SHA | Reviewed candidate identity unchanged | Continue only against exact immutable subject or create new candidate flow | old/new exact SHA, ref history | Branch head cannot substitute for candidate |
| 6. Reviewer process failure | Reviewer died/no valid result | Review remains pending, no verdict | Contain reviewer; start only a new fresh reviewer under fresh authority | unchanged candidate + failed reviewer state | No inferred verdict |
| 7. Correction after review | Executor changes content | Prior review historical | New C2, affected verification, new independent review | C1, finding, C2, impact evidence | Prior review cannot transfer automatically |
| 8. Coordinator restart | Runtime memory lost/uncertain | Semantic state remains owned externally | Enter `RECONCILING`; apply Section 5.4 projection | journal + authority + claim store + transport + Git + effects | No mutation before deterministic projection |
| 9. Duplicate writer attempt | Second executor requests write claim | Existing writer remains sole writer | Atomic acquisition denies second claim; inspect if claim state ambiguous | claim acquisition IDs/generations + live predecessor status | Two current generations never valid |
| 10. Stale writer after restart | Old executor may still be able to write | No successor authority implied | Deny stale generation; contain and reconcile predecessor before any successor generation | current claim store, stale-denial evidence, process/effect containment | No successor writer while predecessor can still effect |
| 11. Changed/ambiguous authority | Current authority differs or cannot be resolved | Dependent gate becomes stale/invalid | Stop and return to accountable owner/reframing | fresh owner/recorder reads and exact versions | No effects based on stale authority |
| 12. Acceptance/ready/merge attempt without authority | Runtime receives prohibited request | No acceptance/publication permission exists | Deny effect | attempted operation + current authority | Mutation prohibited |
| 13. Stale external effect | Delayed/queued effect appears after local expectation changed | Residual/external state requires reconciliation | Isolate, inspect, attribute, then owner-directed recovery | external object identity + original operation descriptor | Stale success cannot count as current success |
| 14. Missing/corrupt journal | Durable runtime record unavailable | No semantic reset occurs | Reconstruct only from live authority/claim/process/Git/effect evidence | exact live evidence and new recovery episode | If writer/effect safety cannot be proven, `BLOCKED` |

Recovery episodes remain durable history. A later successful reconciliation must not rewrite a prior failed, stale or ambiguous attempt into success.

---

# 13. Recovery journal design

## 13.1 Decision

A minimal durable recovery journal is required.

DR-006 identifies a runtime journal as the appropriate place for task, worker, workspace, candidate and reviewer identifiers, provided that it remains execution/recovery evidence rather than a competing task or acceptance owner.

A database is not required by this design. Storage mechanism remains deferred.

The journal is also not the authoritative current writer-claim store unless a later implementation explicitly proves one storage component satisfies both roles while retaining the distinct ownership semantics. This design does not select that implementation.

## 13.2 Minimum permissible record

A journal may contain:

```text
journal schema/version
runtime run ID
task ID and authoritative task reference
observed authority subject/version/digest
resolved designated execution-state owner
resolved sole recorder, where applicable
observed authoritative semantic transition relied upon
repository and authorized base
current runtime-controller state
pre-crash/runtime predecessor phase where relevant

executor:
  transport type
  worker/thread identity
  attempt identity

workspace:
  workspace/worktree identity
  repository identity

writer claim observation:
  authoritative current-claim store reference
  claim ID
  generation
  owner/writer identity
  scope
  observed status
  acquisition/release operation IDs

candidate pointer:
  full SHA
  tree/parent pointers when relied upon

review:
  reviewer runtime identity
  reviewed candidate SHA
  authoritative review-record pointer

current operation/effect:
  operation ID
  effect class
  authority reference
  exact target identity
  expected/precondition state
  writer generation where applicable
  repeatability/idempotency class
  intended result identity/binding rule
  observed outcome
  reconciliation/readback rule
  safe retry predicate

recovery:
  episode ID
  prior episode pointer
  reconciliation status
  unresolved runtime obligations

last reconciliation:
  observed authority versions
  authoritative current claim/generation
  transport/process state
  Git state
  external-effect state
  timestamp/evidence pointers
```

## 13.3 Forbidden journal content as authority

The journal must not independently own mutable values such as:

* task objective;
* product requirements;
* research status;
* Workflow v1 task-control state;
* semantic cancellation or recovery state;
* candidate validity;
* verification verdict;
* review verdict;
* coordinator acceptance;
* publication authorization;
* current writer ownership merely by virtue of containing a claim record.

It may store exact pointers and cached observations of those states.

## 13.4 Retention

The runtime journal must be retained until:

1. runtime reaches a terminal state;
2. no current writer claim or stale-capable predecessor remains;
3. every consequential effect is reconciled;
4. every relied-upon recovery/fencing history item has been moved to or retained by an explicit evidence custodian.

Conformance evidence relying on a recovery/fencing episode must retain that episode until the conformance-evidence disposition is complete.

## 13.5 Missing or corrupt journal

A missing/corrupt journal does not grant a clean start.

If live authority, authoritative writer-claim state, process/transport state, workspace/Git state and external-effect state are sufficient to reconstruct safety deterministically, the controller may establish a new reconciled runtime episode under fresh authority.

If current/stale writer capability, claim generation or consequential effect state cannot be reconstructed, continuation is `BLOCKED`.

A missing journal never permits generation reset, timeout release, candidate recreation, reviewer retargeting or semantic state inference.

---

# 14. D13 conformance-evidence contract

This section defines the prerequisite required by the existing accepted D13 condition.

It does not claim the prerequisite has been satisfied and does not authorize conformance execution.

## 14.1 Gate sequence

### Stage 1: design acceptance

The exact D13 prerequisite design must receive:

* fresh independent review;
* explicit coordinator disposition.

This establishes the accepted architecture/ownership contract.

It is not conformance evidence.

### Stage 2: separately authorized D13 prerequisite conformance evidence

A later evidence gate may authorize an exact conformance realization and scenarios. That gate must identify which conformance layer each claim belongs to and must preserve the claim ceilings in Sections 14.2 through 14.5.

A design, test plan, fixture specification, scenario matrix, green test aggregate or producer statement is not itself conformance evidence.

Fixture-only evidence cannot by itself satisfy the accepted D13 conformance prerequisite.

### Stage 3: D13 PoC consideration

Only after the accepted design and accepted D13 prerequisite conformance evidence exist may a coordinator consider, but is not required to choose:

`CONDITIONALLY SELECT FOR ONE BOUNDED POC`

for D13.

### Stage 4: separately authorized target PoC

A later authorized target-environment PoC produces operational evidence for a selected bounded mechanism and target.

Target PoC evidence is not retroactively part of design acceptance or abstract-controller conformance.

### Stage 5: operational adoption

Routine, reusable or broader orchestration mode requires another explicit disposition based on actual PoC and operational evidence.

Neither D13 prerequisite satisfaction nor one PoC automatically authorizes operational adoption.

## 14.2 Layer A: abstract-controller conformance

### Claim ceiling

Layer A may establish only that an exact executable realization of the transport-neutral controller contract preserves the accepted authority, state, fencing, identity and recovery semantics.

Layer A does not select or certify a transport and does not prove target-environment permissions, credentials, sandboxing or external-service behavior.

### Permitted fixture evidence

Deterministic transport/effect test doubles and non-operational fixtures may legitimately prove controller decisions whose truth depends only on supplied inputs and deterministic controller logic, including:

* transition determinism;
* stale-authority input denial by controller logic;
* DI-1 false-equivalence rejection;
* exact-candidate mismatch rejection;
* one-correction ceiling logic;
* effect-descriptor completeness validation;
* safe-retry predicate evaluation against modeled observations;
* absence of controller transitions to acceptance/ready/merge;
* denial of unauthorized effect requests before a real effect boundary is invoked.

These are limited claims about controller behavior. A fixture result cannot be promoted into a claim about a real persistence, process, Git, transport or target substrate.

### Required real executable/substrate evidence within Layer A

The accepted D13 prerequisite cannot rely only on doubles for these transport-neutral but substrate-dependent properties:

* the exact controller realization must actually execute, not exist only as prose or pseudocode;
* durable journal persistence and controller restart must be exercised against real durable storage behavior, including missing/corrupt/restart cases;
* writer fencing must be exercised against the real authoritative claim implementation with concurrent/competing acquisition and crash/restart conditions;
* stale generation must be denied at actual write-capable boundaries used by the realization;
* process containment must be exercised against real process/worker behavior sufficient to prove predecessor inability to continue in-scope effects;
* real Git repositories must be used for candidate object identity, parent/tree binding and any ref expected-state behavior claimed by the realization;
* at least one ambiguous consequential effect must be exercised with a real operation substrate or a controlled fault around a real operation such that actual before/after state is reconciled by readback rather than supplied by a fake effect outcome;
* restart projection must reconstruct from actual durable journal, claim, process and Git/effect observations.

A deterministic fixture may trigger fault conditions around these substrates, but it may not replace the substrate whose semantics are being claimed.

## 14.3 Layer B: transport conformance

### Claim ceiling

Layer B may establish only that one exact named transport adapter, in an explicitly identified conformance environment, satisfies the execution/reviewer lifecycle contract required by this design.

Transport conformance evidence is technical evidence for later D13 reconsideration. Producing or accepting it does not itself select the transport, change D13, authorize a PoC or satisfy D5 when D5 applies.

### Required real transport evidence

For any transport proposed for later D13 reconsideration, Layer B must use the actual transport surface and establish at minimum:

* fresh executor start under a bounded grant;
* exact worker/session identity observation;
* same-executor continuity where correction continuity is claimed;
* interruption/termination and liveness semantics used by containment;
* restart/reconciliation ability for the identities the controller relies upon;
* fresh reviewer creation as a new execution/context identity;
* no executor-history inheritance for the reviewer path;
* immutable candidate binding to reviewer input;
* structured reviewer result behavior relied upon by the controller;
* reviewer candidate-write capability is withheld at the transport permission boundary to the extent the transport controls it.

A fake transport can test Layer A adapter calls. It cannot establish these Layer B claims.

A transport-specific limitation discovered here may make that candidate ineligible for later D13 reconsideration without changing the abstract architecture.

## 14.4 Layer C: target-environment conformance

### Claim ceiling

Layer C establishes behavior of a concrete selected transport/controller realization in a concrete target environment.

It may cover:

* actual filesystem and process isolation;
* actual sandbox/network behavior;
* actual credentials and repository permissions;
* actual Git remote/protection configuration;
* actual reviewer inability to mutate candidate/remote state;
* actual external effect containment and readback;
* target-specific retention, process lifecycle and operational failure modes.

These properties cannot be proven by abstract fixtures or by transport protocol inspection alone.

### Relationship to the D13 prerequisite

Layer C is separate from the D13 prerequisite conformance gate and normally belongs to later bounded PoC/operational validation after a mechanism is explicitly selected/authorized.

The D13 prerequisite package must therefore mark target-environment properties as `not claimed / deferred to Layer C` rather than simulate them and report PASS.

A later authority may explicitly require a named Layer C property before PoC authorization, but this design does not impose or satisfy that later gate.

## 14.5 Composition required before D13 reconsideration

Before a coordinator may consider a specific transport candidate for `CONDITIONALLY SELECT FOR ONE BOUNDED POC`, the accepted D13 prerequisite evidence must include:

1. accepted Layer A evidence for the exact executable transport-neutral controller realization, including the real substrate properties in Section 14.2;
2. accepted Layer B evidence for the exact transport candidate being considered;
3. explicit accounting of all Layer C properties as deferred/not claimed unless a separate authority already required and accepted them;
4. fresh independent review of the exact conformance evidence package;
5. explicit coordinator acceptance that the package satisfies the D13 prerequisite for reconsideration only.

Passing Layer A alone does not make any transport eligible. Passing Layer B without Layer A does not establish Workflow conformance. Neither layer authorizes Layer C execution or PoC.

## 14.6 Required D13 prerequisite evidence classes

### A. Authority preservation

Evidence that:

* controller consumes current authoritative policy;
* controller resolves one exact designated execution-state owner/recorder;
* controller cannot self-authorize or self-record semantic task-control transitions;
* stale authority denies dispatch/resumption;
* runtime state cannot overwrite Workflow/project state.

### B. DI-1 state-plane separation

Evidence that at least these false equivalences are rejected:

* worker complete != task accepted;
* candidate exists != verified;
* verification passed != review passed;
* review passed != coordinator acceptance;
* PR/branch state != semantic acceptance;
* runtime stopped != Workflow terminal success.

### C. DI-2 behavior

Actual evidence for:

* freshness checks;
* stale-authority denial;
* operation-aware retry;
* containment;
* retained recovery history;
* intervention boundary;
* terminal guards;
* exact identity reconciliation.

Workflow v1 treats inability to represent required non-success and omitted/not-applicable distinctions as nonconformance.

### D. Exclusive writer behavior

Evidence for:

* one authoritative current-claim owner/store;
* atomic unique claim acquisition;
* monotonic generations;
* duplicate acquisition/dispatch rejection;
* current-generation validation on actual write-capable boundaries;
* stale-generation denial;
* no claim release based only on silence;
* stale writer after restart;
* predecessor containment before replacement;
* correction retaining sole-writer semantics;
* durable historical claim/recovery evidence.

### E. Independent-review behavior

Evidence for:

* new reviewer identity;
* new reviewer context;
* no executor-history inheritance;
* no candidate-write claim;
* immutable reviewed SHA;
* failed reviewer creates no verdict;
* replacement reviewer is independently fresh.

### F. Immutable candidate binding

Evidence for:

* exact SHA binding;
* branch movement cannot retarget review;
* wrong-subject review is rejected;
* reviewed candidate mutation creates new identity.

### G. Correction and re-review

Evidence for:

```text
candidate C1
-> review requires correction
-> one authorized correction
-> candidate C2
-> affected verification
-> fresh reviewer R2
```

with `C1 != C2`.

### H. Restart/reconciliation

Evidence that controller restart applies the Section 5.4 projection and cannot dispatch until authority, writer fence, worker/reviewer identity, Git and outstanding effect state resolve to one permitted result.

### I. Partial/ambiguous effect handling

Evidence for at least one allowed consequential effect where:

* the original effect descriptor is preserved;
* blind retry is rejected;
* read-only inspection occurs;
* exact previous effect/non-effect is established where possible;
* continuation/recovery follows the descriptor's operation semantics;
* unresolved ambiguity becomes `BLOCKED` rather than success.

### J. Unauthorized consequential effects

Negative evidence showing denial of:

* automatic human acceptance;
* PR ready transition without authority;
* merge without authority;
* unauthorized external tracker mutation;
* unauthorized reviewer publication;
* external mutation outside the granted scope.

---

# 15. Evidence-to-layer matrix

The conformance package must state exactly which layer supports every claim.

| Property | Deterministic fixture/test double | Real transport-neutral substrate | Actual transport | Target environment |
| --- | --- | --- | --- | --- |
| Controller transition determinism | Sufficient for logic claim on exact executable controller | Not additionally required for pure transition logic | Not required | Not required |
| DI-1 false-equivalence rejection | Sufficient for controller logic | Not required for pure logic | Not required | Not required |
| Stale-authority input denial | Sufficient for decision logic | Real authority-resolution integration required for freshness-source claim | Not inherently | Target owner/config only if target-specific |
| Effect-descriptor validation | Sufficient for descriptor/guard logic | Real effect substrate required for actual reconciliation claim | Not inherently | Target-specific effect claims later |
| Duplicate dispatch inside one controller | Sufficient for local guard logic only | Real claim store/concurrency required for global exclusivity | Not inherently | Not required for generic claim |
| Atomic unique writer acquisition | Not sufficient | Required | Not inherently | Target-specific deployment later |
| Stale writer unable to mutate after successor generation | Not sufficient | Required with real fencing boundary + process containment | Transport evidence may be required for transport-spawned writer containment | Target permissions/process model later |
| Durable journal survives crash | In-memory fake not sufficient | Required with real durable storage + restart | Not inherently | Target storage later if claimed |
| Missing/corrupt journal fail-closed | May test logic branch | Required for storage/recovery claim | Not inherently | Target storage later if claimed |
| Git object/candidate identity behavior | Fake Git not sufficient | Required with real Git repository | Not required | Remote/protection only if later claimed |
| Ref expected-state/CAS behavior | Fake ref not sufficient | Required if ref mutation is in prerequisite realization | Not required | Actual remote rules later if claimed |
| Ambiguous effect reconciliation | Fake outcome only insufficient | Required around a real allowed operation substrate | Transport if ambiguity originates in transport | Target external service later if claimed |
| Fresh reviewer context | Fake transport not sufficient | Controller can prove it requests freshness, not that transport provides it | Required | Target credentials/history isolation later if applicable |
| Transport resume/read/interrupt/reconcile | Not sufficient | Not sufficient | Required | Target process-retention behavior later if different |
| Reviewer lacks effective external write capability | Controller/fixture can prove denied request path only | Local capability can be tested if part of realization | Transport permission boundary may be tested | Actual credentials/remote permissions require Layer C |
| Sandbox/network/credential behavior | Not sufficient | Not sufficient for target claim | Protocol docs not sufficient | Required in Layer C |

Fixture evidence is legitimate only for the claim ceiling shown above. It must never be summarized as evidence that a stronger real-substrate, transport or target property passed.

---

# 16. D13 prerequisite conformance acceptance bar

The D13 conformance prerequisite is satisfied only when all of the following are true:

1. the accepted prerequisite design has an exact immutable identity;
2. the conformance gate has separate explicit authority and scope;
3. the exact executable Layer A controller realization has an immutable identity;
4. every mandatory Layer A controller-logic scenario has actually run;
5. durable journal/restart evidence uses real durable storage behavior, not an in-memory-only double;
6. writer-fencing evidence uses the real claim implementation, competing acquisition and actual current-generation enforcement;
7. process containment evidence proves predecessor inability to continue in-scope effects for the realization under test;
8. Git identity/reconciliation claims use real Git object/ref behavior for every Git property claimed;
9. at least one ambiguous allowed effect is reconciled against actual operation state rather than a fake outcome alone;
10. all negative cases fail closed;
11. no scenario silently converts transport/process state into Workflow semantic truth;
12. exact execution-state owner/recorder resolution and fresh semantic-transition readback are demonstrated;
13. immutable candidate and correction semantics are demonstrated;
14. restart projection and retained recovery history are demonstrated;
15. exact effect descriptors and safe-retry predicates are evidenced for every allowed consequential effect exercised;
16. Layer B conformance has been established for the exact transport candidate proposed for later D13 reconsideration;
17. transport reviewer freshness/independence and lifecycle semantics relied upon by the controller are demonstrated on the real transport surface;
18. Layer C properties are explicitly marked deferred/not claimed unless separately required and accepted;
19. DI-1 and DI-2 are explicitly evaluated against the exact evidence;
20. fixture-only results are not used to satisfy a real-substrate or transport claim;
21. the exact conformance package receives fresh independent review;
22. no unresolved blocker or major finding remains for the claimed D13 prerequisite scope;
23. an explicit coordinator disposition accepts that exact evidence as satisfying the D13 conformance prerequisite for reconsideration only.

A design, fixture specification, scenario matrix, green unit-test aggregate, successful happy path or producer statement does not satisfy this bar by itself.

A successful happy path alone was already rejected as sufficient evidence by DR-006.

Passing this bar does not select a transport, change D13, satisfy D5, authorize a PoC or establish target-environment conformance.

---

# 17. Exact checklist before future D13 bounded-PoC consideration

A future coordinator may consider `CONDITIONALLY SELECT FOR ONE BOUNDED POC` for D13 only after all items below are satisfied.

### Design acceptance

* [ ] Live D13 authority has been freshly reverified.
* [ ] No newer authority supersedes or conflicts with the applicable D13 condition.
* [ ] This prerequisite design has an exact immutable review subject.
* [ ] The exact design has passed fresh independent review.
* [ ] The coordinator has explicitly accepted the design for D13 prerequisite purposes.
* [ ] Semantic execution-state ownership/recorder resolution is accepted.
* [ ] Runtime-state ownership has one accepted owner and no competing semantic-state owner.
* [ ] Recovery-journal boundaries are accepted.
* [ ] Minimal authority/controller/transport adapter contract is accepted.
* [ ] Enforceable writer-fencing contract is accepted.
* [ ] Reviewer-independence contract is accepted.
* [ ] Consequential-effect descriptor/reconciliation contract is accepted.
* [ ] Exhaustive restart/reconciliation projection is accepted.

### Layer A abstract-controller conformance

* [ ] A separately authorized exact executable controller realization exists.
* [ ] Controller transition/negative-guard scenarios were actually exercised.
* [ ] Stale-authority denial passed.
* [ ] DI-1 state separation passed.
* [ ] DI-2 freshness/retry/containment/recovery/intervention/terminal behavior passed for the claimed Layer A scope.
* [ ] Real durable journal/restart scenarios passed.
* [ ] Atomic writer acquisition and duplicate-writer denial passed on the real claim implementation.
* [ ] Stale-generation denial passed on actual write-capable boundaries.
* [ ] Stale-writer replacement denial and predecessor containment passed.
* [ ] Real Git candidate identity/binding behavior passed.
* [ ] Controller restart/reconciliation projection passed.
* [ ] At least one real-substrate ambiguous-effect recovery scenario passed.
* [ ] Unauthorized acceptance/ready/merge request denial passed.
* [ ] Unauthorized external-effect request denial passed.

### Layer B transport conformance for the candidate being reconsidered

* [ ] The transport candidate has an exact version/source/config identity.
* [ ] Real transport lifecycle evidence exists for start/observe/resume-or-continuity/interrupt/reconcile behavior relied upon by the controller.
* [ ] Independent-review freshness passed on the actual transport.
* [ ] Reviewer no-history-inheritance claim passed on the actual transport.
* [ ] Immutable candidate binding passed through the actual reviewer transport path.
* [ ] Correction C1 -> C2 -> fresh R2 behavior passed through the transport path.
* [ ] Transport conformance received fresh independent review.

### Package disposition and Layer C accounting

* [ ] The complete D13 prerequisite conformance package received fresh independent review.
* [ ] Every claim is labeled Layer A, B or deferred Layer C.
* [ ] No fixture-only result is used for a stronger real-substrate/transport/target claim.
* [ ] The coordinator explicitly accepted the exact conformance evidence for D13 prerequisite purposes.
* [ ] All target-environment properties not yet tested are explicitly listed as deferred/not claimed.
* [ ] The bounded orchestration need still exists and remains appropriate for a single supervised writer/reviewer PoC.
* [ ] No unresolved D13 prerequisite blocker remains.

Completion of this checklist makes D13 eligible for reconsideration only.

It does not itself change D13 from `CONFIRM DEFER`, select D5, authorize target-environment PoC execution or establish operational adoption.

---

# 18. D5 separation

D5 remains independently:

**CONFIRM DEFER**

The current disposition explicitly prohibits interpreting D13 design acceptance or prerequisite satisfaction as D5 selection.

Therefore:

```text
D13 prerequisite design accepted
        +
D13 conformance evidence accepted
        |
        v
D13 may become eligible for reconsideration

BUT

App Server PoC
        requires
        |
        +--> applicable D13 PoC disposition
        |
        +--> separate applicable D5 selection/reconsideration
             OR one explicit later disposition naming both D5 and D13
```

If a future PoC proposes App Server, D5 evaluation must separately establish at minimum:

* concrete integration/lifecycle need;
* why the intended native alternative is insufficient for that need;
* exact current App Server/client version or source identity;
* exact required protocol methods/fields;
* stable versus experimental dependency inventory;
* authentication/permission/sandbox assumptions;
* process/thread retention behavior needed by the design;
* target-environment configuration;
* dependency and operational surface;
* explicit D5 mechanism-selection decision.

Current App Server lifecycle facts support comparison only. They do not satisfy these requirements.

---

# 19. Maximum future PoC boundary

This section defines a ceiling for later use. It does not authorize execution.

The maximum intended D13 prerequisite-enabled PoC is:

```text
one already-authorized bounded task
        |
        v
one executor
one active writer claim
        |
        v
exact immutable candidate C1
        |
        v
fresh independent reviewer R1
        |
        +-- PASS --> STOP BEFORE HUMAN ACCEPTANCE
        |
        +-- correction required
                |
                v
        same authorized executor
        one correction cycle only
                |
                v
        new exact candidate C2
                |
                v
        fresh independent reviewer R2
                |
                v
        STOP BEFORE HUMAN ACCEPTANCE
```

The PoC must additionally contain controlled evidence for:

* one coordinator restart/reconciliation episode;
* one duplicate-writer denial.

The maximum boundary excludes:

* automatic acceptance;
* PR ready transition;
* merge;
* branch cleanup;
* automatic reviewer GitHub publication;
* external tracker migration;
* general scheduler;
* parallel writers;
* distributed workers;
* SSH pools;
* dashboards;
* production multi-project operation;
* unattended execution;
* AFK execution.

---

# 20. Decision matrix

| Question | Current design conclusion | Evidence basis | Remaining prerequisite | Authority owner |
| --- | --- | --- | --- | --- |
| Semantic execution-state owner | Resolver must identify exact designated run/task execution-state owner and sole recorder where applicable; controller can supply facts/request transitions only | Workflow v1 + task-control reference + review correction | Independent design acceptance; later conformance | Existing task/run semantic owner and recorder |
| Runtime-state owner | One deterministic runtime controller owns execution-local lifecycle only | Workflow v1, DR-006 | Independent design acceptance; later conformance | Runtime controller for local state; existing owners for semantics |
| Recovery journal | Required, minimal and durable; not a tracker, semantic record or writer-fence owner | Workflow durability/recovery + DR-006 | Storage realization and real restart conformance | Runtime controller for journal history |
| Writer fencing | One authoritative current-claim owner/store, atomic acquisition, monotonic fencing generation, per-write validation, containment before successor generation | DR-006, Workflow owner separation, review correction | Real implementation and conformance exercise | Current-claim owner/store for fencing; project/external owners for effects |
| Adapter boundary | Read-only authority resolver + deterministic controller + replaceable transport + side-effect reconciler | DR-006 disposition and Workflow v1 | Design review/acceptance | Workflow/project owners retain policy; controller owns execution-local state |
| Native thread compatibility | Abstractly compatible, but transport/restart/control evidence remains incomplete | DR-006 | Layer B evidence if later proposed | Future transport decision owner |
| App Server compatibility | Abstractly compatible; current comparison does not select it | DR-006 + targeted current primary source | Separate D5 decision plus Layer B/target evidence if later proposed | D5 coordinator decision owner |
| Reviewer independence | Fresh context, exact SHA, no write claim, no executor-history inheritance | Workflow v1, DR-006 | Layer B actual transport evidence | Review authority / independent reviewer |
| Consequential effects | Default deny; every allowed effect uses immutable descriptor + operation-specific readback/safe-retry predicate | Workflow v1 + protected write path | Real-substrate Layer A exercise for allowed classes | Applicable mutation owner; controller only enforces granted operation |
| D13 conformance evidence | Layer A + Layer B required before a specific transport candidate can be reconsidered; fixture-only insufficient; Layer C remains separately deferred unless later required | DR-005 D13 condition + DR-006 disposition + review correction | Future separately authorized conformance-evidence gate | Coordinator consumes reviewed evidence |
| D5 mechanism selection | Still deferred | DR-005 + DR-006 disposition | Separate D5 reconsideration/selection | Coordinator |
| Target-environment conformance | Separate later Layer C evidence, normally PoC/operational | DR-006 non-authority boundary | Mechanism selection and explicit target gate | Applicable target/accountable owner |
| PoC authorization | None | DR-006 disposition | Accepted D13 design + accepted prerequisite conformance + applicable mechanism authority | Coordinator/accountable human |
| Operational adoption | None | Charter, Workflow v1, DR-006 | PoC result and later operational disposition | Applicable accountable owner |

---

# 21. Open questions and gaps

There are no known `BLOCKS DESIGN ACCEPTANCE` questions left unresolved by this corrected proposal. The semantic rules needed for deterministic implementation and later conformance review are specified without selecting a mechanism or storage technology.

The remaining gaps are later-gate evidence or implementation choices, not unresolved design semantics.

| Open item | Classification | Resolution needed |
| --- | --- | --- |
| Exact future conformance realization and evidence custodian | `BLOCKS D13 RECONSIDERATION` | Later gate must authorize an exact executable Layer A realization, real substrate evidence package and durable evidence owner |
| Concrete implementation of authoritative writer-claim store/fencing and journal storage | `BLOCKS D13 RECONSIDERATION` | Must satisfy Sections 8 and 13 and be actually exercised; technology remains deferred |
| Transport conformance for a candidate proposed for D13 reconsideration | `BLOCKS D13 RECONSIDERATION` | Layer B must exercise the actual named transport without treating evidence collection as selection |
| Native-thread deterministic inspect/resume/containment behavior | `BLOCKS D13 RECONSIDERATION` if Native Threads become the proposed transport | Candidate-specific Layer B evidence required |
| Exact App Server client/version/protocol subset | `BLOCKS D5 SELECTION` and D13 reconsideration if App Server is proposed | Separate D5 evaluation plus candidate-specific Layer B evidence |
| Concrete target project/task authority for one PoC | `BLOCKS POC AUTHORIZATION` | Select an already authorized bounded task and its owners in a later gate |
| Target permissions/sandbox/credentials/process retention and allowed external effects | `BLOCKS POC AUTHORIZATION` or later operational claim when applicable | Layer C target-environment evidence; not simulated as D13 prerequisite PASS |
| Reviewer-to-GitHub publication architecture | `BLOCKS OPERATIONAL ADOPTION` if later required | Separate side-effect design and authorization |
| Routine multi-project persistence/retention policy | `BLOCKS OPERATIONAL ADOPTION` | Only if broader operation is later proposed |
| Adaptive model/reasoning routing | `NON-BLOCKING FOR CURRENT GATE` | Deferred optimization |
| Token/cost optimization | `NON-BLOCKING FOR CURRENT GATE` | Measure only after correct bounded behavior exists |

---

# 22. Explicit non-authorities

This proposal does not:

* satisfy D13;
* reconsider D13;
* select Symphony;
* select a custom harness;
* select Native Threads;
* select App Server;
* reconsider D5;
* authorize an App Server client;
* authorize implementation;
* authorize creation or execution of a conformance realization;
* authorize Layer A, Layer B or Layer C conformance execution;
* authorize a PoC;
* authorize a repository mutation;
* authorize automatic executor dispatch;
* authorize automatic correction loops;
* authorize reviewer-to-GitHub mutation;
* authorize a second tracker;
* require a database or lock service;
* create a general scheduler;
* authorize parallel writers;
* authorize automatic PR ready transition;
* authorize merge;
* authorize human/coordinator acceptance;
* authorize unattended or AFK operation;
* authorize external tracker mutation;
* authorize Workflow v1 amendment;
* change D5/D13/X3 disposition;
* accept a new repository baseline;
* convert Symphony defaults into ADW semantics.

The conformance taxonomy is a design claim model only. Naming a possible real-substrate or transport test does not authorize running it.

X3 therefore remains fully preserved.

---

# 23. Acceptance criteria for this design

The design is suitable for acceptance only if fresh independent review of the exact corrected proposal establishes that:

1. every mutable semantic state class has one authority;
2. exact designated execution-state owner and sole-recorder resolution is deterministic;
3. the controller can supply runtime facts/request transitions but cannot authoritatively write task-control, cancellation, recovery, review, acceptance or publication semantic state;
4. consequential dispatch/resumption requires fresh readback of the required authoritative semantic transition;
5. runtime state cannot become a competing Workflow/project owner;
6. the adapter contract is transport-replaceable;
7. no transport-specific behavior has been promoted into Workflow v1 semantics;
8. the runtime state machine is distinct from engineering semantic state;
9. restart/reconciliation projects every active/awaiting phase to one deterministic result under explicit guards;
10. the recovery journal is minimal and non-authoritative outside runtime history;
11. the journal is not treated as writer fencing merely because it records a claim;
12. writer fencing has one authoritative current-claim owner/store, atomic unique acquisition and monotonic generations;
13. current-generation validation is mandatory at every write-capable boundary or the surface is physically contained before successor generation;
14. writer replacement cannot occur from timeout/silence alone;
15. release/transfer requires predecessor containment and effect reconciliation;
16. reviewer independence excludes inherited executor history and candidate-write authority;
17. correction requires C2 and fresh affected review R2;
18. every allowed consequential effect uses the mandatory descriptor and operation-aware reconciliation/safe-retry rule;
19. effects outside the future minimum PoC have denial conformance only and are not overdesigned;
20. restart and ambiguous-effect reconciliation fail closed;
21. DI-1 remains intact;
22. DI-2 remains intact;
23. conformance claims are separated into Layer A abstract-controller, Layer B transport and Layer C target-environment layers;
24. fixture/test-double evidence has an explicit claim ceiling and fixture-only evidence cannot satisfy the accepted D13 conformance prerequisite;
25. real durable journal/restart, writer fencing, process containment, Git behavior and real-operation ambiguity handling are required where those properties are claimed;
26. actual transport lifecycle/fresh-review properties require Layer B evidence on the named transport;
27. target permissions/sandbox/credentials/external effects require Layer C evidence and are not falsely claimed by prerequisite fixtures;
28. D13 prerequisite conformance remains separate from target PoC/operational validation;
29. D13 eligibility is kept separate from D13 selection;
30. D13 selection is kept separate from PoC authorization;
31. D5 selection remains independent;
32. the future PoC ceiling stops before human acceptance;
33. no Workflow v1 amendment is required to implement the design;
34. no unresolved current-design blocker remains.

Review success would make the corrected proposal eligible for coordinator disposition, not self-accepted.

---

# 24. Proposed next gate

The architecture/design producer does not select the next gate as an authority.

The narrowest next gate supported by this proposal is:

**fresh independent review of the exact proposed D13 prerequisite design**

followed, if that review supports it, by:

**coordinator disposition of the exact reviewed D13 prerequisite design**

That disposition may accept, reject, defer or require correction of the design.

It must not automatically authorize:

* implementation;
* conformance execution;
* D13 selection;
* D5 selection;
* a PoC.

Any later conformance-evidence work requires its own explicit gate after design acceptance.

---

# Final producer status

The proposal defines a coherent single-owner runtime boundary, minimal replaceable adapter, recovery journal, writer and reviewer controls, side-effect and recovery semantics, D13 conformance evidence contract, exact D13 reconsideration prerequisites, and explicit D5 separation without selecting a mechanism or altering Workflow v1.

**READY FOR INDEPENDENT DESIGN REVIEW**

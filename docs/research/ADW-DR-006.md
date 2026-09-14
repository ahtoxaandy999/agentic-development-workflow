---
id: DR-006
artifact_status: draft
authority: evidence
research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: 2026-09-14
owner: agentic-development-research
question: >-
  Does current Symphony and Codex App Server evidence now justify reopening the
  DR-005 deferral of Symphony/custom harness infrastructure for a bounded
  executor -> independent reviewer -> correction orchestration proof of concept,
  while preserving Workflow v1 authority, review independence, exact-candidate
  identity, human acceptance, and current automation restrictions?
scope: >-
  Targeted successor research for the Symphony/App Server portion of DR-005.
  Compare model-driven native thread orchestration with a thin deterministic
  App Server coordinator; inspect the current OpenAI Symphony specification and
  reference implementation; map useful primitives and incompatibilities to ADW
  Workflow v1. No implementation, installation, tooling adoption, unattended
  execution, normative amendment, acceptance, merge, or new baseline.
repository_state:
  repository: ahtoxaandy999/agentic-development-workflow
  research_basis_main: 4e6af3db42950e9b7e5415b89f09b5d325fd78a6
  workflow_v1_owner: WORKFLOW-V1.md
  prior_tooling_evidence: docs/research/ADW-DR-005.md
  prior_tooling_disposition: docs/research/ADW-DR-005-DISPOSITION-001.md
  observation_scope: publication-time evidence snapshot; current mutable state remains with its repository owners
supersedes: >-
  DR-005 Symphony/App Server capability evidence and the factual premise used
  to defer D13 only where this note supplies fresher evidence. It does not
  supersede DR-005 as a whole, ADW-DR-005-DISPOSITION-001, X3, Workflow v1, or
  any current repository authority.
---

# ADW-DR-006 — Symphony and Codex App Server orchestration reassessment

## 1. Executive answer

**REPOSITORY FACT.** DR-005, frozen on 2026-09-04, recommended deferring `D13 — Symphony/custom harness infrastructure` because no proven dispatch volume or recovery need justified another controller. The accepted DR-005 disposition confirmed that deferral and required an accepted adapter/ownership design plus conformance evidence before reconsideration. It separately confirmed `X3`: unmodified Symphony or harness retry/stale-input/cleanup defaults must not be asserted as ADW conformance. [R01] [R02]

**DOCUMENTED FACT.** OpenAI's 2026-04-27 Symphony publication describes the motivating problem as human attention and context switching across multiple interactive Codex sessions. It states that Symphony's first implementation was a Codex session in `tmux` polling Linear and spawning subagents, that this approach worked but was not particularly reliable, and that the later design used Codex App Server as the programmatic execution surface. The current Symphony repository remains a reference/specification rather than a maintained standalone product commitment. [O01] [O02] [O03]

**DOCUMENTED FACT.** Current Codex App Server documentation exposes an explicit JSON-RPC lifecycle including `thread/start`, `thread/resume`, `thread/fork`, `thread/read`, `turn/start`, `turn/steer`, `turn/interrupt`, and final `turn/completed` notifications. `turn/completed` carries a final status of `completed`, `interrupted`, or `failed`. `turn/start` supports a per-turn `outputSchema`, and thread resume preserves a stored executor conversation without requiring the client to infer completion from prose. [O04]

**DOCUMENTED FACT.** At pinned Symphony commit `e0ccc83720a42a600a53b61c5f8d3e518bebe1db`, the Elixir reference implementation has a single orchestrator state, per-work-item workspace management, Codex App Server client, explicit turn event handling, retry/reconciliation logic, blocked-state handling, local and SSH worker support, and tracker adapters for Linear, GitHub Issues, Jira Cloud, Asana, and GitLab. The README still warns that the Elixir implementation is prototype software for evaluation and recommends implementing a hardened version from `SPEC.md`. [O02] [O03] [O05]-[O10]

**INFERENCE.** The factual premise behind D13 has materially changed in one important respect: there is now a concrete recurring orchestration problem to solve, namely manual routing between bounded executors and fresh independent reviewers, plus correction and re-review, and the current first-party App Server surface provides substantially stronger lifecycle primitives than a model-only coordinator. This satisfies the *research trigger to reconsider D13*. It does not by itself satisfy the separate adoption, safety, recovery, or conformance gates required to deploy a controller.

**RECOMMENDATION — GO FOR A BOUNDED ARCHITECTURE POC, NOT DEPLOYMENT.** Reopen D13 only far enough to authorize later evaluation of a minimal Symphony-informed coordinator over Codex App Server. Keep X3 fully intact: do not deploy Symphony unmodified and do not treat Symphony defaults as Workflow v1 semantics. The target should be a thin deterministic coordination layer whose first bounded use case is:

```text
already-authorized bounded task
→ isolated executor
→ existing project-owned verification and exact candidate publication
→ fresh independent reviewer bound to the exact immutable candidate
→ correction routed back to the same executor context when required
→ fresh affected re-review of the new candidate
→ stop at READY FOR HUMAN ACCEPTANCE
```

**RECOMMENDATION — NO-GO FOR CURRENT AUTOMATION AUTHORITY.** This research grants no routine, parallel-write, automated-write, unattended, AFK, acceptance, merge, branch-cleanup, tracker-migration, or new mutable-state authority. Any implementation or operational trial requires its own later gate.

## 2. Boundary with DR-005 and Workflow v1

This note is a targeted evidence successor, not a silent policy change.

The following DR-005 conclusions remain valid:

- exact repository identities, verification, review, disposition, and acceptance stay separate;
- a worktree is isolation, not exclusive writer fencing;
- cancellation or process exit is not verified containment;
- blind retry is not operation-aware recovery;
- producer self-check, auto-review, or a fork of producer context is not independent review;
- unmodified Symphony defaults are not ADW conformance;
- human/coordinator acceptance remains a separate gate.

The only recommendation reopened is the *timing of D13 evaluation*. DR-005 said to reconsider D13 after demonstrated dispatch/recovery need plus accepted ownership/adapter design and conformance evidence. The current problem supplies demonstrated need for a narrower orchestration use case, so a bounded proof of concept is now justified as evidence production. The ownership and conformance prerequisites are still unresolved and therefore block operational adoption. [R01] [R02]

`PROJECT-CHARTER.md` and `WORKFLOW-V1.md` remain authoritative. A future coordinator must consume those semantics; it must not become a second normative workflow owner. [R03] [R04]

## 3. What Symphony actually contributes

### 3.1 Single scheduler authority

**DOCUMENTED FACT.** Symphony's specification requires one authoritative orchestrator state for dispatch, retries, and reconciliation. The current Elixir implementation keeps `running`, `claimed`, `blocked`, `retry_attempts`, completion bookkeeping, token totals, and rate-limit information in the orchestrator. Before dispatch it revalidates the work item and checks claims, active/routable state, and concurrency. [O02] [O08]

**INFERENCE.** This is the most transferable Symphony principle for ADW: orchestration runtime state should have one owner. It must remain distinct from normative workflow state, candidate identity, review verdict, and human acceptance.

### 3.2 Workspace isolation

**DOCUMENTED FACT.** Symphony maps each work item to an isolated workspace, validates that local workspaces stay under the configured root, guards path/symlink escapes, and exposes lifecycle hooks around workspace creation/run/removal. [O06]

**INFERENCE.** ADW should reuse the isolation principle, but not assume Symphony's directory model is sufficient writer fencing. A future implementation must explicitly bind one writer to one task/worktree and keep reviewer workspaces read-only where feasible.

### 3.3 App Server as execution transport

**DOCUMENTED FACT.** Symphony's `AgentRunner` creates a workspace, launches one App Server session, executes one or more turns in the same thread, receives structured updates, and then returns control to the orchestrator. The App Server client performs `initialize`/`initialized`, `thread/start`, `turn/start`, and waits for explicit completion/error events. [O07] [O09]

**INFERENCE.** App Server is an execution transport, not a Workflow v1 owner. This separation is desirable: Codex remains the reasoning/code agent while deterministic code can own lifecycle transitions that should not depend on model interpretation.

### 3.4 Retry and reconciliation

**DOCUMENTED FACT.** Symphony reconciles running/blocked items against fresh tracker state, treats stale or ineligible work as stoppable, detects stalled runs using recent Codex activity, and uses retry/backoff for failures. It also distinguishes input/approval blockers from ordinary failure. [O08]

**INFERENCE.** The pattern is useful, but Symphony's retry policy cannot be copied directly. ADW PR10 requires operation-aware recovery. A future coordinator must reconcile live Git, external side effects, candidate identity, and thread state before retrying a write-capable phase.

### 3.5 Repository-owned workflow configuration

**DOCUMENTED FACT.** Symphony places configuration and agent prompt policy in `WORKFLOW.md`; `WorkflowStore` reloads it and retains the last known good version on invalid updates. [O03] [O10]

**RECOMMENDATION.** Do not introduce a second ADW `WORKFLOW.md`. This repository already has authoritative owners: `PROJECT-CHARTER.md`, `WORKFLOW-V1.md`, the Research Register, and supporting design/policy artifacts. A future coordinator should resolve and reference those existing owners instead of copying their semantics into a new policy file.

## 4. Native thread orchestration versus App Server coordination

These options are not two different execution engines. Both ultimately use Codex threads. The distinction is who owns orchestration decisions.

### A. Model-driven native thread orchestration

```text
parent Codex agent
→ create executor thread
→ wait/read result
→ create reviewer thread
→ interpret verdict
→ route correction
```

**INFERENCE — strengths.** This is the smallest implementation and is suitable as a low-cost comparison baseline. It preserves the Codex UI and requires little custom code.

**INFERENCE — limitation.** The parent model still decides when a phase completed, which result field matters, whether a reviewer should start, and whether a correction should route. Those transitions are therefore partly model-reasoned rather than represented by an explicit external state machine.

### B. Thin coordinator over Codex App Server

```text
deterministic coordinator
→ thread/start executor
→ explicit turn lifecycle
→ candidate identity reconciliation
→ fresh thread/start reviewer
→ structured verdict
→ thread/resume executor for correction
→ fresh reviewer for corrected candidate
→ stop before acceptance
```

**DOCUMENTED FACT.** App Server supports starting, resuming, reading, listing/forking threads, explicit turn lifecycle notifications, per-turn model/sandbox/cwd overrides, and per-turn `outputSchema`. [O04]

**INFERENCE — advantage.** These primitives allow the controller to represent orchestration state directly rather than infer it from a producer's prose. This is a better fit for ADW's separation between reasoning and deterministic control.

**RECOMMENDATION.** Use native thread orchestration as the PoC comparison baseline. Treat a thin App Server coordinator as the leading architecture candidate when the requirement is a reliable executor/reviewer/correction pipeline.

## 5. Recommended Symphony-informed architecture

The target architecture should be smaller than Symphony and should preserve existing owners.

```text
                accountable human/coordinator
                          │
                 authorizes bounded task
                          │
                          ▼
                 ┌────────────────┐
                 │ Runtime        │
                 │ coordinator    │
                 └───────┬────────┘
                         │
               ┌─────────▼─────────┐
               │ Executor worktree │
               │ App Server E      │
               │ persistent thread │
               └─────────┬─────────┘
                         │
           project-owned verification/publication
                         │
                         ▼
                 exact candidate SHA
                         │
               ┌─────────▼─────────┐
               │ Reviewer workspace│
               │ App Server R1     │
               │ fresh thread      │
               │ read-only target  │
               └─────────┬─────────┘
                         │
                 structured verdict
                         │
              ┌──────────┴───────────┐
              │                      │
             PASS          REQUIRES_CORRECTION
              │                      │
              │             resume executor E
              │                      │
              │                new candidate
              │                      │
              │              fresh reviewer R2
              │                      │
              └──────────┬───────────┘
                         ▼
              READY FOR HUMAN ACCEPTANCE
```

### Responsibility boundaries

| Component | Owns | Must not own |
|---|---|---|
| Workflow v1 / project policy | normative phase, authority, review and acceptance semantics | runtime process state |
| Runtime coordinator | ephemeral/persisted orchestration execution state, role dispatch, lifecycle reconciliation | product intent, normative semantics, acceptance, merge authority |
| Workspace manager | isolated workspace/worktree identity and lifecycle | task truth or review verdict |
| App Server client | protocol transport, thread/turn calls and events | workflow decisions |
| Executor | bounded implementation/recovery reasoning within granted scope | independent review or acceptance |
| Reviewer | independent evaluation of an exact immutable candidate | candidate mutation or acceptance |
| Project-owned scripts/tools | deterministic project-specific verification/publication mechanics where already owned | workflow policy |
| Human/coordinator | consequential authorization, disposition, acceptance | hidden executor state |

## 6. Thread and reviewer model

### Executor continuity

**DOCUMENTED FACT.** App Server can persist and later `thread/resume` a recorded thread id. `thread/read` can inspect stored thread status/history without resuming it. [O04]

**RECOMMENDATION.** Persist the executor thread id as runtime evidence so a correction can resume the same execution context after a review finding. On restart, reconcile the recorded id with `thread/read`/`thread/resume` rather than assuming the old process is alive.

### Reviewer freshness

**DOCUMENTED FACT.** `thread/fork` copies source history into a new thread. [O04]

**INFERENCE.** Forking the executor is therefore inappropriate when ADW claims independent fresh-context review because it intentionally inherits producer history.

**RECOMMENDATION.** Start each formal reviewer as a new thread with only the review contract, exact base/candidate identities, authoritative requirements, producer-reported verification evidence, and the minimum necessary context. A materially corrected candidate gets a new fresh reviewer thread unless an adopted later rule permits demonstrated unaffected scope to carry forward.

### Structured review result

**DOCUMENTED FACT.** `turn/start` supports `outputSchema` for the current turn. [O04]

**RECOMMENDATION.** A PoC should require a machine-readable review envelope, for example:

```json
{
  "verdict": "PASS | PASS_WITH_HARDENING | REQUIRES_CORRECTION",
  "reviewedBaseSha": "<40-char sha>",
  "reviewedCandidateSha": "<40-char sha>",
  "findings": []
}
```

The schema is transport-level structure only. The meaning of verdicts and required independence remains owned by the applicable workflow/review policy.

## 7. State model

Do not collapse runtime health into engineering lifecycle state.

### Runtime state

```text
UNCLAIMED
RUNNING
BLOCKED
RETRY_PENDING
FAILED
STOPPED
```

### Engineering orchestration state

```text
AUTHORIZED
→ EXECUTOR_RUNNING
→ VERIFYING
→ CANDIDATE_READY
→ REVIEWER_RUNNING
→ READY_FOR_HUMAN_ACCEPTANCE

REVIEWER_RUNNING
→ CORRECTION_REQUIRED
→ CORRECTING
→ VERIFYING
→ NEW_CANDIDATE_READY
→ FRESH_REVIEWER_RUNNING
```

**INFERENCE.** Keeping these state classes distinct prevents a process status such as `completed` from being mistaken for candidate verification, independent review, or acceptance.

A future runtime journal may cache identifiers such as task id, executor thread id, workspace/worktree path, candidate SHA, reviewer thread id, and reviewed candidate SHA. Such a journal must be explicitly designed as execution/recovery evidence, not a competing owner of task, research, product, review, or acceptance truth.

## 8. Failure and recovery requirements

A PoC must test the failure cases that are load-bearing for later adoption.

1. **Quiet/poll timeout while worker remains active.** Timeout alone must not establish failure or authorize a replacement writer. Reconcile live thread/process state first.
2. **Executor exits without a candidate.** Distinguish blocker, failure, and normal incomplete continuation. Do not fabricate candidate state.
3. **Verification failure.** Remain in the executor/correction domain; do not dispatch reviewer as though a valid candidate exists.
4. **Partial publication.** Reconcile Git/local/remote exact identities before retry. No blind commit/push rerun.
5. **Moving candidate branch.** Reviewer is bound to immutable base/candidate SHAs, never a moving branch head.
6. **Reviewer failure.** A failed reviewer produces no verdict. Starting a replacement reviewer is safe only after confirming it has no write authority and the reviewed candidate is unchanged.
7. **Correction after review.** A corrected candidate receives a new immutable identity and fresh affected verification/review according to the applicable policy.
8. **Coordinator restart.** Reconcile journal/cache, App Server stored thread state, workspace/Git state, remote candidate identity, and any external effects before continuing.
9. **Duplicate writer attempt.** Fail closed when an executor/write claim already exists for the task/worktree.
10. **Ambiguous authority or changed normative input.** Stop before further mutation and return to the accountable owner.
11. **Acceptance or merge attempt by an agent.** Deny unless a separate later human-controlled gate explicitly grants the exact effect. This research grants none.

These requirements preserve DR-003 PR07, PR09, and PR10 and the DR-005 X3/X6/X7 boundaries rather than replacing them. [R01] [R02]

## 9. What not to copy from Symphony

**RECOMMENDATION.** Do not copy these parts into ADW v1 without a separate demonstrated need:

- an issue tracker as a new authoritative control plane;
- a new `WORKFLOW.md` that duplicates existing owners;
- the Elixir/Phoenix implementation stack merely because the reference uses it;
- SSH worker distribution;
- a web dashboard;
- provider-specific dynamic tracker tools;
- ten-agent/default high concurrency;
- automatic ticket transitions, PR landing, or merge;
- unmodified retry/backoff and workspace cleanup semantics;
- in-memory-only blocked state as sufficient durable recovery evidence;
- unattended operation as a default mode.

OpenAI explicitly presents Symphony as a minimal reference implementation and encourages environment-specific implementations rather than treating it as a maintained standalone product. [O01] [O03]

## 10. Minimal proof-of-concept scope

**RECOMMENDATION — later gate only.** The smallest useful PoC should validate architecture, not deliver autonomous development.

### Objective

Demonstrate that a deterministic controller can coordinate one bounded synthetic or disposable-repository task through executor, exact candidate identity, fresh reviewer, one correction, and re-review while preserving role independence and stopping before acceptance.

### Minimum capabilities

1. start one isolated executor thread/workspace;
2. receive explicit `turn/completed` status;
3. retain and later resume the executor thread id;
4. establish an immutable synthetic/disposable candidate identity;
5. start a fresh reviewer thread without executor history;
6. require structured review output;
7. route one correction to the executor;
8. establish a new candidate identity;
9. start a fresh reviewer for the corrected candidate;
10. stop at `READY_FOR_HUMAN_ACCEPTANCE`;
11. demonstrate restart/reconciliation from recorded runtime evidence;
12. demonstrate duplicate-writer rejection.

### Explicit non-goals

- no production project adoption;
- no ADW main-branch automation;
- no tracker migration;
- no parallel writers;
- no automatic PR ready/merge/acceptance;
- no AFK or unattended authorization;
- no new normative Workflow v1 semantics;
- no general scheduler, queue, database, dashboard, SSH worker pool, or multi-project service.

### Success bar

A PoC is evidence only if it demonstrates the exact role and identity transitions above, including at least one controlled failure/recovery path. A successful happy path alone does not justify adoption.

## 11. Decision matrix

| Question | Current evidence conclusion |
|---|---|
| Deploy Symphony unchanged? | **NO-GO.** X3 remains controlling. |
| Copy Symphony's architecture selectively? | **GO WITH CHANGES.** Single coordinator state, workspace isolation, App Server transport, reconciliation, and observability are useful patterns. |
| Make a repo-owned Skill the full coordinator? | **NO as the leading design.** A Skill may supply procedural guidance, but deterministic lifecycle state should not depend solely on model reasoning. |
| Use native Codex threads as a comparison baseline? | **YES.** Lowest-cost baseline for the PoC. |
| Prefer App Server for a reliable executor/reviewer pipeline? | **YES, as the current architecture hypothesis.** It provides direct lifecycle and structured-output primitives needed by a deterministic coordinator. |
| Adopt App Server coordinator now? | **NO.** Requires a bounded PoC, independent evidence review, ownership design, and separate coordinator disposition/adoption gate. |
| Automate human acceptance or merge? | **NO.** Out of scope and unauthorized. |
| Reopen DR-005 D13? | **YES, narrowly for PoC evaluation.** This is a recommendation, not a disposition change. |

## 12. Remaining evidence gaps

The following gaps block operational adoption:

1. No target-environment PoC has exercised current App Server behavior under ADW constraints.
2. No independent source review has yet validated this note.
3. No accepted owner exists for runtime orchestration state or a recovery journal.
4. Exclusive writer fencing beyond workspace separation is not yet designed or tested.
5. App Server process/thread retention across the intended local lifecycle has not been operationally validated in the target environment.
6. Cancellation/containment across child processes and external side effects remains unverified.
7. Project-specific candidate publication and verification integration has not been mapped for a generic cross-project controller.
8. No model/reasoning routing policy is adopted for executor versus reviewer roles.
9. No cost/usage comparison exists between native thread orchestration and App Server coordination.
10. No evidence supports routine, parallel, unattended, or AFK write authority.

None of these gaps blocks recording this research. Gaps 1, 3, 4, 5, 6, and 7 block operational adoption.

## 13. Proposed next gate

**RECOMMENDATION.** Independent source review should first verify this exact research candidate against current primary sources and the pinned ADW basis. If source review passes, the coordinator may separately decide whether to change the current D13 disposition from `DEFER` to a narrowly scoped `CONDITIONALLY SELECT FOR ONE BOUNDED POC` while preserving X3 and every existing automation/acceptance restriction.

No implementation or policy change should occur merely because this research candidate or its pull request exists.

## 14. Sources

### Current ADW authority and prior evidence

- **R01 — DR-005 evidence.** `docs/research/ADW-DR-005.md`, frozen target commit `38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958`; evidence date 2026-09-04. The Symphony/custom-harness assessment is D13 and X3 within that report.
- **R02 — DR-005 accepted tooling disposition.** `docs/research/ADW-DR-005-DISPOSITION-001.md`; confirms D13 `DEFER` and X3 rejection of unmodified Symphony as ADW conformance.
- **R03 — Project Charter.** `PROJECT-CHARTER.md` at research basis main `4e6af3db42950e9b7e5415b89f09b5d325fd78a6`.
- **R04 — Workflow v1.** `WORKFLOW-V1.md` at research basis main `4e6af3db42950e9b7e5415b89f09b5d325fd78a6`.

### Current OpenAI and Symphony evidence

- **O01 — OpenAI, "An open-source spec for Codex orchestration: Symphony."** Published 2026-04-27; reread 2026-09-14. <https://openai.com/index/open-source-codex-orchestration-symphony/>
- **O02 — OpenAI Symphony specification.** Canonical repository, pinned commit `e0ccc83720a42a600a53b61c5f8d3e518bebe1db`; reread 2026-09-14. <https://github.com/openai/symphony/blob/e0ccc83720a42a600a53b61c5f8d3e518bebe1db/SPEC.md>
- **O03 — OpenAI Symphony Elixir README.** Pinned commit `e0ccc83720a42a600a53b61c5f8d3e518bebe1db`; prototype/evaluation warning, architecture and supported adapters. <https://github.com/openai/symphony/blob/e0ccc83720a42a600a53b61c5f8d3e518bebe1db/elixir/README.md>
- **O04 — OpenAI Codex App Server documentation.** Rolling official documentation reread 2026-09-14. Documents initialization, thread start/resume/fork/read, turn lifecycle, final statuses, sandbox/cwd/model overrides, and `outputSchema`. <https://learn.chatgpt.com/docs/app-server>
- **O05 — Symphony runtime supervisor.** <https://github.com/openai/symphony/blob/e0ccc83720a42a600a53b61c5f8d3e518bebe1db/elixir/lib/symphony_elixir/agent_runtime_supervisor.ex>
- **O06 — Symphony workspace manager.** <https://github.com/openai/symphony/blob/e0ccc83720a42a600a53b61c5f8d3e518bebe1db/elixir/lib/symphony_elixir/workspace.ex>
- **O07 — Symphony AgentRunner.** <https://github.com/openai/symphony/blob/e0ccc83720a42a600a53b61c5f8d3e518bebe1db/elixir/lib/symphony_elixir/agent_runner.ex>
- **O08 — Symphony Orchestrator.** <https://github.com/openai/symphony/blob/e0ccc83720a42a600a53b61c5f8d3e518bebe1db/elixir/lib/symphony_elixir/orchestrator.ex>
- **O09 — Symphony App Server client.** <https://github.com/openai/symphony/blob/e0ccc83720a42a600a53b61c5f8d3e518bebe1db/elixir/lib/symphony_elixir/codex/app_server.ex>
- **O10 — Symphony WorkflowStore.** <https://github.com/openai/symphony/blob/e0ccc83720a42a600a53b61c5f8d3e518bebe1db/elixir/lib/symphony_elixir/workflow_store.ex>

## 15. Publication boundary

This file is evidence only. Its recommendation status at publication is `proposed`. It does not modify `WORKFLOW-V1.md`, `PROJECT-CHARTER.md`, `ADW-DR-005-DISPOSITION-001`, the current Research Register, tool configuration, branch protection, installed Codex behavior, or any project-specific workflow.

The Research Register remains the sole mutable owner of current research/decision state. This candidate intentionally does not self-update that state before independent source review and coordinator disposition. A merge of this evidence candidate must not be interpreted as source review, D13 disposition change, implementation authorization, automation authority, or baseline acceptance.

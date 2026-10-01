---
id: ADW-D13-CONVEYOR-PREREQUISITE-DESIGN-001
artifact: design-proposal
artifact_status: draft
owner: chatgpt-coordinator
repository: ahtoxaandy999/agentic-development-workflow
subject_base: 796fef15a7ba3b78b57c1f06f5911c6a3f85dad5
dr006_disposition_ref: docs/research/ADW-DR-006-DISPOSITION-001.md
decision_effect: none
designed_on: 2026-09-20
supersedes: null
---

# D13 autonomous engineering conveyor prerequisite design

## Status and boundary

This is the single bounded D13 prerequisite-scoping/design proposal authorized by
`ADW-DR-006-DISPOSITION-001`.

It designs and proposes only. It does not implement orchestration, select a D13
mechanism, reopen D5, amend Workflow v1, authorize automatic dispatch, enable
unattended execution, or satisfy the D13 conformance prerequisite.

D13 remains `CONFIRM DEFER`. D5 remains `CONFIRM DEFER`. X3 remains
`CONFIRM REJECT`.

The proposal consolidates the latest multi-repository research, exact-candidate
CI pilots, executor/reviewer experiments, GitHub control-plane analysis, Claude
engineering-skill evaluation, and the local learned-orchestrator idea into one
decision-ready architecture.

## 1. Exact live evidence snapshot

The following default-branch identities were re-read from live GitHub before
candidate production:

| Repository | Live `main` |
| --- | --- |
| `ahtoxaandy999/agentic-development-workflow` | `796fef15a7ba3b78b57c1f06f5911c6a3f85dad5` |
| `ahtoxaandy999/pet-project` | `28f84fe4324925adae0f17163d578ed2e1f9bc19` |
| `ahtoxaandy999/shalena-fishing-automation` | `9bb2357e6f596331abf30007e47bd373b0b02baa` |
| `ahtoxaandy999/shalena-game-research` | `96dd493e9b27fd99d40e70ba01fe33155c4bd484` |
| `ahtoxaandy999/housing-recovery` | `01b3ae5288069660a12c6b35254e4fa59867429e` |

These SHAs are publication-time evidence for this proposal, not standing current
state.

## 2. Observed implementation baseline

### Pet Project

Pet now has a merged exact-candidate GitHub Actions verifier. PR #100 transferred
the repository-owned verification planner to a clean published-candidate mode
without moving semantic test ownership into YAML.

The important distinction remains:

- local/task verification owns repository semantics;
- GitHub Actions independently executes that owner against an exact candidate;
- CI PASS is machine evidence, not semantic review or Product acceptance.

Pet also has accepted supervised correction and fresh-review semantics, but no
accepted unattended task-to-task advancement profile.

### Housing Recovery

Housing has a simpler exact-PR-head CI path and deterministic post-merge closeout.
It is the preferred low-risk pilot repository for event/review/correction wiring.

Housing demonstrates that exact-SHA verification and merge-closeout can stay
small when the repository test surface is small. That simplicity should not be
mistaken for a universal verifier design.

### Shalena Fishing Automation

Fishing remains local-first for important browser/device/package behavior. It has
strong repository-owned tests and packaging logic but no current standard Actions
pipeline for the full development flow.

A later migration should move deterministic build/test/package work to GitHub
while preserving explicit local/device lanes for real game/browser evidence.

### Shalena Game Research

The research repository has a different evidence model: capture integrity,
provenance, immutable hashes, offline verification and accountable adoption are
separate.

Research findings must not auto-activate product implementation. Missing retained
source bytes remain an evidence gap, not a semantic conclusion.

### ADW

ADW remains the cross-project control-plane owner only for explicitly adopted
shared semantics. Project repositories retain product rules, local verification
and live execution state.

No common runtime should be introduced here before local pilots prove a genuinely
shared contract.

## 3. Target role split

### GPT

GPT is the semantic coordinator and independent reviewer surface:

- milestone analysis and bounded decomposition;
- authority and evidence reconciliation;
- intermediate independent review of exact candidates;
- final cumulative milestone review;
- genuine stop-condition escalation.

GPT should not be the ordinary implementation executor and should not own
deterministic routing that GitHub can evaluate mechanically.

### Claude

Claude is the default producer/executor candidate:

- bounded implementation;
- focused semantic tests;
- producer-side internal code review;
- debugging and fixes until producer-green;
- invocation of repository-owned verification/publication procedures.

Useful Claude engineering skills are procedural aids only:

- `engineering:code-review` for producer-side review;
- `engineering:testing-strategy` when observable behavior changes;
- `engineering:debug` for bounded CI/review corrections.

`architecture`, `system-design` and `tech-debt` must not silently expand an
authorized implementation task.

Claude internal review is never independent review of Claude-produced work.

### GitHub

GitHub is the preferred event and durable identity plane:

- branch and exact commit identity;
- PR state;
- Actions execution and artifacts;
- structured transition signals;
- review/result publication;
- manual merge observation;
- mechanical post-merge closeout.

GitHub does not own Product semantics or acceptance.

### Human

The desired mature milestone profile has three human roles:

1. authorize one bounded milestone envelope;
2. resolve genuine Product/architecture/security/permission stops;
3. accept the final exact candidate and merge manually.

No intermediate human gate is desired for predetermined technical tasks that
remain inside the authorized envelope.

## 4. Target milestone flow

```text
human milestone authorization
-> Claude task implementation
-> Claude focused tests + internal review + fixes
-> exact candidate publication
-> GitHub exact-SHA CI/evidence
-> fresh GPT independent task review
-> bounded correction back to same Claude logical task when permitted
-> new candidate -> CI -> fresh affected review
-> automatic activation of next already-authorized task
-> fresh cumulative GPT final review
-> READY FOR HUMAN
-> human acceptance + manual merge
-> deterministic GitHub closeout
```

“No intermediate review” means no intermediate human Product-acceptance gate. It
does not remove producer review, CI, independent technical review or correction.

## 5. Control-plane design

The preferred coordinator is ephemeral and event-driven, but the design does not
make an event runner, chat, GitHub workflow or model session the owner of ADW
semantics.

Each run should receive a signal, reread live authoritative state, establish the
exact subject and authorization, perform one permitted transition, publish the
required evidence/receipt, and terminate.

A permanently alive chat, private agent memory or second task database is not a
required correctness component.

### 5.1 Authoritative runtime orchestration state

For each active milestone/task there is exactly one designated execution-state
recorder. That role owns only the mutable orchestration lifecycle state needed to
answer which authorized transition, if any, may occur next. It does not own
Product policy, repository/Git identity, CI truth, review truth, disposition,
normativity, baseline acceptance, join state or side-effect truth.

The recorder's state is a projection over the orthogonal authoritative planes,
not a replacement for them. A transition is valid only when every relied-upon
plane owner independently supports it.

The recorder must preserve durable transition history before another actor,
session, retry, recovery step or decision relies on it. A later implementation
may choose a repository-local or GitHub-native representation only through its
own mechanism-selection gate. This design selects no storage product.

Any runtime cache is derived and disposable. It may accelerate lookup but may
never authorize a transition or override durable evidence. It must be rebuildable
from the authoritative plane owners plus durable transition history.

If a recovery journal is implemented, it is an append-only historical evidence
record, not a competing current-state owner. It records operation identities,
attempts, observations, containment/recovery decisions and links to immutable
evidence. The designated execution-state recorder remains the sole recorder of
current orchestration state. Loss of a cache is recoverable. Loss or ambiguity
of required durable recovery history blocks reliance until evidence is restored
or an accountable owner resolves the gap.

This preserves X2: no Register/Issue/file/harness database combination may become
multiple independently mutable owners of the same current state.

### 5.2 Minimal adapter boundary

The mechanism-neutral adapter has three responsibility layers.

Policy and authority layer:

- Workflow v1 and project-specific authorities define permitted objectives,
  semantic planes, task/milestone scope, stop conditions and accountable owners.
- This layer never executes transport operations and never infers runtime success
  from product-native statuses.

Lifecycle orchestration layer:

- the designated execution-state recorder evaluates whether a transition is
  allowed from fresh evidence;
- it binds the transition to the exact task/milestone subject, policy revision,
  current generation and required plane-owner evidence;
- it records the resulting orchestration transition or a blocked/intervention
  state;
- it cannot mutate Git, publish reviews, merge, create privileged effects or
  decide Product/architecture semantics on its own.

Execution and transport layer:

- bounded executors perform implementation/review work;
- repository/GitHub adapters read current shared state;
- privileged effect owners perform authorized mutations only after validating
  the lifecycle request and their own preconditions;
- every material operation returns independently addressable effect evidence.

Adapter inputs must include exact authorization/policy identity, task/milestone
identity, current orchestration generation, exact relied-upon repository/evidence
identities and the requested operation. Outputs are a typed observation, a
denied/blocked result, or an effect receipt tied to the same operation identity.

The adapter must not invent authority, collapse planes, silently retry a failed
operation or promote an observed product status into an ADW decision.

### 5.3 Exclusive-writer, duplicate and stale-event semantics

Shared mutation uses one logical writer at a time.

Before a mutation-capable task begins, the execution-state recorder establishes a
writer generation for that logical task. Every write request is bound to:

- milestone/task identity;
- writer generation;
- exact expected remote head/base as applicable;
- operation kind;
- a stable operation identifier.

A privileged publisher/effect owner must refuse the operation when the supplied
generation is not current, the expected remote identity no longer matches, the
operation is outside scope, or another active writer owns the same mutation
domain.

The concrete fencing primitive is deliberately not selected here. A later
mechanism must prove that stale writers cannot successfully publish merely
because they still possess a workspace or credential. Worktree separation,
CODEOWNERS or prompt instructions alone are not writer fencing, preserving X4.

Duplicate delivery of the same operation identifier and exact subject is
idempotent: the adapter returns the existing completed receipt or reports the
already-active operation without repeating the side effect. A changed candidate
SHA, changed authority/policy revision or changed requested effect is a new
operation, not a retry of the old one.

A stale event is only a wake-up signal. Before acting, the lifecycle layer
rereads current plane owners. If the event subject no longer matches current
authority, head or generation, it records no advancing transition.

Retry is operation-aware. A retry is permitted only after prior-effect evidence
classifies the previous attempt sufficiently to make another attempt safe.
Unknown or partial effects force reconciliation/intervention rather than blind
retry.

### 5.4 External side-effect ownership and containment

Every privileged external effect has exactly one accountable side-effect owner
for the operation domain, for example repository publication, review publication,
external notification or another separately authorized service.

The lifecycle layer may request an effect but does not execute it. The side-effect
owner:

1. validates authorization, exact subject, writer generation and operation ID;
2. performs or rejects the bounded effect;
3. observes authoritative post-effect state;
4. returns a durable receipt including attempted/completed/partial/unknown state;
5. owns containment reporting and residual-effect inventory for that operation
   until reconciliation transfers or closes the obligation.

Model execution must not share the privileged credential when a deterministic
publisher/effect owner can enforce the operation contract separately.

Cancellation request, process exit or transport failure is never containment.
Containment is established only when every relevant side-effect domain proves
that further effects have ceased or are boundedly isolated and any residual
effect is durably owned. This preserves X7 and the existing Workflow v1
cancellation/recovery separation.

### 5.5 Reconciliation across runtime, workspace, remote and effects

Reconciliation is required after interruption, stale identity, ambiguous effect,
writer conflict, restart with incomplete state, or any mismatch between:

1. current policy/task authority and current orchestration generation;
2. durable orchestration transition/recovery history;
3. workspace/local Git state, treated as tentative work product;
4. live remote Git/PR/check state, authoritative for shared repository identity;
5. authoritative receipts/observations from every affected side-effect owner.

Precedence is by ownership, not timestamp:

- normative/project owners decide authority and semantic permission;
- Git/GitHub decides current shared repository identity;
- the designated execution-state recorder decides only current orchestration
  lifecycle state, constrained by the other owners;
- a workspace never overrides remote shared identity;
- each side-effect owner decides what actually happened in its domain;
- prose summaries and caches decide nothing.

The reconciliation procedure is:

1. stop initiating new effects and fence stale writers;
2. inventory in-flight and potentially completed operations by stable operation ID;
3. reread every relevant authoritative plane and remote identity;
4. compare expected and observed state without rewriting either;
5. classify each operation as no-effect, completed, partial/residual or unknown;
6. if any domain is partial/unknown or authority is stale, record blocked or
   intervention-required as applicable and deny retry/resumption/terminal closure;
7. obtain the applicable owner's bounded recovery/reconciliation decision;
8. execute only the authorized recovery action with a new attempt identity;
9. validate the resulting authoritative state against the authorized target;
10. retain the completed recovery episode and residual-risk disposition before
    any separate resumption or terminal transition.

No latest-wins rule is allowed. A remote write observed after an invalid or stale
request does not retroactively authorize the operation. Missing critical evidence
blocks reliance rather than being interpreted as success or semantic failure.

## 6. Review architecture

Two review layers are required.

### Producer layer

Claude reviews and fixes its own task before publication. This is quality control,
not independence.

### Independent layer

A fresh GPT context independently retrieves:

- exact base/head;
- relevant repository authority;
- changed code/docs;
- exact machine evidence.

It returns a structured verdict bound to the exact candidate.

A changed candidate invalidates the earlier verdict for advancement purposes and
requires fresh affected review.

The final milestone review is another fresh context over milestone base to final
head. It verifies cross-task integration rather than merely aggregating earlier
PASS results.

## 7. Correction loop

A `REQUIRES_CORRECTION` finding may route automatically to the same logical
Claude task only when the correction:

- is required by the already-authorized outcome;
- stays within permitted paths/effects;
- preserves Product/architecture/public-API decisions;
- adds no new dependency or privilege;
- needs no new external effect.

A correction that crosses one of those boundaries stops for human authority.

The first profile should cap semantic correction attempts per task. The current
research recommendation is two attempts, but that number is not an adopted ADW
default.

## 8. Current invocation constraints

### GPT reviewer

The desired formal GPT review path is exact-SHA, fresh-context and
machine-readable.

The official Codex GitHub Action can satisfy the GitHub-native execution shape,
but the tested Housing pilot stopped correctly because the repository had no
`OPENAI_API_KEY` and the user did not authorize separate API billing.

The tested Codex automation interface exposed schedule/heartbeat behavior but did
not provide the required native read-only GitHub PR event trigger. That empirical
result means the current design must not depend on a Work/Codex event trigger
until the exact user/account surface proves it.

Automatic Reviews are useful as an optional human-facing review product, but they
do not replace the formal structured-result contract by assumption.

### Claude producer

Claude Code Action is a strong hosted-producer candidate because it can run inside
GitHub Actions and use Claude Code. Subscription OAuth is a possible personal
pilot path where supported by the official integration, but personal subscription
credentials are not treated as a durable organization service identity.

### GitHub Agentic Workflows

`gh-aw` is the strongest ready-made challenger to a custom orchestration layer.

Its relevant properties are:

- GitHub-native event/scheduled execution;
- read-only agent jobs by default;
- sandbox/security controls;
- explicit safe outputs executed by separate permissioned jobs;
- support for multiple agent engines.

The first implementation pilots should compare a thin repository-local adapter
against `gh-aw`. A custom controller is justified only if the ready-made
mechanism cannot satisfy the accepted identity, evidence, retry and authority
boundaries.

## 9. Minimal machine contracts

Do not adopt the large research draft schema as one block.

The first pilots need only four narrow contracts:

1. **candidate identity**: repository, PR/task, base, exact head;
2. **CI evidence**: exact head, verifier revision/run, result, artifact digest;
3. **review result**: exact subject, reviewer execution identity, findings,
   verdict, unresolved evidence;
4. **correction dispatch**: originating review/finding IDs, permitted correction
   scope, expected current head, attempt number.

Additional milestone/final-review/closeout contracts should be materialized only
when the corresponding pilot needs them.

This avoids building a workflow engine before the control loop is proven.

## 10. Repository profile optimization

One workflow shape should not be forced across all repositories.

- **Pet**: deterministic application profile, rich affected/full verification,
  gameplay/runtime-specific evidence.
- **Housing**: lightweight application profile, ideal for control-loop pilots.
- **Fishing**: automation/package profile with deterministic hosted work plus
  explicit local/device lanes.
- **Game research**: evidence/research profile with adoption separated from
  implementation.
- **ADW**: governance/design profile, not a product executor or global task DB.

Shared components should be extracted only after at least two repositories prove
the same semantics with materially duplicated implementation.

## 11. Local learned orchestrator optimization lane

A local learned orchestrator is promising but is not a prerequisite for the
GitHub/Claude/GPT conveyor.

The correct first asset is a high-quality trajectory dataset, not immediate
fine-tuning.

After the conveyor is stable, record observable transitions such as:

```text
state/evidence
-> available actions
-> selected action
-> actor
-> outcome
-> human override
-> final accepted result
```

Do not collect or depend on hidden chain-of-thought. Store only observable
artifacts, decisions, tool calls and outcomes allowed by the applicable data
policy.

### Learning stages

**Stage L0 - shadow policy model**

Benchmark local models against accepted historical routing decisions without
letting them control execution.

**Stage L1 - supervised adaptation**

Train a small local policy model on state-to-next-action examples. On Apple
Silicon, MLX-LM supports LoRA/QLoRA-style fine-tuning and is a practical research
surface.

**Stage L2 - preference learning**

Use chosen/rejected routing decisions when real human or reviewer corrections
produce clean preference pairs.

**Stage L3 - agentic reinforcement learning**

Only after the harness has stable deterministic rewards, evaluate systems such as
Agent Lightning for trajectory-based policy training. This is later research,
not the initial local-Mac implementation path.

### Candidate model roles

A small dense Qwen-class model is a reasonable trainable-policy research
candidate.

`gpt-oss-20b` is a strong local inference/teacher benchmark because it is
open-weight, supports agentic/tool/structured-output use cases and is designed to
fit in roughly 16 GB of memory. Its suitability for this exact routing task must
be measured, not assumed.

The learned local orchestrator should initially route only high-confidence,
well-represented states. Low-confidence, novel or authority-sensitive states
escalate to GPT/human.

This creates a data flywheel:

```text
frontier model/human resolves hard state
-> accepted observable decision becomes training evidence
-> local policy handles recurring equivalent states
-> frontier calls concentrate on novel/ambiguous work
```

## 12. Phased implementation recommendation

### P0 - preserve current accepted flows

Do not retire browser/manual/supervised fallback paths yet.

### P1 - structured shadow independent reviewer

Housing remains the preferred first pilot. The goal is exact-SHA structured GPT
review with no write authority.

Credential/event limitations discovered during the attempted pilot are evidence,
not reasons to invent a weaker trigger contract.

### P2 - one-task bounded correction

Claude produces/fixes one approved task. CI and fresh GPT review gate each
candidate. No intermediate human correction approval inside the bounded scope.

### P3 - two-task Pet milestone

One draft PR, one writer, exact task checkpoints, independent review per task,
automatic task-to-task advance, fresh cumulative final review, manual merge.

### P4 - Fishing deterministic CI/package lane

Move deterministic test/package production to hosted CI, preserving real-browser
and device-bound evidence as explicit local lanes.

### P5 - research/evidence profile

Automate integrity verification only. Product adoption remains a distinct human
decision.

### P6 - shared extraction

Move only proven common identity/schema helpers into ADW or a reusable workflow
after two repository pilots justify reuse.

### P7 - local learned orchestrator

Begin trajectory collection before training; benchmark shadow routing; adopt any
local policy only through a later evidence/review decision.

## 13. D13 conformance evidence required before reconsideration

This design proposal defines the evidence boundary but does not satisfy it.
Actual accepted conformance evidence remains a later prerequisite and disposition
gate before D13 may be reconsidered.

### 13.1 DI-1 and DI-2 preservation

This proposal preserves the controlling design invariants without creating new
semantics.

DI-1: orthogonal semantic planes remain orthogonal.

Task control, cancellation, recovery, work product/product state, verification,
review, disposition, normativity, baseline acceptance and join/integration state
must not collapse into one native product status. A GitHub green, merged or
closed status, completed run, model done response or orchestration transition can
advance only the plane owned by the applicable authority. Legitimate
non-applicability is distinct from PASS.

DI-2: stale authority and recovery shortcuts cannot authorize reliance.

Materially stale authority or evidence blocks reliance. Retry remains
operation-aware; containment and recovery remain distinct; completed prior
episodes and relied-upon evidence remain durable; reopening creates a distinct
episode; accountable intervention and separate resumption/reset remain reachable;
terminal guards cannot be bypassed by a controller, native status or model
confidence.

The conformance package must demonstrate both invariants under normal and adverse
execution, not merely assert them in configuration.

### 13.2 Evidence subject and binding

A future conformance evaluation must bind its entire evidence package to one
exact runtime subject containing at minimum:

- accepted design/policy revision under evaluation;
- exact orchestration implementation revision;
- exact adapter/controller revision;
- exact runtime/engine versions and relevant configuration;
- exact permission/credential capability profile, without exposing secrets;
- exact repository/profile fixtures used by the scenarios;
- exact scenario-suite revision;
- start/end timestamps and run/attempt identities.

Changing any load-bearing implementation, policy, permission or scenario input
creates a new conformance subject unless an accepted impact analysis explicitly
permits carry-forward.

Every evidence artifact must have an immutable locator or retained byte content
plus cryptographic digest and provenance sufficient for independent retrieval.
A green aggregate without underlying subject-bound evidence is insufficient.

### 13.3 Required evidence forms

The future package must contain, at minimum:

1. subject manifest: exact revisions/configuration/permissions and scenario
   inventory;
2. transition evidence: input state, requested operation, generation/operation
   ID, resulting orchestration state and authoritative plane reads for every
   relied-upon transition;
3. repository identity evidence: workspace/local Git observations plus live
   remote Git/PR/check readback where applicable;
4. side-effect receipts: attempted/completed/partial/unknown result and
   authoritative post-effect observation for every privileged operation;
5. writer-fencing evidence: competing/stale writer attempts and deterministic
   rejection/readback showing they did not gain write authority;
6. recovery history: interruption, containment, residual-effect inventory,
   recovery authorization/attempt/validation and preserved prior episode history;
7. review-isolation evidence: reviewer subject, input authority/evidence,
   permission profile and proof that reviewer execution lacks candidate-code
   mutation/merge authority;
8. negative-control results: stale, duplicate, missing-evidence, out-of-order
   and unauthorized-operation scenarios with expected denial;
9. independent conformance review of the exact complete package, separate from
   producer self-check;
10. disposition record from a later accountable owner stating whether the exact
    package establishes the D13 conformance prerequisite.

Logs alone are insufficient when they cannot prove exact subject or retained
effects. Digests alone are insufficient when the relied-upon bytes are not
independently retrievable under the evidence-retention policy.

### 13.4 Mandatory positive and negative scenario matrix

The exact implementation-specific scenarios may be expanded later, but these
semantic cases are mandatory.

| Scenario | Required evidence | Primary invariant |
| --- | --- | --- |
| authorized single-writer happy path | exact transition chain, writer generation, candidate/CI/review identity and expected effect receipts | DI-1, DI-2 |
| stale event after head/authority change | live reread plus denied transition, with no advancing effect | DI-2 |
| duplicate event / duplicate operation | same operation ID returns prior receipt or active status without duplicate side effect | DI-2 |
| competing or stale writer | old/non-current generation attempts a shared write and is rejected before authoritative publication | DI-2, X4 |
| process interruption before known effect | restart reconstructs state from durable owners/history and does not infer success | DI-2 |
| interruption after partial/queued external effect | effect owner reports residual/unknown state; containment/reconciliation blocks blind retry | DI-2, X7 |
| missing required evidence | transition/review/retry is blocked as evidence gap, not converted to PASS | DI-2 |
| contradictory plane statuses | native green/merged/done cannot collapse task/review/disposition/acceptance planes | DI-1 |
| reviewer isolation | reviewer can read exact subject/evidence but cannot mutate candidate, merge or self-accept | DI-1 |
| recovery episode reopening | completed prior recovery remains immutable; a later obligation opens a distinct episode | DI-2 |
| intervention-required state | unresolved ambiguity reaches a durable blocked/intervention owner rather than unsafe continuation | DI-2 |
| terminal-guard attempt | incomplete containment/recovery/evidence prevents completion, cancellation closure, resumption or release | DI-2 |

A future implementation must also test any additional mechanism-specific failure
modes introduced by its selected transport/runtime. Passing only this table does
not excuse untested load-bearing mechanism behavior.

### 13.5 Acceptance bar

The D13 conformance prerequisite is established only when a later coordinator
disposition accepts one exact conformance package after fresh independent review.

A package is eligible for such disposition only when:

- every mandatory scenario applicable to the selected mechanism was executed
  against the exact runtime subject;
- all required positive scenarios reached their authorized target states;
- all required negative scenarios demonstrated required denial/containment;
- DI-1 and DI-2 are explicitly evidenced, not inferred from a generic green run;
- exclusive-writer and stale/duplicate controls are demonstrated by effect-level
  evidence;
- interruption/restart and partial-effect recovery preserve durable history and
  terminal guards;
- reviewer isolation and privileged-effect separation are demonstrated;
- all load-bearing evidence is independently retrievable and identity-bound;
- there is no unresolved BLOCKER/MAJOR conformance finding;
- there is no unresolved critical evidence gap, contradictory result or unowned
  residual effect.

If a required scenario is not applicable, the package must identify the
controlling reason and the independent reviewer must confirm legitimate
non-applicability. Non-applicable is not PASS.

Missing, stale, contradictory or partial load-bearing evidence yields
CONFORMANCE NOT ESTABLISHED for the prerequisite. It is an evidence result, not
a Product-semantic failure and not permission to retry or broaden authority.

### 13.6 Later-gate boundary

Defining this evidence contract, test matrix and acceptance bar does not itself
satisfy D13.

Actual execution of conformance trials, installation/selection of a mechanism,
collection of runtime evidence, acceptance of the package and any later D13
reconsideration each require their own applicable authority.

D5 remains independent. Even accepted D13 conformance evidence does not select or
authorize a Codex SDK/App Server mechanism unless D5 is separately reconsidered
or explicitly superseded within its own named scope.

## 14. Explicit non-authorities

This proposal does not authorize:

- `gh-aw` adoption;
- Claude Code Action installation;
- Codex GitHub Action installation;
- API billing or secret creation;
- automatic corrections;
- automatic task activation;
- unattended/AFK execution;
- automatic PR comments or reviews;
- branch-protection changes;
- automatic merge;
- local LLM training;
- collection of private model chain-of-thought;
- a new common task database;
- D5 or D13 mechanism selection;
- Workflow v1 amendment.

## 15. Recommended next gate

The next D13-specific gate after publication of this candidate should be:

**fresh independent review of this exact design candidate**

That review should determine whether the proposal:

- faithfully stays inside the accepted D13 prerequisite design scope;
- preserves D5/D13/X3 boundaries;
- fully defines the prerequisite ownership/conformance evidence question;
- avoids silently selecting a mechanism;
- keeps local-learning work a later optimization rather than a prerequisite.

A permitting review would support a separate coordinator disposition. Only that
later disposition may decide whether this proposal becomes an accepted
prerequisite design basis.

## External capability references

These are evidence/navigation links, not normative owners:

- GitHub Agentic Workflows overview:
  https://github.github.io/gh-aw/
- GitHub Agentic Workflows safe outputs:
  https://github.github.io/gh-aw/reference/safe-outputs/
- GitHub Agentic Workflows engines:
  https://github.github.io/gh-aw/reference/engines/
- OpenAI Codex GitHub Action:
  https://learn.chatgpt.com/docs/github-action
- MLX-LM LoRA/QLoRA:
  https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md
- Microsoft Agent Lightning:
  https://github.com/microsoft/agent-lightning
- OpenAI gpt-oss:
  https://openai.com/index/introducing-gpt-oss/

## Candidate acceptance boundary

A commit, push or PR containing this document is not acceptance.

The exact candidate requires independent review. Any material correction creates
a new candidate identity and requires fresh affected review. Coordinator
acceptance and later merge remain separate gates.

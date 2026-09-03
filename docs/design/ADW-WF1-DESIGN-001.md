---
id: ADW-WF1-DESIGN-001
artifact: workflow-v1-design
artifact_status: draft
maturity: bootstrap
owner: chatgpt-coordinator
task_contract_status: authorized
design_stage: contract-durable
task_id: ADW-WF1-DESIGN-GATE-001
design_base_sha: 29581dc9b7d1f2c368e2eca9098500ddabbd3a49
input_disposition_refs:
  - ADW-DR-001-DISPOSITION-001
  - ADW-DR-002-003-DISPOSITION-001
normative_effect: none
supersedes: null
---

# Workflow v1 Initial Design Contract

## Status and authority boundary

This artifact currently contains the authorized design contract only.

No substantive Workflow v1 design has yet been produced.

`normative_effect: none` means:

- this artifact is not Workflow v1 policy;
- no design content is adopted by existing in this file;
- no executor receives new implementation or autonomy authority;
- later design completion, candidate identity, independent review, coordinator
  disposition, normative adoption, and baseline acceptance remain separate
  states.

The authoritative design inputs are the accepted DR-001, DR-002, and DR-003
dispositions in the repository at `design_base_sha`.

Research reports remain evidence. Their publication-time recommendations do
not themselves control the design.

## Design objective

Produce one coherent, tool-agnostic initial Workflow v1 design proposal that
translates the accepted DR-001, DR-002, and DR-003 dispositions into
unambiguous lifecycle, authority, task, candidate, review, evidence,
parallelism, handoff, stopping, recovery, and proportionality semantics.

The design is sufficient when two competent implementers, given the same
authoritative inputs, would understand the same required workflow behavior
without inventing material intent.

Immediate decision consumers:

- an independent design reviewer;
- the ChatGPT coordinator and accountable human for later design disposition.

DR-005 is only a later consumer of accepted capability and enforcement
requirements.

## Accepted input boundary

### DR-001

Preserve accepted separation among:

- evidence;
- recommendation disposition;
- authorization;
- candidate identity;
- verification;
- review;
- acceptance;
- mutable authoritative state.

Preserve:

- one owner per mutable authoritative state;
- exact immutable candidate identity;
- live-state rereads at state-dependent gates;
- reliance-based durability;
- fresh bounded execution/review context;
- qualitative proportionality.

Do not derive universal gates, schemas, thresholds, or tools from DR-001.

### DR-002

Preserve:

- contextual clarification readiness;
- specification sufficiency based on executability and verifiability;
- coherent and verifiable decomposition;
- explicit dependencies, interfaces, integration, and recomposition;
- vertical slicing as a conditional preference only;
- legitimate enabling, infrastructure, risk-reduction, and learning work;
- distinct feedback purposes;
- reliance-based durability;
- fresh-context continuity;
- qualitative proportionality.

Do not require complete up-front specification or a universal process size.

### DR-003

Preserve:

- bounded delegation;
- relied-upon identity and effective-configuration freshness;
- constrained parallelism and joins;
- isolated side-effect domains;
- fresh-context rehydration;
- reconstructable execution evidence;
- new identity after material candidate correction;
- affected re-verification and applicable re-review;
- necessary evidence before unattended operation may be considered;
- cancellation request, acknowledgement, and verified containment as distinct;
- operation-aware retry and recovery;
- least privilege;
- separation of authentication, authorization, approval, identity, provenance,
  review, and correctness;
- mechanism deferral.

## Required design semantics

The substantive Workflow v1 proposal must resolve all of the following.

### 1. Lifecycle

Define:

- meaningful workflow states;
- allowed state transitions;
- transition owners;
- state-dependent gates;
- conditions for legitimately omitted conditional gates;
- conditions that make a claimed gate false or invalid.

A gate that is not applicable must not be represented as passed.

### 2. Authority and ownership

Define responsibilities and boundaries for:

- ChatGPT coordinator;
- researcher where applicable;
- executor;
- reviewer;
- independent reviewer where required;
- accountable human or risk owner where required.

Require one owner for each mutable authoritative state class.

Preserve prohibitions on:

- self-authorization beyond assigned authority;
- self-review where independence is claimed;
- self-acceptance.

### 3. Clarification and readiness

Define sufficient readiness before bounded commitment using contextual
information such as:

- intended outcome;
- authority;
- scope;
- constraints;
- assumptions;
- interfaces;
- material unknowns;
- observable acceptance conditions.

Unknowns may be:

- resolved;
- converted into bounded learning work;
- recorded as blockers.

Do not define a universal heavyweight readiness checklist.

### 4. Task formation and decomposition

Define:

- coherent outcome-traceable units;
- bounded interfaces;
- explicit dependencies;
- local verification boundaries;
- integrated verification boundaries;
- recomposition and integration points.

Prefer vertical slices conditionally when behavioral or end-to-end learning is
the objective.

Permit explicit enabling, infrastructure, risk-reduction, and learning work
where vertical slicing is incoherent or uneconomic.

Do not establish a universal task size.

### 5. Delegation contract semantics

For consequential or otherwise nontrivial delegation, define the semantic
information needed for:

- authority;
- objective;
- immutable or exact relied-upon inputs;
- allowed scope and actions;
- constraints;
- acceptance or validation;
- evidence destination;
- ceilings;
- stopping;
- escalation.

Scale these obligations contextually.

Do not require one universal packet representation or fixed packet size.

### 6. Candidate lifecycle

Define:

- exact immutable candidate identity;
- candidate verification;
- correction;
- impact analysis;
- material versus unaffected scope;
- affected re-verification;
- applicable renewed independent review;
- acceptance as a separate state.

A material correction to the candidate creates a new candidate identity.

### 7. Review model

Keep distinct:

- formation feedback;
- execution verification;
- peer review;
- independent review when warranted;
- integration validation;
- outcome validation.

Define their purposes and contextual invocation semantics.

Do not define a universal reviewer count or require formal independent review
for every task.

### 8. Durable and ephemeral state

Define:

- what becomes durable because downstream reliance, authority, audit, recovery,
  or cross-session coordination depends on it;
- what may remain disposable working or navigation state;
- authoritative-state ownership;
- explicit promotion of working state where needed;
- prevention of competing mutable truth.

Do not create duplicate current-state owners.

### 9. Fresh-context handoff and rehydration

Define:

- authoritative pointers;
- sufficient continuation context;
- current objective and authority;
- baseline identity;
- progress;
- material decisions;
- dependencies;
- uncertainty;
- verification state;
- safe next action;
- stale-state and critical-identity checks.

Summaries and handoffs remain navigation state unless explicitly promoted into
an authorized owner.

No prose summary or compaction mechanism may be assumed lossless.

### 10. Parallel execution

Define eligibility using:

- independence;
- read/write sets;
- side-effect domains;
- invariants;
- dependencies.

Cover:

- read-only parallel work;
- isolated outputs;
- proposal-only contributors under one authoritative writer;
- shared mutation only where enforceable version/conflict control exists;
- aggregation ownership;
- join semantics;
- complete-result accounting;
- partial results;
- missing results;
- conflicts and failures.

Do not establish a universal concurrency count.

### 11. Observability and execution evidence

Define enough protected, secret-safe evidence to reconstruct relied-upon:

- authority;
- identities and important inputs;
- side effects;
- progress;
- resource use where relevant;
- outputs;
- retries;
- cancellation state;
- validation state.

Do not select:

- a tracing product;
- a logging product;
- a storage system;
- sampling policy;
- universal retention duration.

### 12. Stop, cancellation, containment, and recovery

Define:

- explicit stop conditions;
- escalation conditions;
- cancellation request;
- cancellation acknowledgement;
- verified containment;
- ambiguous completion;
- operation-aware retry;
- stable identifiers and deduplication where applicable;
- reconciliation;
- authorized compensation where applicable;
- residual risk for irreversible or external effects.

Do not assume:

- cancellation request equals containment;
- arbitrary rollback is possible;
- retry is always safe;
- compensation restores prior reality.

### 13. Proportionality

Define qualitative tailoring using relevant factors such as:

- context;
- consequence;
- uncertainty;
- reversibility;
- privilege;
- affected scope.

Clarify:

- which ceremony may scale;
- which semantic invariants cannot simply be removed.

Do not create:

- numerical risk scores;
- universal thresholds;
- universal small-task exemptions.

### 14. Unattended and AFK boundary

Define necessary evidence categories before unattended work may even be
considered, including as applicable:

- bounded authority;
- freshness;
- isolation;
- least privilege;
- semantic side-effect safety;
- enforceable ceilings;
- observability;
- cancellation and containment;
- recovery;
- accountable intervention.

State explicitly that Workflow v1 design itself grants no unattended or AFK
execution authority.

Consequential work remains subject to task-specific evidence, authorization,
and later mechanism verification.

### 15. Join and failure behavior

Resolve at least:

- missing required branch or result;
- stale baseline;
- authority conflict;
- failed verification;
- review rejection;
- material correction;
- partial completion;
- ambiguous external effect;
- failed or incomplete containment;
- unreconciled side effects.

No required failure may silently become success.

### 16. Later-stage boundary

Define:

- what remains proposal state during design;
- what may become normative only through later explicit adoption;
- what capability and enforcement requirements later pass to DR-005;
- what remains project-specific;
- what remains post-v1.

## Explicit non-scope

The initial design must not select:

- GitHub Issues or GitHub Projects as the workflow implementation;
- another tracker;
- Apps;
- MCP servers;
- skills;
- hooks;
- models;
- OpenAI products;
- orchestration frameworks;
- workflow engines;
- queues;
- logging products;
- tracing products;
- attestation systems;
- credential providers;
- worktree or container implementations;
- automation.

It must not establish unsupported universal numbers for:

- risk;
- task size;
- concurrency;
- retries;
- duration;
- token use;
- cost;
- reviewer count;
- AFK eligibility.

It must not:

- start DR-005;
- implement Workflow v1;
- grant routine repository-write authority;
- grant parallel direct-main write authority;
- grant AFK or automated-write authority;
- redesign the accepted branch-protection decision without a new contradiction.

## Required design outputs

The smallest reviewable substantive proposal must include equivalent semantic
coverage for:

1. purpose and authority boundary;
2. terminology;
3. explicit proposed design decisions;
4. lifecycle/state model;
5. transition and gate table;
6. role and authority model;
7. authoritative-state ownership map;
8. readiness semantics;
9. task and delegation semantic contract;
10. decomposition, dependency, integration, and recomposition rules;
11. candidate, verification, correction, review, and acceptance lifecycle;
12. durable versus ephemeral state;
13. handoff and rehydration contract;
14. parallel eligibility, isolation, ownership, join, and partial-result rules;
15. observability and evidence obligations;
16. stop, cancellation, containment, retry, reconciliation, and recovery;
17. proportionality;
18. unattended-operation boundary;
19. failure and escalation behavior;
20. deferred capability and enforcement requirements for DR-005;
21. unresolved design items, with blocking effect and owner;
22. conformance scenarios sufficient to expose ambiguous semantics.

Document aesthetics or a fixed section count are not requirements.

## Required conformance scenarios

The substantive design must include enough scenarios to prove semantics for at
least:

1. a conditional gate that is legitimately omitted;
2. a gate falsely claimed as passed;
3. stale authoritative state detected before a state-dependent transition;
4. a parallel execution join with a missing or failed required result;
5. a material candidate correction requiring a new identity;
6. uncertain cancellation where containment is not yet verified;
7. a fresh context rehydrating from authoritative pointers;
8. unattended execution denied because necessary evidence is incomplete.

## Authoritative state ownership model

For this design stream:

- Research status, research dispositions, and DR-005 dependency remain owned by
  `docs/research/research-register.md`.
- Repository current next gate and design-contract navigation pointer remain
  owned by `docs/research/research-register.md`.
- This artifact owns the design task contract, substantive proposal content,
  and its design-stage metadata.
- Candidate identity is the exact full Git commit SHA.
- An independent review verdict and findings belong to a later durable review
  record bound to the exact candidate SHA.
- Initial design disposition belongs to a later durable
  coordinator/accountable-human disposition record.
- Normative Workflow v1 content and adoption belong only to a later explicitly
  adopted normative owner and adoption record.

The Research Register must not become a general design tracker.

No competing mutable owner may be created.

## Substantive design execution model

After this contract is durable:

1. Start substantive design in a fresh Command Center context.
2. Rehydrate from the repository, exact contract commit SHA, and this task
   contract.
3. Re-read live authoritative state before any state-dependent design decision.
4. Produce the substantive proposal within this artifact's authorized scope.
5. Verify completeness, internal consistency, accepted-input traceability,
   non-scope preservation, and conformance scenarios.
6. Persist the substantive proposal through a separately authorized bounded
   transition.
7. The full resulting commit SHA becomes the design candidate identity.

Do not treat this contract-materialization commit as the substantive design
candidate.

## Candidate, review, and disposition lifecycle

The intended lifecycle is:

design contract durable
-> substantive initial design proposal
-> exact candidate commit identity
-> independent review of that exact unchanged SHA
-> material correction creates a new candidate if required
-> affected verification and applicable review repeated
-> coordinator/accountable-human design disposition
-> initial tool-agnostic Workflow v1 design disposition
-> separate DR-005 gate may then become eligible

Keep distinct:

- design work completion;
- commit creation;
- candidate identity;
- verification;
- independent review;
- design disposition;
- normative adoption;
- accepted baseline.

Workflow v1 becomes normative only through a later explicit adoption decision
and faithful materialization into the designated normative owner.

## DR-005 boundary

DR-005 may later consume accepted, mechanism-neutral requirements for:

- lifecycle and gate enforcement;
- authoritative state placement and freshness;
- delegation semantics and least privilege;
- immutable candidate identity and review binding;
- isolation, concurrency control, joins, and aggregation;
- handoff rehydration;
- observability, redaction, retention, and evidence integrity;
- interruption and containment;
- retry, reconciliation, compensation, and recovery;
- unattended-operation ceilings and intervention;
- effective-configuration verification.

DR-005 remains blocked now because no exact substantive design candidate,
independent design review, durable design disposition, satisfied dependency,
or explicit DR-005 research gate yet exists.

## Branch-protection and write boundary

The repository remains private and branch protection is unavailable under the
accepted current-plan limitation.

Therefore:

- bounded serialized writes may continue only under exact-base discipline and
  explicit scope;
- routine agent writes remain unauthorized;
- parallel direct-main writes remain unauthorized;
- AFK and automated writes remain unauthorized;
- privileged, destructive, or externally consequential unattended writes remain
  unauthorized;
- effective protection remains required before those modes.

This contract does not amend the accepted bootstrap protection decision.

## Stop boundary

At contract materialization there must be no substantive Workflow v1 design
proposal in this file.

The next eligible gate after durable materialization is:

Workflow v1 initial design candidate gate

That gate still requires a fresh live repository re-read.

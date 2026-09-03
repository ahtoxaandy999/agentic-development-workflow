---
id: ADW-WF1-DESIGN-001
artifact: workflow-v1-design
artifact_status: draft
maturity: bootstrap
owner: chatgpt-coordinator
task_contract_status: authorized
design_stage: initial-design-complete
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

---

# Workflow v1 Initial Design Proposal

## Proposal status and authority boundary

The preceding contract records the authorized contract and materialization state. Statements there such as “No substantive Workflow v1 design has yet been produced” describe that earlier contract-durable stage. This appended section is the current substantive proposal. Neither the preceding contract nor this proposal has normative effect yet.

This proposal defines required tool-agnostic behavior. It does not implement Workflow v1, choose mechanisms, authorize repository writes, or establish an accepted candidate. Its current design stage means only that producer-side design and verification are complete enough for later byte-exact persistence and independent review.

For correction traceability, this proposal supersedes only the affected semantics of candidate `24b378832f4edc8ec55d7f3063114dc536d7e24e` identified by `ADW-WF1-DR-MAJ-001` and `ADW-WF1-DR-MAJ-002`. The prior candidate remains historical; this statement does not decide whether independent review will find either correction sufficient.

Candidate-003 corrects only the affected recovery/intervention and resumption-reset semantics of candidate-002 `bca878ea3a2576ef2c354bac00e0049041d616e1` for `ADW-WF1-DR-MAJ-003` and `ADW-WF1-DR-MAJ-004`, as identified in `docs/design/ADW-WF1-DESIGN-REVIEW-002.md`. The candidate-001 correction history above is retained. These corrections are producer-verified proposal content; no independent-review acceptance is claimed.

Candidate-004 corrects only the affected recovery-episode reopening semantics of candidate-003 `fd047c7563a9c44be5b3a4bde7d12f9e88d27414` for `ADW-WF1-DR-MAJ-005`, as identified in `docs/design/ADW-WF1-DESIGN-REVIEW-003.md`, under correction task `ADW-WF1-DESIGN-CORR-003`. Prior correction history is retained. This is producer-verified proposal content; no independent-review acceptance is claimed.

## Purpose, terminology, and design decisions

Workflow v1 coordinates bounded work from clarification through a validated outcome while preserving authority, identity, evidence, and failure semantics. It is a semantic workflow, not a required artifact sequence or Git branching model.

Terms:

| Term | Meaning |
|---|---|
| authoritative owner | The sole current owner allowed to change one mutable authoritative state class. References and caches do not become co-owners. |
| authority | A current grant from an accountable owner defining permitted decisions or actions. Authentication, identity, approval, and capability do not imply authority. |
| task contract | The context-scaled semantic agreement that bounds an objective, authority, scope, inputs, validation, evidence, stopping, and escalation. It need not use a fixed schema. |
| working output | Mutable, non-candidate work that has not been assigned an immutable candidate identity. |
| candidate | Exact immutable content submitted to a gate that relies on content identity. For a repository candidate, identity is the exact full commit SHA. |
| verification | Evidence-producing checks against specified properties. Producer verification may be performed by the executor but is not independent review. |
| review | Deliberate evaluation of a defined subject and criteria. Independence exists only when the reviewer is conflict-free for that subject. |
| acceptance | An explicit decision by the authorized accountable owner about a precisely identified subject. It is not inferred from verification, review, persistence, or use. |
| gate | A predicate controlling a transition. Applicability, satisfaction, and freshness are separately represented. |
| side-effect domain | State whose mutation can affect an external, shared, privileged, or otherwise relied-upon system. |
| containment | Verified cessation or bounded isolation of further effects across every relevant side-effect domain. |
| rehydration | Reconstruction of sufficient current context from authoritative pointers and validated identities before a loss-sensitive action. |
| join | Accountable reconciliation of declared branch obligations into one integration decision; it is not mere receipt of messages. |

The proposal makes these decisions:

| Decision | Required behavior |
|---|---|
| ADW-WF1-DD-001 — orthogonal state | Represent task control, work product, verification, review, decision, normativity, baseline acceptance, and parallel join as distinct semantic state planes. Artifact or Git state may evidence a plane but may not substitute for it. |
| ADW-WF1-DD-002 — explicit conditional gates | Every invoked conditional gate records applicability, satisfaction, freshness, subject, criteria, owner, and evidence. Required-and-passed, not-applicable-with-rationale, and required-but-unsatisfied are distinct. |
| ADW-WF1-DD-003 — single mutable owner | Assign exactly one current authoritative owner to every mutable state class. Other representations are references, evidence, or disposable working state. Ownership transfer is explicit and atomic at the semantic boundary. |
| ADW-WF1-DD-004 — bounded commitment | A task becomes ready and may be authorized only when a qualified executor can act without inventing material intent and the result can be verified at the stated boundary. Unknowns are resolved, bounded as learning work, or block commitment. |
| ADW-WF1-DD-005 — immutable relied-upon identity | Pin and freshly verify every identity or effective-configuration dimension actually relied upon at dispatch, resumption, join, publication, review, acceptance, or other state-dependent transition. Identity proves only which object was examined. |
| ADW-WF1-DD-006 — outcome-traceable decomposition | Decomposed units have explicit outcomes, boundaries, dependencies, interfaces, local verification, integration points, and recomposition obligations. Vertical slices are preferred only when they best expose behavioral or end-to-end learning. |
| ADW-WF1-DD-007 — bounded delegation | Delegated authority is no broader than the parent authority and is explicit enough to constrain action, validation, evidence, ceilings, stopping, and escalation. Delegation of work is not delegation of acceptance unless the accountable owner separately grants that authority. |
| ADW-WF1-DD-008 — controlled parallelism | Parallel work is eligible only when independence, read/write sets, side effects, invariants, dependencies, isolation, ownership, and join behavior are known sufficiently for the proposed concurrency. No concurrency count is universal. |
| ADW-WF1-DD-009 — correction by impact | A material correction creates a new candidate identity. Impact analysis determines affected verification and review; unaffected evidence carries forward only with an explicit, supported finding. |
| ADW-WF1-DD-010 — reliance-based durability | Make state durable before downstream authority, reliance, audit, recovery, or cross-session coordination depends on it. Keep disposable exploration ephemeral and promote it explicitly when reliance changes. |
| ADW-WF1-DD-011 — operation-aware interruption | Cancellation request, acknowledgement, verified containment, reconciliation, recovery, and compensation are distinct. Retry depends on operation semantics and evidence of prior effects. |
| ADW-WF1-DD-012 — qualitative proportionality | Scale representation and ceremony using consequence, uncertainty, reversibility, privilege, affected scope, and context, while retaining semantic invariants. No universal score, threshold, or small-task exemption exists. |
| ADW-WF1-DD-013 — unattended denial by default | This design grants no unattended or AFK authority. Necessary evidence can only make a task eligible for a later explicit decision; incomplete evidence denies eligibility. |
| ADW-WF1-DD-014 — mechanism deferral | The design states behavior and evidence obligations. Storage, schemas, products, identity systems, enforcement, topology, automation, and numeric limits remain for later authorized decisions. |

## Lifecycle and semantic state model

Workflow state is a vector. A work item occupies one value in each applicable plane; no single numeric phase or universal linear process is implied.

| State plane | Values and meaning |
|---|---|
| task control | framing; ready; authorized; active; blocked; recovering; completed; cancelled; abandoned |
| work product | none; working; proposed-output; candidate-identified; superseded |
| verification | not-invoked; pending; passed; failed; stale |
| review | not-evaluated; not-applicable; required-pending; passed; rejected; stale |
| disposition | none; pending; accepted; rejected; deferred; superseded |
| normative status | non-normative; adopted; superseded |
| baseline acceptance | not-applicable; pending; accepted-exact-identity; rejected; superseded |
| join | not-applicable; planned; branches-active; pending; passed; partial; failed; conflicted |
| cancellation | none; requested; acknowledged; contained; residual-effects |
| recovery | not-applicable; assessment; retry-authorized; reconciling; compensated; recovered; intervention-required |

A terminal value in one plane does not collapse another. For example, a verified candidate may still have review required-pending, no disposition, non-normative status, and no accepted baseline. Completed task control means the authorized task stopped with its required terminal accounting; it does not imply candidate acceptance or normative adoption.

Blocked preserves resumability when the obstacle might be resolved. Generic stopping is represented by `task control=blocked`; it does not by itself change the cancellation plane. In the cancellation plane, `requested` means delivery or controller action is not yet acknowledged, `acknowledged` means the controller received and acted on the request but containment is not yet verified, `contained` means cessation or bounded isolation of further effects has been verified across every relevant domain with no residual effect requiring accountable handling, and `residual-effects` means containment has been verified but completed, partial, queued, published, or otherwise durable effects remain explicitly assigned for reconciliation or risk disposition. These meanings do not duplicate task-control values.

`task control=cancelled` and `task control=abandoned` are terminal. Cancelled requires verified containment and terminal accounting; residual effects additionally require completed accountable handling before cancellation may close. Merely requesting or acknowledging cancellation cannot produce cancelled. Abandoned is an explicit decision by the task-contract owner that the bounded objective will not continue; it is legal only after active work has stopped and no hidden active or uncontained effect remains. A terminal task-control value does not erase cancellation, recovery, effect, or evidence history.

For one work item, the designated run/task execution-state owner is the sole mutable owner that records task-control, cancellation, and recovery plane transitions. Controllers and side-effect owners supply authoritative evidence for the operations or domains they own, and task-contract or risk owners supply required decisions, but none becomes a second writer of those planes. A composite transition is recorded only after every required domain finding is available.

For a join's exact integration subject, `join=passed` is permitted only after its integrated-verification gate is effective: required and passed with current evidence, or legitimately not applicable under the existing conditional-gate semantics with a recorded governing rule and rationale. Pending, failed, stale, missing, conflicted, or silently omitted required integrated verification cannot coexist with a successful join for that subject; a material change invalidates the pass and requires reevaluation.

### Gate semantics

A gate evaluation contains:

- the transition and exact subject it governs;
- its accountable owner and evaluation time;
- applicability: required or not-applicable, with the governing rule and rationale;
- satisfaction, only when required: passed or unsatisfied;
- freshness: current or stale for every relied-upon authority, identity, configuration, dependency, and prerequisite;
- criteria, evidence pointers, exceptions, and unresolved conditions;
- the permitted destination state if effective.

Effective outcomes are:

| Outcome | Meaning and transition effect |
|---|---|
| required and passed | Criteria are satisfied with current evidence; the named transition may proceed. |
| not applicable and legitimately omitted | A governing rule permits omission and the accountable owner records the rationale; no pass is claimed. |
| required but not satisfied | The transition is denied and the item remains in or moves to a non-success state such as framing, blocked, failed, or pending. |
| invalid or stale | The evaluation relied on the wrong subject, unauthorized owner, missing criteria, altered identity, stale authority/configuration, or contradictory state; any claimed pass is void and must be reevaluated. |

Absence of a record is not not-applicable. When downstream reliance requires the outcome, both required passes and not-applicable rationales become durable before the transition.

### Transition rules

The table specifies semantic transitions. Each source and destination names the state-plane values changed by that transition; unmentioned planes retain their current values unless a stated predicate invalidates them. Implementations may combine transitions when all owners, predicates, and evidence remain distinguishable.

| Transition | Source → destination | Transition owner and required authority | Required evidence and conditional gates | Invalid or blocked conditions | Durable effect |
|---|---|---|---|---|---|
| frame work | no task or blocked → framing | coordinator or assigned task authority with a current mandate to define the work | authoritative objective source, known authority boundary, current baseline pointers when already relied upon | conflicting owner, unverifiable source, or required scope expansion | durable only when another actor/session or later decision will rely on the framing |
| declare ready | framing → ready | task-contract owner within current framing authority | contextual readiness finding; observable acceptance conditions; unknowns classified; dependencies and interfaces sufficient | executor would have to invent material intent; authority, outcome, acceptance, or material unknown is unresolved | current ready decision and relied-upon task contract become durable |
| authorize | ready → authorized | coordinator or accountable human/risk owner authorized for the consequence | exact task contract; current authority; required exception or risk decisions; any prerequisite gate passed or legitimately not applicable | self-authorization, stale baseline, scope exceeds owner authority, required gate unsatisfied | authorization subject, scope, owner, time, ceilings, and stop boundary become durable when reliance follows |
| dispatch or resume without a cancellation recovery | `task control=authorized or blocked; cancellation=none; recovery=not-applicable or recovered` → `task control=active; cancellation=none; recovery=not-applicable` | designated run/task execution-state owner, on the coordinator or execution-control owner's dispatch/resumption decision under current authorization | fresh reread of relied-upon authority, baseline, inputs, dependencies, and effective controls; delegate identity/configuration when relied upon; completed required recovery and the common resumption reset rule below | revoked or stale authority, changed critical input, unresolved conflict, unverified required control, any cancellation request, acknowledgement, containment uncertainty, residual effect, incomplete required recovery, or unresolved intervention | execution identity, baseline, scope, and start/resumption decision become durable when consequential; clearing the recovered current value retains episode history under the common resumption reset rule |
| delegate | authorized or active parent → bounded child authorized or framing | parent task authority; child grant cannot exceed parent | context-scaled delegation contract and exact relied-upon inputs; independence and ceiling decisions if concurrent | recursive or expanded authority not granted, ambiguous owner, missing stop/escalation, inability to validate | durable child authority and parent/child dependency where downstream coordination relies |
| produce output | active → proposed-output with verification pending or not-invoked | executor within assigned scope | output identity or location, deviations, side effects, evidence, unresolved items | work escaped scope, ambiguous effect, missing required evidence, stale inputs affecting result | relied-upon output and execution evidence become durable |
| verify | pending or not-invoked → passed, failed, or stale | designated verifier; executor may perform producer verification unless independence is required | criteria, exact subject, environment/configuration identities when relied upon, result evidence | wrong subject, altered candidate, unverifiable environment, suppressed failure | durable result when publication, review, acceptance, recovery, or coordination relies |
| apply generic stop | `task control=active` → `task control=blocked`; cancellation and all other planes unchanged | designated run/task execution-state owner; a coordinator, risk owner, controller, or executor may supply the mandatory stop trigger within authority | reason, affected operations and domains, last known safe state, and escalation destination | treating local cessation as cancellation acknowledgement, containment, completion, or authority for remediation | stop event and safe next action become durable for consequential or cross-session work |
| request cancellation | `task control=active or blocked; cancellation=none` → `task control=blocked; cancellation=requested` | designated run/task execution-state owner, on a request from a coordinator, accountable risk owner, or execution controller with cancellation authority | desired cancellation scope, operation/domain identities, reason, requested boundary, and controller destination | inferred authority, unidentified operations/domains, or treating request delivery as acknowledgement or containment | cancellation request and affected inventory become durable |
| acknowledge cancellation | `task control=blocked; cancellation=requested` → `task control=blocked; cancellation=acknowledged` | designated run/task execution-state owner, using acknowledgement evidence from the controller responsible for every affected operation/domain | acknowledgement tied to operation identities; evidence every request was received and acted upon; known in-flight work | acknowledgement inferred from silence or request delivery; any relevant controller omitted | durable acknowledgement and inventory of domains whose containment remains unverified |
| verify containment | `task control=blocked; cancellation=acknowledged` → `task control=blocked; cancellation=contained or residual-effects` | designated run/task execution-state owner, using authoritative findings from every accountable side-effect/control owner | observation across every relevant operation/domain; cessation or bounded isolation of further effects; reconciliation finding for completed, partial, queued, published, or ambiguous effects | any relevant domain unobserved, continuing, or ambiguously bounded; request or acknowledgement presented as containment | durable containment finding, residual-effect inventory and owner, and restrictions on resumption, completion, and release |
| begin recovery or reconciliation | `task control=blocked; cancellation=none, contained, or residual-effects; recovery=not-applicable, intervention-required, or recovered` → `task control=recovering; cancellation unchanged; recovery=assessment`; entry from `recovered` opens a new episode only under the reopening guard below | designated run/task execution-state owner, on an authorized recovery decision from the applicable state/side-effect owner | failed, partial, conflicted, contained, residual-effect, or positively established new recovery condition; operation classification; prior-effect evidence; recovery authority and scope; validation target; residual-effect owner when applicable; for `recovered`, the new-episode evidence required below | cancellation requested or acknowledged; unresolved containment or authority; recovery activity already in progress; unowned residual effect; `recovered` without the reopening guard satisfied | durable recovery decision, scope, owner, and planned safe target; reopening records a distinct episode linked to the prior completed episode and retains its history |
| authorize recovery action | `task control=recovering; cancellation=none, contained, or residual-effects; recovery=assessment` → `task control=recovering; cancellation unchanged; recovery=retry-authorized or reconciling` | designated run/task execution-state owner, on the applicable state/side-effect owner's operation-specific recovery decision | operation classification; prior-effect evidence; stable identifiers, deduplication, or version preconditions as applicable; recovery or compensation plan and authority | cancellation requested or acknowledged; blind retry, unauthorized compensation, irreversible effects presented as reversible, or unresolved ambiguity that requires the separate intervention transition | durable operation classification, authorized action, owner, and validation target |
| record recovery action | `task control=recovering; cancellation=none, contained, or residual-effects; recovery=retry-authorized or reconciling` → `task control=recovering; cancellation unchanged; recovery=compensated or reconciling` | designated run/task execution-state owner, using effect evidence from every affected state/side-effect owner | action identity, attempted and observed effects, version/deduplication result where applicable, and remaining reconciliation | cancellation requested or acknowledged; repeated action without its precondition, effect evidence missing, unauthorized compensation, or ambiguity requiring the separate intervention transition | durable attempt, effects, compensation status where applicable, and remaining reconciliation |
| conclude recovery | `task control=recovering; cancellation=none, contained, or residual-effects; recovery=assessment, retry-authorized, reconciling, or compensated` → `task control=blocked; cancellation unchanged; recovery=recovered` | designated run/task execution-state owner, using authoritative validation from every affected state/side-effect owner | resulting authoritative state, validation against the authorized target, complete required reconciliation, remaining residual effects and risk disposition | cancellation requested or acknowledged; target state unvalidated, relevant effect unreconciled, risk decision missing, or ambiguity requiring the separate intervention transition | durable recovery outcome, effects, validation, and residual risk; no resumption or terminal task-control result is implied |
| require accountable intervention | `task control=recovering; cancellation=none, contained, or residual-effects; recovery=assessment, retry-authorized, reconciling, or compensated` → `task control=blocked; cancellation unchanged; recovery=intervention-required` | designated run/task execution-state owner records the recovery blocker; the applicable state/side-effect owner owns the next recovery decision, with accountable human/risk-owner authority where the consequence requires it | available operation/attempt and prior-effect evidence; explicit missing, conflicting, or insufficient evidence/authority; reason recovery cannot safely proceed or conclude; affected domains, residual-effect obligations, and named accountable decision owner | continuing recovery despite the blocker, recording recovered without validation, hiding uncertainty, or treating intervention as permission for another action | durable blocked/intervention outcome, reason, available evidence and gaps, last known safe state, residual obligations, decision owner, and escalation destination; no unavailable evidence or approval is required merely to record the block |
| resume after cancellation recovery | `task control=blocked; cancellation=contained; recovery=not-applicable or recovered`, or `task control=blocked; cancellation=residual-effects; recovery=recovered` → `task control=active; cancellation=none; recovery=not-applicable` | designated run/task execution-state owner under current resumption authority; accountable risk-owner decision also required where residual effects remain | explicit resumption decision, fresh authority and inputs, verified containment, completed required reconciliation when applicable, accepted or assigned residual risk, and safe resource state; the common resumption reset rule below | cancellation only requested or acknowledged; containment uncertain; required recovery incomplete; residual effects unowned or unaccepted | durable resumption decision retains the historical cancellation, containment, recovery, and residual-effect records under the common resumption reset rule |
| enter join | branches-active → join pending | named aggregation owner | declared membership, required/optional status, exact branch outputs, dependency results, local validation, side effects, freshness | unknown branch set, competing aggregator, missing ownership, stale baseline | join inventory and observed result states become durable when relied upon |
| pass join | `join=pending` → `join=passed` | aggregation/integration owner | every required result present and acceptable; optional omissions recorded as not applicable or omitted; conflicts resolved; current baseline; integrated-verification gate for the exact integration subject is required and passed with current evidence, or legitimately not applicable with its governing rule and rationale recorded | missing/failed/stale required result, unresolved conflict, stale shared state, unreconciled side effect, or integrated verification pending, failed, stale, conflicted, missing, or silently omitted | join decision, included identities, exclusions, conflict disposition, integration subject, and integrated-verification gate outcome become durable |
| record non-passing join | `join=pending` → `join=partial, failed, or conflicted`, or remains `join=pending` while required integrated verification is pending or stale | aggregation owner | complete accounting of received, missing, failed, excluded, and ambiguous results; integrated-verification state; containment/recovery obligations | relabeling incomplete required work or unsatisfied integrated verification as successful | durable non-success state and safe next action |
| identify candidate | proposed-output with applicable producer verification → candidate-identified | candidate-producing owner under explicit publication/persistence authority | exact immutable content identity, scope claim, provenance/evidence pointers, producer verification status; when the output relies on a join, `join=passed` for the same exact integration subject | mutable reference used as identity, required verification failed or stale, relied-upon join non-passing or invalid, publication authority absent | candidate identity and claimed scope become durable; persistence alone confers no acceptance |
| invoke review | candidate-identified or defined non-candidate subject → review required-pending or not-applicable | accountable governance/task owner, not the candidate executor acting beyond authority | qualitative invocation decision; exact subject; criteria; conflict test; evidence/context | omitted gate has no legitimate rationale; reviewer conflict where independence is claimed; mutable target | invocation or not-applicable rationale becomes durable when disposition relies on it |
| conclude review | required-pending → passed or rejected | assigned reviewer; independent reviewer must be conflict-free | exact unchanged target, criteria, findings, verification links, scope, independence basis when claimed | self-review claimed independent, target changed, critical context stale, findings destination unavailable when reliance requires durability | durable verdict/findings bound to exact subject |
| correct candidate | candidate-identified, review rejected, or verification failed → prior candidate superseded and new working output | authorized executor/corrector; no acceptance power follows | correction record and impact analysis identifying changed content, load-bearing assumptions, affected verification and review | editing in place while retaining prior identity; unsupported claim that evidence is unaffected | old identity remains historical; new identity exists only after immutable persistence |
| reverify or rereview | corrected working output or new candidate → applicable verification/review states | relevant verifier and reviewer owners | new identity; impact analysis; affected checks rerun; unchanged evidence carried only with explicit support | automatic inheritance from prior candidate, missed changed assumption, conflicted reviewer | new results bind to new identity; prior verdict remains only for prior identity |
| disposition | verified/reviewed subject as required → accepted, rejected, or deferred disposition | coordinator or accountable human/risk owner authorized for that consequence | exact subject; all required gates passed; omitted gates have legitimate rationales; current authority and evidence | executor self-acceptance, inference from pass/merge/use, stale candidate, unresolved required finding | durable disposition identifies subject, scope, rationale, and owner |
| normative adoption | accepted design disposition → normative adopted | owner authorized to amend the designated normative artifact | explicit adoption decision naming recommendation/design, target owner, scope, exact identity, and faithful materialization | candidate or disposition treated as policy; target owner unspecified; materialization differs | normative owner and adoption record become durable; this is separate from baseline acceptance |
| baseline acceptance | exact persisted candidate with required review/disposition → accepted-exact-identity | coordinator/accountable owner under baseline policy | exact full commit identity, current review and decision records, fresh live state | branch, tag, short identity, changed commit, or successful checks treated as acceptance | durable acceptance record bound to exact identity |
| complete task | `task control=active or blocked; cancellation=none` → `task control=completed`; other planes retain their recorded terminal values | task owner | terminal accounting against authorized objective, outputs, validation, joins, side effects, evidence, unresolved items, and next gate | missing required result, non-passing relied-upon join, any cancellation state other than `none`, unhandled residual effect, incomplete required recovery, unresolved intervention, ambiguous effect hidden, or dependent plane falsely treated as passed | durable completion only when downstream reliance or coordination requires it; prior cancellation/recovery history, if any, remains durable outside the current plane values |
| close cancelled | `task control=blocked; cancellation=contained; recovery=not-applicable or recovered`, or `task control=blocked; cancellation=residual-effects; recovery=recovered` → `task control=cancelled`; cancellation and recovery retain their values | designated run/task execution-state owner acting on explicit terminal-closure authority from the task-contract or execution-control owner; accountable risk-owner decision is also required for residual-effect disposition | verified containment across every relevant domain; reconciliation and terminal accounting; for `residual-effects`, completed handling with durable ownership, obligations, and accepted or escalated residual risk | cancellation merely requested or acknowledged; active or recovering work; any domain unobserved, active, or uncontained; recovery/reconciliation incomplete; residual effect unowned or risk disposition absent | terminal cancellation decision, decision owner, evidence, residual-effect disposition, and unresolved obligations become durable without erasing other planes |
| abandon task | `task control=framing, ready, authorized, or blocked` → `task control=abandoned`; cancellation and recovery retain their values | designated run/task execution-state owner acting on an explicit discontinuation decision by the task-contract owner; accountable risk-owner decision is also required where residual effects remain | explicit abandonment rationale and scope; no active or recovering work; cancellation is `none` or containment is verified; terminal accounting for outputs, effects, evidence, dependencies, and successor responsibility; if `cancellation=residual-effects`, recovery is `recovered` and accountable handling is complete | executor self-abandonment; active or recovering work; cancellation requested or acknowledged only; any hidden, unobserved, or uncontained effect; residual effect unowned or recovery incomplete; abandonment used to bypass required failure or residual-risk handling | terminal abandonment decision, decision owner, rationale, retained outputs/effects, unresolved obligations, and successor or no-successor decision become durable |

A state-dependent transition is reevaluated after any material change to its subject, authority, critical input, dependency, effective configuration, or governing rule. Prior evidence remains historical but cannot authorize the changed transition.

### Recovery episode reopening, intervention, and resumption rules

The **recovery-episode reopening guard** extends **begin recovery or reconciliation**, without adding a separate transition. From `task control=blocked; cancellation=none, contained, or residual-effects; recovery=recovered`, a positively established new current recovery obligation may open a distinct episode at `task control=recovering; cancellation unchanged; recovery=assessment`. The prior episode must be complete against its authorized target, and the new obligation must be materially distinct or have been created/discovered afterward. Required evidence identifies the prior completed episode and its validation, the new obligation and evidence of its distinction or later creation/discovery, affected operations/domains and owners, and the new bounded recovery scope and validation target. Examples include a newly discovered residual effect, new reconciliation requirement, separately authorized compensation, changed authoritative target, or another independently arising recoverable condition. The applicable state/side-effect owner authorizes the new episode, with accountable human/risk-owner authority where the consequence requires it; the designated run/task execution-state owner alone records the transition. The new episode identity, link to the prior episode, decision, and supporting evidence become durable. Prior episode identity, decisions, attempts, effects, validation, and remaining assigned/accepted residual obligations remain historical and durable; opening the new episode does not retroactively mark the prior episode failed.

`recovered` is not interchangeable with `not-applicable`. Reopening is invalid without positive evidence of the new obligation, with an incomplete prior episode, as a relabeling of unresolved prior recovery, or without the existing entry authority, ownership, and containment predicates. Cancellation request and acknowledgement retain `recovered` and cannot start a new episode; verified containment must first establish `contained` or `residual-effects`. The same reopening rule applies to a new non-cancellation obligation before resumption. A prior recovered value cannot satisfy a new obligation: the existing predicates continue to deny resumption, completion, terminal cancellation, and abandonment while required recovery/reconciliation or residual-effect handling is incomplete. Once reopened, the existing action, conclusion, and **require accountable intervention** transitions apply to the new episode; unsafe continuation records `blocked / cancellation unchanged / intervention-required`, never a persistent `recovering / intervention-required` state.

The sole entry to `recovery=intervention-required` is **require accountable intervention**. Whenever assessment, action authorization, attempted recovery, or conclusion determines that recovery cannot safely proceed or conclude under current evidence and authority and requires an accountable decision, the designated run/task execution-state owner records `task control=blocked; recovery=intervention-required`, retaining cancellation. If no listed recovery-action or successful-conclusion transition is permitted, this intervention transition is required. This includes missing evidence or unresolved ambiguity; it does not require successful validation. `task control=recovering; recovery=intervention-required` is not permitted. Available evidence, uncertainty, ownership, and obligations remain durable; recording the block neither grants recovery authority nor implies recovery success, resumption, completion, cancellation, or abandonment.

While intervention is unresolved, the task remains blocked and escalated with its named accountable decision owner; unavailable intervention is an intentional blocked state, never permission to continue. The following next-action classes are explicit and remain subject to the transition table:

- **Renew recovery:** the applicable state/side-effect owner supplies a fresh bounded recovery decision and supporting evidence addressing the blocker sufficiently for the proposed attempt, with human/risk-owner authority where required. **Begin recovery or reconciliation** changes `blocked/intervention-required` to `recovering/assessment` only when its gates are satisfied; another attempt may again require intervention.
- **Continue blocked/escalated:** when no permitted next action is supported, retain `blocked/intervention-required`, cancellation, evidence gaps, residual obligations, and the accountable escalation destination. Record any new decision or evidence without claiming a state advance.
- **Request cancellation:** if `cancellation=none`, an authorized **request cancellation** changes it to `requested` while retaining `task control=blocked; recovery=intervention-required`. Acknowledgement and containment then follow their existing transitions, retaining recovery. Requested or acknowledged cancellation prevents recovery; after verified containment, renewed recovery can begin under its own authority.
- **Abandon:** only the separate **abandon task** decision and all of its independent guards permit terminal abandonment. Incomplete required recovery or residual-effect handling still denies it; intervention does not waive those obligations. Where recovery remains required, renew and conclude it before considering abandonment.
- **Close cancelled:** **close cancelled** retains its exact source predicates and terminal guards. Intervention-required is not an eligible recovery value; renewed recovery must first conclude as `blocked/recovered`, with verified containment and completed required residual-effect handling, before a separate terminal-cancellation decision.

These rules also constrain generic task-control transitions: reframing or reauthorization cannot move an unresolved intervention into executable work or bypass required recovery. Only the listed next-action classes may leave or maintain the intervention state; terminal decisions preserve the history and independently required obligations.

The **common resumption reset rule** applies to both dispatch/resumption rows. `recovery=not-applicable` is the idle current value; `recovery=recovered` records a completed, validated episode awaiting a separate resumption or terminal decision, unless a new obligation opens another episode under the reopening guard. When authorized resumption clears that recovered current value, the same transition explicitly sets `task control=active; cancellation=none; recovery=not-applicable`. This reset is mandatory, not inferred from unmentioned-plane retention, and never occurs from intervention-required or incomplete recovery. Both paths require current resumption authority, validated required recovery/reconciliation, and their existing containment and residual-effect guards. The reset preserves durable episode identity, decisions, attempts, effects, validation, and any remaining assigned/accepted residual obligations; it cannot erase an unresolved effect, accept risk, or bypass intervention. A later independent failure therefore follows **apply generic stop** to `blocked/none/not-applicable`, then **begin recovery or reconciliation** to `recovering/none/assessment` under a new authorized recovery decision. Terminal closure preserves recorded recovery values rather than applying a resumption reset.

## Roles and authority

One actor may hold multiple roles only when their duties do not conflict and no independence claim is made.

| Role | May | Must not |
|---|---|---|
| ChatGPT coordinator | frame work; resolve bounded design choices; determine contextual gate applicability within granted authority; issue or request authorization; coordinate joins; present candidates and evidence | infer authorization, adoption, or acceptance; broaden scope; claim human risk authority it does not hold; accept its own work without an explicit authorized decision |
| accountable human or risk owner | authorize consequential scope; own exceptions and residual risk; require independence; accept, reject, defer, stop, abandon, or approve recovery within their authority | treat tool capability, authentication, or another actor’s confidence as approval; accept an unidentified or stale subject |
| researcher | gather and analyze evidence under a research gate; preserve source qualification and uncertainty | convert evidence or recommendations into policy; change current disposition unless assigned that owner |
| executor | act inside exact scope; produce outputs; report deviations, evidence, side effects, and blockers; perform producer verification when allowed | self-authorize expansion; suppress failures; claim independent review; self-accept; continue past a stop trigger |
| verifier | execute or assess specified checks and bind results to the exact subject | claim review or acceptance solely from checks; reuse stale results without impact support |
| reviewer | evaluate a defined subject and criteria; issue findings and a review verdict | broaden review into acceptance; imply independence without a conflict test |
| independent reviewer | perform review with no authorship, execution, acceptance stake, or other material conflict for the subject | review their own candidate as independent; change the candidate under review; accept it by implication |
| aggregation/integration owner | own branch accounting, resolve or escalate conflicts, produce one integration subject, and decide whether the join passes | hide missing or failed branches; allow multiple authoritative aggregators for one join |
| repository maintainer or state custodian | preserve designated artifacts, enforce exact-base operations, and execute separately authorized persistence | create workflow policy through maintenance; treat a write, commit, push, or merge as acceptance |
| authoritative state or side-effect owner | validate current state, control mutation, reconcile effects, and authorize applicable recovery | permit a competing mutable owner or claim rollback where effects remain |
| evidence custodian | protect, redact, retain, and provide addressable relied-upon evidence under applicable rules | retain unnecessary secrets or become the owner of the underlying decision merely by storing its evidence |

Consequential authorization and acceptance are reserved for an accountable coordinator or human risk owner whose authority covers the effect. Consequence is contextual: governed policy, shared baselines, security or privilege, compliance, irreversible/external effects, and comparable downstream reliance are relevant. Ordinary work is not automatically consequential, and no numerical threshold is defined.

## Authoritative-state ownership

| Mutable state class | Sole current authoritative owner | References that do not own it |
|---|---|---|
| research status, research dispositions, dependencies, supersession, DR-005 dependency | Research Register | reports, summaries, candidate proposal |
| repository current next gate and design-contract navigation pointer | Research Register | chat, handoff, task notes |
| this design task contract, substantive proposal, design-stage metadata | this design artifact until a later explicit ownership change | reviews, disposition records, copied proposals |
| task objective, scope, readiness, authority, ceilings, stop boundary | designated task-contract owner | executor notes and summaries |
| live repository, external system, or effective control state | the relevant live system and accountable control owner | local copies, caches, reports |
| mutable execution progress and current operation/cancellation state | designated run/task execution-state owner | logs and handoffs unless explicitly promoted |
| each side-effect domain | its designated state/side-effect owner | executor cache or orchestration status |
| decomposition graph, dependency status, required branch membership | designated task/decomposition owner | child task summaries |
| aggregation and join disposition for one parallel group | one named aggregation owner | branch producers |
| working output | designated executor or editor until handoff | reviewers and evidence stores |
| immutable candidate content | no mutable owner; it is immutable | branches, tags, working trees, descriptions |
| candidate registry/pointer and supersession relation, when needed | designated candidate-record owner | mutable branch names |
| verification state | designated verification-record owner | candidate metadata or review |
| review verdict and findings | designated review-record owner; reviewer authors the result | candidate author, task summary |
| design disposition or other recommendation decision | coordinator/accountable-human disposition record owner | Research Register except where it is explicitly the adopted owner for research disposition |
| normative Workflow v1 content and adoption state | later explicitly designated normative owner and adoption record | this non-normative proposal |
| accepted baseline identity | baseline-acceptance record owner | file front matter, branch, tag, check result |
| evidence retention/protection metadata | designated evidence custodian | underlying task or decision owner remains unchanged |
| project-specific product state and operating rules | the applicable project repository/system owner | this cross-project control plane |

Ownership transfer identifies the state class, previous owner, new owner, transfer authority, effective point, and reconciliation of in-flight writes. Until that succeeds, the previous owner remains authoritative. Mirroring is permitted only as a labeled reference with freshness/provenance and without independent mutation.

## Readiness, task formation, and delegation

### Contextual readiness

The task-contract owner asks whether the current bounded commitment is executable and verifiable, not whether every future fact is known. Sufficient context includes, as material to the task:

- intended outcome and why it is relied upon;
- current authority and accountable owner;
- included and excluded scope, allowed actions, constraints, and assumptions;
- exact baseline and critical input identities;
- interfaces, dependencies, invariants, and side-effect domains;
- material unknowns and uncertainty;
- observable local, integrated, and outcome acceptance conditions;
- evidence destination, ceilings, stop conditions, and escalation path.

Each material unknown is resolved before commitment, converted into separately bounded learning or risk-reduction work with its own observable result, or recorded as a blocker. Refinement during execution is allowed when the task contract authorizes the decision range and the refinement does not invent material intent or expand authority. Otherwise the executor stops for reframing.

Representation scales to the context. Trivial, low-consequence, reversible work may express several semantics together; consequential or cross-session work needs addressable detail. Semantic absence is not excused by a short format.

### Decomposition, dependencies, integration, and recomposition

A decomposition is valid when:

- every unit traces to an authorized outcome or an explicit enabling, infrastructure, risk-reduction, or learning need;
- the unit boundary and interfaces are independently understandable;
- inputs, outputs, read/write sets, side effects, invariants, dependencies, and responsible owner are explicit to the degree relied upon;
- local verification can establish the unit’s promised boundary;
- integrated verification and final outcome validation are assigned;
- integration and recomposition points say who combines which exact outputs, in what dependency condition, and how omissions or conflicts are handled;
- unavoidable coupling is visible and does not masquerade as independence.

Use an observable vertical slice when behavioral, user, or end-to-end learning is the objective and the slice is coherent and economical. Use horizontal or enabling work when it is necessary for infrastructure, risk reduction, feasibility, or learning and its value and integration dependency are explicit. Unit size and scheduling are contextual.

A dependency is satisfied only by the exact required result and its specified validation state. A pointer to in-progress work, a partial result, or an unverified substitute does not satisfy it. Recomposition cannot pass until all required dependency results and side effects are accounted for. Integrated verification tests the composed subject; local branch verification alone is insufficient when interactions matter.

### Delegation semantics

A consequential or otherwise nontrivial delegation communicates enough of the following semantic information for the delegate and later verifier to reach the same boundaries:

- granting owner, authority source, delegate role, and permitted decisions;
- objective, expected output, and relation to the parent outcome;
- repository/system scope, exact baseline, relied-upon inputs, and effective configuration;
- allowed reads, writes, actions, side-effect domains, and explicit non-goals;
- constraints, assumptions, dependencies, interfaces, invariants, and isolation expectations;
- local validation, integrated acceptance, and evidence destination;
- privilege, time/resource/effect ceilings where relevant, without universal numeric defaults;
- required progress or exception reporting;
- stop triggers, cancellation contact, containment obligations, safe next action, and escalation destination.

The parent remains responsible for dependency and join accounting. A delegate may further delegate only if that power is explicit, bounded, and consistent with the same ownership and evidence rules. Delegation never enlarges authority through recursion. A delegated result is a proposal or task output until the owner of the receiving state validates and promotes it.

## Candidate, verification, review, correction, and acceptance

Formation feedback tests whether intent, boundaries, risks, and acceptance conditions are adequate before or during work. It may change framing and is not execution verification.

Execution verification tests specified properties of the exact output using reproducible or otherwise reconstructable evidence. Producer verification may support candidacy but carries no review independence.

Peer review finds defects or improves quality through another qualified perspective. It is not necessarily independent and never substitutes for outcome validation or acceptance.

Independent review is invoked when applicable governance or a contextual decision based on consequence, uncertainty, privilege, affected scope, conflict exposure, or downstream reliance warrants it. The invocation owner records required or not-applicable before disposition. An independent reviewer must be conflict-free for the exact subject and receives its immutable identity, requirements, claimed scope, relevant context, linked verification, review criteria, independence expectation, stop boundary, allowed dispositions, and findings destination.

Integration validation checks interactions and recomposed invariants against the integrated subject. Outcome validation checks whether the authorized result achieves the intended observable outcome. Either may expose a design or framing defect even when local checks pass.

A formal candidate record identifies exact immutable content, provenance, claimed scope, relevant baseline, known deviations, producer verification, and pending gates. For Git persistence, only the full commit SHA identifies the candidate. A branch, tag, short SHA, diff narrative, file digest alone, author name, or working tree is insufficient. Candidate identity does not prove authority, provenance trust, correctness, retention, review, or acceptance.

Correction follows these rules:

1. Record the finding and determine whether content, behavior, evidence, assumptions, interfaces, dependencies, side effects, or criteria change.
2. Any change to candidate content creates a new immutable candidate identity. The prior candidate remains historical and may be marked superseded; it is never edited while retaining identity.
3. Analyze affected scope relationally. Materiality means the change or a changed load-bearing assumption can alter a relied-upon conclusion, not that it crosses a line-count threshold.
4. Rerun affected verification and integrated/outcome validation. Carry prior evidence only when the unchanged subject, assumptions, environment, and criteria are demonstrated.
5. Renew any applicable review whose target or load-bearing basis changed. A prior verdict remains bound to the prior identity.
6. Submit the new exact identity for disposition. No executor, verifier, or reviewer may infer acceptance.

A review rejection is a non-success review outcome. It may cause correction, reframing, abandonment, or an explicitly authorized exception process; it cannot be relabeled passed. Coordinator disposition, normative adoption, and baseline acceptance remain later distinct decisions even after a review passes.

## Durable and ephemeral state

Durability is required before another actor, session, decision, recovery step, audit, or authority grant relies on the state. Durable records are addressable, attributable to their state owner, protected according to consequence, and bound to exact subjects when identity matters. At minimum when relied upon, durability covers material authorizations and exceptions, task/delegation boundaries, candidate identities, gate evaluations, review findings and verdicts, dispositions and acceptance, join accounting, side effects, cancellation/containment, recovery decisions, and unresolved residual risk.

Exploration, scratch reasoning, transient progress narration, caches, and summaries may remain ephemeral while no downstream reliance depends on them. Promotion is explicit: identify the authoritative owner, reconcile against current state, record provenance and effective time, and label superseded copies. Copying text into a durable medium is not promotion by itself.

Logs and evidence do not become mutable workflow-state owners merely because they are durable. The relevant task, decision, side-effect, or state owner remains authoritative. Secret material is excluded or redacted to the minimum necessary; redaction must preserve enough context to understand the relied-upon event without exposing credentials or unnecessary sensitive data.

## Handoff and fresh-context rehydration

A handoff is navigation state. For consequential continuation it points to:

- authoritative task contract and authority owner;
- current objective, allowed scope/actions, non-goals, constraints, and stop boundary;
- exact baseline and critical input/output identities;
- current state-plane values and owner of each mutable class;
- completed progress and remaining obligations;
- material decisions, exceptions, assumptions, uncertainty, blockers, and residual risk;
- dependencies, interfaces, side effects, parallel membership, and join state;
- verification, review, disposition, cancellation, containment, and recovery states;
- evidence locations and the safest authorized next action.

A fresh actor does not treat prose as lossless. Before a loss-sensitive, state-dependent action it reads the authoritative pointers, verifies access and identity, rereads current mutable state from its owner, checks that authority remains effective, validates relied-upon configuration/control state, and reconciles discrepancies. Missing or inconsistent critical identity, authority, ownership, containment, or dependency data blocks action.

If navigation prose conflicts with an authoritative owner, the authoritative owner controls and the discrepancy is recorded. If two artifacts both claim mutable authority or precedence is unclear, action stops for owner resolution. More history does not cure an authority conflict.

## Parallelism, isolation, and joins

Parallel work is eligible only after the task/decomposition owner establishes enough information about independence, read/write sets, side-effect domains, invariants, dependencies, output identities, validation, ownership, ceilings, and join behavior. Eligibility is reevaluated when any of those change.

Permitted semantic classes are:

| Class | Eligibility and ownership |
|---|---|
| read-only parallel work | Inputs may be read concurrently when reads do not consume or mutate hidden state and snapshots/freshness requirements are compatible. |
| isolated outputs | Each branch has an exclusive output and side-effect domain; integration occurs through a named join owner. |
| proposal-only contributors | Contributors create non-authoritative proposals; one authoritative writer validates, selects, and performs the sole mutation. |
| shared mutation | Allowed only when effective version/conflict control, ownership, isolation, and recovery are verified at reliance time. Without that evidence, serialize or redesign the work. |

No worker may concurrently mutate the same authoritative state under ambiguous ownership. Parallel direct-main repository writes are not authorized by this proposal. Under the current accepted repository protection state, routine, parallel, automated, and AFK repository writes remain unauthorized.

A parallel plan names the aggregation owner, branch membership, required versus optional results, dependencies, exact output/evidence expectations, side-effect domains, conflict policy, stop propagation, partial-result policy, integration subject, and local/integrated validation.

At join, the aggregation owner:

1. freezes or otherwise identifies the considered result set without choosing a mechanism;
2. accounts for every declared branch as present, missing, failed, cancelled, partial, stale, or excluded;
3. verifies exact result identities, authority, required local validation, baseline freshness, side effects, and dependency satisfaction;
4. rejects or escalates conflicting ownership, overlapping mutation, unresolved invariant violations, and ambiguous external effects;
5. distinguishes an optional omission with a legitimate rationale from a required missing result;
6. forms one exact integration subject and evaluates the integrated-verification gate for that subject;
7. when the gate is required, runs the required integrated verification and records its current pass, failure, or stale/pending state; when a governing rule makes it not applicable, records that rule and rationale without claiming a pass;
8. records join pass only after that gate is effective; otherwise records or retains the applicable pending, partial, failed, or conflicted non-success state plus the safe next action.

A required missing, failed, stale, conflicted, or uncontained result prevents join pass. Required integrated verification that is pending, failed, stale, conflicted, missing, or omitted without a legitimate not-applicable decision also prevents join pass. A failed required integrated verification makes the join failed for that integration subject; stale or pending verification leaves it non-passing until current evidence supports reevaluation. Candidate formation, completion, disposition, or other downstream success may not rely on a non-passing join. If a passed join's integration subject or relied-upon evidence later changes or becomes stale, the pass is invalid for reliance and the join returns to pending until reevaluated.

Partial outputs may be retained as evidence or inputs only if the task owner explicitly reframes their permitted use; partial never silently becomes complete. Optional results may be omitted only under the declared rule and are recorded as omitted or not applicable, never passed. A failed branch does not require discarding sound independent results, but carrying them forward requires exact identity, impact analysis, and a new authorized integration plan.

## Reconstructable evidence

Evidence is sufficient when an authorized fresh actor can reconstruct the relied-upon claim and distinguish fact, inference, decision, and unresolved uncertainty. Depending on context, record:

- authority source, grant, actor/role, applicable approval, and effective time;
- task, operation, candidate, baseline, dependency, configuration, and environment identities actually relied upon;
- expected versus observed preconditions;
- reads, writes, external calls, publications, privilege use, and other material side effects;
- progress milestones and current owner;
- inputs and outputs with integrity/provenance appropriate to reliance;
- resource consumption and ceiling state when relevant to safety or authorization;
- verification criteria, method, result, and limitations;
- review subject, independence basis, findings, and verdict;
- failures, exceptions, retries, deduplication/version keys, and reconciliation;
- stop and cancellation requests, acknowledgements, containment observations, residual effects, and recovery;
- redaction, access, retention, and evidence-integrity decisions where relied upon.

Evidence is expectation-checked: a trace or named actor is not trusted solely because it exists. Capture only what is needed; do not record secrets or unnecessary sensitive payloads. This design sets no product, schema, sampling policy, protection mechanism, or universal retention duration.

## Stop, cancellation, containment, retry, and recovery

Mandatory stop triggers include authority loss or ambiguity; stale or unverifiable relied-upon state; unexpected scope or content; conflicting mutable owners; required scope expansion; ceiling breach or inability to observe a ceiling; verification failure that invalidates safe continuation; unplanned shared mutation; ambiguous or consequential external effect; secret exposure; inability to preserve required evidence; missing required dependency; cancellation request from an authorized owner; or any condition the task contract names.

For a generic stop trigger, the actor stops initiating new effects, preserves evidence, reports the last known safe state, identifies in-flight operations and affected domains, moves `task control` from `active` to `blocked`, and leaves the cancellation plane unchanged. This local stop is not an acknowledgement or containment claim. If an authorized owner requests cancellation, or in-flight operations require cancellation to establish a safe boundary, the separate cancellation transition sets `cancellation=requested`; absent that authority, the task remains blocked and escalates. Emergency containment allowed by the task contract may proceed, but no new remediation or rollback authority is inferred.

Cancellation is a protocol:

- request changes `task control` to `blocked` and `cancellation` from `none` to `requested`, and records desired scope, operations, and domains;
- acknowledgement changes only `cancellation` from `requested` to `acknowledged`, proves every relevant controller received and acted on the request, and still means containment is unverified;
- containment verification changes only `cancellation` from `acknowledged` to `contained` or `residual-effects` after observing that further effects have ceased or are boundedly isolated across every relevant domain; unobserved, continuing, or ambiguously bounded effects leave it `acknowledged` and blocked;
- reconciliation and authorized recovery use the recovery plane while retaining the cancellation value, and determine completed, partial, duplicated, queued, published, or ambiguous effects; if containment establishes a new recovery obligation while recovery is `recovered`, **begin recovery or reconciliation** explicitly opens a new episode under the reopening guard, without resumption or an implicit reset;
- recovery or compensation occurs only with authority and operation-specific evidence; successful conclusion returns task control to `blocked` with recovery `recovered`; whenever accountable intervention is required, the separate intervention transition instead records `task control=blocked; recovery=intervention-required` and the explicit next-action rules apply; neither outcome directly resumes, completes, or cancels the task;
- resumption is a separate authorized transition that requires verified containment and completed required recovery when applicable, then applies the common resumption reset rule used by both cancellation and non-cancellation resumption: `task control=active; cancellation=none; recovery=not-applicable`, retaining historical records and residual obligations;
- terminal cancellation is a separate closure decision by the authorized task/execution-control owner after verified containment and terminal accounting, recorded in task control by the designated run/task execution-state owner; residual effects also require completed accountable handling and risk disposition;
- abandonment is a separate task-contract-owner decision, recorded in task control by the designated run/task execution-state owner, available only with no active work and no hidden active or uncontained effects; it cannot bypass cancellation, recovery, or residual-effect obligations.

Request, acknowledgement, containment, recovery, terminal cancellation, and abandonment are separate decisions. Request or acknowledgement alone permits neither `task control=cancelled`, resumption, completion, nor release of resources needed for containment or reconciliation. Containment uncertainty remains `cancellation=acknowledged`; it fails closed until observation proves containment or an accountable owner resolves the state. `cancellation=residual-effects` identifies verified containment with durable effects still requiring assigned handling; it is not a synonym for containment uncertainty or recovery completion.

Before retry, classify the operation as safely repeatable, conditionally repeatable with stable identity/deduplication/version precondition, compensatable but not reversible, irreversible, nondeterministic, or ambiguous. Use the applicable safeguards and verify prior effects. Ambiguous completion blocks blind retry. A compensation is a new authorized effect and does not claim the previous reality was restored.

Recovery succeeds only when the authoritative state owner validates the resulting state against an authorized target, all side effects and evidence are reconciled to the required degree, and residual risk is accepted or escalated. While authorized work toward that target can safely continue, the listed recovery-action transitions apply. If a required accountable decision prevents continuation or validated conclusion, **require accountable intervention** records `task control=blocked; recovery=intervention-required`, with cancellation unchanged and the explicit next-action rules above. An unsuccessful or unvalidated attempt cannot be recorded as recovered.

## Qualitative proportionality

The task-contract or governance owner tailors representation, durability, review formality, independence, integrated verification depth, evidence protection, recovery planning, and intervention using:

- consequence and downstream reliance;
- uncertainty, novelty, coupling, and conflict exposure;
- reversibility and ambiguity of side effects;
- privilege and sensitivity;
- affected users, systems, repositories, policy, and scope;
- cross-session duration and number of coordinating actors;
- applicable safety, legal, regulatory, or organizational governance.

Low-consequence, local, reversible, well-understood work may combine records and use lightweight feedback. Higher-consequence, uncertain, privileged, external, irreversible, parallel, or cross-session work requires more explicit and durable boundaries.

The following invariants do not disappear through proportionality: current authority; one mutable owner; bounded scope; observable success; honest gate applicability; no omission-as-pass; immutable identity when formal review/acceptance relies on content; freshness at state-dependent transitions; failure visibility; no self-acceptance; no false independence; side-effect accounting; stop/escalation on authority conflict or unsafe ambiguity; and no unattended authority by implication.

## Unattended and AFK boundary

Workflow v1 design itself grants no unattended, AFK, automated-write, privileged, destructive, or externally consequential execution authority. Consequential work remains subject to task-specific evidence, authorization, and later verification of the selected mechanism and its effective configuration.

Before unattended operation may even be considered, the accountable risk owner must have current evidence, as applicable, for:

- bounded task authority and exact allowed actions;
- fresh baseline, inputs, dependencies, identities, and effective configuration;
- isolated or enforceably controlled read/write and side-effect domains;
- per-task least privilege and secret handling;
- semantic safety of repeated, partial, delayed, reordered, and ambiguous effects;
- enforceable resource, time, privilege, mutation, and external-effect ceilings;
- reconstructable observability and evidence protection;
- tested cancellation acknowledgement and verified-containment behavior;
- operation-aware retry, reconciliation, recovery, and residual-risk handling;
- reachable accountable intervention and a defined safe state when intervention is unavailable.

These categories are necessary, not sufficient. If any applicable category is missing, stale, unverified, or only asserted by the proposed mechanism, eligibility is denied. Passing the screen creates no authority; a separate explicit task-specific authorization and any applicable governance decision are still required. No numeric eligibility threshold or categorical safe task class is created.

## Failure and escalation behavior

| Condition | Required state and response |
|---|---|
| stale baseline or critical identity | invalidate the dependent gate; stop dispatch, join, publication, review, acceptance, or resumption; reread and reframe impact |
| authority conflict or two mutable owners | block mutation; preserve evidence; escalate to the accountable owner for an explicit ownership decision |
| failed verification | verification failed; do not promote, join-pass, or accept on that basis; required integrated failure makes that integration subject's join failed; correct, reframe, waive only through an authorized exception, or stop |
| review rejection | review rejected for the exact subject; correct and create a new identity if content changes, reframe, explicitly defer/reject, or use a separately authorized exception |
| missing required parallel result | join partial or failed, never passed; account for the branch and either recover, reauthorize a reduced outcome, or stop |
| failed required branch | join failed unless the task owner explicitly reframes dependencies; unaffected results remain proposals/evidence until authorized reuse |
| partial completion | label partial; identify satisfied and unsatisfied obligations, side effects, and safe next action; no completion claim |
| material candidate correction | supersede prior candidate for current consideration; create new identity; rerun affected verification and applicable review |
| ambiguous external effect | stop new effects and set `task control=blocked`; if cancellation is requested, remain `cancellation=requested` until acknowledged and then `acknowledged` until containment is verified; inspect and reconcile before retry or disposition |
| failed or incomplete containment | remain `task control=blocked` and `cancellation=acknowledged`; deny completion, resumption, terminal cancellation, abandonment, resource release, and unattended continuation; escalate |
| unreconciled side effects | retain `cancellation=residual-effects`; **begin recovery or reconciliation** explicitly enters assessment, including from `recovered` when the new-episode reopening guard is satisfied; authorized assessment/reconciliation uses `task control=recovering` and the applicable recovery value; if accountable intervention is required, use **require accountable intervention** to record `task control=blocked; recovery=intervention-required`; do not claim rollback, recovery, successful cancellation, completion, or abandonment |
| inaccessible required evidence | dependent gate unsatisfied or invalid; preserve available evidence and escalate |
| ceiling breach | stop new effects, request/verify containment, record exposure, and require accountable recovery decision |
| secret or sensitive-data exposure | stop affected flow, contain access where authorized, preserve secret-safe evidence, and escalate under the responsible security owner |
| unexpected scope expansion | block and return to framing/authorization; no executor may ratify the expansion |
| disagreement that does not affect an owned state | record uncertainty and continue only if the task contract permits; otherwise escalate before reliance |

No failure, omission, timeout, silence, or unavailable evidence defaults to success.

## Later-stage boundary and DR-005 handoff

Until later disposition, all design decisions in this proposal remain proposal state. Byte-exact persistence would create a candidate identity only; independent review, design disposition, normative adoption, and baseline acceptance would still be separate.

Only an explicit later adoption decision naming the target normative owner, scope, exact design identity, and faithful materialization can make Workflow v1 normative. Project repositories continue to own project-specific architecture, product state, risk constraints, acceptance conditions, side-effect semantics, and operating rules. Post-v1 evidence may refine ceremony cost, retention policy, and domain-specific controls without silently amending the adopted workflow.

If the initial tool-agnostic design is later dispositioned and the Research Register dependency plus an explicit research gate are satisfied, DR-005 may evaluate mechanisms against these requirements:

- represent orthogonal lifecycle planes and conditional gate outcomes without omission-as-pass;
- enforce or reliably evidence one mutable owner, explicit ownership transfer, and current authoritative pointers;
- pin and reverify relied-upon identity and effective configuration at state-dependent transitions;
- express context-scaled task/delegation authority, least privilege, ceilings, stopping, and escalation;
- preserve immutable candidates and bind verification/review/acceptance records to exact identities;
- support isolated work, version/conflict control for shared mutation, single aggregation ownership, full join accounting, and partial/failure states;
- support fresh-context rehydration from authoritative sources and detect stale or conflicting state;
- produce protected, secret-safe, reconstructable evidence with appropriate integrity, access, redaction, and retention controls;
- distinguish stop request, acknowledgement, verified containment, residual effects, and accountable intervention;
- support operation-aware stable identifiers, deduplication/version preconditions, retry, reconciliation, compensation, and recovery;
- enforce unattended-operation ceilings and denial when necessary evidence or control effectiveness is incomplete;
- verify authentication, authorization, approval, actor/configuration identity, provenance, review independence, and correctness as distinct claims.

DR-005 must test actual availability and effective configuration at the point of reliance. It may compare tools and mechanisms but may not redefine accepted workflow semantics by convenience. This handoff does not start DR-005 and selects no tool.

## Conformance scenarios

| Scenario | Required resolution |
|---|---|
| conditional gate legitimately omitted | A reversible local documentation correction has no governing requirement for independent review. The task/governance owner records review applicability as not-applicable with the contextual rule and rationale. The review plane is not-applicable, never passed; verification and any required acceptance remain separate. |
| gate falsely claimed passed | An executor labels an independent-review gate passed using their own producer check. The subject lacks a conflict-free review record. The claimed pass is invalid, the review remains required-pending, and disposition is blocked. |
| stale state before transition | A task was authorized against baseline A, but live reread before dispatch resolves baseline B or a changed effective control. Dispatch is denied; prior authorization remains historical, impact is assessed, and the task returns to framing or reauthorization. |
| parallel join missing a required result | Three branches are declared required; two pass locally and one is missing. The aggregator records complete branch accounting and join partial or failed. It cannot produce join passed. A reduced outcome requires explicit reframing and authorization. |
| required integrated verification fails | All required branches pass local verification, but the exact composed integration subject fails its required integrated verification. The integration owner records verification failed and join failed; candidate formation, completion, and downstream success cannot rely on that join. |
| required integrated verification passes | All required branches and dependencies are current and acceptable, conflicts and side effects are reconciled, and required integrated verification passes for the exact composed subject. The integration owner may record join passed with the branch identities and verification evidence. |
| integrated verification legitimately not applicable | A governing contextual rule makes integrated verification not applicable for the exact integration subject. The integration owner records the integrated-verification gate outcome as not-applicable with the rule and rationale; the verification plane remains not-invoked rather than passed, omission is not silent, and the join may pass only if every other required input is satisfied. |
| material candidate correction | Review finds a changed interface contract. The correction changes candidate content and a load-bearing integration assumption. The prior identity and verdict remain historical; a new immutable identity is created, affected local/integration checks rerun, and applicable independent review is renewed. |
| generic stop without cancellation | A mandatory stop trigger occurs during active work without a cancellation request. Task control changes to blocked, cancellation remains none, new effects stop, and the actor escalates; no acknowledgement or containment is inferred. |
| cancellation requested but not acknowledged | An authorized owner requests cancellation for identified operations. State becomes `task control=blocked; cancellation=requested`; absent acknowledgement, containment, resumption, completion, terminal cancellation, abandonment, and release of containment-critical resources are denied. |
| cancellation acknowledged but containment not verified | Every relevant controller acknowledges receipt and action, but an external publication may still be queued. State is `task control=blocked; cancellation=acknowledged`; no retry, resumption, completion, terminal cancellation, abandonment, resource release, or unattended continuation occurs until observation verifies containment. |
| containment verified and cancellation closes | Every affected domain is observed, further effects have ceased or are boundedly isolated, no residual effect requires handling, and terminal accounting is complete. Cancellation changes to contained; on explicit terminal-closure authority from the task/execution-control owner, the designated run/task execution-state owner may record terminal task control cancelled while retaining containment evidence. |
| residual effects delay terminal cancellation | Containment is verified, but a publication already occurred. Cancellation becomes residual-effects; the designated run/task execution-state owner records recovery/reconciliation using the side-effect owner's decisions and evidence. Terminal cancellation remains denied until handling, durable ownership and obligations, validation, and accountable residual-risk disposition are complete. |
| cancellation reopens recovery before resumption | Episode A validates repair of a published result against its authorized target and **conclude recovery** records `blocked/none/recovered` (task control/cancellation/recovery). No resumption occurs. Authorized **request cancellation** → `blocked/requested/recovered`; **acknowledge cancellation** → `blocked/acknowledged/recovered`; **verify containment** finds further effects contained but identifies a newly required compensating withdrawal → `blocked/residual-effects/recovered`. The withdrawal obligation arose after A completed and has fresh operation-specific evidence, a side-effect owner, bounded authority, and a validation target. Terminal cancellation is denied while it remains unsatisfied. The designated run/task execution-state owner records **begin recovery or reconciliation**, satisfying the reopening guard → episode B at `recovering/residual-effects/assessment`, with a distinct identity and a durable link to A; A remains complete and its evidence historical. **Authorize recovery action** → `recovering/residual-effects/reconciling`; **record recovery action** with withdrawal evidence → `recovering/residual-effects/compensated`; validated withdrawal, completed required reconciliation, and residual-risk disposition permit **conclude recovery** → `blocked/residual-effects/recovered` for B. Only then, with terminal accounting and separate terminal-closure authority, may **close cancelled** → `cancelled/residual-effects/recovered`. A retained recovered value cannot discharge B; an implementation that lacks explicit reopening, infers a reset, rewrites A as failed, or closes cancellation before B is satisfied is nonconforming. |
| intervention-required exit | An authorized non-cancellation recovery is in `task control=recovering; cancellation=none; recovery=reconciling`. Attempt evidence exposes ambiguous prior effects that cannot be resolved within current authority. **Require accountable intervention** records `task control=blocked; cancellation=none; recovery=intervention-required`, evidence gaps, affected obligations, and the accountable state/side-effect decision owner; human/risk-owner authority is required for the consequential decision. Execution and blind retry cannot continue. If that owner supplies fresh evidence and authorizes a bounded reconciliation attempt satisfying **begin recovery or reconciliation**, the recorder changes the state to `task control=recovering; cancellation=none; recovery=assessment`. If no such decision is available, it remains `blocked/none/intervention-required` and escalated. Neither path infers recovery success. |
| repeated non-cancellation recovery | Starting at `active/none/not-applicable` (task control/cancellation/recovery), an independent recoverable failure invokes **apply generic stop** → `blocked/none/not-applicable`; authorized **begin recovery or reconciliation** → `recovering/none/assessment`; operation-specific **authorize recovery action** → `recovering/none/retry-authorized`; **record recovery action** → `recovering/none/reconciling`; authoritative validation and **conclude recovery** → `blocked/none/recovered`. Ordinary authorized resumption applies the common reset in that transition → `active/none/not-applicable`, with the first episode's evidence retained. A later independent recoverable failure repeats **apply generic stop** → `blocked/none/not-applicable` and a new authorized **begin recovery or reconciliation** → `recovering/none/assessment`. The second cycle is permitted by the explicit source values; retaining `recovered` on resumption is nonconforming. |
| explicit abandonment | The task-contract owner decides a blocked bounded objective will not continue. No work is active, cancellation is none or containment is verified, and any residual effect has completed accountable handling; the designated run/task execution-state owner records terminal task control abandoned, decision owner, rationale, retained outputs/effects, obligations, and successor or no-successor decision. |
| fresh-context rehydration | A new executor receives a summary plus pointers. It reads the task-contract owner, resolves the exact baseline and dependencies, rereads current cancellation and verification state, and detects a stale summary. Authoritative state controls; the corrected safe next action is recorded before resumption. |
| unattended evidence incomplete | A proposed unattended mutation has bounded scope and logs, but cancellation containment has not been tested and privilege ceilings are not enforceably verified. Necessary evidence is incomplete, so unattended eligibility is denied. No manual success or tool capability overrides the denial. |
| optional parallel result omitted | A branch declared optional under a recorded rule yields no result. The join records the omission and rationale as omitted or not applicable, not passed. Join may pass only if all required results are satisfied and the integrated-verification gate is required-and-passed or legitimately not applicable with a recorded rationale. |
| ambiguous retry | An external operation timed out after dispatch and lacks a stable deduplication key. Completion is ambiguous, so blind retry is blocked; the side-effect owner must reconcile or authorize a different recovery action. |
| executor proposes scope expansion | Execution exposes an additional repository requiring mutation. The executor stops and returns to framing; the original authorization cannot be stretched to cover the new repository. |
| carried-forward evidence after correction | A candidate wording-only correction leaves executable content and criteria unchanged. Impact analysis identifies the exact unaffected checks and assumptions. Only supported evidence carries forward; the new candidate still receives a new identity and any review whose target changed is reevaluated for applicability. |

These scenarios are conformance obligations: an implementation that cannot represent the required non-success and not-applicable states is nonconforming.

## Traceability to accepted dispositions

| Design decisions | Accepted controlling inputs |
|---|---|
| DD-001, DD-002 | DR-001 R1, R4; DR-002 R6; DR-003 PR07 |
| DD-003, DD-010 | DR-001 R2, R7, R12; DR-002 R7; DR-003 PR04, PR05, PR06 |
| DD-004, DD-006 | DR-002 R1–R5 |
| DD-005, DD-009 | DR-001 R3, R9, R10; DR-003 PR02, PR07 |
| DD-007 | DR-001 R11; DR-003 PR01, PR11 |
| DD-008 | DR-002 R3, R5; DR-003 PR03, PR04 |
| DD-011 | DR-003 PR09, PR10 |
| DD-012 | DR-001 R5, R6, R8; DR-002 R9 |
| DD-013 | DR-003 PR08, PR09, PR10, PR11 |
| DD-014 | DR-001 qualifications and later dependencies; DR-002 qualifications; DR-003 PR12 |

The controlling disposition records are ADW-DR-001-DISPOSITION-001 and ADW-DR-002-003-DISPOSITION-001. This mapping carries their accepted scopes and qualifications, not the full research recommendations or overbroad interpretations they excluded.

## Unresolved and deferred items

| Item | Classification and blocking effect | Owner or later gate |
|---|---|---|
| candidate persistence, exact commit identity, independent review, design disposition, normative adoption, and baseline acceptance | pending lifecycle gates, not unresolved design; they block their respective later claims but do not block candidate content readiness | separately authorized repository persistence, review, coordinator/accountable-human disposition, adoption, and acceptance owners |
| concrete artifact schemas and packet formats | mechanism deferred; non-blocking because the required semantic information and ownership are defined | DR-005 or later explicitly adopted implementation design |
| tracker, storage, synchronization, logging, tracing, identity, credential, attestation, orchestration, queue, worktree, isolation, and automation choices | mechanism/tooling deferred; non-blocking for tool-agnostic design | DR-005 after its dependency and explicit gate |
| effective enforcement controls and branch protection alternatives | current repository restriction remains controlling; future mechanism evidence is non-blocking for this proposal but blocks modes that depend on it | applicable governance owner and DR-005; accepted bootstrap protection decision remains unchanged |
| context-specific review invocation, risk acceptance, ceilings, retention, and recovery parameters | project/task policy inputs; non-blocking because decision owners and qualitative semantics are defined; absence at execution blocks the affected gate | accountable project/task/risk owner under later adopted policy |
| project-specific side-effect classifications, acceptance criteria, architecture, and operating rules | intentionally project-specific; non-blocking for cross-project design, required before affected execution | applicable project repository or system owner |
| empirical optimization of ceremony cost and generally applicable retention periods | post-v1 research; non-blocking | later explicit research/adoption gates |
| identity and effective-configuration mechanism validation | deferred enforcement work; non-blocking for design and blocking for any transition that proposes to rely on an unverified control | DR-005 and the accountable control owner |

There are no blocking unresolved design semantics. The remaining items are explicit later gates, mechanism choices, or project-specific parameters. Two competent implementers can derive the same required behavior: where a mechanism or contextual parameter is absent, the corresponding relied-upon transition remains blocked rather than being invented.

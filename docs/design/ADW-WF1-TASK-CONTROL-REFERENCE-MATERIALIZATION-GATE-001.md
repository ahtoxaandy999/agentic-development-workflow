---
id: ADW-WF1-TASK-CONTROL-REFERENCE-MATERIALIZATION-GATE-001
artifact: materialization-gate
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-gate
decision: authorize-one-non-operative-task-control-reference-materialization-with-ru1-evidence
selected_artifact_path: docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md
ru1_selection_ref: docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-RU1-SELECTION-001.md
gate_subject_main: 01b9165e6003519cf6892b436a693e6137204bf8
decided_on: 2026-09-06
normative_effect: none
supersedes: null
---

# Workflow v1 task-control reference materialization gate

## Result

**AUTHORIZE BOUNDED TASK-CONTROL REFERENCE MATERIALIZATION**

Decision:

`authorize-one-non-operative-task-control-reference-materialization-with-ru1-evidence`

Authorize one future bounded local production task to create:

1. one annotated, non-operative Markdown task-control reference;
2. one minimum task-local producer-verification evidence package structured
   using the accepted producer-verification evidence reference; and
3. one RU-1 utility-observation record.

The task-control reference is the sole proposed repository artifact. Evidence
and utility observations remain local working output unless a later exact-base
gate separately authorizes their repository persistence.

This gate does not itself execute production, create output, authorize a
candidate, persist anything, perform review, accept the result or make Workflow
v1 normative.

## Exact live basis

Connected `@GitHub` read-only verification established:

- repository: `ahtoxaandy999/agentic-development-workflow`;
- live `main`: `01b9165e6003519cf6892b436a693e6137204bf8`;
- sole parent: `12d9d38d53b00ec495486f2a8b9d758a1955d228`;
- live tree: `d9f1c7d74f0765b9f3faaf4c4ae70c673de9df7b`;
- Research Register blob:
  `395322a9119cb8812f37c823580e68a4b76fec22`;
- both current Register gates:
  `Workflow v1 task-control reference materialization authorization gate`;
- RU-1 selection blob:
  `64db1fd4626317a98ab309907b0cb1478b781ebb`;
- branch `protected: false`, embedded protection `enabled: false`, and
  required status-check enforcement `off`.

The selected destination
`docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md` is absent at live main.
No competing current task-control reference was found in connected repository
search.

## Controlling inputs

The exact accepted bases are:

- Workflow v1 tooling design:
  `docs/design/ADW-WF1-TOOLING-DESIGN-001.md`, blob
  `2e0c640e8cab61b0bf165712c27e02ff9a455ec6`;
- tooling-design disposition:
  `docs/design/ADW-WF1-TOOLING-DESIGN-DISPOSITION-001.md`, blob
  `d029e25406442ff5a44768c06e88333f6e1cd779`, decision
  `accept-initial-tooling-enforcement-design`;
- gate-evaluation reference:
  `docs/design/ADW-WF1-GATE-EVALUATION-REFERENCE-001.md`, blob
  `5c08148db6f0d96197b268c3567a15a4981aff81`;
- gate-evaluation reference disposition blob:
  `2586fe5919df18e215008be026dd412ba2f66454`;
- producer-verification evidence reference:
  `docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-001.md`,
  blob `36240635b1fab86052964c4f3a779555e05b81d9`;
- producer-verification reference disposition:
  blob `ef9e99dd062e8bae6c6419a31153b68086854b5a`, decision
  `accept-producer-verification-evidence-reference-as-explanatory-design-basis`;
- representative-use scoping blob:
  `edd7d1f48f6a785102e3d810e2c70ad1c150ca2d`;
- RU-1 selection blob:
  `64db1fd4626317a98ab309907b0cb1478b781ebb`;
- DR-005 disposition blob:
  `70cea63938bf4a8b908904d2b9c7b0c9aec1b401`.

The tooling design and its disposition determine semantics. The
gate-evaluation reference determines gate interpretation. The
producer-verification evidence reference guides evidence representation. This
gate only authorizes one local materialization task.

## Gate assessment

Can a competent producer create one explanatory task-control reference from
the accepted tooling design while using the accepted evidence reference for
RU-1 without inventing an operative schema, product context, new mechanism or
authority?

**YES, within the bounded contract below.**

- **Design sufficiency — PASS.** TD-01 through TD-10 define owner placement,
  representation, exact identity, evidence, lifecycle, recovery, dependency
  and gate semantics.
- **RU-1 selection — PASS.** The persisted selection binds one
  documentation-oriented artifact and no other output.
- **Non-operative boundary — PASS.** An annotated explanatory reference can
  show semantic slots and examples without adopting field syntax or creating a
  task instance.
- **Evidence-use boundary — PASS.** The accepted producer-verification
  reference can structure task-local verification without becoming a schema or
  state owner.
- **Mechanism boundary — PASS.** No conditional/deferred mechanism is needed.
- **Contextual-value boundary — PASS.** Product, actor, permission, custody,
  retention and runtime values can remain visibly fictional or be supplied
  only by the later execution grant.
- **RG compatibility — PASS.** Unresolved gaps can remain explicit denials and
  prerequisites.
- **Authority boundary — PASS.** Local production can stop before candidate
  persistence, review, disposition or operational use.

## Authorized artifact

The sole proposed repository artifact is:

`docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md`

Recommended metadata:

```yaml
---
id: ADW-WF1-TASK-CONTROL-REFERENCE-001
artifact: design-reference
artifact_status: draft
owner: chatgpt-coordinator
authority: explanatory-design-reference
tooling_design_ref: docs/design/ADW-WF1-TOOLING-DESIGN-001.md
gate_evaluation_reference_ref: docs/design/ADW-WF1-GATE-EVALUATION-REFERENCE-001.md
producer_verification_reference_ref: docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-001.md
materialization_gate_ref: docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-MATERIALIZATION-GATE-001.md
ru1_selection_ref: docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-RU1-SELECTION-001.md
produced_on: 2026-09-06
normative_effect: none
supersedes: null
---
```

The artifact must not contain a competing current gate or mutable project
status. The Research Register remains the ADW current-gate owner.

## Required reference content

The reference must include:

### A. Authority and non-authority

- explanatory, non-operative and non-normative status;
- no actual task, adopted schema, parser, validator, recorder or runtime;
- no authorization derived from completing or copying an example;
- controlling precedence of the accepted tooling design.

### B. Owner map

For every mutable domain identified in the accepted tooling design, show one
sole current placement and the authority allowed to supply a decision or
observation:

- contract and readiness;
- authorization;
- execution/task-control progress;
- work product;
- verification;
- review;
- disposition;
- cancellation;
- recovery;
- decomposition/dependencies/join;
- product continuation gate;
- normativity;
- baseline acceptance;
- external side-effect observations.

The example must not let an Issue, chat, runner, evidence manifest or task file
independently own the same current field.

### C. Annotated fictional control projection

Provide one readable Markdown example using visibly fictional placeholders. It
must illustrate semantic slots for:

- task, contract revision and current control revision;
- exact authorized base and bounded authority;
- current run/operation/attempt where applicable;
- separate orthogonal state planes;
- exact W, C and I references without implicit promotion;
- current evidence, review and disposition references;
- cancellation and recovery episode references;
- decomposition snapshot and dependency/join accounting;
- current product continuation gate;
- immutable transition history pointers.

Field names and layout must be labelled illustrative. They are not an adopted
serialization or compatibility contract.

### D. Immutable/current split

Explain which facts belong in immutable contract revisions, authorization
records, transition events, evidence manifests, review records, disposition
records and recovery episodes, versus the single mutable current projection.

Corrections require successor identities. Historical facts and failed/stale
episodes are not rewritten.

### E. Update responsibilities and lifecycle

Explain:

- one named recorder updates the current projection only on supplied authority;
- decision owners retain their domains;
- evidence producers do not gain decision authority;
- every update rereads the current owner and prior control revision;
- unsupported transitions and material scope drift fail closed;
- candidate persistence, review, disposition, adoption and baseline acceptance
  remain separate.

### F. Exact identity and freshness

Explain exact B/W/C/I relationships, complete repository identity tuples,
criteria/configuration/dependency freshness and wrong-subject invalidation.
Branch names, PR state, green checks and human-readable status are
insufficient.

### G. Gate and obligation semantics

Incorporate the accepted gate-evaluation reference by pointer and explain:

- required versus not-applicable;
- passed versus unsatisfied;
- missing/skipped/failed/stale versus pass;
- legitimate N/A without pass credit;
- permitted destinations only from effective gate decisions.

Do not duplicate or redefine the gate-evaluation reference as a competing
owner.

### H. Cancellation and recovery

Show separate request, acknowledgement, containment, residual-effect,
recovery-episode, intervention, reset/resumption and terminal-guard references.
Do not collapse cancellation into recovery or treat a stopped process as
contained.

### I. Decomposition and join

Show one immutable decomposition snapshot, required/optional dependency
accounting, exact child-result references and one join decision. Missing
required results and failed integrated verification deny downstream success.
No parallel execution is enabled.

### J. Rehydration

Define pointer-based rehydration from repository authority: exact repository
and ref, task/control revision, controlling contract and authorization, current
plane references, unresolved obligations and product next gate. Chat and
memory remain navigation aids only.

### K. Denied transitions and unresolved inputs

List failures caused by missing authority, stale base, wrong subject, unknown
permissions/effects, unsafe evidence, unavailable custody, unresolved
containment/recovery, missing dependency results, absent independent review or
missing acceptance.

### L. Fictional walkthroughs

Include at least:

1. framed to ready;
2. ready to authorized;
3. authorized to active;
4. W verification without candidate promotion;
5. exact candidate publication;
6. changed C invalidating review/evidence;
7. failed required obligation;
8. legitimate N/A;
9. cancellation with incomplete containment;
10. recovery episode before resumption;
11. missing required dependency at join;
12. rehydration from exact pointers.

Every example must remain visibly fictional and must state what it cannot
authorize.

### M. RG, DI and adoption boundaries

Carry RG1 through RG12 as unresolved. Preserve DI-1 and DI-2. State that
Workflow v1 remains unadopted and that this reference selects no optional tool
or integration.

## Local production outputs

The later execution grant may authorize one isolated output root containing
only:

- the proposed task-control reference at its repository-relative path;
- one task-local producer-verification evidence package;
- one RU-1 utility-observation record;
- temporary files strictly required for deterministic checks, removed before
  completion.

The exact absolute output root, evidence paths, named producer/verifier,
supervisor, custodian, escalation owner, runtime and retention/retrieval
requirements must be supplied by the execution grant.

No repository checkout or Git metadata may be modified during local
production.

## Producer-verification contract

Producer verification must use the accepted evidence reference as explanatory
guidance and cover at least:

- exact controlling source identities and local output inventory;
- metadata and serialization;
- presence and consistency of sections A through M;
- unique owner placement for each mutable domain;
- orthogonal state-plane coverage;
- immutable/current separation;
- exact B/W/C/I semantics and stale invalidation;
- required/N/A and gate semantics;
- cancellation/recovery separation;
- dependency/join denial behavior;
- pointer-based rehydration;
- all twelve fictional walkthroughs;
- explicit non-schema, non-operative, non-normative and non-authority wording;
- RG1-RG12 and DI-1/DI-2 preservation;
- absence of product, actor, permission, custody or retention invention.

The evidence package must record actual method, results, limitations, payload
identities, producer/verifier, authority and custody facts supplied by the
execution grant. Missing required evidence remains non-passing.

Producer checks are not independent review and cannot accept the artifact.

## RU-1 utility observations

The local utility record must capture:

- fields that still required clarification;
- omissions caught before review;
- evidence-representation-related review findings, initially `not yet
  reviewed`;
- approximate duplicated prompt/reference material avoided;
- ambiguity, maintenance cost or ceremony introduced;
- unused, unclear or insufficient reference sections;
- a provisional conclusion: useful, inconclusive or not useful.

The provisional conclusion cannot close RU-1. Final RU-1 assessment occurs
only after candidate review/disposition or earlier abandonment.

## Acceptance test for the produced reference

Two competent later implementers given the accepted tooling design and the
produced reference must derive the same initial semantic task-control
representation without inventing material intent about:

- current owner placement;
- immutable versus mutable content;
- state-plane separation;
- exact B/W/C/I relationships;
- evidence, review and disposition references;
- cancellation/recovery;
- dependency/join accounting;
- gate and N/A semantics;
- rehydration;
- denied transitions.

They must also be unable to honestly interpret the reference as an operative
schema, actual task instance, selected recorder implementation, authorization,
Workflow v1 adoption or permission for routine/parallel/automated/AFK work.

## Lifecycle and stop boundary

gate persistence
→ fresh bounded local production
→ producer verification and RU-1 observations
→ coordinator assessment of production result
→ separate exact-base candidate-persistence gate
→ immutable candidate
→ fresh independent candidate review
→ correction/new candidate if required
→ coordinator candidate disposition
→ RU-1 utility assessment
→ only then decide whether to select RU-2

No step is automatic. Local production stops before any repository write.

## RG and design-impact boundaries

RG1 through RG12 remain unresolved. Missing applicable assurance fails closed.
This gate supplies no branch protection, writer fencing, publication
enforcement, reviewer identity, permission proof, cancellation/containment
control, durable recovery mechanism, custody guarantee, installed-capability
proof, optional integration selection, documentation resolution or AFK
control.

DI-1 is preserved: all accepted state planes and legitimate N/A remain
distinct.

DI-2 is preserved: freshness, stale-subject invalidation, operation-aware
retry, containment, durable recovery history, reopening, resumption/reset and
terminal guards are not weakened.

## Non-goals

This gate does not authorize:

- repository or GitHub modification;
- candidate persistence, review, disposition or acceptance;
- an actual product task or operative `control.md`;
- a schema, parser, validator, recorder, generator or automation;
- installation or configuration;
- product dogfooding;
- RU-2 selection;
- routine, direct-main, parallel, automated, unattended or AFK work;
- Workflow v1 adoption;
- RG resolution or a new baseline.

## Intended Register transition after gate persistence

A later separately authorized persistence task should:

- add a pointer to
  `docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-MATERIALIZATION-GATE-001.md`;
- record task ID
  `ADW-WF1-TASK-CONTROL-REFERENCE-MATERIALIZATION-GATE-001`;
- record decision
  `authorize-one-non-operative-task-control-reference-materialization-with-ru1-evidence`;
- record authorized artifact
  `docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md`;
- preserve all controlling identities and restrictions;
- change both current next-gate fields to
  `Workflow v1 task-control reference bounded materialization execution`.

It must not invent production, evidence, candidate, review or utility status.

## Next gates

Immediate next gate:

`Workflow v1 task-control reference materialization gate persistence`

Recommended post-persistence gate:

`Workflow v1 task-control reference bounded materialization execution`

## Explicit non-actions

This gate did not:

- modify GitHub, the repository or Research Register;
- create the task-control reference, evidence package or utility record;
- run the persistence checker;
- execute RU-1 or select RU-2;
- install or configure tooling;
- change protection or permissions;
- authorize routine, parallel, automated, unattended or AFK work;
- adopt Workflow v1;
- resolve RG1 through RG12;
- establish a baseline.

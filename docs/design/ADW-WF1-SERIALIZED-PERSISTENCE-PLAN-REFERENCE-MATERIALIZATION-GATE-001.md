---
id: ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-MATERIALIZATION-GATE-001
artifact: materialization-gate
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-gate
decision: authorize-one-non-operative-serialized-persistence-plan-reference-materialization
selected_artifact_path: docs/design/ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-001.md
scoping_ref: docs/design/ADW-WF1-TOOLING-NEXT-MATERIALIZATION-SCOPING-002.md
gate_subject_main: c7abdf8fe3cf63e558a66c4670ae462dedc44c90
decided_on: 2026-09-06
normative_effect: none
supersedes: null
---

# Workflow v1 serialized persistence plan reference materialization gate

## Result

**AUTHORIZE ONE NON-OPERATIVE SERIALIZED-PERSISTENCE PLAN REFERENCE MATERIALIZATION**

Decision:

`authorize-one-non-operative-serialized-persistence-plan-reference-materialization`

Authorize one future bounded local production task to create one annotated,
human-readable Markdown reference for planning supervised serialized
repository persistence:

`docs/design/ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-001.md`

The reference may consolidate already accepted exact-base, identity, delta,
commit, guarded-publication, readback, failed-attempt and stop-boundary
semantics. It may not create new selection intent, operative syntax, execution
authority or a competing current-state owner.

This gate does not create the reference, persist a candidate, update the
Research Register, authorize a repository write, perform independent review,
accept the future artifact or make Workflow v1 normative.

## Exact live basis

Connected `@GitHub` read-only verification established:

- repository: `ahtoxaandy999/agentic-development-workflow`;
- live `main`: `c7abdf8fe3cf63e558a66c4670ae462dedc44c90`;
- sole parent: `a7b789ee717aa60f11c00bb6e67047c112b0da86`;
- live tree: `dee0425ad4388347a6f8b7ec226c32d5ff2a3d21`;
- commit message: `docs: persist second tooling materialization scoping`;
- parent comparison: one commit ahead, zero behind, exactly two changed paths;
- Research Register blob:
  `9d6a7cbac9ec375aa063ca5f066166a47f410b00`;
- both mutable Register gates:
  `Workflow v1 serialized persistence plan reference materialization authorization gate`;
- scoping record:
  `docs/design/ADW-WF1-TOOLING-NEXT-MATERIALIZATION-SCOPING-002.md`,
  blob `0a8164e59951bec76e9dc0f1de5f3e4f514e2af6`;
- branch `protected: false`, embedded protection `enabled: false`, and required
  status-check enforcement `off`.

The selected destination is absent at live main. No competing current
serialized-persistence plan reference was found in the inspected repository
owners.

## Controlling inputs

The materialization is bound to:

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
- producer-verification evidence reference:
  `docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-001.md`, blob
  `36240635b1fab86052964c4f3a779555e05b81d9`;
- task-control reference:
  `docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md`, blob
  `1968993da7dded58d70d705ef3d23165667e94b4`;
- DR-005 disposition:
  `docs/research/ADW-DR-005-DISPOSITION-001.md`, blob
  `70cea63938bf4a8b908904d2b9c7b0c9aec1b401`;
- controlling scoping decision:
  `propose-serialized-persistence-plan-reference-as-next-bounded-materialization`.

The accepted tooling design and its disposition own the architecture. The
existing references own their explanatory scopes. The Research Register owns
mutable repository gate state. This gate owns only the authorization contract
for one local materialization task.

## Gate assessment

Can a competent producer create one coherent explanatory serialized-
persistence plan reference from the accepted inputs without inventing material
intent, choosing a new mechanism or relaxing an accepted boundary?

**YES, within the bounded contract below.**

- **Accepted design basis — PASS.** The accepted tooling design already
  defines the exact-base serialized write path and its identity/evidence
  obligations.
- **Persisted scoping — PASS.** The current Register points to the exact
  scoping decision and the selected destination.
- **Independent usefulness — PASS.** Repeated bounded persistence assignments
  demonstrate a stable recurring contract whose explanatory consolidation can
  reduce duplicated prose and clarification loops.
- **Representation sufficiency — PASS.** Existing accepted references provide
  enough semantics to describe the plan without an operative schema.
- **Mechanism boundary — PASS.** No helper, generator, parser, skill, hook,
  Action, runner or new integration is needed.
- **Context boundary — PASS.** Repository, candidate, actors, permissions,
  ceilings and custody remain task-specific supplied facts, not defaults.
- **Gap compatibility — PASS.** RG1 through RG12 can remain unresolved as
  explicit prerequisites, procedural limitations and denied modes.
- **Authority boundary — PASS.** Local production can stop before candidate
  persistence, review, disposition, representative use or automation.

## Authorized artifact

The sole future repository candidate is:

`docs/design/ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-001.md`

Recommended metadata:

```yaml
---
id: ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-001
artifact: design-reference
artifact_status: draft
owner: chatgpt-coordinator
authority: explanatory-design-reference
tooling_design_ref: docs/design/ADW-WF1-TOOLING-DESIGN-001.md
gate_evaluation_reference_ref: docs/design/ADW-WF1-GATE-EVALUATION-REFERENCE-001.md
producer_verification_reference_ref: docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-001.md
task_control_reference_ref: docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md
scoping_ref: docs/design/ADW-WF1-TOOLING-NEXT-MATERIALIZATION-SCOPING-002.md
materialization_gate_ref: docs/design/ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-MATERIALIZATION-GATE-001.md
produced_on: 2026-09-06
normative_effect: none
supersedes: null
---
```

The future producer may refine descriptive headings but may not change the
artifact's authority, scope, selected path or non-operative status.

## Required reference content

### A. Authority and status

The reference must state that it is explanatory, non-operative and
non-normative. It must identify the accepted tooling design as controlling and
must not claim that completing or copying its example grants authority.

It must distinguish:

- a reusable fixed planning meaning;
- task-specific authority and contextual facts;
- execution evidence;
- immutable candidate identity;
- independent review;
- coordinator disposition;
- normative adoption.

### B. Required task-specific inputs

The reference must require explicit supply of:

- repository and exact target ref;
- exact full base commit, base tree and current authoritative owner identities;
- source W path, class, bytes, SHA-256, Git blob, mode and serialization;
- exact destination and its required absence or replacement authority;
- complete allowed path set and exact delta semantics;
- exact Register before/after constraints when applicable;
- named executor, coordinator/serialization controller, supervisor and
  evidence custodian;
- permitted effects, ceilings, stop boundary, retry status and next gate.

Unknown values fail closed. Examples must use conspicuously fictional values
and may not supply permissive defaults.

### C. Preflight plan

The reference must cover:

- fresh connected-`@GitHub` verification for acceptance-sensitive dispatch;
- native remote freshness immediately before local mutation and push;
- exact origin, checkout, clean index/worktree and one-worktree checks;
- unfinished Git operation and lock checks;
- exact Register and controlling-artifact identities;
- source identity, destination and competing-owner checks;
- explicit sole-writer declaration plus stop on contrary evidence.

Procedural exclusivity must not be described as technical writer fencing.

### D. Preparation and candidate construction

The reference must require:

- byte-for-byte persistence of an accepted source unless rewriting is
  explicitly authorized;
- exact permitted modes and serialization;
- complete before/after inventories and changed-path classification;
- bounded Register reconstruction and exact occurrence checks;
- unchanged controlling-artifact verification;
- whitespace/error checking appropriate to the artifact class;
- no inference of review or acceptance from local preparation;
- exact commit count, message, sole parent and resulting tree identity.

Silent rebase, replay, merge, amend, adaptation, repair or scope expansion is
forbidden.

### E. Guarded publication

The reference must explain:

- publication requires a separate explicit write grant;
- expected-old-SHA lease binds the authorized base;
- remote movement causes stop without push;
- only the authorized push-attempt count may be used;
- no retry is inherited from an earlier grant;
- a safety-layer request after commit creation is a separate incomplete
  execution episode and requires an exact-commit confirmation;
- an unpushed local commit is not a published candidate.

The reference must not present direct-main publication as routine or safe merely
because the branch is currently unprotected.

### F. Readback and result

The reference must require verification of:

- live remote ref, fetched ref and local HEAD equality;
- exact commit, tree, ordered parent, message and full changed-path set;
- modes, blobs, byte counts, digests and serialization;
- exact Register transition and preserved controlling identities;
- final clean checkout;
- result as PASS, BLOCKED or UNEVALUABLE;
- explicit non-actions and exact next gate.

Candidate creation remains evidence only. It does not imply independent review,
disposition, adoption or operational readiness.

### G. Failure, interruption and correction

The reference must preserve separate execution episodes and require fail-closed
behavior for:

- stale authority or remote drift;
- ambiguous or conflicting owner state;
- unknown or competing writer;
- unsafe or mismatched source/destination;
- incomplete delta or Register reconstruction;
- publication failure or inconsistent readback;
- unavailable evidence required for the current transition.

It must distinguish preparation, push attempt and readback. A later grant may
authorize only the exact precreated commit push or may require a new corrected
candidate. Reviewed immutable candidates are never amended, and prior failed
or interrupted episodes are not rewritten as successful.

### H. Compact annotated handoff

The reference must include one compact, human-readable example containing:

- a clearly fictional planning block;
- preflight facts;
- complete allowed delta;
- commit and guarded-push contract;
- readback contract;
- denied actions;
- result fields;
- stop boundary and next-gate field.

The example is not an adopted schema, compatibility grammar, executable prompt
or authorization. It must be usable by pointer while leaving task-specific
values visible.

### I. Utility hypothesis

The reference must state a falsifiable hypothesis that its use should:

- materially shorten repeated persistence prompts;
- reduce missing identities, occurrence constraints and stop rules;
- reduce clarification loops and duplicate safety-layer wording;
- preserve or improve reviewability and failure visibility.

Any later utility assessment must also count ceremony, lookup burden,
task-specific fields that remain unavoidable and errors caused by compression.
No helper selection follows automatically from success.

## State ownership

The reference may own fixed explanatory meanings only. It must not own:

- the Research Register current gate;
- task authorization, readiness or mutable control state;
- repository branch or writer state;
- W/C/I lifecycle status;
- verification, review or disposition decisions;
- cancellation or recovery state;
- external side-effect state;
- normativity or baseline acceptance.

Task records, chats, prompts, runner state and evidence reports may point to
owners but cannot independently own the same current field.

## Acceptance test for the produced reference

The future materialization is ready for candidate persistence only if two
competent coordinators or executors, given the same task facts and the produced
reference, can derive the same bounded supervised persistence contract without
inventing material intent about:

- exact base and freshness;
- owner and writer separation;
- W, C and publication identity;
- complete path/delta scope;
- Register transition;
- commit and push ceilings;
- safety-layer and retry episode handling;
- readback evidence;
- denied modes and stop conditions;
- review, disposition and next-gate separation.

It must be impossible to honestly interpret the reference as an operative
schema, automatic publisher, generic write authorization, selected helper or
permission for routine/parallel/automated/unattended/AFK operation.

Producer checks are not independent review. Candidate persistence, fresh
independent review and coordinator disposition remain separate.

## RG and design-impact boundaries

RG1 through RG12 remain unresolved. The reference may identify procedural
checks and missing prerequisites but cannot claim that it supplies branch
protection, writer fencing, integration publication guarantees, reviewer
identity, cross-surface permissions, cancellation containment, durable
recovery, evidence custody, installed capability verification, optional
integration leverage, documentation disambiguation or AFK end-to-end control.

Missing enforcement must fail closed for the affected action.

DI-1 remains preserved: authorization, execution, verification, review,
disposition, normativity, baseline acceptance, cancellation, recovery and join
remain orthogonal; legitimate N/A is not pass.

DI-2 remains preserved: freshness, operation-aware retry, containment/recovery
separation, durable episode history, qualified reopening, intervention,
resumption/reset and independent terminal guards are not weakened.

## Explicit non-goals

The future materialization must not create or authorize:

- an operative JSON/YAML schema or compatibility contract;
- a script, validator, generator, custom skill, hook, Action, runner, SDK
  client, planner or publisher;
- automatic Register edits, commit creation, push or retry;
- persistence-checker invocation, modification or operational reliance;
- actual task records, candidates, fixtures, reports or product operations;
- routine, parallel, automated, unattended or AFK execution;
- a product dogfooding task or RU-2 selection;
- protection or permission changes;
- Workflow v1 normative adoption;
- resolution of RG1 through RG12;
- a new accepted baseline.

## Production execution contract

After this gate is durably persisted, one fresh bounded production task may:

1. reread the exact persisted gate and controlling inputs;
2. create only the proposed Markdown reference in a designated local output
   root;
3. perform producer structural, traceability and consistency checks;
4. serialize as UTF-8 without BOM, LF-only, exactly one final LF;
5. report absolute path, bytes, SHA-256, Git blob and mode;
6. stop before repository persistence.

The execution task must not create a repository copy, Register delta, commit,
push, review, disposition, utility claim or tooling implementation.

## Intended Register transition after gate persistence

A later separately authorized exact-base persistence task should add exactly
one durable pointer set equivalent to:

```yaml
workflow_v1_serialized_persistence_plan_reference_materialization_gate: docs/design/ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-MATERIALIZATION-GATE-001.md
workflow_v1_serialized_persistence_plan_reference_materialization_gate_task_id: ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-MATERIALIZATION-GATE-001
workflow_v1_serialized_persistence_plan_reference_materialization_gate_decision: authorize-one-non-operative-serialized-persistence-plan-reference-materialization
workflow_v1_serialized_persistence_plan_reference_selected_path: docs/design/ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-001.md
```

It should update both mutable current gates to exactly:

`Workflow v1 serialized persistence plan reference materialization execution`

It must preserve all accepted artifact identities and dispositions, RU-1 as
completed/useful-with-moderate-ceremony, RU-2 as deferred/unselected with its
slot unused, RG1 through RG12 unresolved, DI-1 and DI-2, Workflow v1's
non-normative/unadopted/unimplemented status and all current write/AFK
restrictions.

The Research Register remains the sole repository owner of mutable current
gate and materialization-selection state.

## Lifecycle and next gate

The bounded sequence is:

materialization authorization
→ gate persistence
→ fresh bounded local reference production
→ immutable candidate persistence
→ fresh independent review
→ coordinator disposition
→ bounded representative-use/utility assessment
→ only then reconsider one small helper if evidence justifies it.

No step is automatic, and design acceptance does not require later
implementation.

Immediate next gate:

`Workflow v1 serialized persistence plan reference materialization gate persistence`

Recommended post-persistence gate:

`Workflow v1 serialized persistence plan reference materialization execution`

## Explicit non-actions

This gate did not:

- modify GitHub, the repository or Research Register;
- create or persist the proposed reference;
- execute a persistence operation or the persistence checker;
- create a schema, helper, generator, validator or automation;
- perform independent review or coordinator acceptance of a candidate;
- select or consume RU-2;
- change protection or permissions;
- authorize routine, parallel, automated, unattended or AFK work;
- adopt Workflow v1;
- resolve RG1 through RG12;
- establish a baseline.

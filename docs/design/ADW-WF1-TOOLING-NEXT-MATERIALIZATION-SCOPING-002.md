---
id: ADW-WF1-TOOLING-NEXT-MATERIALIZATION-SCOPING-002
artifact: implementation-materialization-scoping
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-scoping
decision: propose-serialized-persistence-plan-reference-as-next-bounded-materialization
proposed_artifact_path: docs/design/ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-001.md
scoping_subject_main: a7b789ee717aa60f11c00bb6e67047c112b0da86
decided_on: 2026-09-06
normative_effect: none
supersedes: null
---

# Workflow v1 next tooling/enforcement materialization scoping 002

## Result

**PROPOSE ONE NON-OPERATIVE SERIALIZED-PERSISTENCE PLAN REFERENCE**

Decision:

`propose-serialized-persistence-plan-reference-as-next-bounded-materialization`

The next smallest independently useful materialization is one annotated,
non-operative Markdown reference for planning bounded serialized repository
persistence. Its purpose is to replace repeated bespoke explanations of the
same exact-base, identity, delta, commit, guarded-push, readback and stop
boundaries with stable pointers while preserving task-specific authority.

Proposed repository artifact:

`docs/design/ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-001.md`

This scoping does not authorize production or persistence of that reference,
does not create an operative schema, generator or runner, and does not grant a
repository write. A separate materialization authorization gate is required.

## Live and authoritative basis

Connected `@GitHub` was used read-only at this scoping gate.

Verified current state:

- repository: `ahtoxaandy999/agentic-development-workflow`;
- live `main`: `a7b789ee717aa60f11c00bb6e67047c112b0da86`;
- live tree: `32bdc38c6f54fd3da428aa3080fcdbd25226807f`;
- sole parent: `9da8c4ad04176db44bd1bb065250d92db53cc231`;
- branch `protected`: `false`;
- Research Register blob:
  `f4d838e93038131c2ae6828c9af991a9819ab99e`;
- both current mutable gates:
  `Workflow v1 tooling/enforcement next materialization scoping gate`;
- RU-1 status: completed;
- RU-1 result: `useful-with-moderate-ceremony`;
- RU-2 status: `deferred-unselected`;
- RU-2 slot: unused;
- proposed scoping destination
  `docs/design/ADW-WF1-TOOLING-NEXT-MATERIALIZATION-SCOPING-002.md`
  was absent.

No current repository artifact was found that owns a compact reusable
serialized-persistence plan representation. Existing gate and task-control
references provide controlling semantics but do not provide one concise
handoff-oriented planning reference.

## Controlling accepted inputs

This proposal remains within the accepted initial tooling architecture:

- tooling design:
  `docs/design/ADW-WF1-TOOLING-DESIGN-001.md`, blob
  `2e0c640e8cab61b0bf165712c27e02ff9a455ec6`;
- tooling disposition:
  `docs/design/ADW-WF1-TOOLING-DESIGN-DISPOSITION-001.md`, blob
  `d029e25406442ff5a44768c06e88333f6e1cd779`, decision
  `accept-initial-tooling-enforcement-design`;
- gate-evaluation reference blob:
  `5c08148db6f0d96197b268c3567a15a4981aff81`;
- producer-verification evidence reference blob:
  `36240635b1fab86052964c4f3a779555e05b81d9`;
- task-control reference blob:
  `1968993da7dded58d70d705ef3d23165667e94b4`;
- DR-005 disposition blob:
  `70cea63938bf4a8b908904d2b9c7b0c9aec1b401`.

The accepted design already specifies the narrow serialized path: exact live
base, single-parent bounded delta, one writer, guarded publication, exact
readback, independent review and separate disposition. This scoping proposes
only a reusable explanation of that path.

## Evidence of present need

The completed ADW materialization lifecycles repeatedly required the same
manual information:

- repository, exact full base SHA, parent tree and current Register blob;
- exact source and destination identities and serialization;
- destination absence and competing-owner checks;
- an exact allowed-path set and bounded Register transition;
- commit message, sole-parent rule and expected-old-SHA lease;
- stop-on-drift behavior and post-publication readback;
- explicit separation of persistence from review, acceptance and the next
  gate.

The repeated assignments also exposed predictable friction:

- long prompts restating identical safety semantics;
- manual occurrence and Register-reconstruction instructions;
- confusion between preauthorized persistence and a later safety-layer request
  to confirm the exact already-created commit;
- execution contexts that can use native Git but cannot independently access
  connected `@GitHub`;
- duplicated reporting fields across otherwise routine two-file persistence
  tasks.

This is sufficient evidence for a compact explanatory reference. It is not
sufficient to select a machine-readable schema, script, custom skill, hook,
generator, task runner or automated publisher.

## Why this slice is next

The proposed reference has independent project value:

- coordinators can form shorter pointer-based persistence assignments;
- executors can distinguish immutable task authority from task-specific
  supplied values;
- reviewers can compare an execution report against one stable checklist of
  semantic obligations;
- correction loops can preserve exact commit episodes without rewriting the
  original authorization;
- later automation research can measure a stable manual baseline instead of
  inferring one from heterogeneous prompts.

It is smaller and safer than implementing a persistence planner or extending
the checker. It introduces no new effect surface and does not require an
operative task-control schema.

It is also independently useful from RU-2. The choice was not optimized to
create a qualifying code/test case. RU-2 remains deferred and unused.

## Proposed artifact objective

The later reference should let two competent coordinators or executors derive
the same bounded serialized-persistence contract from the same task facts,
without inventing authority about:

- exact live base and authoritative current owner;
- source W and destination path;
- candidate C identity created by publication;
- allowed complete path/delta set;
- exact Register transition where applicable;
- sole writer and serialization ownership;
- preflight, commit, guarded push and readback obligations;
- safety-layer confirmation and failed-attempt episode accounting;
- stop conditions, correction rules and next-gate separation.

The reference should reduce duplicated prose without concealing required
task-specific values or turning defaults into authority.

## Required content of the later reference

The materialization authorization gate should require at least:

### A. Authority and status

- explanatory, non-operative and non-normative status;
- controlling precedence of the accepted tooling design and current task gate;
- no authority created by copying or completing an example;
- Research Register and applicable task owner remain the mutable owners.

### B. Required task-specific inputs

- repository and target ref;
- exact full base commit, parent/tree and current owner identities where
  material;
- exact source path/class/bytes/SHA-256/Git blob/serialization;
- exact destination and required absence or replacement authority;
- complete allowed path set and delta semantics;
- exact Register before/after constraints where applicable;
- named executor, coordinator/serialization owner, supervisor and evidence
  custodian;
- permitted effects, ceilings, stop boundary and next gate.

Every contextual value must be supplied by its accountable owner. A field left
unknown does not inherit a permissive default.

### C. Preflight

- fresh connected-`@GitHub` read for acceptance-sensitive dispatch facts;
- native remote Git freshness immediately before local mutation and push;
- origin, checkout, clean index/worktree, single worktree and unfinished
  operation/lock checks;
- exact current Register and controlling artifact identities;
- destination and competing-owner checks;
- sole-writer declaration plus contrary-evidence stop.

The reference must distinguish procedural exclusivity evidence from technical
writer fencing. RG1 and RG2 remain unresolved.

### D. Preparation and verification

- byte-for-byte source persistence unless rewriting is explicitly authorized;
- exact permitted modes and serialization;
- complete before/after inventories and changed-path set;
- bounded Register reconstruction and occurrence checks;
- unchanged controlling-artifact checks;
- `git diff --check` or an explicitly justified equivalent;
- no candidate, review or acceptance inference from local preparation.

### E. Commit and guarded publication

- exactly authorized commit count and message;
- exact sole parent; no silent rebase, replay, merge, amend or scope repair;
- one expected-old-SHA lease attempt when explicitly authorized;
- stop without push when remote moved;
- separate accounting when a safety layer requires a new exact-commit
  confirmation after commit creation;
- no retry unless a new operation/attempt is explicitly authorized.

### F. Readback and outcome

- live remote ref, fetched ref and local HEAD equality;
- exact commit, tree, parent, message, modes, blobs, bytes and full delta;
- exact Register current-state transition;
- clean final checkout;
- PASS, BLOCKED or UNEVALUABLE stated without treating partial progress as
  publication;
- new candidate identity is evidence only, not review or acceptance.

### G. Failure and correction behavior

- drift, conflict, unknown writer, unsafe source, unavailable authority or
  inconsistent readback fail closed;
- an unpushed local commit is a retained failed/incomplete execution episode,
  not a published candidate;
- a new authorization may permit only the exact precreated commit push or may
  require a new corrected identity;
- reviewed immutable candidates are never amended;
- prior attempts remain visible and are not rewritten as successful.

### H. Compact handoff form

Provide an annotated, human-readable example with visibly fictional values and
a short required-output form. The example may name semantic fields but must be
labelled illustrative, not an adopted machine schema or compatibility
contract.

## Utility and later automation boundary

The later reference should carry a falsifiable utility hypothesis:

- reduce repeated persistence-prompt prose materially;
- reduce missing exact identities, occurrence constraints and stop rules;
- reduce coordinator/executor clarification loops;
- preserve equal or better reviewability and failure visibility.

Any representative-use assessment must also count ceremony, reference lookup,
task-specific fields that remain necessary and errors introduced by
compression.

Only after repeated use demonstrates a stable compact contract and a material
manual deficit may a separate gate reconsider D3 scripts/custom skills or a
small deterministic preparation helper. That later gate must choose one exact
effect boundary and independently justify whether to extend the existing
checker or create another component. This scoping makes neither choice.

## State ownership

The proposed reference owns only fixed explanatory meanings. It must not own:

- the Research Register current gate;
- a product task's current control projection;
- repository branch state;
- source W or candidate C lifecycle status;
- review or disposition state;
- current writer/executor status;
- external side-effect state.

Chats, prompts, runner state and helper reports remain derived evidence or
navigation. They cannot independently own the same current field.

## RG and design-impact boundaries

RG1 through RG12 remain unresolved. The reference supplies none of their
missing technical controls. In particular it cannot prove protection, writer
fencing, publication atomicity, reviewer identity, cross-surface permissions,
custody, installed capability or AFK safety.

DI-1 remains preserved: authorization, execution, verification, review,
disposition, normativity, baseline acceptance, cancellation, recovery and join
remain orthogonal; legitimate N/A is not pass.

DI-2 remains preserved: exact-subject freshness, operation-aware retry,
containment/recovery separation, durable episode history, qualified reopening,
intervention, resumption/reset and terminal guards are not weakened.

## Explicit non-goals

This scoping does not authorize or create:

- the proposed persistence-plan reference;
- an operative schema, JSON/YAML contract or compatibility grammar;
- a script, helper, generator, validator, custom skill, hook, Action, task
  runner, SDK client or publisher;
- automatic Register edits, commit creation or push;
- routine, direct-main, parallel, automated, unattended or AFK work;
- persistence-checker invocation or extension;
- a product task, dogfooding execution or RU-2 selection;
- Workflow v1 normative adoption;
- resolution of RG1 through RG12;
- a new accepted baseline.

## Intended Register transition after scoping persistence

A later separately authorized exact-base persistence task should add:

- `workflow_v1_tooling_next_materialization_scoping_002`:
  `docs/design/ADW-WF1-TOOLING-NEXT-MATERIALIZATION-SCOPING-002.md`;
- `workflow_v1_tooling_next_materialization_scoping_002_task_id`:
  `ADW-WF1-TOOLING-NEXT-MATERIALIZATION-SCOPING-002`;
- `workflow_v1_tooling_next_materialization_scoping_002_decision`:
  `propose-serialized-persistence-plan-reference-as-next-bounded-materialization`;
- `workflow_v1_serialized_persistence_plan_reference_proposed_path`:
  `docs/design/ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-001.md`.

It should preserve RU-1 as completed, RU-2 as deferred/unselected with its
slot unused, and all accepted artifact identities and authority restrictions.
It should update both current mutable `next_gate` values to:

`Workflow v1 serialized persistence plan reference materialization authorization gate`

It must not create the proposed reference, select a helper, authorize a write
procedure, change Workflow v1 adoption, resolve an RG gap or establish a new
baseline.

The Research Register remains the sole repository owner of mutable current
gate and materialization-selection state.

## Lifecycle and next gate

The bounded continuation is:

next-materialization scoping
→ scoping persistence
→ persistence-plan reference materialization authorization gate
→ separate local reference production
→ candidate persistence
→ fresh independent review
→ coordinator disposition
→ bounded utility assessment
→ only then reconsider a small helper if evidence justifies it.

No step is automatic.

Immediate next gate:

`Workflow v1 tooling/enforcement next materialization scoping 002 persistence`

Recommended post-persistence gate:

`Workflow v1 serialized persistence plan reference materialization authorization gate`

## Explicit non-actions

This scoping did not:

- modify GitHub, the repository or Research Register;
- create or authorize the proposed reference;
- create an implementation, schema, helper or automation;
- run or modify the persistence checker;
- select or consume RU-2;
- change protection or permissions;
- authorize routine, parallel, automated, unattended or AFK work;
- adopt Workflow v1;
- resolve RG1 through RG12;
- establish a baseline.

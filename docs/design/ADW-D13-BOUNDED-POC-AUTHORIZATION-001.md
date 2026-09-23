---
id: ADW-D13-BOUNDED-POC-AUTHORIZATION-001
artifact: coordinator-pilot-authorization
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-decision
repository: ahtoxaandy999/agentic-development-workflow
subject_main: 2bc213c857e6e3713b881470408dbe429906f68a
subject_tree: e949379234c3e745db579b40e2958d5facbdb32e
subject_register_blob: dbad679389ce09c79a79cf9c23ff8b3255664428
scoping_ref: docs/design/ADW-D13-CONFORMANCE-EVIDENCE-ACQUISITION-SCOPING-001.md
selected_profile_repository: ahtoxaandy999/housing-recovery
observed_profile_main: 01b3ae5288069660a12c6b35254e4fa59867429e
decided_on: 2026-09-23
human_signal: "++"
decision: conditionally-select-task-local-python-github-graphql-cas-for-one-bounded-d13-poc-and-authorize-implementation-preflight-candidate-production
d13_status: CONDITIONALLY SELECT FOR ONE BOUNDED POC
d5_status: CONFIRM DEFER
x3_status: CONFIRM REJECT
pilot_execution_authorized: false
housing_mutation_authorized: false
credential_creation_authorized: false
implementation_preflight_authorized: true
conformance_result: not-established
normative_effect: none
supersedes: null
---

# D13 bounded conformance-evidence PoC authorization

## Decision

`conditionally-select-task-local-python-github-graphql-cas-for-one-bounded-d13-poc-and-authorize-implementation-preflight-candidate-production`

For the exact Housing profile and scoping contract already accepted, conditionally
select one mechanism for one bounded D13 proof of concept:

- a supervised task-local deterministic Python runtime;
- a separate deterministic privileged publisher;
- GitHub GraphQL `createCommitOnBranch` as the commit-mutation primitive on the
  dedicated pilot branch;
- provider-side exact-head fencing through required `expectedHeadOid`;
- writer generation bound to the pilot runtime subject and branch-head progression;
- a separate minimal Housing publisher credential available only to the publisher;
- a separate isolated Housing read-only reviewer credential;
- a local append-only evidence/recovery journal outside the governed repositories.

D13 current status becomes:

**CONDITIONALLY SELECT FOR ONE BOUNDED POC**

for this exact mechanism/profile only.

D5 remains:

**CONFIRM DEFER**

X3 remains:

**CONFIRM REJECT**

This decision authorizes production of one exact implementation/preflight
candidate only. It does not yet authorize Housing mutation or pilot execution.

## Why selection is now permitted

The previously accepted D13 prerequisite design, readiness assessment and
evidence-acquisition scoping have now defined:

- authoritative state ownership;
- adapter/publisher separation;
- exact conformance evidence;
- writer fencing;
- side-effect receipts;
- reconciliation;
- mandatory positive/negative scenarios;
- reviewer capability isolation;
- evidence custody expectations;
- attempt/retry and stop boundaries.

The accepted scoping record names Housing as the representative profile and makes
the remaining mechanism decision explicit.

Human signal `++` accepted the mechanism decision above. That signal is bound to
this bounded PoC selection only. It is not merge acceptance for this repository
candidate and is not Housing execution authority.

## Selected runtime architecture

### Supervised task-local Python runtime

The orchestration control loop is a deterministic Python process used only for
this pilot.

It is not:

- a shared workflow engine;
- a daemon;
- a scheduler;
- a task database;
- a production service;
- an unattended agent runtime.

The runtime owns only the current pilot lifecycle projection described by the
accepted scoping contract.

The implementation is to be retained as exact byte-addressable pilot evidence,
not silently adopted as shared ADW tooling.

No third-party Python dependency is authorized by this decision. A later
implementation/preflight may use the standard library unless an explicit
evidence-backed need for another dependency is separately accepted.

### Privileged publisher

The publisher is a separate deterministic process/interface from the lifecycle
recorder.

Only the publisher receives the Housing write credential.

The runtime, executor role and independent reviewer do not receive that credential.

The publisher must:

1. verify the exact runtime subject;
2. verify the current writer generation;
3. verify target repository/ref/path allowlists;
4. verify exact expected branch head;
5. reject conflicting operation IDs;
6. invoke the selected provider mutation;
7. perform authoritative post-effect readback;
8. emit one durable effect receipt;
9. expose partial/unknown/residual effects for reconciliation.

A model response, prompt or remembered instruction is never a privileged write
authorization.

## Selected GitHub commit primitive

The selected commit mutation for an already-existing pilot branch is GitHub
GraphQL:

`createCommitOnBranch`

Current first-party GitHub documentation inspected on 2026-09-23 states that the
mutation appends a commit to a branch and that
`CreateCommitOnBranchInput.expectedHeadOid` is a required Git object ID
representing the head expected before the commit.

Reference:

https://docs.github.com/en/graphql/reference/commits#createcommitonbranch

This selection uses that documented exact-head precondition as the provider-side
compare-and-swap boundary.

Important qualification:

- `expectedHeadOid` fences the remote branch head;
- it does not by itself implement ADW writer-generation semantics;
- it does not by itself prove operation idempotency;
- it does not by itself contain arbitrary credential misuse;
- it does not replace the accepted publisher generation check, receipt,
  reconciliation or stop rules.

The implementation/preflight must verify the live GraphQL schema/capability again
before any effect.

If the documented/provider behavior is unavailable or materially different, the
pilot stops. No fallback mechanism is implicitly selected.

## Generation binding

The pilot generation is part of the exact runtime subject and every operation
request.

Each successful authorized pilot-branch commit advances the remote head and
records the current generation in pilot evidence.

A stale operation carries:

- a stale generation;
- and/or a stale `expectedHeadOid`.

The publisher must reject stale generation before effect where it can be known
locally, and the provider-side exact-head mutation must reject a stale remote head
at the effect boundary.

For a competing same-head attempt, at most one exact-head commit may succeed.
Every competing result must be read back and retained.

This is the selected proof strategy for S4. It must still be demonstrated in the
actual PoC; this decision does not claim the proof already exists.

## Credential boundary

The selected credential architecture is separation by role, not shared user
authentication.

### Publisher credential

A future publisher credential must:

- be a separate credential used only by the deterministic publisher;
- be limited to `ahtoxaandy999/housing-recovery`;
- have only the repository permissions required for the authorized pilot branch,
  draft PR setup/observation and Actions readback;
- have no administration, ruleset, secrets, workflow-definition or merge authority
  beyond what is strictly required by the exact later permission profile;
- never be written to logs, evidence, prompts or repository files;
- never be exposed to executor/reviewer contexts.

The exact credential product and effective permission set are not created or
assumed by this decision. They must be fixed and verified during implementation
preflight before any Housing effect.

### Reviewer credential

The reviewer uses a separate Housing credential/profile whose effective
capabilities are read-only for the pilot evidence and repository state.

It must not have:

- contents write;
- PR mutation;
- ready/merge;
- ruleset/protection mutation;
- publisher-secret access.

The later preflight must produce an effective permission proof suitable for S9.

### Current credential non-reuse

Existing broad local GitHub authentication is not automatically the selected
publisher or reviewer credential.

This decision authorizes no token creation, secret creation or credential
reconfiguration.

## Local evidence and recovery state

The selected evidence/state surface is a user-controlled local filesystem
workspace outside ADW and Housing Git repositories.

It must contain at minimum:

- `subject.json`;
- `state.json` as the current lifecycle projection;
- append-only `journal.ndjson`;
- `operations/`;
- `receipts/`;
- `recovery/`;
- `scenarios/`;
- exact retained implementation bytes;
- `MANIFEST.sha256`.

The journal and immutable receipts are historical evidence.

`state.json` is a projection and cannot override:

- GitHub truth;
- review truth;
- Product/coordinator authority;
- acceptance;
- conformance disposition.

The exact evidence root and custodian identity must be fixed in the later runtime
subject before any Housing effect.

## Housing effect boundary

This conditional selection inherits the accepted scoping boundary:

- dedicated branch:
  `pilot/d13-runtime-control-evidence-001`;
- one draft PR targeting `main`;
- inert marker:
  `docs/d13-runtime-control-evidence-pilot.md`;
- indirect Candidate verification workflow runs caused by opened/synchronize
  activity.

Forbidden:

- direct `main` mutation;
- merge;
- force push;
- ruleset/protection changes;
- workflow/verifier changes;
- canonical Housing data/application changes;
- production/user data;
- destructive cleanup.

Branch creation and draft-PR creation are privileged Housing effects. They remain
unauthorized until a later exact execution authorization binds the final runtime
subject and permission profile.

## What is authorized now

This decision authorizes exactly one local implementation/preflight candidate.

That candidate may, without Housing mutation:

1. create the task-local Python runtime and publisher implementation in a local
   evidence workspace;
2. create stdlib tests and scenario fixtures;
3. create subject/operation/receipt/journal schema implementations;
4. implement exact allowlists and fail-closed state transitions;
5. implement the GraphQL request builder for
   `createCommitOnBranch(expectedHeadOid)` without sending a mutation;
6. implement read-only GitHub reconciliation calls;
7. implement fault-injection controls locally;
8. record exact implementation bytes and SHA-256 digests;
9. define the exact proposed publisher/reviewer permission profiles;
10. produce a complete preflight report identifying unresolved credential or
    platform gaps.

It may use read-only live GitHub inspection to confirm repository state and
documented/API schema availability.

## What remains unauthorized

Until a later exact execution authorization:

- no Housing branch creation;
- no Housing commit mutation;
- no Housing draft PR creation;
- no GraphQL mutation;
- no credential/token creation;
- no new GitHub App;
- no workflow installation/change;
- no secret configuration;
- no reviewer mutation test;
- no fault injection against GitHub;
- no unattended execution;
- no automatic retry;
- no merge;
- no cleanup/deletion.

## Implementation/preflight candidate requirements

The candidate must make the later execution decision possible without inventing
material intent.

It must provide:

1. exact implementation files and digests;
2. exact Python/runtime versions;
3. exact runtime-subject schema;
4. exact operation/receipt schema;
5. exact generation transition logic;
6. exact target repository/ref/path allowlists;
7. exact GraphQL mutation document and variables shape;
8. tests demonstrating no mutation occurs in preflight mode;
9. synthetic stale-head, stale-generation, duplicate and contradictory-state
   tests;
10. restart/reconstruction tests using only durable local evidence;
11. exact publisher permission proposal;
12. exact reviewer read-only permission proposal;
13. exact evidence root and custodian;
14. exact scenario execution order;
15. exact branch/PR setup procedure;
16. exact fault-injection procedure;
17. exact stop/recovery owner;
18. a list of every remaining fact requiring live readback before execution.

No producer-green result from that candidate authorizes Housing effects.

## Execution authorization boundary

A later execution authorization is mandatory.

It must bind:

- exact Housing live base and tree;
- exact implementation digests;
- exact GraphQL capability readback;
- exact selected credential product(s);
- effective publisher permission profile;
- effective reviewer permission profile;
- exact local evidence root/custodian;
- exact branch/PR setup effects;
- exact scenario suite;
- exact attempts/recovery authority;
- exact independent reviewer identity/profile.

Only that later decision may authorize the first Housing mutation.

## D13 / D5 / X3 effect

### D13

Current D13 status changes from:

`CONFIRM DEFER`

to:

`CONDITIONALLY SELECT FOR ONE BOUNDED POC`

only for the exact selected Housing mechanism and evidence purpose in this record.

This is not:

- D13 conformance satisfaction;
- D13 general adoption;
- routine orchestration authority;
- multi-project authority;
- production authority.

### D5

D5 remains:

`CONFIRM DEFER`

No Codex SDK/App Server component is selected or authorized.

### X3

X3 remains:

`CONFIRM REJECT`

No Symphony/custom-harness default gains authority.

## Mechanisms explicitly not selected

This decision does not select:

- `gh-aw`;
- GitHub-native workflow/job orchestration as the control runtime;
- Claude Code Action;
- Codex GitHub Action;
- Codex SDK/App Server;
- Symphony;
- a persistent custom daemon;
- a shared task database;
- a local learned orchestrator.

Future comparison does not silently reopen this exact PoC mechanism once the
runtime subject is frozen.

## Acceptance and conformance boundary

A successful implementation/preflight is readiness evidence only.

A successful future PoC run would still be evidence only.

Neither establishes D13 conformance.

The accepted D13 conformance contract still requires:

- exact complete package;
- fresh independent review;
- no unresolved critical evidence gaps/residual effects;
- later accountable coordinator disposition.

`d13_conformance_result` therefore remains:

`not-established`

## Intended Register transition

After exact candidate review, coordinator/human acceptance and protected
publication of this authorization record, the Research Register should:

- retain the historical DR-006 disposition and its original decision scope;
- change current `d13_status` to
  `CONDITIONALLY SELECT FOR ONE BOUNDED POC`;
- retain `d5_status: CONFIRM DEFER`;
- retain `x3_status: CONFIRM REJECT`;
- add this authorization artifact/task/decision;
- record the selected Housing profile and task-local Python + GitHub GraphQL CAS
  mechanism;
- record `implementation_preflight_authorized: true`;
- record `pilot_execution_authorized: false`;
- record `housing_mutation_authorized: false`;
- record `credential_creation_authorized: false`;
- preserve `d13_conformance_result: not-established`;
- preserve the repository-wide current gate;
- set the D13-specific next gate to:

`D13 bounded PoC implementation/preflight candidate production gate`

## Next gate

After fresh independent review, coordinator/human acceptance, protected merge
publication and verified readback of this exact authorization candidate:

**D13 bounded PoC implementation/preflight candidate production gate**

That gate is local-only and read-only with respect to Housing.

No Housing effect is authorized until a later execution authorization accepts one
exact preflighted runtime subject.

## Explicit non-actions

This decision does not:

- mutate Housing;
- create branch/PR state;
- create credentials;
- install a GitHub App;
- execute GraphQL mutations;
- install workflows;
- run the PoC;
- establish conformance;
- reconsider D5;
- weaken X3;
- amend Workflow v1;
- accept a repository baseline;
- authorize unattended/AFK operation.

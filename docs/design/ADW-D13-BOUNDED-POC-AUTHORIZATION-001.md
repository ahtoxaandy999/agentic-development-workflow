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
decision: conditionally-select-task-local-python-single-publisher-lifetime-lock-github-graphql-cas-for-one-bounded-d13-poc-and-authorize-implementation-preflight-candidate-production
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
- exactly one credential-holding publisher process per pilot evidence root;
- a canonical POSIX lifetime lock held with Python stdlib `fcntl.flock` for the
  entire credential-bearing publisher process lifetime;
- a canonical generation record stored beside that lock, outside any repository
  worktree;
- GitHub GraphQL `createCommitOnBranch` as the commit-mutation primitive on the
  dedicated pilot branch;
- provider-side exact-head fencing through required `expectedHeadOid`;
- writer generation activated only by the lock-owning publisher after prior
  publisher cessation is established;
- a separate minimal Housing publisher credential available only to that
  lock-owning publisher;
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

Exactly one credential-holding publisher process may be active for the pilot
evidence root.

Before the process may receive or use the publisher credential for an operation,
it must own the canonical publisher lifetime lock:

`publisher.lock`

using Python stdlib `fcntl.flock(..., LOCK_EX | LOCK_NB)`.

The lock is held for the entire credential-bearing process lifetime. The
publisher must not release the lock and continue running with the credential.
Normal release is process termination/descriptor close. If the process is still
alive and the lifetime lock is not proven released, replacement is blocked.

The canonical lock and generation record are located in the selected local
evidence root, outside ADW, Housing and disposable worktrees.

The publisher must:

1. acquire and hold the canonical lifetime lock;
2. verify the exact runtime subject;
3. reread the canonical generation record while holding the lock;
4. verify the request generation equals that canonical current generation;
5. verify target repository/ref/path allowlists;
6. verify exact expected branch head;
7. reject conflicting operation IDs;
8. invoke the selected provider mutation;
9. perform authoritative post-effect readback;
10. emit one durable effect receipt;
11. expose partial/unknown/residual effects for reconciliation.

A model response, prompt, remembered instruction, stale workspace copy or mere
possession of the publisher credential is never a privileged write
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

The selected generation fence combines two independent conditions:

1. process-level stale-instance exclusion through the canonical publisher
   lifetime lock; and
2. provider-side exact-head compare-and-swap through `expectedHeadOid`.

The canonical current generation is not owned by a worktree or process-local
cache. It is stored in one canonical generation record in the local evidence
root and may be read or changed only while holding `publisher.lock`.

### Generation activation rule

Generation `N+1` may become current only after all of the following are true:

1. the prior publisher is proven ceased or otherwise contained;
2. its credential-bearing process no longer holds the canonical lifetime lock;
3. the replacement publisher exclusively acquires that same lock;
4. while holding the lock, it rereads the durable generation record and recovery
   history;
5. unresolved prior effects are reconciled or the transition remains blocked;
6. it atomically replaces the canonical generation record from `N` to `N+1`
   using write-to-temp + fsync + `os.replace`;
7. it reads the resulting generation record back before accepting any mutation
   request.

A local variable, stale workspace, chat state or copied `state.json` cannot
activate a generation.

The publisher must not decrement, reuse or overwrite a completed generation
identity. Recovery reopening creates new history; it does not rewrite old
generation evidence.

### Stale credential-holding publisher exclusion

The stale-instance case is defined explicitly.

If publisher instance `P1` still runs and still holds the prior valid publisher
credential, then either:

- `P1` still owns `publisher.lock`, in which case `P2` cannot activate a new
  generation and execution remains blocked; or
- `P1` no longer owns the lifetime lock, which is permitted only after `P1`
  has terminated/ceased as a credential-bearing publisher under this selected
  runtime contract.

Therefore generation `N+1` cannot become current while a live generation-`N`
credential-bearing publisher remains eligible to execute the mutation path.

A publisher process that loses the lifetime lock is not allowed to continue with
the credential. The exact implementation must fail closed and terminate before
any further provider call.

The implementation/preflight must demonstrate:

- a second publisher cannot acquire the lock while the first lives;
- generation cannot advance while the prior publisher holds the lock;
- after prior-process termination, the replacement can acquire the lock and
  advance generation exactly once;
- a stale generation request delivered after advancement is rejected from the
  canonical generation record before GraphQL mutation construction/sending;
- copied/stale worktree state cannot substitute for the canonical generation
  record.

This lifetime-lock behavior is part of the selected mechanism, not merely a
testing suggestion.

### Provider head fence

Within the currently active generation, every commit request additionally binds
the exact remote branch head through `expectedHeadOid`.

The publisher must verify the expected head by authoritative readback and pass
that same OID to `createCommitOnBranch`.

For competing same-head provider mutations, at most one exact-head commit may
succeed. Every result must be read back and retained.

`expectedHeadOid` does not replace the lifetime lock/generation authority.
The lifetime lock/generation authority does not replace provider exact-head CAS.
Both conditions are required.

### Recovery and replacement consequence

If prior publisher cessation cannot be established, replacement is not
authorized and generation cannot advance.

If the prior publisher is killed/crashes, kernel lock release is necessary but
not alone sufficient: the replacement must still reconcile prior operation
receipts and live GitHub state before generation activation.

This preserves the accepted containment/recovery distinction.

This is the selected proof strategy for S4. It must still be demonstrated in the
actual PoC; this decision does not claim the proof already exists.

## Credential boundary

The selected credential architecture is separation by role, not shared user
authentication.

The credential-bearing publisher is also constrained by the selected lifetime
lock contract above. Credential possession without ownership of the canonical
publisher lock and current canonical generation is insufficient authorization
under this PoC mechanism.

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
6. exact canonical `publisher.lock` and generation-record paths;
7. exact lifetime-lock acquire/hold/release/termination semantics;
8. atomic generation-record replacement and readback logic;
9. exact target repository/ref/path allowlists;
10. exact GraphQL mutation document and variables shape;
11. tests demonstrating no mutation occurs in preflight mode;
12. synthetic competing-publisher, stale-head, stale-generation, duplicate and
    contradictory-state tests;
13. tests proving a second publisher cannot acquire the lifetime lock while the
    first credential-bearing publisher remains alive;
14. tests proving generation cannot advance until prior publisher cessation and
    lock release are established;
15. restart/reconstruction tests using only durable local evidence;
16. exact publisher permission proposal;
17. exact reviewer read-only permission proposal;
18. exact evidence root and custodian;
19. exact scenario execution order;
20. exact branch/PR setup procedure;
21. exact fault-injection procedure;
22. exact stop/recovery owner;
23. a list of every remaining fact requiring live readback before execution.

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

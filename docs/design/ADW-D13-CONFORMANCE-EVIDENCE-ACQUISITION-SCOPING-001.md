---
id: ADW-D13-CONFORMANCE-EVIDENCE-ACQUISITION-SCOPING-001
artifact: coordinator-pilot-scoping
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-decision
repository: ahtoxaandy999/agentic-development-workflow
subject_main: 07fdfc72cf21488b6190547aeaa14f8b19152a8e
subject_tree: 02a6771a0ae6c85ba58a332cc000d5655e12abc6
subject_register_blob: 8e1ae4cd0479a9b79113c5780bfe1c02d7b13da4
readiness_assessment_ref: docs/design/ADW-D13-CONFORMANCE-EVIDENCE-READINESS-ASSESSMENT-001.md
selected_profile_repository: ahtoxaandy999/housing-recovery
observed_profile_main: 01b3ae5288069660a12c6b35254e4fa59867429e
observed_profile_tree: 2f5186613df4a9be34e672631cefb09d96d88d3f
scoped_on: 2026-09-22
decision: scope-one-housing-runtime-control-evidence-pilot-for-later-explicit-authorization
conformance_result: not-established
normative_effect: none
supersedes: null
---

# D13 conformance-evidence acquisition scoping

## Decision

scope-one-housing-runtime-control-evidence-pilot-for-later-explicit-authorization

Select Housing only as the representative profile for one later bounded runtime-control evidence pilot.

This record does not select or install an orchestration runtime, does not authorize pilot execution, and does not reconsider D13 or D5.

## Exact scoping basis

At scoping time:

- ADW main: 07fdfc72cf21488b6190547aeaa14f8b19152a8e
- ADW tree: 02a6771a0ae6c85ba58a332cc000d5655e12abc6
- ADW Research Register blob: 8e1ae4cd0479a9b79113c5780bfe1c02d7b13da4
- Housing main: 01b3ae5288069660a12c6b35254e4fa59867429e
- Housing tree: 2f5186613df4a9be34e672631cefb09d96d88d3f
- Housing open pull requests: none
- active Housing workflows: Candidate verification and Merge closeout verification
- repository-ruleset and classic branch-protection reads returned a plan-related 403
- branch listing reported main as protected: false

The protection API limitation is an evidence gap, not proof that GitHub lacks a capability. This pilot may not rely on branch protection or a ruleset as writer fencing.

The exact Housing execution base must be freshly resolved at a later authorization/dispatch gate.

## Why Housing

Housing has the smallest current repository surface that already proves exact PR-head verification, deterministic repository verification, fresh evidence for changed candidate SHAs, exact merge identity, tree equality, and fail-closed sequential closeout.

No product-runtime behavior needs to be exercised for this evidence task.

Selecting Housing is not selecting a D13 runtime.

## One bounded outcome

A future separately authorized pilot should answer one question:

Can one bounded runtime enforce exact operation identity, generation-bound single-writer mutation, idempotent privileged GitHub effects, restart/reconciliation after known and ambiguous outcomes, and technical reviewer isolation on one disposable Housing branch without touching main or merging?

## Proposed effect boundary

The future pilot effect domain is limited to:

- dedicated branch: pilot/d13-runtime-control-evidence-001
- one draft pull request targeting main
- inert marker path on that branch: docs/d13-runtime-control-evidence-pilot.md

The marker is not Product state, policy, a task tracker or repository authority.

The pilot may create successive immutable commits changing only that marker path.

The pilot may not write main, merge, change rulesets/protection, modify canonical Housing data/decisions/intake/schemas/application code, delete branches/PR history, modify verifier/workflow files, use production/user data, or persist secrets.

Cleanup is not part of the pilot.

## Required logical roles

### Coordinator / authorization owner

Owns pilot authority, exact selected runtime subject, allowed scenarios/effects, stop decisions and later conformance disposition.

### Execution-state recorder

Owns only pilot lifecycle projection: pilot epoch, writer generation, current operation, transition state, recovery episode identity and terminal eligibility.

Its durable state must be reconstructable without conversational memory.

### Privileged side-effect owner / publisher

Is the only role allowed to mutate the dedicated Housing branch/PR domain.

It owns mutation precondition validation, the GitHub write credential, effect execution, post-effect readback, durable effect receipt and containment/residual-effect reporting.

No executor, coordinator model or reviewer may share that write credential.

### Executor

May prepare proposed operation payloads or candidate bytes within the marker-file scope.

It must not possess the publisher write credential.

### Independent reviewer

Receives the exact runtime subject and evidence package in fresh context.

It must have read-only access and no candidate-branch write, PR-write, ready, merge or ruleset mutation capability.

## Runtime subject manifest

Before any effect, one immutable subject manifest must bind at minimum:

- task ID and pilot epoch
- repository and exact Housing base SHA/tree
- selected orchestration/runtime implementation revision
- adapter/publisher revision
- scenario-suite revision
- material OS/runtime/provider versions
- exact permission profile for every actor
- identity of the single privileged publisher
- dedicated branch/ref
- draft PR identity once created
- writer-generation seed/current value
- operation-ID namespace/version
- receipt schema/version
- evidence-capture version
- fault-injection configuration
- maximum attempts
- evidence root and custodian

Any load-bearing change creates a new runtime subject.

## Writer-generation contract

Every mutation request must contain:

- pilot_id
- pilot_epoch
- operation_id
- writer_generation
- effect_kind
- target_repository
- target_ref
- expected_head
- desired_head or exact desired effect
- exact authorization/subject digest

Before a write, the publisher must verify the request belongs to the current subject, generation is current, ref is the dedicated pilot branch, live head equals expected_head, the operation ID has no conflicting completed payload, the effect kind is allowed, and no stop/intervention state is active.

Stale generation, stale head, changed payload under the same operation ID, unexpected ref or authority drift must fail before mutation.

The concrete fencing primitive is not selected here.

The later mechanism must prove an old executor cannot bypass the publisher merely because it still has a workspace or remembered command. Credential separation is mandatory.

## Stable operation identity

The same operation_id plus the exact same request may resolve to an existing receipt without another mutation.

The same operation_id with any changed load-bearing field is a conflict and blocks.

A new desired mutation requires a new operation ID.

Duplicate event delivery is only a wake-up signal and never grants another mutation attempt.

## Effect receipt

Every privileged mutation must produce a durable receipt containing:

- operation ID and writer generation
- runtime-subject digest
- requested effect
- expected and observed pre-state
- mutation attempt count
- provider request/response identity where available
- result classification: no-effect, completed, partial/residual, or unknown
- authoritative post-effect readback
- exact observed branch/PR identities
- receipt timestamp and digest

A successful return without readback is insufficient.

A failed or lost return is not evidence of no effect.

## Reconciliation

After restart, timeout, lost response, contradictory state or missing evidence:

1. load exact runtime subject and durable transition history
2. stop new effects
3. identify in-flight operation and writer generation
4. read live Housing branch/PR state
5. retrieve any durable publisher receipt
6. compare expected state, receipt and live provider state
7. classify prior operation as proven no-effect, proven completed, partial/residual, or unknown
8. advance only when evidence is sufficient
9. otherwise record blocked/intervention-required
10. never repeat a mutation solely because the caller did not receive a response

GitHub owns what happened in GitHub. The execution-state recorder owns lifecycle projection only.

## Mandatory scenario matrix

| ID | Scenario | Required outcome |
| --- | --- | --- |
| S1 | authorized single-writer happy path | one authorized operation moves only the pilot branch from exact expected head to exact desired head; receipt/readback agree |
| S2 | duplicate same operation | repeated identical operation ID causes no second mutation and reuses/returns existing receipt |
| S3 | stale event | earlier head/generation event is reread against live state and denied without mutation |
| S4 | stale writer generation | old generation after advance is rejected before effect |
| S5 | interruption before effect | operation is durably prepared, runtime stops before publisher call, restart proves no effect before any continuation |
| S6 | lost response after completed effect | mutation completes, caller acknowledgement is lost, restart discovers completion and does not repeat it |
| S7 | missing required receipt/evidence | unsafe conclusion is impossible; runtime blocks/intervention-required and does not retry |
| S8 | contradictory state | recorder, receipt and live branch disagree; runtime fails closed |
| S9 | reviewer isolation | reviewer reads package but controlled mutation attempt with reviewer capability is denied |
| S10 | recovery episode reopening | later independent recovery obligation opens a new episode without rewriting the completed first one |
| S11 | intervention-required | unresolved ambiguity reaches durable blocked/intervention-required with named owner |
| S12 | terminal guard | completion/closure is denied while containment, recovery, evidence or intervention remains unresolved |

## Fault-injection boundary

Later authorization may consider only control-path faults such as suppressed caller acknowledgement, restart before publisher invocation, restart after publisher effect, duplicate event replay, stale generation, withheld test-local receipt, contradictory expected state, and one reviewer mutation attempt expected to be denied.

It may not corrupt Git, mutate/delete main, force-push, alter rulesets/protection, affect non-pilot branches, use production data or intentionally create an unrecoverable repository state.

## Reviewer isolation evidence

The package must include fresh reviewer execution identity, runtime-subject digest, package digest, reviewer permission profile, proof the reviewer did not receive publisher credentials, one bounded denied mutation attempt or equivalent effective permission proof, exact read accesses, and final verdict.

Procedural role separation alone is insufficient.

## Evidence package

The run must retain one exact package containing:

- subject manifest and scenario inventory
- transition history
- operation requests and generation transitions
- publisher receipts
- safe raw provider responses and authoritative readbacks
- branch/PR identity snapshots
- permission profiles
- fault-injection records
- restart/reconstruction records
- recovery/intervention/terminal-guard records
- reviewer-isolation evidence
- per-scenario results
- SHA-256 manifest for every retained payload
- overall package digest

Secrets/tokens must never be retained.

The later authorization must name one custodian and one retention surface. This scoping record selects neither local-only storage nor GitHub artifact storage as authoritative.

## Attempt and retry ceiling

Each privileged mutation operation may be attempted at most once.

Duplicate delivery is reconciliation/idempotency, not a second mutation attempt.

No automatic retry is permitted.

Read-only reconciliation may repeat.

Any second mutation attempt requires a fresh explicit recovery decision bound to the exact subject and prior-effect evidence.

## Stop conditions

Stop before new effects if:

- Housing main/authority drifts before dispatch
- pilot branch/PR already exists unexpectedly
- another writer is active
- permissions differ from subject manifest
- publisher credential reaches executor/reviewer
- runtime/config differs from manifest
- live branch head differs from expected
- receipt conflicts with live GitHub state
- required evidence is missing
- an unauthorized ref/path is touched
- direct main mutation succeeds unexpectedly
- containment is uncertain
- a second mutation attempt would be needed without recovery authority
- mechanism behavior requires new semantics

Unexpected success of a forbidden mutation is reconciliation/incident state, not PASS.

## Mechanism candidates and non-selection

This scoping defines semantics, not implementation.

A later decision may compare:

1. a thin task-local deterministic adapter/publisher around GitHub primitives
2. GitHub-native workflow/job primitives with explicit permission separation
3. gh-aw if live evidence at that gate proves required permission, event, state, recovery and evidence surfaces

No candidate is selected here.

Codex App Server/SDK is not eligible for silent use while D5 remains CONFIRM DEFER.

Symphony/custom harness defaults do not gain authority while X3 remains CONFIRM REJECT.

If the later pilot mechanism itself constitutes a D13 bounded PoC, the later authorization must explicitly make the applicable conditional D13 PoC decision.

If App Server is proposed, a separate D5 decision or one explicit superseding decision naming D5 and D13 is required before execution.

## Pilot acceptance bar

A completed run may be proposed as D13 conformance evidence only when:

- exact runtime subject is immutable and independently retrievable
- all mandatory applicable scenarios ran against that subject
- positive scenarios reached authorized targets
- negative scenarios demonstrated required denial/fail-closed behavior
- no unauthorized repository effect occurred
- writer generation and stale-writer denial are evidenced at effect level
- duplicate evidence proves no repeated side effect
- lost-response recovery proves no blind replay
- restart/reconstruction uses durable evidence, not conversation memory
- reviewer isolation is effective
- recovery/intervention/terminal guards are observable
- every load-bearing artifact is retained and digest-bound
- no critical gap, contradiction or unowned residual effect remains
- fresh independent review has no unresolved BLOCKER or MAJOR finding

Pilot PASS would remain evidence, not D13 reconsideration or operational adoption.

## Future authorization requirements

Before implementation/effect, a separate coordinator/human decision must name:

- exact Housing execution base
- exact selected mechanism/runtime
- exact implementation/config revisions
- actor identities and permission profiles
- publisher credential boundary
- evidence custodian/retention surface
- exact fault-injection plan
- exact allowed Housing mutations
- attempt ceiling
- stop/recovery authority
- exact independent reviewer
- whether this is a conditional D13 bounded PoC
- any additional D5 authority if applicable

Absent that decision, this record authorizes no execution.

## Intended Register transition

After exact review, acceptance and protected publication of this scoping record, the Research Register should add this artifact/task, bind scoping subject main 07fdfc72cf21488b6190547aeaa14f8b19152a8e, record Housing as selected profile with observed main 01b3ae5288069660a12c6b35254e4fa59867429e, record this scoping decision, preserve d13_conformance_result: not-established, preserve D13/D5/X3 and the repository-wide current gate, and set the D13-specific next gate to:

D13 bounded conformance-evidence pilot authorization gate

## Next gate

After fresh independent review, explicit coordinator/human acceptance, protected merge publication and verified readback:

D13 bounded conformance-evidence pilot authorization gate

That gate may authorize no execution unless it resolves exact mechanism, permissions, runtime subject and the applicable D13/D5 decision boundary.

## Explicit non-authorities

This scoping creates no authority for Housing mutation, pilot implementation, PoC execution, mechanism selection, gh-aw adoption, workflow changes, new secrets/Apps/tokens, Claude/Codex Action installation, App Server/SDK selection, Symphony/custom runtime deployment, automatic review/correction/task advancement, automatic ready/merge, ruleset/protection change, unattended/AFK operation, local LLM training/data collection, D13 reconsideration outcome, D5 reconsideration outcome, Workflow v1 amendment or baseline acceptance.

D13 remains CONFIRM DEFER.
D5 remains CONFIRM DEFER.
X3 remains CONFIRM REJECT.

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
- indirect GitHub Actions runs triggered by the existing Housing pull_request workflow for opened/synchronize events

The marker is not Product state, policy, a task tracker or repository authority.

The pilot may create successive immutable commits changing only that marker path.

Opening the draft PR and later pilot-branch pushes are known to trigger the existing Candidate verification workflow. Those workflow runs are indirect external effects of the branch/PR operations and must be inventoried, observed and reconciled as part of the effect domain. A queued, in-progress, cancelled or completed run is not ignored merely because the primary branch mutation already completed.

Merge closeout verification is not expected because merge is forbidden. If any unexpected closeout or other workflow effect appears, the pilot must stop and reconcile.

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

It cannot be the producer/publisher of the evidence package and cannot accept its own review result, advance the acceptance plane or confer merge authority.

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

A pre-read followed by an unconditional provider write is not sufficient fencing. The selected later mechanism must close the check-to-write race at the effect boundary.

The mutation must be conditionally fenced against both:

- the exact expected remote head at write time; and
- the current writer generation.

The concrete primitive is deliberately not selected here. The later authorization must identify and independently verify a mechanism in which a stale or competing publisher instance cannot successfully mutate merely because it still possesses a workspace or credential.

A stale instance that retains a previously valid repository write credential is part of the threat model. Credential separation between publisher and executor/reviewer is necessary but not sufficient by itself.

The selected mechanism must prove one of the following, without this scoping record choosing which:

- provider-side conditional/CAS-like write semantics plus an effective generation fence; or
- an equivalently strong serialized/fenced publisher critical section whose stale-instance exclusion and provider-head precondition are independently evidenced.

Worktree separation, prompt instructions, a remembered command, or an ordinary check-then-write sequence do not satisfy this requirement.

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
- expected and observed indirect workflow-run identities/states when branch/PR activity triggers GitHub Actions
- residual/queued-effect inventory
- receipt timestamp and digest

A successful return without readback is insufficient.

A failed or lost return is not evidence of no effect.

A branch mutation is not fully reconciled merely because the ref reached the desired SHA if it also caused a queued or in-progress external workflow effect that remains unobserved or unowned.

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

The accepted D13 scenarios map exactly as follows. Supplemental scenarios do not replace any accepted mandatory scenario.

| Accepted D13 scenario | Pilot scenario |
| --- | --- |
| authorized single-writer happy path | S1 |
| stale event after head/authority change | S3 |
| duplicate event / duplicate operation | S2 |
| competing or stale writer | S4 |
| process interruption before known effect | S5 |
| interruption after partial/queued external effect | S6 |
| missing required evidence | S7 |
| contradictory plane statuses | S8 |
| reviewer isolation | S9 |
| recovery episode reopening | S10 |
| intervention-required state | S11 |
| terminal-guard attempt | S12 |

| ID | Scenario | Required outcome |
| --- | --- | --- |
| S1 | authorized single-writer happy path | one authorized operation moves only the pilot branch from exact expected head to exact desired head; exact candidate SHA, triggered candidate-verification identity, receipt/readback and later exact reviewer subject all bind consistently without advancing acceptance by implication |
| S2 | duplicate same operation | repeated identical operation ID causes no second mutation and reuses/returns existing receipt |
| S3 | stale event | earlier head/generation event is reread against live state and denied without mutation |
| S4 | competing or stale writer/publisher | after generation advances, a stale or concurrent credential-holding publisher instance attempts the same mutation boundary; only the current generation may succeed and the stale/competing instance is denied with no second effect |
| S5 | interruption before known effect | operation is durably prepared, runtime stops before publisher call, restart proves no effect before any continuation |
| S6 | interruption after partial/queued external effect | a branch/PR mutation has created or may have created a queued/in-progress Candidate verification run or other residual effect; restart inventories branch/PR plus workflow state, records residual/unknown effects, verifies containment where applicable, and blocks blind retry until reconciliation is complete |
| S7 | missing required receipt/evidence | unsafe conclusion is impossible; runtime blocks/intervention-required and does not retry |
| S8 | contradictory plane statuses / DI-1 non-collapse | a native status such as green candidate verification, PR open/closed state or runtime done state cannot advance review, disposition, Product/coordinator acceptance, merge authority or terminal task state; the orthogonal planes remain distinct |
| S9 | reviewer isolation | reviewer reads the exact package; any controlled mutation attempt is limited to the pilot branch/marker or draft PR domain and is denied, and the reviewer cannot self-accept, ready or merge |
| S10 | recovery episode reopening | later independent recovery obligation opens a new episode without rewriting the completed first one |
| S11 | intervention-required | unresolved ambiguity reaches durable blocked/intervention-required with named owner |
| S12 | terminal guard | completion/closure is denied while containment, recovery, evidence or intervention remains unresolved |

Supplemental scenarios are also required because the readiness assessment identified them as load-bearing gaps:

| ID | Supplemental scenario | Required outcome |
| --- | --- | --- |
| F1 | lost response after completed effect | mutation completes, caller acknowledgement is intentionally lost, restart discovers the completed effect by durable receipt/live readback and does not repeat it |
| F2 | provider/recorder contradiction | execution-state projection, receipt and live GitHub state disagree; no plane is overwritten, the conflict is retained, and execution fails closed pending reconciliation |

## Fault-injection boundary

Later authorization may consider only control-path faults such as:

- suppressed caller acknowledgement after a completed publisher action
- restart before publisher invocation
- restart after publisher effect but before caller acknowledgement
- duplicate event replay
- stale writer generation
- a competing/stale credential-holding publisher instance
- a queued/in-progress Candidate verification run remaining after the primary branch mutation
- withheld test-local receipt
- deliberately contradictory test-local expected state
- one reviewer mutation attempt expected to be denied, targeted only at the dedicated pilot branch/marker or draft PR domain

It may not corrupt Git, mutate/delete main, force-push, alter rulesets/protection, affect non-pilot branches, use production data or intentionally create an unrecoverable repository state.

A reviewer-isolation negative test must never target main or any Housing canonical data path.

The partial/queued-effect scenario must observe and account for the existing pull_request-triggered Candidate verification workflow rather than pretending the branch mutation is the only external effect.

## Reviewer isolation evidence

The package must include:

- fresh reviewer execution identity
- exact runtime-subject digest
- exact evidence-package digest
- reviewer permission/capability profile
- proof the reviewer did not receive publisher credentials
- one bounded denied mutation attempt targeted only at the dedicated pilot branch/marker or draft PR domain, or an equivalent effective permission proof
- exact read accesses used for the review
- proof the reviewer cannot ready, merge or otherwise mutate the acceptance/publication planes
- explicit statement that reviewer verdict cannot self-accept or advance coordinator/human acceptance
- final verdict bound to the exact package

Procedural role separation alone is insufficient.

## Evidence package

The run must retain one exact package containing:

- subject manifest and scenario inventory
- transition history
- operation requests and generation transitions
- publisher receipts
- safe raw provider responses and authoritative readbacks
- branch/PR identity snapshots
- triggered GitHub Actions run identities/states and residual/queued-effect inventory
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

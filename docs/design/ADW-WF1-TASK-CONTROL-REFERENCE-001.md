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

# Workflow v1 task-control reference

## A. Authority and non-authority

This document is an explanatory, non-operative and non-normative design
reference for the task-control meanings already accepted in
`docs/design/ADW-WF1-TOOLING-DESIGN-001.md`. That accepted tooling design,
as qualified by its disposition, controls whenever this explanation and the
accepted design could be read differently. The accepted gate-evaluation and
producer-verification evidence references remain the explanatory owners of
their respective semantics; this document points to them and does not redefine
them.

This is not an actual task, an adopted serialization, a schema, a parser, a
validator, a recorder, a generator, a runtime, an executable checklist or an
operational template. Its labels, ordering and fictional examples are teaching
devices. Copying, completing, persisting or reviewing an example creates no
task, owner appointment, readiness, authorization, candidate, verification,
review, disposition, adoption, baseline acceptance or permission to act.

This reference owns no mutable task, product, repository, research or workflow
state. The Research Register remains the sole owner of the current ADW gate.
Any future product task would require its own explicit authority, exact
repository and task identity, named accountable actors and separately
authorized materialization. Workflow v1 remains unadopted.

## B. Sole-owner map

For a hypothetical future product task, the accepted design proposes one
mutable current projection at `docs/adw/tasks/<T>/control.md`. The task's
appointed recorder, R, is its sole updater. R records only decisions and
observations supplied by the accountable authority shown below; recording does
not transfer decision authority. Immutable records retain the fixed inputs and
history. An Issue, chat, runner, evidence manifest or another task file may
point to the current owner but may not independently own the same current
field.

| Mutable state domain | Sole current placement or real-world owner | Authority that may supply the value; updater |
|---|---|---|
| Contract, objective, scope and readiness | The task's one `control.md` contract/readiness projection | Task-contract authority A decides; R alone updates the projection |
| Authorization and task gate | The same file's authorization and gate pointers | Authorized coordinator or risk owner decides; R alone records |
| Execution and task-control progress | The same file's task-control plane and run/operation pointers | Execution-control authority supplies transitions; R alone records |
| Work product | Mutable working bytes remain solely in the executor's authorized output location; the same file owns their current semantic pointer | Executor owns W bytes; authorized candidate authority supplies promotion facts; R alone records the pointer |
| Verification | The same file's verification plane and current obligation/evidence map | Assigned verifier supplies attributed results; applicability owner supplies N/A; R alone records |
| Independent review | The same file's review plane and current assignment/verdict pointer | Review authority appoints and a conflict-free reviewer decides; R alone records |
| Disposition | The same file's disposition plane and current decision pointer | Authorized coordinator/accountable owner decides; R alone records |
| Cancellation | The same file's cancellation plane and request/acknowledgement/domain pointers | Authorized requester and affected controllers/domain owners supply findings; R alone records the aggregate |
| Recovery | The same file's recovery plane, episode pointer and open obligations | State/side-effect owner and required risk authority decide; R alone records |
| Decomposition, dependencies and join | The same file's decomposition/dependency pointers and join plane | Named decomposition and aggregation/integration authorities decide; R alone records |
| Product continuation gate | The same file's product-task next-gate pointer | Applicable product/task authority decides; R alone records; it has no ADW Register effect |
| Normativity | The applicable adopted normative owner remains the real authority; the task file contains only its reference-derived projection | Normative/adoption owner decides; R only records a supported pointer |
| Baseline acceptance | The applicable existing acceptance owner remains the real authority; the task file contains only its reference-derived projection | Designated baseline-acceptance authority decides; R only records a supported pointer |
| Evidence custody/access/retention | The task file owns current custody-record pointers; the named custodian owns the actual commitment | Custodian decides within governance; R alone records the pointer and gains no verdict authority |
| External side-effect/control observations | The live external system remains the sole owner of its actual state | Separately authorized domain operator may change it; domain owner supplies observations and R only records references |
| ADW research state and current gate | `docs/research/research-register.md` in ADW | Existing Register governance under separate authority; a product-task recorder cannot update it |

If two credible sources claim the same current domain, dependent reliance stops
until the existing accountable owner resolves the conflict. Timestamps do not
select an owner. A transfer requires an immutable decision naming the domain,
old and new owner/recorder, exact prior revision, effective point, in-flight
effects, reconciled writes and custody; both recorders are never authorized at
once.

## C. Annotated fictional current projection

The block below is deliberately fictional and human-oriented. Every
angle-bracketed token is an unallocated teaching placeholder. The names and
layout are illustrative, not an adopted field set or compatibility contract.

```yaml
illustration_only: <FICTIONAL-NON-OPERATIVE-CONTROL-PROJECTION>
identity:
  product_repository: <FICTIONAL-OWNER/FICTIONAL-PRODUCT-REPOSITORY>
  authoritative_mutable_ref: <FICTIONAL-CURRENT-REF>
  task_id: <FICTIONAL-TASK-ID>
  task_root: docs/adw/tasks/<FICTIONAL-TASK-ID>/
  contract_revision_ref: <FICTIONAL-IMMUTABLE-CONTRACT-REVISION-REF>
  current_control_revision:
    containing_commit: <FICTIONAL-FULL-CONTROL-COMMIT-SHA>
    path: docs/adw/tasks/<FICTIONAL-TASK-ID>/control.md
    git_blob: <FICTIONAL-FULL-CONTROL-BLOB-SHA>
  previous_control_revision: <FICTIONAL-EXACT-PREDECESSOR-REF>

role_bindings:
  task_contract_authority: <FICTIONAL-ACTOR-A>
  sole_recorder: <FICTIONAL-ACTOR-R>
  executor: <FICTIONAL-ACTOR-E>
  supervisor: <FICTIONAL-ACTOR-S>
  escalation_owner: <FICTIONAL-ACTOR-X>
  verification_authority: <FICTIONAL-ACTOR-V>
  review_authority: <FICTIONAL-ACTOR-RA>
  integration_authority: <FICTIONAL-ACTOR-J>
  evidence_custodian: <FICTIONAL-ACTOR-K>

bounded_authority:
  authorization_ref: <FICTIONAL-IMMUTABLE-AUTHORIZATION-REF>
  B:
    repository: <FICTIONAL-OWNER/FICTIONAL-PRODUCT-REPOSITORY>
    mutable_ref: <FICTIONAL-CURRENT-REF>
    authorized_base_commit: <FICTIONAL-FULL-B-SHA>
    authority_and_control_inputs: <FICTIONAL-EXACT-INPUT-REFS>
    allowed_delta: <FICTIONAL-BOUNDED-PATH-AND-EFFECT-SCOPE>
  allowed_actions: <FICTIONAL-BOUNDED-ACTIONS>
  ceilings_and_stop_conditions: <FICTIONAL-SUPPLIED-LIMITS>

current_execution:
  run_id: <FICTIONAL-RUN-ID>
  operation_id: <FICTIONAL-OPERATION-ID>
  attempt_id: <FICTIONAL-ATTEMPT-ID>

orthogonal_planes:
  task_control: <FICTIONAL-ONE-OF-ACCEPTED-TASK-CONTROL-VALUES>
  work_product: <FICTIONAL-ONE-OF-ACCEPTED-WORK-PRODUCT-VALUES>
  verification: <FICTIONAL-ONE-OF-ACCEPTED-VERIFICATION-VALUES>
  review: <FICTIONAL-ONE-OF-ACCEPTED-REVIEW-VALUES>
  disposition: <FICTIONAL-ONE-OF-ACCEPTED-DISPOSITION-VALUES>
  normative_status: <FICTIONAL-ONE-OF-ACCEPTED-NORMATIVE-VALUES>
  baseline_acceptance: <FICTIONAL-ONE-OF-ACCEPTED-BASELINE-VALUES>
  join: <FICTIONAL-ONE-OF-ACCEPTED-JOIN-VALUES>
  cancellation: <FICTIONAL-ONE-OF-ACCEPTED-CANCELLATION-VALUES>
  recovery: <FICTIONAL-ONE-OF-ACCEPTED-RECOVERY-VALUES>

subjects:
  W:
    canonical_local_root: <FICTIONAL-AUTHORIZED-ABSOLUTE-OUTPUT-ROOT>
    complete_output_inventory: <FICTIONAL-PATH-BYTES-DIGEST-MANIFEST>
    working_snapshot_basis: <FICTIONAL-WORKING-REVISION>
    proposed_repository_paths: <FICTIONAL-BOUNDED-PATHS>
  C:
    candidate_commit: <FICTIONAL-FULL-C-SHA-OR-NONE>
    sole_parent_B: <FICTIONAL-FULL-B-SHA-OR-NONE>
    candidate_tree: <FICTIONAL-FULL-TREE-SHA-OR-NONE>
    complete_delta_manifest: <FICTIONAL-PATH-BLOB-MANIFEST-OR-NONE>
  I:
    integration_commit: <FICTIONAL-FULL-I-SHA-OR-NONE>
    integration_scope: <FICTIONAL-INTEGRATED-SCOPE-OR-NONE>
    exact_relation_to_C: <FICTIONAL-C-TO-I-EVIDENCE-OR-NONE>

current_records:
  output_manifest_ref: <FICTIONAL-IMMUTABLE-OUTPUT-REF>
  verification_evidence_refs: <FICTIONAL-CURRENT-CORRECT-SUBJECT-REFS>
  review_assignment_and_verdict_refs: <FICTIONAL-EXACT-C-REFS>
  disposition_ref: <FICTIONAL-EXACT-SUBJECT-DECISION-REF>
  cancellation_refs:
    request: <FICTIONAL-REQUEST-REF-OR-NONE>
    acknowledgement_by_domain: <FICTIONAL-ACK-REFS-OR-NONE>
    containment_findings: <FICTIONAL-DOMAIN-FINDING-REFS-OR-NONE>
    residual_effects: <FICTIONAL-RESIDUAL-INVENTORY-OR-NONE>
  recovery_refs:
    current_episode: <FICTIONAL-EPISODE-ID-OR-NONE>
    predecessor_episode: <FICTIONAL-COMPLETED-EPISODE-REF-OR-NONE>
    authorization_and_target: <FICTIONAL-RECOVERY-AUTHORITY-REFS>
    attempts_and_interventions: <FICTIONAL-IMMUTABLE-CHAIN>
    validation_and_resumption: <FICTIONAL-EXACT-REFS-OR-NONE>

composition:
  decomposition_snapshot_ref: <FICTIONAL-IMMUTABLE-GRAPH-REF>
  required_dependencies: <FICTIONAL-EXACT-CHILD-RESULT-REFS>
  optional_dependencies: <FICTIONAL-RESULT-OR-GOVERNED-OMISSION-REFS>
  join_decision_ref: <FICTIONAL-EXACT-I-AND-ACCOUNTING-REF>

continuation:
  unresolved_obligations: <FICTIONAL-COMPLETE-BLOCKING-LIST>
  product_task_next_gate: <FICTIONAL-PRODUCT-GATE-REF>
  permitted_next_action: <FICTIONAL-AUTHORITY-DERIVED-ACTION-OR-NONE>
  immutable_transition_history: <FICTIONAL-ORDERED-EVENT-POINTERS>
```

The accepted plane vocabularies stay separate: task control, work product,
verification, review, disposition, normative status, baseline acceptance,
join, cancellation and recovery. A value in one plane does not imply a value
in another. In particular, `completed`, `candidate-identified`, `passed`,
`accepted`, `contained` and `recovered` are different claims owned and
supported separately.

## D. Immutable records and the mutable projection

The single mutable projection answers “what is current?” by pointing to fixed
sources. It carries current plane values, the exact prior control revision,
current run/operation/attempt pointers, current subject/evidence/review/
disposition/custody pointers, unresolved obligations and the product next
gate. It does not duplicate editable contract text, verdict prose or history.

Immutable contract revisions carry objective, scope, constraints, criteria and
role appointments. Authorization records carry the exact B, permitted
paths/actions/effects, executor/supervisor, ceilings, revocation and stop
conditions. Transition events carry source/destination plane values, retained
planes, prior control revision, decision/evidence references, actor, time,
reason and open obligations. Evidence manifests carry exact subject, method,
criteria, results, payload identities, freshness, producer and limitations.
Review records carry assignment, conflict assessment, exact unchanged C,
findings and verdict. Disposition records carry exact subject/scope, deciding
authority, relied-upon gates and conclusion. Recovery episodes carry opening
authority/target, attempts, effects, intervention, validation, conclusion and
links to a predecessor when a distinct later obligation qualifies.

Corrections create successor identities with an explicit supersedes or impact
relationship. Historical failures, stale evidence, wrong-subject results,
completed recovery episodes and earlier custody statements are never edited
into a pass. A new contract revision does not inherit readiness or
authorization silently; a changed C is a new candidate.

## E. Update responsibility and lifecycle

Before every separately authorized update, R rereads the authoritative mutable
ref and exact previous control revision, then checks current authority,
affected evidence, transition source and guards. R records only a decision or
observation attributable to its proper owner. Evidence production does not
grant decision authority, and faithful persistence does not make R the
reviewer, custodian or acceptor.

Unsupported source/destination pairs, a stale base, conflicting ownership,
material scope drift or a required unknown fail closed. R may preserve a
denial event with unchanged values; it may not invent a transition. If durable
recording is unavailable, new dependent effects stop. Candidate persistence,
candidate verification, independent review, disposition, normative adoption
and baseline acceptance are distinct gates; none follows from a successful
command, commit, green status or another plane's value.

The accepted narrow lifecycle is explanatory here: framing may become ready
only from an executable and verifiable exact contract; ready may become
authorized only through a separate current grant; authorized may become active
only after a fresh dispatch decision and all applicable prerequisites. Working
output may become proposed output without becoming C. C exists only after
separately authorized immutable persistence and exact readback. Review,
disposition, adoption, acceptance and terminal accounting remain independent.

## F. Exact B, W, C and I identity and freshness

**B** is the full authorized base commit plus repository, mutable ref, exact
authority/control inputs and allowed delta. **W** is mutable local output bound
to its authorized absolute root, complete paths, byte counts, digests,
proposed repository paths and working snapshot. W is not a Git candidate.
**C** is an immutable repository candidate: full commit SHA, sole parent B for
the accepted initial narrow path, tree SHA and complete allowed-path
blob/delta manifest. **I** is the exact integration commit and scope plus its
proved relation to all component results and reviewed C. For a
non-composing narrow persistence, I may equal C only when the applicable gate
so determines; equality is not assumed.

Verification V names W, C or I explicitly. Independent review Rv names exact
unchanged C. A relied-upon publication must establish
`V.subject = Rv.subject = I = published subject = C` wherever those gates
apply. Evidence about W can carry content properties to C only through a new
exact candidate-binding decision; it cannot prove commit provenance or
unrelated tree properties. A later evidence commit about C is not thereby
reviewed as a whole.

Before dispatch, resumption, persistence, verification reliance, review, join
and disposition, reread every material mutable dimension: authority, ref/base,
subject, criteria, configuration, dependencies and evidence access/custody.
Freshness is item-specific. A changed C or load-bearing basis makes affected
prior evidence stale for current reliance while preserving it as history.
Branch names, short SHAs, PR state, green checks and human-readable status are
insufficient. Repository pointers use repository + full containing commit SHA
+ path + Git blob + optional fragment; relied-upon payloads also use byte count
and SHA-256. Identity proves equality only—not truth, authority, independence,
correctness, retention or acceptance.

## G. Gate and obligation semantics

The accepted
`docs/design/ADW-WF1-GATE-EVALUATION-REFERENCE-001.md` controls the
explanatory gate semantics. This section is only a pointer-oriented summary:

- Applicability is `required` or a governed `not-applicable`.
- Satisfaction is `passed` or `unsatisfied` only for a required gate.
- A required pass needs complete, current, correct-subject evidence for every
  criterion.
- Missing, incomplete, skipped, failed, unavailable, unsafe, inaccessible,
  stale or wrong-subject required evidence is non-passing.
- Legitimate N/A names its governing rule, accountable owner and contextual
  rationale, has no satisfaction value and earns no pass credit.
- Every declared obligation is accounted for; N/A cannot offset a failed
  required obligation and aggregate green output is only an observation.
- A destination is permitted only when the governing authority's effective
  decision names it. A recorded destination neither performs nor authorizes a
  transition by itself.

An evidence manifest may record the supplied applicability decision and
results, but it is not the gate decision or current verification owner.

## H. Cancellation and recovery remain distinct

Cancellation is represented by separate immutable request,
per-controller/domain acknowledgement, containment findings and residual-effect
inventory references. Request is not acknowledgement. Partial acknowledgement
does not advance the aggregate. A stopped process is not containment.
Containment requires every affected local, subprocess, queue, remote and
external-effect domain to be observed ceased or bounded; uncertainty blocks
containment-dependent retry, resumption, closure and release of critical
resources.

Recovery has a distinct episode ID and immutable opening, authorization,
attempt, effect, intervention, validation and conclusion chain. An operation
is classified before retry as safely repeatable, conditionally repeatable,
compensatable, irreversible, nondeterministic or ambiguous. Ambiguous
completion denies blind retry. Compensation is a new authorized effect, not
proof of reversal.

A completed episode remains completed. Reopening requires positive evidence
that its target was satisfied and that a materially distinct or later
discovered obligation exists, plus new bounded authority and a new linked
episode ID. Intervention is blocked/intervention-required; renewal addresses
the unfinished episode. Resumption requires explicit current authority,
complete applicable containment/recovery and one transition resetting
active/none/not-applicable while preserving all episode history. Completion,
cancelled closure and abandonment each have independent terminal guards; an
old recovered value cannot discharge a new obligation.

## I. Decomposition, dependencies and join

One immutable decomposition snapshot identifies each unit, owner, inputs,
outputs, read/write/effect domains, interfaces, dependencies, required or
optional classification, local checks, integration point and final criteria.
It does not enable parallel execution.

Every required dependency is satisfied only by its exact declared child-result
identity and required validation state. Missing, partial, cancelled, failed,
stale or substituted required results remain non-satisfying. Optional omission
is recorded with its governing N/A rationale and never counted as success.

One immutable join decision accounts for every unit, omission, conflict,
side-effect and exclusion; identifies exact I; and binds integrated
verification. Missing required results make the join partial or failed.
Failed integrated verification makes it failed; pending or stale integrated
verification leaves it non-passing; unresolved conflicts make it conflicted.
Required integrated verification must actually pass on exact I before
`join=passed`. Candidate formation, completion, publication reliance and
disposition cannot rely on a non-passing join.

## J. Pointer-based rehydration

A fresh actor starts from repository authority, never from chat or memory:

1. verify the exact repository, authoritative ref and its current full SHA;
2. read governing instructions and the single current task root/control
   revision;
3. retrieve the exact contract revision, authorization and prior control
   revision;
4. reconstruct every orthogonal plane from its current immutable references,
   including W/C/I, evidence, review, disposition, cancellation, recovery,
   decomposition/dependencies/join and custody;
5. retrieve critical evidence and compare commit/path/blob plus payload
   size/digest, current authority, criteria, configuration and dependencies;
6. enumerate unresolved obligations and read the product continuation gate;
7. reconcile any summary discrepancy under the owner hierarchy and record the
   rehydration observation and allowed or denied next action before
   consequential continuation.

Missing or stale critical authority, identity, evidence, dependency, custody
or containment blocks continuation. Chat, memory, summaries and handoffs are
navigation aids only. Surface unavailability grants no alternate interface,
installation or background authority.

## K. Denied transitions and unresolved inputs

The following conditions deny the affected transition rather than inviting an
implementer guess:

| Condition | Denied reliance or next step |
|---|---|
| Missing decision authority, role appointment or bounded grant | No readiness, dispatch, mutation, recovery, review or disposition attributed to that role |
| Live base/ref differs from B or scope materially drifts | No persistence, automatic rebase, retry or harmless-change assumption; return for impact and fresh authority |
| W/C/I, verification or review binds the wrong subject | No promotion, carry-forward, join, publication or acceptance reliance |
| Criteria, configuration, dependency, rule or evidence becomes stale | Affected pass becomes non-current; preserve old record and obtain new authorized evidence |
| Actual permission, effect surface, ceiling, supervision or exclusivity is unknown | No affected effect; labels, authentication or host approval are insufficient |
| Required payload is unsafe, inaccessible, missing, expired or mismatched | No dependent pass; preserve safe evidence and obtain a separate custody/evidence decision |
| Cancellation acknowledgement or containment is incomplete | No retry, resumption, closure or resource release requiring containment |
| Recovery is incomplete, ambiguous or intervention-required | No blind retry, reset, resumption or terminal closure |
| Required dependency result is missing/failed/stale or integrated verification fails | No passing join or downstream success |
| Independent review is required but absent, conflicted or stale | Review remains pending/non-passing; producer checking cannot substitute |
| Disposition, adoption or baseline acceptance is absent | No implicit acceptance from output, checks, commit, publication or another state plane |
| Two sources claim the same current mutable domain | Stop reliance until the accountable owner resolves ownership |

Unknown product, actor, permission, custody, retention, risk and runtime values
must be supplied by their accountable owners at the relevant future gate.
This reference supplies none of them.

## L. Twelve fictional walkthroughs

Every walkthrough below uses unallocated fictional tokens and describes only
semantic interpretation. None authorizes the transition it discusses.

### L1. Framed to ready

`<FICTIONAL-TASK-L1>` points to a complete immutable contract whose objective,
scope, criteria, dependencies and material unknowns are classified. The
fictional task authority supplies a readiness decision on that exact revision;
R rereads the prior control revision and records `framing -> ready`.
This cannot authorize execution: a separate current authorization is absent.

### L2. Ready to authorized

For `<FICTIONAL-TASK-L2>`, a bounded grant names exact B, executor,
supervisor, allowed paths/actions/effects, ceilings, evidence destination,
revocation and stop conditions. R records `ready -> authorized` without
changing work-product or verification planes. This cannot dispatch work or
grant any authority outside that fictional record.

### L3. Authorized to active

`<FICTIONAL-TASK-L3>` has a fresh dispatch decision after rereading B,
contract, dependencies, permissions, exclusivity and applicable gates. R
records a new run/operation/attempt and `authorized -> active`. This cannot
prove the fictional permissions are real or enable this transition in any
actual repository.

### L4. W verification without candidate promotion

The producer checks exact `<FICTIONAL-W-L4>` inventory and every required
criterion. The W-bound evidence passes and the verification plane may point to
that result, while work product remains `proposed-output`. W has no commit,
tree or candidate binding. This cannot create C, authorize persistence,
perform review or grant pass to a later edited W.

### L5. Exact candidate publication

A separate fictional persistence grant on `<FICTIONAL-B-L5>` permits one
exact delta. Readback returns `<FICTIONAL-C-L5>` with sole parent B, exact
tree and path/blob manifest; a fixed record relates the verified W bytes to C.
This creates only an illustrative candidate identity. It cannot establish
review, disposition, adoption, baseline acceptance or permission to publish
anything real.

### L6. Changed C invalidates evidence and review

`<FICTIONAL-C1-L6>` had passing candidate evidence and review. A content
change creates `<FICTIONAL-C2-L6>`. Current verification and review for C2
become non-passing until affected checks and applicable fresh review bind C2;
C1 records remain intact. Equal filenames or green labels cannot carry them
forward. This walkthrough cannot decide that any real change is unaffected.

### L7. Failed required obligation

Two required checks for `<FICTIONAL-I-L7>` pass and one fails. The aggregate
is non-passing and join cannot pass even if a dashboard is green. The failed
payload and limitation remain recorded. This cannot authorize omission,
scope reduction or downstream completion.

### L8. Legitimate N/A

A fictional governing rule excludes an integrated-binary check only because
the exact `<FICTIONAL-SCOPE-L8>` contains no binary or integration
destination. The accountable fictional owner records applicability N/A with
current scope evidence and no satisfaction value. It earns no pass and must be
reevaluated if scope changes. This cannot make any actual criterion N/A.

### L9. Cancellation with incomplete containment

An authorized fictional request covers a local process and a remote queue.
The local controller acknowledges and stops, but the remote queue remains
unobserved. Cancellation may remain requested/partially evidenced; it cannot
advance to aggregate acknowledged or contained. Retry, resumption, cancelled
closure and release of containment resources are denied. This does not cancel
any real operation.

### L10. Recovery episode before resumption

After verified fictional containment, `<FICTIONAL-EPISODE-A-L10>` opens with
bounded recovery authority and a validation target. An ambiguous effect is
reconciled, an authorized action is recorded, and the target is independently
validated before recovery becomes recovered. A separate resumption decision
then resets active/none/not-applicable while retaining the episode. This
cannot authorize retry, compensation or resumption in an actual system.

### L11. Missing required dependency at join

The decomposition snapshot for `<FICTIONAL-JOIN-L11>` declares child results
A and B required and C optional. A is current, B is missing and C has a
governed omission. Exact I cannot receive a passing join; the result is
partial or failed and downstream candidate success is denied. This does not
enable parallel work or authorize removing B from scope.

### L12. Rehydration from exact pointers

A fresh fictional actor receives only the repository/ref, task root and prior
control pointer. It rereads the live ref, exact contract and authorization,
all plane references, evidence payload identities, recovery history,
dependencies and product next gate. A narrative summary disagrees with the
current review pointer, so the exact owner wins and the discrepancy is
recorded. This cannot appoint the actor, cure missing evidence or authorize
continuation in a real task.

## M. RG, DI and adoption boundaries

RG1 through RG12 remain unresolved. This reference supplies no:

1. **RG1 protection:** effective branch protection or protected integration;
2. **RG2 writer fencing:** technical exclusive-writer or stale-writer control;
3. **RG3 exact integration publication:** enforced C/I/publication mapping;
4. **RG4 reviewer identity:** platform-enforced identity, independence or
   approval routing;
5. **RG5 cross-surface permissions:** proof across local, network, connector,
   browser or cloud effects;
6. **RG6 cancellation/containment:** effective interruption or all-domain
   containment control;
7. **RG7 durable recovery:** generic retry, reconciliation, compensation or
   recovery mechanism;
8. **RG8 retention/integrity:** permanent custody, access or integrity
   guarantee;
9. **RG9 installed capabilities:** version, entitlement, configuration or
   compatibility proof;
10. **RG10 integration leverage:** optional integration selection or measured
    value;
11. **RG11 documentation ambiguity:** resolution of deferred documentation,
    transport, authentication or lifecycle questions; or
12. **RG12 AFK end-to-end controls:** unattended/AFK readiness, monitoring,
    containment or recovery.

RG1-RG9 and RG12 remain blocking in their applicable scopes. RG10 and RG11 are
non-blocking only for this minimum explanatory artifact and still block their
optional candidates. Missing applicable assurance fails closed. No App, MCP,
skill, hook, Action, tracker, database, checker extension, external store,
orchestrator or optional integration is selected.

**DI-1 is preserved:** task control, work product, verification, review,
disposition, normativity, baseline acceptance, join, cancellation and recovery
remain orthogonal; required/pass, required/unsatisfied and legitimate N/A
remain distinct.

**DI-2 is preserved:** exact-subject invalidation and item-specific freshness
remain mandatory; retry is operation-aware; containment and recovery remain
distinct; completed episode history is durable; reopening needs a distinct
qualified obligation and authority; intervention, resumption/reset and
terminal guards cannot be bypassed.

This document creates no actual task or current projection, selects no recorder
implementation, runs no checker, grants no routine, direct-main, parallel,
automated, unattended or AFK authority, resolves no RG gap and adopts no
Workflow v1 policy. Any future use remains subject to a separate exact current
gate and all accountable owner inputs.

---
artifact: research-register
artifact_status: active
maturity: bootstrap
authority: research-index
as_of: 2026-09-03
---

# Research Register

## Authority and update rule

This file is created for the first time by the bootstrap materialization. No earlier repository register or register update is claimed.

From this materialization onward, this register is the sole repository owner of mutable research status, current decision disposition, dependencies, artifact pointers, supersession, and the current next gate. Research notes retain publication-time evidence; normative artifacts retain adopted policy. Do not dual-write this state to README, AGENTS.md, chat, memory, or an external tracker without an explicit migration decision.

## Status taxonomy

| Axis | Allowed values |
|---|---|
| `artifact_status` | `draft`, `active`, `superseded`, `archived` |
| `adoption_status` | `proposed`, `accepted`, `rejected` |
| `maturity` | `bootstrap`, `v1`, `stable` |
| `authority` | `normative`, `navigation`, `research-index`, `evidence` |
| `research_status` | `planned`, `in-progress`, `completed`, `reviewed`, `superseded` |
| `current_decision_status` | `proposed`, `accepted`, `rejected`, `deferred`, `superseded` |

`artifact_status` describes artifact lifecycle, `adoption_status` applies only to normative decisions, and `maturity` is independent of both. `reviewed` means source and quality review; it does not mean policy or commit acceptance.

## Current bootstrap gate

```yaml
baseline_name: Bootstrap Context Baseline v0
baseline_status: accepted
accepted_sha: 13b05e075ec04aa91494cd18f7d29f7249028cb5
acceptance_decision_ref: ADW-BOOTSTRAP-ACCEPT-001
acceptance_record: GitHub Issue #1
branch_protection_path: PATH B
branch_protection_status: unavailable-for-private-repository-under-current-plan
review_control: temporary-manual-sha-freeze
review_control_status: completed
control_decision_ref: ADW-BOOTSTRAP-PROTECTION-DEC-001
workflow_v1_design_contract: docs/design/ADW-WF1-DESIGN-001.md
workflow_v1_design_contract_task_id: ADW-WF1-DESIGN-GATE-001
workflow_v1_design_review: docs/design/ADW-WF1-DESIGN-REVIEW-003.md
workflow_v1_design_review_task_id: ADW-WF1-DESIGN-REVIEW-003
next_gate: Workflow v1 corrected design independent review gate
```

Bootstrap Context Baseline v0 is accepted permanently at commit `13b05e075ec04aa91494cd18f7d29f7249028cb5` by decision `ADW-BOOTSTRAP-ACCEPT-001`, recorded in [GitHub Issue #1](https://github.com/ahtoxaandy999/agentic-development-workflow/issues/1). Later commits are post-baseline state and do not replace the accepted baseline.

Under protection decision `ADW-BOOTSTRAP-PROTECTION-DEC-001`, the temporary manual SHA-freeze served the independent bootstrap candidate review, which passed with no findings. That review control is now completed; it does not imply that `main` remains frozen after baseline acceptance, and it did not and does not replace branch protection.

Branch protection remains unavailable for this private repository under the current plan and configuration. It remains mandatory before routine agent writes, parallel execution, AFK execution, automated writes, or multiple maintainers or contributors.

Workflow v1 remains unadopted.

## Reviewed research and adopted disposition

```yaml
id: ADW-BOOTSTRAP-RESEARCH-001
research_status: reviewed
current_decision_status: accepted
artifact: docs/research/ADW-BOOTSTRAP-RESEARCH-001.md
evidence_as_of: 2026-09-02
adoption_ref: ADW-BOOTSTRAP-ADOPT-001
adoption_scope: >
  the adopted six-file bootstrap design, all six content contracts,
  metadata/state model, research-policy separation,
  pre-materialization authorization model,
  conditional branch-protection model,
  SHA-linked acceptance requirement,
  two-Project intended topology,
  tooling deferral to DR-005,
  and DR-001 as first post-baseline research task.
superseded_by: none
```

Artifact: [ADW-BOOTSTRAP-RESEARCH-001](ADW-BOOTSTRAP-RESEARCH-001.md).

The source review accepted this note as research evidence. The adoption reference accepted only the scope stated above. The note's publication-time recommendation remains `proposed`; this register records the later current disposition.

## Source-reviewed research with accepted coordinator disposition

```yaml
id: DR-001
question: coordinator gates and artifact lifecycle before Workflow v1
research_status: reviewed
current_decision_status: accepted
owner: agentic-development-research
artifact: docs/research/ADW-DR-001.md
dependency: accepted Bootstrap Context Baseline v0
dependency_status: satisfied
research_gate_ref: ADW-DR-001-GATE-001
research_gate_correction_ref: ADW-DR-001-GATE-CORR-001
research_started_on: 2026-09-03
evidence_as_of: 2026-09-03

review_target: "DR-001@sha256:825204b8c45da36c4c7cd087d572e0b014352aee7a6fe1c54e0772aaec6acf0f"
review_target_bytes: 66017
review_target_blob: f142919d1ed1f6b1717cc965ab9232bbc60d4389
review_target_commit: 9537e5f80af0ed04ed28bfd06573e8ef13b3ba6f

source_review_ref: docs/research/ADW-DR-001-SOURCE-REVIEW-001.md
source_review_record: "ADW-DR-001-SOURCE-REVIEW-001@sha256:fc710d1bdd3a1eba2c8fde4bd94ef7a5081ceb0a1cc0f5a0d74917173fd6deb4"
source_review_record_bytes: 17105
source_review_verdict: accepted-as-source-reviewed-evidence
source_reviewed_on: 2026-09-03
source_review_findings:
  blocker: 0
  major: 0
  minor: 1

decision_id: ADW-DR-001-DISPOSITION-001
evidence_target: "DR-001@sha256:825204b8c45da36c4c7cd087d572e0b014352aee7a6fe1c54e0772aaec6acf0f"
decided_on: 2026-09-03
decision_scope: >
  The twelve DR-001 recommendations are accepted as scoped inputs,
  semantic constraints, conditional governance principles, or later design
  inputs. This disposition does not create Workflow v1 and gains normative
  effect only through a later explicitly authorized update to the applicable
  authoritative owner.

recommendation_dispositions:
  - id: R1
    disposition: ACCEPT
    classification: semantic invariant
    accepted_scope: >
      Preserve distinct meanings for evidence, disposition, authorization,
      candidate identity, verification, review, and acceptance.
    qualification: >
      Separate artifacts, actors, or formal gates are not required universally.
    does_not_authorize: >
      Workflow v1 sequencing or mandatory heavyweight ceremony.
    later_dependency: >
      Proportionate mechanism selection during later design.
    proposed_owner_class: >
      Existing project-charter state-separation scope.

  - id: R2
    disposition: ACCEPT WITH QUALIFICATION
    classification: conditional governance principle
    accepted_scope: >
      Give each mutable authoritative state class one current owner within
      this repository and workflow control plane; treat other copies as references.
    qualification: >
      This is not asserted as a universal rule for every software system.
      Concrete storage and synchronization remain unresolved.
    does_not_authorize: >
      A tracker, storage system, synchronization design, or universal owner map.
    later_dependency: >
      State-placement and synchronization design.
    proposed_owner_class: >
      Existing authority hierarchy plus the applicable authoritative owner
      for each state class.

  - id: R3
    disposition: ACCEPT
    classification: semantic invariant
    accepted_scope: >
      Bind every formal review to an immutable candidate identity; material
      candidate changes require applicable renewed review.
    qualification: >
      Immutable identity proves content identity only.
    does_not_authorize: >
      Mandatory formal review for every task, or treating a SHA as proof of
      authorship, approval, reviewer identity, retention, or acceptance.
    later_dependency: >
      Authentication, signing, retention, and enforcement design.
    proposed_owner_class: >
      Existing project-charter candidate semantics and applicable review-record owner.

  - id: R4
    disposition: ACCEPT
    classification: semantic invariant
    accepted_scope: >
      Keep verification, review, and acceptance semantically distinct.
    qualification: >
      Conditional gates may be omitted where governance permits, but may not
      be represented as completed or conflated.
    does_not_authorize: >
      Mandatory formal review or acceptance for every task.
    later_dependency: >
      Later design of conditional gate invocation.
    proposed_owner_class: >
      Existing project-charter acceptance-semantics scope.

  - id: R5
    disposition: ACCEPT WITH QUALIFICATION
    classification: conditional governance principle
    accepted_scope: >
      Require a conflict-free reviewer whenever independence is claimed, and
      invoke independent review when consequence, uncertainty, privilege, or
      applicable governance warrants it.
    qualification: >
      No universal invocation threshold is adopted.
    does_not_authorize: >
      An independent-review gate for every task.
    later_dependency: >
      Thresholds, conflict tests, authentication, applicable governance, and enforcement.
    proposed_owner_class: >
      Existing role/authority scope plus a later adopted workflow-governance owner.

  - id: R6
    disposition: ACCEPT WITH QUALIFICATION
    classification: conditional governance principle
    accepted_scope: >
      Reserve materially consequential authorization and acceptance for an
      accountable coordinator or human risk owner. Consequence is contextual
      and includes material effects on governed policy, shared baselines,
      security or privilege, compliance, or comparable downstream reliance.
    qualification: >
      No numerical threshold is adopted, and ordinary code changes are not
      automatically consequential.
    does_not_authorize: >
      A universal human-acceptance gate.
    later_dependency: >
      Context-specific invocation and accountability design.
    proposed_owner_class: >
      Existing project-charter role, authority, and acceptance scopes.

  - id: R7
    disposition: ACCEPT WITH QUALIFICATION
    classification: conditional governance principle
    accepted_scope: >
      Preserve addressable records for material authorizations, exceptions,
      reviews, adoption, and acceptance when downstream reliance, audit,
      recovery, or cross-session coordination depends on them.
    qualification: >
      Retention duration, storage mechanism, protection strength, and concrete
      record owner remain unresolved.
    does_not_authorize: >
      Durable storage of every working note or selection of a record system.
    later_dependency: >
      Applicable governance and later retention/storage design.
    proposed_owner_class: >
      Existing research-evidence scope for research records and the applicable
      accountable decision or task owner for other record classes.

  - id: R8
    disposition: ACCEPT
    classification: conditional governance principle
    accepted_scope: >
      Tailor ceremony according to documented context and risk rather than
      task size alone.
    qualification: >
      No scoring model or threshold is adopted.
    does_not_authorize: >
      A definition of small task, normative risk score, or formal treatment
      of reversibility or blast radius.
    later_dependency: >
      Tailoring criteria require later evidence and design.
    proposed_owner_class: >
      Later adopted workflow-governance or policy owner.

  - id: R9
    disposition: ACCEPT
    classification: semantic invariant
    accepted_scope: >
      Verify a proposed enforcement control's actual availability and effective
      configuration before relying on it.
    qualification: >
      Applies at the point of reliance.
    does_not_authorize: >
      A protection product, mechanism, or compensating control.
    later_dependency: >
      Live configuration evidence and later enforcement/tooling selection.
    proposed_owner_class: >
      Applicable governance or control-policy owner.

  - id: R10
    disposition: ACCEPT WITH QUALIFICATION
    classification: semantic invariant
    accepted_scope: >
      Re-read live authoritative state at state-dependent transition gates,
      including after acceptance when subsequent current state or coordination
      depends on the accepted event.
    qualification: >
      No standalone synchronization phase is required after every task.
    does_not_authorize: >
      A concrete synchronization or dual-write architecture.
    later_dependency: >
      Identification of state-dependent gates and synchronization design.
    proposed_owner_class: >
      Applicable live-state owner plus the relevant governance owner for the rule.

  - id: R11
    disposition: ACCEPT WITH QUALIFICATION
    classification: later design input
    accepted_scope: >
      For consequential delegated execution, provide repository and authority,
      baseline/ref, objective, inputs, allowed scope, non-goals, acceptance
      criteria, verification, stop conditions, and required evidence destination.
      For independent review, provide immutable target, requirements, claimed
      scope, linked verification evidence, relevant context, criteria,
      independence expectation, stop boundary, dispositions, and a durable
      findings destination when reliance warrants it.
    qualification: >
      Categories may be combined and scaled; no fixed schema or mandatory full
      packet for trivial work is adopted.
    does_not_authorize: >
      A task schema, review schema, tracker, or document format.
    later_dependency: >
      Later workflow and packet-representation design.
    proposed_owner_class: >
      Later adopted task-contract and review-contract owner classes.

  - id: R12
    disposition: ACCEPT WITH QUALIFICATION
    classification: semantic invariant
    accepted_scope: >
      Within this repository/control-plane authority model, treat chat, memory,
      local worktrees, and handoffs as working or navigation state unless
      explicitly promoted into an authoritative owner.
    qualification: >
      These media remain useful; the restriction concerns authority and is
      not asserted universally for every system.
    does_not_authorize: >
      Discarding useful context or treating informal state as inherently invalid.
    later_dependency: >
      Promotion, provenance, and synchronization design if needed.
    proposed_owner_class: >
      Existing project-charter authority-hierarchy scope.

next_gate: Workflow v1 prerequisite-research sequencing gate
```

The durable contract and source-reviewed evidence exist at [ADW-DR-001](ADW-DR-001.md). DR-001 has completed and passed independent source review for evidence quality, and the verdict is tied to the exact frozen target `DR-001@sha256:825204b8c45da36c4c7cd087d572e0b014352aee7a6fe1c54e0772aaec6acf0f` (66017 bytes). Coordinator decision `ADW-DR-001-DISPOSITION-001` sets `current_decision_status: accepted`. All twelve recommendations are accepted within their recorded scopes and qualifications: five are `ACCEPT` and seven are `ACCEPT WITH QUALIFICATION`; none is rejected or deferred as a whole. The overbroad interpretations identified by each decision boundary are not accepted.

The recommendations are accepted inputs and constraints only. This disposition does not create Workflow v1, and `docs/research/ADW-DR-001.md` does not become normative or active through this decision. Normative effect still requires later explicit materialization into the applicable authoritative owner. The [durable review artifact](ADW-DR-001-SOURCE-REVIEW-001.md) records one non-blocking MINOR finding, which must be preserved in future use; it does not require a new frozen report target. The next gate is the Workflow v1 prerequisite-research sequencing gate.

`docs/research/ADW-DR-001.md` owns the frozen publication-time evidence. This Research Register owns mutable research status, dependencies, the artifact pointer, current decision disposition, supersession, and the next gate.

## Workflow v1 prerequisite research sequence

```yaml
decision_id: ADW-WF1-PREREQ-SEQUENCE-001
corrections:
  - ADW-WF1-PREREQ-SEQUENCE-CORR-001
  - ADW-WF1-PREREQ-SEQUENCE-CORR-002
decided_on: 2026-09-03
decision_scope: >
  Authorize DR-002 and DR-003 as independent prerequisite research tasks that
  may proceed in parallel. This decision does not start either task or design
  Workflow v1.

authorized_research:
  - id: DR-002
    canonical_question_ref: DR-002 register entry
    purpose: practitioner workflow formation and decomposition evidence
  - id: DR-003
    canonical_question_ref: DR-003 register entry
    purpose: bounded agent execution, parallelism, and autonomy-control evidence

dependency_edges:
  - ADW-DR-001-DISPOSITION-001 -> DR-002
  - ADW-DR-001-DISPOSITION-001 -> DR-003
  - DR-002 source review and coordinator disposition -> Workflow v1 design gate
  - DR-003 source review and coordinator disposition -> Workflow v1 design gate
  - initial tool-agnostic Workflow v1 design disposition -> DR-005

parallel_group:
  - DR-002
  - DR-003

initial_authorized_gates:
  - DR-002 practitioner workflow formation and decomposition research gate
  - DR-003 bounded agent execution, parallelism, and autonomy controls research gate

workflow_v1_design_readiness: >
  DR-002 and DR-003 each have an immutable evidence identity, accepted
  independent source review, durable coordinator disposition, and no
  unresolved material contradiction at their join.

dr_005_placement_decision:
  placement: after initial tool-agnostic Workflow v1 design
  required_dependency: >
    Initial tool-agnostic Workflow v1 design disposition and an explicit
    DR-005 research gate.
  reason: >
    Tool selection consumes workflow capability and enforcement requirements
    and must not define workflow semantics prematurely.

unresolved_or_deferred:
  design_time:
    - concrete lifecycle and gate mechanics
    - packet representation and possible schemas
    - state owner map and synchronization
    - candidate correction and review iteration
  tooling_stage:
    - tracker and persistence implementation
    - enforcement, identity, Apps, MCP, skills, hooks, and automation
  post_v1:
    - empirical ceremony-cost optimization
    - generally applicable retention periods
```

DR-002 and DR-003 each have accepted coordinator dispositions within their recorded scopes and qualifications. Source review established evidence quality only, and recommendation disposition does not create normative Workflow v1 rules. The prerequisite compatibility assessment passed, with no same-scope material contradiction remaining between the accepted sets. Workflow v1 remains unadopted. Invocation of the Workflow v1 design gate requires a fresh live Research Register re-read.

## Source-reviewed prerequisite research with accepted coordinator disposition

### DR-002

```yaml
id: DR-002
question: >
  Which tool-agnostic practitioner workflow patterns for question
  clarification, specification, decomposition, vertical slicing, review,
  documentation, context transitions, and qualitative proportionality should
  constrain Workflow v1?
research_status: reviewed
current_decision_status: accepted
owner: agentic-development-research
artifact: docs/research/ADW-DR-002.md
evidence_as_of: 2026-09-03
review_target: "DR-002@sha256:5458020be85cde909705fc1fbbc489c98e43ce0b6c058f6fd5d67901dc1ecb03"
review_target_bytes: 46593
evidence_family: practitioner workflow patterns (Family A)
dependency: ADW-DR-001-DISPOSITION-001
dependency_status: satisfied
parallel_with: DR-003
research_gate_ref: ADW-DR-002-GATE-001
research_started_on: 2026-09-03
decision_consumer: Workflow v1 design gate
source_review_required: true
coordinator_disposition_required: true
source_review_ref: docs/research/ADW-DR-002-SOURCE-REVIEW-001.md
source_review_record: "ADW-DR-002-SOURCE-REVIEW-001@sha256:c1ab54d5ccf1e6cd42c28fe4a2edb13d764150d7c2003ad4a50bcddba332b2b8"
source_review_record_bytes: 12332
source_review_verdict: accepted-as-source-reviewed-evidence
source_reviewed_on: 2026-09-03
source_review_findings:
  blocker: 0
  major: 0
  minor: 1

decision_id: ADW-DR-002-003-DISPOSITION-001
decision_target: "DR-002@sha256:5458020be85cde909705fc1fbbc489c98e43ce0b6c058f6fd5d67901dc1ecb03"
decided_on: 2026-09-03
decision_scope: >
  Accept DR-002 R1 through R9 only within their recorded scopes and
  qualifications as Workflow v1 constraints, conditional principles, or later
  design inputs. This disposition does not itself create or materialize
  Workflow v1.

recommendation_dispositions:
  - id: R1
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 constraint - conditional readiness
    accepted_scope: >
      Require sufficient clarification of outcome, authority, scope,
      constraints, assumptions, interfaces, material unknowns, and observable
      acceptance conditions before the next bounded specification or execution
      commitment.
    qualification: >
      Readiness is contextual. Unknowns may be resolved, bounded into learning
      work, or recorded as blockers; no universal checklist or complete-up-front
      requirement follows.
    does_not_authorize: >
      A fixed readiness schema, mandatory ceremony, lifecycle sequence, or
      universal minimum document.
    later_dependency: >
      Workflow v1 readiness and escalation design.
    proposed_owner_class: >
      Later adopted workflow-governance/task-readiness owner; concrete artifact
      is design-time unresolved.

  - id: R2
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 semantic constraint
    accepted_scope: >
      Judge specification sufficiency by whether a qualified executor can
      proceed without inventing material intent and whether the result can be
      verified.
    qualification: >
      Controlled refinement remains permitted; applicable safety, regulatory,
      or governance contexts may require fuller baselines.
    does_not_authorize: >
      A universal document size, format, completeness threshold, or rejection
      of up-front baselines where required.
    later_dependency: >
      Context-specific readiness and verification design.
    proposed_owner_class: >
      Later adopted workflow-governance/task-contract owner.

  - id: R3
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 constraint - conditional decomposition
    accepted_scope: >
      Require units to be coherent, outcome-traceable, bounded at interfaces,
      dependency-aware, independently understandable, and verifiable at their
      stated boundary.
    qualification: >
      Unit size and independent schedulability remain contextual; unavoidable
      coupling is permitted when explicit.
    does_not_authorize: >
      A universal unit size, batch target, task schema, or requirement that
      every unit run independently.
    later_dependency: >
      Decomposition, dependency, and recomposition design.
    proposed_owner_class: >
      Later adopted task/decomposition owner; concrete representation is
      design-time unresolved.

  - id: R4
    disposition: ACCEPT WITH QUALIFICATION
    classification: Later design input - conditional slicing preference
    accepted_scope: >
      Prefer observable vertical slices when behavioral, user, or end-to-end
      learning feedback is the objective.
    qualification: >
      Vertical slicing is not universally superior. Explicit enabling,
      infrastructure, risk-reduction, or learning work remains legitimate when
      a valuable vertical slice is incoherent or uneconomic.
    does_not_authorize: >
      Mandatory vertical slicing, user-visible output for every unit, or a ban
      on horizontal/enabling work.
    later_dependency: >
      Workflow v1 decomposition guidance and applicability criteria.
    proposed_owner_class: >
      Later adopted task/decomposition owner; otherwise design-time unresolved.

  - id: R5
    disposition: ACCEPT
    classification: Workflow v1 semantic constraint
    accepted_scope: >
      Make dependencies, interfaces, integration/recomposition points, and
      local versus integrated verification boundaries explicit during
      decomposition.
    qualification: >
      None beyond the accepted scope; exact ordering remains a later mechanism
      choice.
    does_not_authorize: >
      A scheduler, integration algorithm, topology, worktree strategy, or
      sequencing rule.
    later_dependency: >
      Workflow v1 dependency and integration design.
    proposed_owner_class: >
      Later adopted task/dependency and integration owner.

  - id: R6
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 constraint - feedback semantics with conditional invocation
    accepted_scope: >
      Preserve distinct purposes for formation review, execution verification,
      peer review, integration validation, and outcome review, and provide
      reviewers enough intent and change context.
    qualification: >
      No universal reviewer count, formal-review invocation rule, or claim that
      peer review alone assures correctness.
    does_not_authorize: >
      Mandatory formal or independent review for every task, a reviewer-count
      threshold, or conflation with verification or acceptance.
    later_dependency: >
      Conditional review invocation, independence, and correction-loop design.
    proposed_owner_class: >
      Existing Charter review/acceptance semantics plus a later adopted
      workflow-governance owner.

  - id: R7
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 governance constraint within this control plane
    accepted_scope: >
      Preserve information durably when downstream reliance, authority, audit,
      recovery, or cross-session coordination depends on it; disposable working
      detail may remain ephemeral.
    qualification: >
      Scoped to this repository/workflow control plane. No universal retention
      duration, representation, protection strength, or rule for every working
      note follows.
    does_not_authorize: >
      Universal retention, exhaustive logging, duplicate state stores, or
      selection of a tracker or storage system.
    later_dependency: >
      Retention, state placement, protection, and synchronization design.
    proposed_owner_class: >
      Existing Research Register/research-evidence owners for research state;
      otherwise the applicable authoritative decision/task owner, with concrete
      non-research classes design-time unresolved.

  - id: R8
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 constraint - fresh-context transition
    accepted_scope: >
      For consequential fresh-practitioner or fresh-agent transitions, preserve
      sufficient objective, authority, baseline, progress, decisions,
      dependencies, verification, uncertainty, and safe-next-action context
      while retaining authoritative source pointers.
    qualification: >
      Human-to-agent transfer remains partly inferential. This is a content
      constraint, not a fixed packet schema; execution-control semantics remain
      governed by DR-003.
    does_not_authorize: >
      Agent autonomy, a handoff schema, promotion of summaries to authority, or
      any execution mechanism.
    later_dependency: >
      DR-003 accepted controls and later handoff/rehydration design.
    proposed_owner_class: >
      Later task/delegation-context owner; concrete artifact is design-time
      unresolved.

  - id: R9
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 conditional governance principle
    accepted_scope: >
      Tailor clarification, documentation, review, integrated verification, and
      correction safeguards using context, consequence, uncertainty,
      reversibility, and affected scope.
    qualification: >
      These are qualitative inputs only. No numerical weights, thresholds,
      universal small-task exemption, or controlling reversibility rule is
      supported.
    does_not_authorize: >
      A risk score, automatic eligibility rule, numeric threshold, or removal
      of otherwise applicable controls.
    later_dependency: >
      Context-specific tailoring criteria and accountable invocation design.
    proposed_owner_class: >
      Later adopted workflow-governance or risk-policy owner.

source_review_finding_treatment: >
  The single DR-002 MINOR concerns historical pre-freeze process wording only.
  Current front matter, immutable freeze identity, and the Register disambiguate
  state. It does not narrow any recommendation and does not require a new
  frozen target.

next_gate: Workflow v1 design gate
```

### DR-003

```yaml
id: DR-003
question: >
  Which tool-agnostic execution-control requirements are necessary for
  bounded agent delegation, parallel work, state freshness, context handoffs,
  observability, correction/review waves, unattended execution, stopping,
  and recovery?
research_status: reviewed
current_decision_status: accepted
owner: agentic-development-research
artifact: docs/research/ADW-DR-003.md
evidence_as_of: 2026-09-03
review_target: "DR-003@sha256:8017e5fbe1ee7b2d7ad92ba76b89e69dc2b51c52e0d56c650a293e99e63b0d46"
review_target_bytes: 75710
evidence_family: OpenAI agent/harness execution patterns plus parallelism and autonomy controls (Families B+C)
dependency: ADW-DR-001-DISPOSITION-001
dependency_status: satisfied
parallel_with: DR-002
research_gate_ref: ADW-DR-003-GATE-001
research_started_on: 2026-09-03
decision_consumer: Workflow v1 design gate
source_review_required: true
coordinator_disposition_required: true
source_review_ref: docs/research/ADW-DR-003-SOURCE-REVIEW-001.md
source_review_record: "ADW-DR-003-SOURCE-REVIEW-001@sha256:5b548b5fa2943b1d6faebef89acfad66359b7146b706726456f360048fc1ea3b"
source_review_record_bytes: 10908
source_review_verdict: accepted-as-source-reviewed-evidence
source_reviewed_on: 2026-09-03
source_review_findings:
  blocker: 0
  major: 0
  minor: 3

decision_id: ADW-DR-002-003-DISPOSITION-001
decision_target: "DR-003@sha256:8017e5fbe1ee7b2d7ad92ba76b89e69dc2b51c52e0d56c650a293e99e63b0d46"
decided_on: 2026-09-03
decision_scope: >
  Accept DR-003 PR01 through PR12 only within their recorded scopes and
  qualifications as tool-agnostic Workflow v1 constraints or later design
  inputs. This disposition grants no autonomy, implementation, tooling, or
  normative Workflow v1 authority.

recommendation_dispositions:
  - id: PR01
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 bounded-delegation constraint
    accepted_scope: >
      Require consequential or otherwise nontrivial delegation to carry
      sufficient authority, objective, immutable inputs, allowed scope/actions,
      constraints, evidence destination, validation, ceilings, stopping, and
      escalation information, scaled to context and risk.
    qualification: >
      No fixed packet schema or universal nontrivial threshold follows; fields
      may be combined or omitted when their semantic information is genuinely
      unnecessary.
    does_not_authorize: >
      A task schema, packet format, tracker, mandatory full packet for trivial
      work, or delegated authority beyond the recorded scope.
    later_dependency: >
      Task-contract representation and proportionality design.
    proposed_owner_class: >
      Later adopted task/delegation-contract owner.

  - id: PR02
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 freshness and identity constraint
    accepted_scope: >
      Pin and reverify each authoritative identity or effective-configuration
      dimension actually relied upon at state-dependent dispatch, join,
      publication, review, acceptance, or resumption transitions.
    qualification: >
      Identity establishes the identified object or configuration claim only;
      it does not establish authority, approval, correctness, availability,
      retention, or trust.
    does_not_authorize: >
      Pinning every possible dimension, trusting a digest or actor name, or
      selecting an attestation/configuration mechanism.
    later_dependency: >
      Identification of state-dependent transitions and later
      enforcement/tooling evidence.
    proposed_owner_class: >
      Applicable live-state owner plus the later workflow/control-policy owner.

  - id: PR03
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 conditional parallel-execution constraint
    accepted_scope: >
      Permit parallel execution only for independent/read-only work, isolated
      outputs, proposal-only contributors under one authoritative writer, or
      shared writes protected by enforceable version/conflict controls.
    qualification: >
      Independence depends on explicit read/write sets, side effects,
      invariants, and dependencies. No universal safe concurrency number
      exists.
    does_not_authorize: >
      A concurrency count, parallel-wave algorithm, recursive delegation, or
      unconstrained shared mutation.
    later_dependency: >
      Task/environment-specific ceilings and coordination design.
    proposed_owner_class: >
      Later adopted execution-coordination owner.

  - id: PR04
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 isolation and join constraint
    accepted_scope: >
      Require isolated output/side-effect domains as applicable, one owner for
      each mutable authority and aggregation responsibility, complete result
      accounting, exact identities, validation state, freshness checks, and
      explicit partial/failure/conflict handling at joins.
    qualification: >
      Central, hierarchical, and distributed aggregation remain alternatives;
      no topology is selected.
    does_not_authorize: >
      An aggregation architecture, scheduler, workspace mechanism, or silent
      success when a required result is absent.
    later_dependency: >
      Join semantics, aggregation topology, and isolation implementation design.
    proposed_owner_class: >
      Existing applicable authoritative state owners; aggregation/join owner is
      design-time unresolved.

  - id: PR05
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 handoff and rehydration constraint
    accepted_scope: >
      Treat handoffs and summaries as navigation state; retain exact
      authoritative pointers and material task state, and require rehydration
      and critical-identity validation before loss-sensitive state-dependent
      action.
    qualification: >
      No prose summary or compaction process is assumed lossless; more history
      is not automatically safer.
    does_not_authorize: >
      Promotion of summaries to authority, full-history retention, a handoff
      schema, or reliance on stale cached context.
    later_dependency: >
      Handoff representation, loss-sensitive field selection, and tooling
      validation.
    proposed_owner_class: >
      Later task/delegation-context owner; referenced authoritative facts remain
      with their existing owners.

  - id: PR06
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 observability/evidence constraint
    accepted_scope: >
      Require enough protected, secret-safe evidence to reconstruct relied-upon
      run state, authority, identities, side effects, progress, resource use,
      failure/retry/cancellation, outputs, and validation.
    qualification: >
      This is an outcome obligation, not an exhaustive logging schema.
      Retention, logging, sampling, instrumentation, integrity, and storage
      remain unresolved.
    does_not_authorize: >
      Full-fidelity capture, sensitive payload retention, a log store, tracing
      product, or universal retention period.
    later_dependency: >
      Evidence-minimum, access, redaction, retention, and instrumentation
      design.
    proposed_owner_class: >
      Applicable accountable run/evidence owner; concrete owner is design-time
      unresolved.

  - id: PR07
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 candidate-correction and re-review constraint
    accepted_scope: >
      Give each corrected formal candidate a new immutable identity, record the
      change and affected scope, rerun affected verification, and renew
      applicable independent review when its target or a load-bearing
      assumption changed.
    qualification: >
      Materiality is relational and contextual, not a line-count or numeric
      threshold; unaffected scope may carry forward only when demonstrated.
    does_not_authorize: >
      Self-review, self-acceptance, a numeric materiality rule, or treating prior
      review as applying automatically to changed content.
    later_dependency: >
      Impact-analysis and conditional re-review design.
    proposed_owner_class: >
      Existing Charter candidate/review semantics plus the applicable
      review-record and later workflow-governance owner.

  - id: PR08
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 necessary-evidence constraint for unattended eligibility
    accepted_scope: >
      Use bounded authority, freshness, isolation, least privilege, semantic
      side-effect safety, enforceable ceilings, observability,
      cancellation/containment, recovery, and accountable intervention as
      necessary evidence categories before unattended operation may be
      considered.
    qualification: >
      This is only a conservative necessary-evidence screen. It is not proof of
      sufficient safety, automatic eligibility, or a universal threshold.
      Consequential classes remain ineligible without task-specific evidence
      and explicit authorization.
    does_not_authorize: >
      Unattended execution, AFK writes, privileged/destructive/external
      mutation, a categorical eligibility rule, or numeric ceilings.
    later_dependency: >
      Task-specific risk authorization, Workflow v1 eligibility design, and
      later mechanism/configuration evidence.
    proposed_owner_class: >
      Accountable authorization/risk-control owner; concrete authoritative
      artifact is design-time unresolved.

  - id: PR09
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 stop and containment constraint
    accepted_scope: >
      Require explicit stop/escalation triggers and treat cancellation as
      request, acknowledgement, and verified containment across relevant
      side-effect boundaries.
    qualification: >
      A cancellation request is not containment. Mechanism-specific kill,
      revocation, queue, subprocess, and external-effect semantics must be
      tested later.
    does_not_authorize: >
      Assuming synchronous cancellation, declaring success on request issuance,
      or selecting a cancellation mechanism.
    later_dependency: >
      Mechanism-specific interruptibility, inspection, quarantine, and
      reconciliation design.
    proposed_owner_class: >
      Later execution-control owner plus the accountable side-effect owner.

  - id: PR10
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 operation-aware recovery constraint
    accepted_scope: >
      Classify operation semantics before retry and apply stable identifiers,
      deduplication, version preconditions, checkpoints, isolated/atomic
      publication, reconciliation, or authorized compensation as applicable.
    qualification: >
      Retry and compensation are conditional effects. Irreversible, externally
      visible, nondeterministic, or ambiguously completed operations retain
      residual risk and may require accountable intervention.
    does_not_authorize: >
      Arbitrary rollback, blind retry, a retry count, or an assertion that
      compensation restores prior reality.
    later_dependency: >
      Domain-specific side-effect classification, recovery ownership, and
      mechanism selection.
    proposed_owner_class: >
      Applicable state/side-effect owner plus the later execution-recovery
      owner.

  - id: PR11
    disposition: ACCEPT WITH QUALIFICATION
    classification: Workflow v1 security, identity, and provenance constraint
    accepted_scope: >
      Keep authentication, authorization, approval, identity, provenance,
      review independence, and correctness distinct; enforce per-task least
      privilege and secret-safe, expectation-checked evidence.
    qualification: >
      No identity, credential, signing, attestation, trust-root, retention, or
      provenance implementation is selected. Identity or signature alone does
      not prove authority, approval, correctness, or trust.
    does_not_authorize: >
      Credential forwarding, ambient privilege, a provider/system choice, or
      trust based solely on names, digests, signatures, or traces.
    later_dependency: >
      Identity, credential, reviewer-authentication, trust-policy, redaction,
      and tooling research.
    proposed_owner_class: >
      Existing Charter authority/security scope plus a later
      identity/provenance control owner; concrete owner is design-time
      unresolved.

  - id: PR12
    disposition: ACCEPT
    classification: Research-to-design boundary constraint
    accepted_scope: >
      Carry accepted requirements forward as outcome and evidence obligations
      while deferring sequencing, schemas, numeric limits, topology, products,
      credentials, storage, tracking, and automation to their authorized gates.
    qualification: >
      None beyond the stated requirement/mechanism boundary.
    does_not_authorize: >
      Workflow v1 design, DR-005, tooling selection, implementation, or
      validation of any future mechanism.
    later_dependency: >
      Separate Workflow v1 design disposition, followed by DR-005 only through
      its explicit gate.
    proposed_owner_class: >
      Research Register owns current disposition; later normative owner classes
      are design-time unresolved.

source_review_finding_treatment:
  - >
    E02 author attribution should use Qiuyuan Ai and coauthors in later
    downstream citation handling; substantive support remains intact.
  - >
    E05 downstream citation handling should preserve the corrected
    title/version/publication provenance; substantive support remains intact.
  - >
    NIST SP 800-53 Release 5.2.0 downstream citation handling should preserve
    August 27, 2025 as the issuance date; control attribution remains intact.

next_gate: Workflow v1 design gate
```

These findings do not require changes to the frozen report or source-review record.

### Prerequisite research join

```yaml
decision_id: ADW-DR-002-003-DISPOSITION-001
decided_on: 2026-09-03
join_verdict: PREREQUISITE RESEARCH JOIN PASS
dr_002_target: "DR-002@sha256:5458020be85cde909705fc1fbbc489c98e43ce0b6c058f6fd5d67901dc1ecb03"
dr_003_target: "DR-003@sha256:8017e5fbe1ee7b2d7ad92ba76b89e69dc2b51c52e0d56c650a293e99e63b0d46"
compatibility:
  clarification_and_bounded_delegation: compatible/complementary
  decomposition_parallelism_and_join: compatible-with-design-time-boundary
  review_correction_and_rereview: compatible/complementary
  durability_observability_and_provenance: compatible-with-design-time-boundary
  fresh_context_handoff_and_rehydration: compatible/complementary
  proportionality_and_unattended_controls: compatible-with-design-time-boundary
material_contradiction: none
design_gate_condition: >
  Workflow v1 design gate is eligible only after this disposition state is
  durably persisted and a fresh live Research Register re-read confirms both
  accepted dispositions and the join remains current.
```

DR-004 is intentionally not registered. No tooling, tracker, task schema, or review schema is selected.

## Deferred research

```yaml
id: DR-005
question: tooling evaluation and selection
research_status: planned
current_decision_status: deferred
dependency: initial tool-agnostic Workflow v1 design disposition and an explicit DR-005 research gate
dependency_status: unsatisfied
placement: after initial tool-agnostic Workflow v1 design
```

DR-005 remains deferred until after initial tool-agnostic Workflow v1 design. No App, MCP server, skill, hook, connector workflow, or automation is selected by this entry.

## Superseded

None.

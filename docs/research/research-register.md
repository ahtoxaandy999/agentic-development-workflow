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
next_gate: independent DR-002 and DR-003 evidence completion and exact-byte freeze gates
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

DR-002 and DR-003 are now in progress from the same durable authorization base. They remain independent and may conduct read-only evidence production in parallel. Each has its own contract, freeze target, source review, and later coordinator disposition. This does not authorize concurrent direct writes to `main`. Workflow v1 design still waits for both completed and disposed research streams.

## In-progress prerequisite research

### DR-002

```yaml
id: DR-002
question: >
  Which tool-agnostic practitioner workflow patterns for question
  clarification, specification, decomposition, vertical slicing, review,
  documentation, context transitions, and qualitative proportionality should
  constrain Workflow v1?
research_status: in-progress
owner: agentic-development-research
artifact: docs/research/ADW-DR-002.md
evidence_family: practitioner workflow patterns (Family A)
dependency: ADW-DR-001-DISPOSITION-001
dependency_status: satisfied
parallel_with: DR-003
research_gate_ref: ADW-DR-002-GATE-001
research_started_on: 2026-09-03
decision_consumer: Workflow v1 design gate
source_review_required: true
coordinator_disposition_required: true
next_gate: DR-002 evidence completion and exact-byte freeze gate
```

### DR-003

```yaml
id: DR-003
question: >
  Which tool-agnostic execution-control requirements are necessary for
  bounded agent delegation, parallel work, state freshness, context handoffs,
  observability, correction/review waves, unattended execution, stopping,
  and recovery?
research_status: in-progress
owner: agentic-development-research
artifact: docs/research/ADW-DR-003.md
evidence_family: OpenAI agent/harness execution patterns plus parallelism and autonomy controls (Families B+C)
dependency: ADW-DR-001-DISPOSITION-001
dependency_status: satisfied
parallel_with: DR-002
research_gate_ref: ADW-DR-003-GATE-001
research_started_on: 2026-09-03
decision_consumer: Workflow v1 design gate
source_review_required: true
coordinator_disposition_required: true
next_gate: DR-003 evidence completion and exact-byte freeze gate
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

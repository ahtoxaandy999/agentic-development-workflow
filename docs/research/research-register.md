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
next_gate: DR-001 recommendation-disposition gate
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

## Source-reviewed research awaiting coordinator disposition

```yaml
id: DR-001
question: coordinator gates and artifact lifecycle before Workflow v1
research_status: reviewed
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
source_review_ref: docs/research/ADW-DR-001-SOURCE-REVIEW-001.md
source_review_record: "ADW-DR-001-SOURCE-REVIEW-001@sha256:fc710d1bdd3a1eba2c8fde4bd94ef7a5081ceb0a1cc0f5a0d74917173fd6deb4"
source_review_record_bytes: 17105
source_review_verdict: accepted-as-source-reviewed-evidence
source_reviewed_on: 2026-09-03
source_review_findings:
  blocker: 0
  major: 0
  minor: 1
next_gate: DR-001 recommendation-disposition gate
```

The durable contract and source-reviewed evidence exist at [ADW-DR-001](ADW-DR-001.md). DR-001 has passed independent source review for evidence quality, and the verdict is tied to the exact frozen target `DR-001@sha256:825204b8c45da36c4c7cd087d572e0b014352aee7a6fe1c54e0772aaec6acf0f` (66017 bytes). The [durable review artifact](ADW-DR-001-SOURCE-REVIEW-001.md) records one non-blocking MINOR finding; it does not require a new frozen report target. DR-001 recommendations remain proposed and non-normative. The next gate is coordinator recommendation disposition.

`docs/research/ADW-DR-001.md` owns the frozen publication-time evidence. This Research Register owns mutable research status, dependencies, the artifact pointer, current decision disposition, supersession, and the next gate.

## Deferred research

```yaml
id: DR-005
question: tooling evaluation and selection
research_status: planned
current_decision_status: deferred
dependency: DR-001 disposition and an explicit DR-005 research gate
```

No App, MCP server, skill, hook, connector workflow, or automation is selected by this entry.

## Superseded

None.

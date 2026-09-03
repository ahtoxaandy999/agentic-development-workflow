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
branch_protection_path: PATH B
branch_protection_status: unavailable-for-private-repository-under-current-plan
review_control: temporary-manual-sha-freeze
control_decision_ref: ADW-BOOTSTRAP-PROTECTION-DEC-001
next_gate: independent candidate review under temporary manual SHA-freeze
```

The coordinator adopted this temporary manual SHA-freeze because the required branch-protection capability is unavailable for this private repository under the current plan and configuration. The control applies only to independent review of the bootstrap candidate.

During independent candidate review:

1. Remote `main` must remain pinned to the exact candidate SHA reported by this execution.
2. No pushes to `main` are permitted.
3. No force pushes are permitted.
4. No GitHub web edits are permitted.
5. No merges are permitted.
6. No Codex repository writes are permitted.
7. No ChatGPT or GitHub connector writes are permitted.
8. The reviewer must verify remote `main` immediately before review.
9. The reviewer must review that exact full SHA.
10. The reviewer must verify remote `main` again immediately after review.
11. Any SHA change invalidates the review.

The manual SHA-freeze is temporary and bootstrap-specific. It does not replace branch protection. Branch protection must be revisited before routine agent writes, parallel execution, AFK execution, automated writes, or multiple maintainers or contributors.

The candidate SHA is not reviewed or accepted by this entry.

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

## Planned research

```yaml
id: DR-001
question: coordinator gates and artifact lifecycle before Workflow v1
research_status: planned
dependency: accepted Bootstrap Context Baseline v0
blocked_until: accepted Bootstrap Context Baseline v0
```

DR-001 is the first post-baseline research task. It has not started and is blocked until the baseline is explicitly accepted.

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

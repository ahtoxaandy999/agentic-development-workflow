# Repository role

This repository is the versioned, cross-project control plane for the Agentic Development Workflow. It is not a product repository or an automatic second task tracker.

# Authority and read order

1. Read [PROJECT-CHARTER.md](PROJECT-CHARTER.md) for mission, scope, roles, authority, and the bootstrap safety floor.
2. Read [docs/policies/research-evidence.md](docs/policies/research-evidence.md) before producing or promoting research.
3. Read [docs/research/research-register.md](docs/research/research-register.md) for current research state and the next gate.

Current repository artifacts outrank chat, memory, summaries, and handoffs. Those sources are navigation aids only. Research reports are evidence; they do not modify normative policy unless an explicit adoption decision names the target artifact and adoption scope. Repository use additionally requires an accepted baseline SHA.

# Current maturity

The repository is at bootstrap maturity. Workflow v1 is not adopted. Do not infer workflow phases, task state, tool choices, or implementation authority from planned or research material. The Research Register owns the current work and next gate.

# Agent boundaries

- Work only within the explicitly authorized task and repository scope.
- Do not create policy, architecture, workflow mechanics, task schemas, or speculative directories without an explicit adoption gate.
- Do not select or install Apps, MCP servers, skills, hooks, or automation, and do not make broad connector writes, without an explicit later gate.
- Do not expose, commit, or transmit secrets or unnecessary sensitive data.
- Preserve the separation between evidence, normative policy, mutable research state, and commit acceptance state.

# Verification and acceptance

Reverify live repository and platform state before state-dependent work. A local clone, memory, report, or uploaded snapshot is not proof of current remote state.

Tests, checks, a commit, or a pull request do not imply acceptance. Candidate identity requires the exact full commit SHA. Independent review and explicit coordinator acceptance are separate gates.

# Escalation

Stop and escalate ambiguity, conflicting authority, stale or unverifiable state, scope expansion, or any condition that would require inventing policy. Do not resolve authority conflicts by assumption.

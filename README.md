# Agentic Development Workflow

This repository is the durable, versioned control plane for a cross-project Agentic Development Workflow. It provides a small authoritative base for coordination, evidence governance, decision boundaries, and navigation across projects without copying product repositories or their task state.

## Current maturity

The repository is at **bootstrap** maturity. The bootstrap establishes only the context and governance floor needed for later research and adoption. Workflow v1 is not adopted, and this repository does not yet define workflow phases, task mechanics, parallel execution, AFK operation, or a tooling stack.

A file being active or a normative decision being adopted does not make a repository commit an accepted baseline. Candidate review and coordinator acceptance remain separate, exact-SHA gates.

## Purpose

The repository exists to make shared workflow authority durable, reviewable, and addressable by commit SHA. It separates four concerns that are easy to conflate:

- normative mission, scope, roles, and safety boundaries;
- rules for producing and promoting research evidence;
- mutable research and adoption disposition;
- candidate, review, and baseline acceptance state tied to exact commits.

This separation lets coordinators and bounded agents find the current owner of a claim without relying on historical chat, memory, or handoff summaries.

## Start here

1. Read the [Project Charter](PROJECT-CHARTER.md) for the repository mission, boundaries, roles, authority hierarchy, and acceptance principles.
2. Read the [Research Evidence Policy](docs/policies/research-evidence.md) before starting research or using research to support a decision.
3. Read the [Research Register](docs/research/research-register.md) for current research state, adoption disposition, dependencies, and the next gate.
4. Consult the [bootstrap research note](docs/research/ADW-BOOTSTRAP-RESEARCH-001.md) only when its publication-time evidence and reasoning are needed. The note is evidence, not policy.

## Protected supervised publication

Separately authorized supervised writes follow the [protected publication path](docs/design/ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-OPERATIONAL-USE-SCOPING-001.md): a bounded candidate branch, draft PR, exact-candidate independent review, coordinator acceptance and separately authorized merge. The [Research Register](docs/research/research-register.md) remains the sole owner of the mutable current gate.

Using this mechanism does not authorize a substantive repository change. Direct-main, routine, parallel, automated, unattended and AFK writes remain unauthorized. Workflow v1 remains unadopted.

## Authority map

| Artifact | Role |
|---|---|
| [Project Charter](PROJECT-CHARTER.md) | Normative owner of mission, scope, roles, authority, and the bootstrap safety floor |
| [Research Evidence Policy](docs/policies/research-evidence.md) | Normative owner of research quality, review, adoption separation, freshness, and supersession |
| [Research Register](docs/research/research-register.md) | Sole repository owner of mutable research state, current decision disposition, dependencies, and the current next gate |
| [Bootstrap research note](docs/research/ADW-BOOTSTRAP-RESEARCH-001.md) | Source-reviewed publication-time evidence snapshot and reasoning |
| `AGENTS.md` | Concise agent-facing navigation and hard-boundary map |

Committed and current repository artifacts are the durable authority for their scopes. Chat, project memory, uploaded copies, summaries, and handoffs can point to that authority but cannot replace it. State-dependent work must also verify the live repository and exact commit rather than infer current state from a stored copy.

## What belongs here

- adopted cross-project workflow premises and governance boundaries;
- concise navigation to authoritative artifacts;
- source-reviewed research notes with durable publication metadata;
- a compact index of research state, dependencies, adoption disposition, and gates;
- later workflow or tooling artifacts only after their own explicit research, ownership, and adoption gates.

## What does not belong here

- product code, product architecture, or project-specific implementation rules;
- an automatic duplicate of issues, plans, or task state owned elsewhere;
- historical chat transcripts, memory exports, or handoff archives;
- secrets, credentials, production identities, or unnecessary sensitive data;
- speculative architecture, ADR, context, task, tooling, hook, or automation structures;
- unadopted research recommendations presented as policy.

## Current work

See the [Research Register](docs/research/research-register.md) for current research state and the next gate. This landing page intentionally does not duplicate mutable status.

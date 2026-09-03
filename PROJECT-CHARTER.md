---
artifact: project-charter
artifact_status: active
adoption_status: accepted
maturity: bootstrap
authority: normative
owner: repository-maintainer
---

# Project Charter

## Status and authority

This charter is the normative owner of the repository mission, scope, non-scope, roles, authority hierarchy, bootstrap safety floor, acceptance principles, and amendment boundary. Its content was adopted before materialization. The metadata records artifact lifecycle, decision disposition, and maturity; it does not state that the containing commit is a reviewed or accepted baseline.

## Mission

The Agentic Development Workflow repository is a durable, versioned, cross-project workflow control plane. It makes shared coordination rules, evidence boundaries, adopted decisions, and navigation addressable by exact Git commit SHA. It supports coordinators and bounded agents while keeping policy, evidence, mutable state, and commit acceptance distinct.

## Scope

This repository may own:

- adopted cross-project premises and governance boundaries for agentic development;
- normative policies with an explicit owner and adoption decision;
- source-reviewed research evidence and its publication-time metadata;
- a single mutable index of research state and current adoption disposition;
- navigation that directs humans and agents to the authoritative owner of each claim;
- later shared workflow or tooling artifacts only after an explicit research, ownership, and adoption gate.

Repository artifacts provide a common baseline for multiple projects. Project-specific repositories remain responsible for their product code, architecture, delivery constraints, and execution state.

## Non-scope

This is not a product repository. It does not own product implementation, product architecture, or project-specific operating rules.

It is not automatically a second task tracker. A task or research state must have one current owner; no Markdown file, external tracker, Project memory, or chat may be maintained as an unapproved duplicate.

Bootstrap adoption does not define Workflow v1. It does not establish workflow phases, a task schema, planning mechanics, a parallel-wave algorithm, AFK execution, implementation commands, project adapters, or tool-selection rules.

The repository is not a catalog of available Apps, MCP servers, skills, hooks, connectors, or automation. Availability is not adoption, and a later artifact may select tooling only through its own explicit gate.

## Roles

### ChatGPT coordinator

The ChatGPT coordinator frames decisions, confirms scope and authority, adopts or rejects normative recommendations, and makes explicit acceptance decisions. Adoption and acceptance must name their subject precisely. The coordinator does not turn unreviewed research or implicit chat agreement into repository policy.

### Repository maintainer

The repository maintainer preserves the integrity, discoverability, and current ownership of repository artifacts; verifies repository operations; and executes authorized administrative changes. Maintenance authority does not authorize new workflow policy or self-acceptance of a candidate.

### Bounded agents

Agents may act as executors, researchers, or reviewers only within an explicit assignment. They must observe the applicable repository authority, reverify state-dependent facts, preserve scope, and surface ambiguity or conflict. They may not broaden their own authority, silently promote evidence, invent missing policy, or treat their own output as accepted.

An independent reviewer evaluates the assigned evidence or exact candidate SHA. Review establishes only the state named by the review gate; it is not coordinator adoption or baseline acceptance.

## Authority hierarchy

For a specific claim, apply the highest relevant current owner:

1. live connected repository state, the exact commit or diff, and effective GitHub protection state for claims about current repository state;
2. accepted and current repository charter, policies, architecture, or decision records within their scopes;
3. an accepted task contract in the selected task owner for task-specific scope;
4. a source-reviewed research note as evidence, with current research and decision disposition taken from the Research Register;
5. runtime or Project instructions that point to an exact repository baseline;
6. chat, memory, summaries, snapshots, and handoffs as non-authoritative navigation aids.

Repository artifacts are durable authority for the scopes they own. A lower level cannot amend a higher level. A copied or remembered artifact does not establish live state, and a stale artifact cannot support a state-dependent gate.

When two artifacts appear to own the same state or conflict, work stops until the accountable owner resolves the conflict. Convenience, tool output, or agent confidence is not a substitute for authority.

## Research and policy separation

Research produces evidence, inference, and recommendations. It does not change normative policy by publication, source review, completion, citation quality, or inclusion in the repository.

A normative change requires an explicit adoption decision that identifies the recommendation, target artifact, and adoption scope, followed by a faithful update to the normative owner. Publication-time research metadata remains a historical snapshot. The Research Register alone owns mutable research status and current decision disposition after materialization.

Silent research-to-policy promotion is prohibited.

## Bootstrap safety floor

All work must remain within an explicit repository and task scope. State-dependent operations must verify live state through an appropriate connected repository, Git, or API surface before mutation. Local clones, uploaded snapshots, chat, memory, and prior reports are insufficient proof of current remote state.

Secrets, credentials, tokens, production identities, and unnecessary sensitive data must not be committed or copied into research, prompts, handoffs, or logs. Access must be limited to what the authorized task requires.

Broad connector writes and the adoption, installation, or configuration of Apps, MCP servers, skills, hooks, automation, or other tooling require an explicit later gate. Tool availability, advertised capability, provider permission, and interface approval are distinct and do not grant one another authority.

Agents must stop on ambiguity, stale or unverifiable state, authority conflict, unexpected repository content, or a required scope expansion. They must escalate rather than invent policy or a workaround that changes the adopted boundary.

## Acceptance semantics

Normative adoption, artifact lifecycle, and commit acceptance are separate state planes.

A candidate is identified by its exact full 40-character commit SHA. A content or metadata change creates a different candidate and invalidates review of the prior object. A branch name, short SHA, mutable tag, diff description, or working tree is not a substitute for exact candidate identity.

Research completion or review does not adopt its recommendation. A successful command, test, check, commit, push, or pull request does not establish acceptance. Candidate review must evaluate the exact unchanged SHA, and only an explicit coordinator acceptance record tied to that SHA can establish an accepted baseline.

No executor or reviewer may accept its own work by implication. Baseline acceptance does not require rewriting file metadata in the accepted commit; the SHA-level record owns that state.

## Amendment and supersession

This charter may change only through an explicit decision that names the amended scope and the target normative artifact. A material change creates a new candidate SHA and proceeds through fresh review and acceptance.

A successor must identify what it replaces or supersedes. Prior evidence and Git history remain available; they are not silently rewritten to reflect later decisions. No chat instruction, research recommendation, runtime adapter, or project-specific rule may amend this charter by interpretation.

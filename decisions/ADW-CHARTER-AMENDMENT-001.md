---
id: ADW-CHARTER-AMENDMENT-001
artifact: decision-record
artifact_status: active
authority: owner-decision
owner: repository-owner
decided_on: 2026-11-07
decision: amend-charter-owner-led-minimal-core
target: PROJECT-CHARTER.md
amended_scope: whole charter
base_commit: a1bd2fb76f3038d53e115e0218f3b8e1e0c8509e
supersedes: PROJECT-CHARTER.md at a1bd2fb76f3038d53e115e0218f3b8e1e0c8509e
---

# ADW-CHARTER-AMENDMENT-001: owner-led charter for a minimal core

## Context

Workflow v1 (WORKFLOW-V1.md, docs/, tools/, tests/ and
skills/adw-repo-handoff) built a ChatGPT-coordinated control plane with
separate gates for research, adoption, review and baseline acceptance. Its
process proved too heavy for day-to-day work and is no longer followed. The
README still described the repository as a control plane.

The repository owner, who assigned the ChatGPT coordinator role, reviewed an
audit of the repository and decided the following on 2026-11-07.

## Decision

1. **Coordinator.** The repository owner replaces the ChatGPT coordinator. The
   owner may work with any agent tool, or none. Agents of any tool may draft,
   check and review under the owner's assignment. Acceptance is the owner's
   explicit approval of an exact candidate SHA.
2. **Direction.** The repository becomes a minimal, tool-agnostic workflow core
   (`core/`), portable skills (`skills/`) and project profiles (`profiles/`).
   These arrive in a later change under their own decision record.
3. **Workflow v1.** Workflow v1 is tagged `v1` at
   `a1bd2fb76f3038d53e115e0218f3b8e1e0c8509e` and later removed from the tree.
   The tag and Git history keep it readable.
4. **Consumers.** A project copies files from a release tag into its own
   repository. There is no submodule, plugin, runtime dependency or automatic
   sync.
5. **License.** Unchanged: the repository has no license file. This decision
   grants no reuse rights.

## Amended scope

Target normative artifact: [PROJECT-CHARTER.md](../PROJECT-CHARTER.md). The
whole charter is restated: mission, scope, non-scope, roles, authority, the
safety floor, acceptance, releases and amendment.

## What this supersedes

- The charter text at `a1bd2fb`, including the ChatGPT coordinator role and
  the rule that only a coordinator acceptance record accepts a baseline.
- The normative effect of [WORKFLOW-V1.md](../WORKFLOW-V1.md) and of every
  decision, design, policy and research record under `docs/`. They become
  historical. Their front matter (for example `owner: chatgpt-coordinator`) is
  not rewritten.
- The Research Register as the owner of mutable state. This is the explicit
  migration decision that the register requires: from this decision on, the
  `Unreleased` section of [CHANGELOG.md](../CHANGELOG.md) is the single owner
  of planned and in-progress changes to this repository.

Accepted baseline v0 (`13b05e075ec04aa91494cd18f7d29f7249028cb5`) and all
earlier records stay in history unchanged. Nothing is rewritten.

## Effect and acceptance

This decision takes effect when its candidate commit is accepted by the owner
and merged to `main` through a pull request. Until then the charter at
`a1bd2fb` controls. A check, commit, push or pull request does not accept it.

## Follow-ups

- Create the annotated tag `v1` at `a1bd2fb76f3038d53e115e0218f3b8e1e0c8509e`
  (owner action; a published tag is not moved).
- Next change, under its own decision record: add `core/`, `skills/` and
  `profiles/`, and remove the v1 material from the tree.

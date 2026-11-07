---
id: ADW-CORE-ADOPTION-001
artifact: decision-record
artifact_status: active
authority: owner-decision
owner: repository-owner
decided_on: 2026-11-07
decision: adopt-minimal-core-and-remove-v1-from-tree
targets: core/, skills/, profiles/, PROJECT-CHARTER.md (Scope, Releases and consumers), THIRD-PARTY-NOTICES.md
builds_on: ADW-CHARTER-AMENDMENT-001
supersedes: the v1 material in the tree (WORKFLOW-V1.md, docs/, tools/, tests/, skills/adw-repo-handoff/)
---

# ADW-CORE-ADOPTION-001: adopt the minimal core, remove v1 from the tree

## Context

[ADW-CHARTER-AMENDMENT-001](ADW-CHARTER-AMENDMENT-001.md) recorded the
owner's direction: a minimal, tool-agnostic core with skills and profiles,
Workflow v1 tagged `v1` and removed from the tree, consumers copying from a
tag. The owner accepted the target layout from the same audit: six core
files, a set of skills, and code, non-code and template profiles. This
record adopts that content.

## Decision

1. **Core.** Six rule files, each readable on its own and at most 120 lines:
   `core/repo-contract.md`, `core/backlog-loop.md`, `core/decisions.md`,
   `core/evidence.md`, `core/review.md`, `core/closeout.md`. Each rule has one
   owner file; skills point to it instead of restating it.
2. **Skills.** `clarify-task`, `decision-split`,
   `verification-before-completion`, `independent-review`, `handoff`
   (replaces `adw-repo-handoff`), `workspace-closeout`, `status-digest`, and,
   for the code profile, `ci-triage` and `condition-based-waiting`. They name
   no vendor or tool and take project values from the profile placeholders.
3. **Profiles.** `profiles/template.md` (the placeholders a project fills),
   `profiles/code.md` and `profiles/non-code.md` (defaults).
4. **Third-party text.** Two skills adapt MIT-licensed text; their notice is
   in `THIRD-PARTY-NOTICES.md`. This does not license the rest of the
   repository; the license decision is still pending.
5. **v1 leaves the tree.** `WORKFLOW-V1.md`, `docs/`, `tools/`, `tests/` and
   `skills/adw-repo-handoff/` are removed. They stay at tag `v1`
   (`a1bd2fb76f3038d53e115e0218f3b8e1e0c8509e`) and in history. Earlier
   decision records are not edited; their links to removed files resolve at
   that tag.
6. **Charter wording.** The charter's Scope now lists `core/`, `skills/` and
   `profiles/` as present, and its Releases section states the `v1` tag as
   existing. No role, authority or acceptance rule changes.
7. **Merge convention.** Merges to `main` are merge commits through a pull
   request, followed by a readback of `main`. This records the practice of
   every earlier merge in the history.

## Effect and acceptance

This decision takes effect when its candidate is accepted by the owner and
merged to `main`. The merge waits until the tag `v1` exists on the remote and
points to `a1bd2fb76f3038d53e115e0218f3b8e1e0c8509e`.

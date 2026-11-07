# Agentic Development Workflow

A small, versioned, tool-agnostic workflow core for projects that work with AI
agents: how work is picked, decided, checked, reviewed and closed out. A
project copies what it needs from a release tag and adapts it with a profile.

## Status: being rebuilt

- **Workflow v1** (September to October 2026) designed a ChatGPT-coordinated
  control plane with separate gates for research, adoption, review and
  baseline acceptance. The process proved too heavy for day-to-day work and is
  no longer followed. It stays readable at tag `v1` (planned, commit
  `a1bd2fb76f3038d53e115e0218f3b8e1e0c8509e`) and in Git history.
- **The charter** was amended by
  [ADW-CHARTER-AMENDMENT-001](decisions/ADW-CHARTER-AMENDMENT-001.md): the
  repository owner leads, agents of any tool assist, and acceptance is the
  owner's approval of an exact commit.
- **The core is not published yet.** The next change adds `core/`, `skills/`
  and `profiles/` and removes the v1 material from the tree. Until a core
  release tag exists, there is nothing to adopt.

Planned and in-progress work lives only in the `Unreleased` section of the
[changelog](CHANGELOG.md).

## What is here now

| Path | Status |
|---|---|
| [PROJECT-CHARTER.md](PROJECT-CHARTER.md) | Current: mission, scope, roles, authority, safety floor, acceptance |
| [decisions/](decisions/) | Current: one record per decision about ADW itself |
| [CHANGELOG.md](CHANGELOG.md) | Current: releases and the single list of planned changes |
| [AGENTS.md](AGENTS.md) | Current: how agents change this repository |
| `WORKFLOW-V1.md`, `docs/`, `tools/`, `tests/`, `skills/adw-repo-handoff/` | Historical v1 material; not current rules; to be removed from the tree |

## How a project will use it

1. Pick a release tag.
2. Copy the core files and the skills you need into your own repository.
3. Write your profile (check command, review tool, where decisions and plans
   live) into your own agent instructions.
4. Record the tag and commit you copied from. Update by copying again from a
   newer tag.

There is no submodule, plugin, runtime dependency or automatic sync.

## License

There is no license file yet, so no reuse rights are granted. A license
decision is pending.

# Agentic Development Workflow

A small, versioned, tool-agnostic workflow core for projects that work with AI
agents: how work is picked, decided, checked, reviewed and closed out. A
project copies what it needs from a release tag and adapts it with a profile.

ADW is not a runtime dependency, a hosted service or a control plane. Nothing
syncs automatically; each project's own repository stays the authority for its
work.

## What is here

| Path | What it is |
|---|---|
| [core/](core/) | Six short rule files, each readable on its own |
| [skills/](skills/) | Step-by-step skills that apply the core rules |
| [profiles/](profiles/) | The values a project fills in, with code and non-code defaults |
| [PROJECT-CHARTER.md](PROJECT-CHARTER.md) | How ADW itself is governed: roles, authority, acceptance |
| [decisions/](decisions/) | One record per decision about ADW itself |
| [CHANGELOG.md](CHANGELOG.md) | Releases, and the single list of planned changes |
| [AGENTS.md](AGENTS.md) | How agents change this repository |
| [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) | Notices for adapted third-party text |

### Core

| File | Covers |
|---|---|
| [repo-contract.md](core/repo-contract.md) | What a project's agent entry file must say: where things live, invariants, when to stop and ask, what never to do |
| [backlog-loop.md](core/backlog-loop.md) | One planning file and the delivery loop |
| [decisions.md](core/decisions.md) | Owner-class versus minor decisions, asking, the decision log |
| [evidence.md](core/evidence.md) | No "done" without fresh evidence; the evidence line |
| [review.md](core/review.md) | Independent review of an exact change; the verdict format |
| [closeout.md](core/closeout.md) | What a task leaves behind, and the cleanup line |

## How a project uses it

1. Pick a release tag (the first core release is planned; see the
   changelog).
2. Copy `core/`, the skills you need, and one profile into your own
   repository.
3. Fill the [profile template](profiles/template.md) in your agent
   instructions: plan file, checks, review channel, who accepts.
4. Record the tag and commit you copied from. Update by copying again from a
   newer tag.

There is no submodule, plugin, runtime dependency or automatic sync. The
skills use the common `SKILL.md` format (a name, a description, then the
steps) and name no vendor or tool.

## History

Workflow v1 (September to October 2026) designed a ChatGPT-coordinated control
plane with separate gates for research, adoption, review and baseline
acceptance. The process proved too heavy for day-to-day work and was replaced
by this core. It stays readable at tag `v1`
(`a1bd2fb76f3038d53e115e0218f3b8e1e0c8509e`) and in Git history.

## License

There is no license file yet, so no reuse rights are granted for this
repository. A license decision is pending. Adapted third-party text keeps its
own license; see [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

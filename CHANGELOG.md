# Changelog

Notable changes to ADW. Releases are annotated Git tags; a published tag is
never moved. A project that copies from ADW records the tag and commit it
copied from.

## Unreleased

This section is the single owner of planned and in-progress changes to ADW
([charter](PROJECT-CHARTER.md#the-single-owner-of-state)).

### Added

- The core, under
  [ADW-CORE-ADOPTION-001](decisions/ADW-CORE-ADOPTION-001.md): six rule files
  in `core/`, nine skills in `skills/` (`clarify-task`, `decision-split`,
  `verification-before-completion`, `independent-review`, `handoff`,
  `workspace-closeout`, `status-digest`, `ci-triage`,
  `condition-based-waiting`), and three profiles in `profiles/` (template,
  code, non-code).
- `THIRD-PARTY-NOTICES.md` for the two skills adapted from MIT-licensed text.

### Changed

- Charter restated by
  [ADW-CHARTER-AMENDMENT-001](decisions/ADW-CHARTER-AMENDMENT-001.md): the
  repository owner replaces the ChatGPT coordinator, agents of any tool may
  assist, and acceptance is the owner's approval of an exact commit SHA. ADW is
  now described as a minimal core copied from tags, not a control plane.
- README and AGENTS.md rewritten to match the charter and the core.
- Workflow v1 and the Research Register are historical. This section replaces
  the register as the owner of current work.
- `skills/adw-repo-handoff` is replaced by `skills/handoff`.

### Removed

- The v1 material from the tree: `WORKFLOW-V1.md`, `docs/`, `tools/`,
  `tests/` and `skills/adw-repo-handoff/`. It stays at tag `v1` and in
  history.

### Planned

- Tag `v1` at `a1bd2fb76f3038d53e115e0218f3b8e1e0c8509e`, the last Workflow v1
  commit, before the removal above merges.
- First core release tag after these changes.
- A license decision for the repository.

## v1 (tag `v1` at `a1bd2fb`, 2026-10-01)

Workflow v1: a ChatGPT-coordinated control plane with separate gates for
research, adoption, independent review and baseline acceptance. It contains
the bootstrap charter and accepted baseline v0
(`13b05e075ec04aa91494cd18f7d29f7249028cb5`), the Workflow v1 contract, the
research and design records under `docs/`, a persistence checker with tests,
and one handoff skill. It is no longer followed and carries no normative
effect.

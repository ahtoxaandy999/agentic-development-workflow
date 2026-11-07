# Changelog

Notable changes to ADW. Releases are annotated Git tags; a published tag is
never moved. A project that copies from ADW records the tag and commit it
copied from.

## Unreleased

This section is the single owner of planned and in-progress changes to ADW
([charter](PROJECT-CHARTER.md#the-single-owner-of-state)).

### Changed

- Charter restated by
  [ADW-CHARTER-AMENDMENT-001](decisions/ADW-CHARTER-AMENDMENT-001.md): the
  repository owner replaces the ChatGPT coordinator, agents of any tool may
  assist, and acceptance is the owner's approval of an exact commit SHA. ADW is
  now described as a minimal core copied from tags, not a control plane.
- README and AGENTS.md rewritten to match the charter.
- Workflow v1 and the Research Register are historical. This section replaces
  the register as the owner of current work.

### Planned

- Tag `v1` at `a1bd2fb76f3038d53e115e0218f3b8e1e0c8509e`, the last Workflow v1
  commit, before any v1 file leaves the tree.
- Next change, under its own decision record: add `core/` (six short rule
  files), `skills/` and `profiles/` (code, non-code, template); remove
  `WORKFLOW-V1.md`, `docs/`, `tools/`, `tests/` and `skills/adw-repo-handoff/`
  from the tree; rename `PROJECT-CHARTER.md` to `CHARTER.md`.
- First core release tag after that change.

## v1 (tag planned at `a1bd2fb`, 2026-10-01)

Workflow v1: a ChatGPT-coordinated control plane with separate gates for
research, adoption, independent review and baseline acceptance. It contains
the bootstrap charter and accepted baseline v0
(`13b05e075ec04aa91494cd18f7d29f7249028cb5`), the Workflow v1 contract, the
research and design records under `docs/`, a persistence checker with tests,
and one handoff skill. It is no longer followed and carries no normative
effect.

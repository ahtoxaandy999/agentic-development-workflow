# Code profile

Defaults for a software project under Git with a code host and CI. Copy the
[template](template.md), start from these values, and change what differs.

## Change unit and identity

- One branch and one pull request per plan item, from the live main line.
- `<change id>` is the exact full commit SHA of the pull request head. A new
  push is a new candidate.
- The pull request description is the task record: what and why, how it was
  checked, decisions a reviewer might question.

## Checks

| Tier | When | Typical content |
| --- | --- | --- |
| `<check fast>` | while working | tests related to the changed files, lint, type check |
| `<check full>` | once, on the final id | the full test suite; CI runs it again |
| release | before a release | the full suite plus slow or end-to-end suites |

- Rule and interface changes start with a failing test (red), then the fix
  (green). Limits are tested just below, at and just above.
- Tests assert literal values from the spec, never values computed with the
  code under test.
- A red CI run is read with the `ci-triage` skill; flaky checks go to
  `<flaky list>` with an owner and a due date. Waits in tests follow
  `condition-based-waiting`.

## Review and merge

- `<review channel>`: one pull request comment per verdict, naming the head
  SHA.
- Risky paths get the strongest reviewer and, if the project says so, the
  owner's acceptance. Typical risky paths: rules and specs, authentication
  and secrets handling, data migrations, public interfaces, CI and release
  configuration.
- Merge when CI is green on the head SHA, the latest verdict is PASS for that
  SHA, and no review thread is open. Merge pinned to the reviewed SHA, as a
  merge commit or the project's chosen method, then read the main line back.
- Branch protection on the main line: pull request required, no force push,
  no deletion.

## Guards worth having

- Deny reading environment and credential files in the agent tool settings.
- Deny force push and hook bypass flags.
- Keep the main line protected on the server, not only in agent settings.

## Skills

`clarify-task`, `decision-split`, `verification-before-completion`,
`independent-review`, `handoff`, `workspace-closeout`, `ci-triage`,
`condition-based-waiting`; `status-digest` when several sessions run.

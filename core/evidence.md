# Evidence

No claim of "done", "fixed" or "passing" without fresh evidence from this
session, quoted in the report.

## The evidence line

Every report ends with:

```text
Evidence: <last line of the check, copied> @ <change id>
```

- `<change id>` is the exact full commit SHA, or the profile's identifier for
  work outside Git. Evidence for one id says nothing about another.
- Visual or document work also lists the paths of what was looked at (render,
  screenshot, export) and what was checked in it.

## Before claiming

1. Name the check that proves the claim.
2. Run it now, in full. An earlier run does not count.
3. Read the whole output and the exit status. Count failures and warnings.
4. If it does not confirm the claim, report the real state.
5. Only then claim, and quote the evidence.

## What counts

| Claim | Needs | Not enough |
| --- | --- | --- |
| Checks pass | the runner's output with 0 failures | "should pass", an older run |
| Bug fixed | the original symptom no longer reproduces | "the code changed" |
| Regression covered | the check fails without the fix and passes with it | one green run |
| Output valid | a validator's output on the file | "it opens" |
| Looks right | the render read at full size against the brief | a description from the code |
| Another agent finished | the changed files exist and match the brief | the agent said "success" |
| Requirements met | each brief line checked | checks passing |
| A number (speed, cost, quality) | several runs, with spread | one run |

## Checks that prove something

- Assert literal expected values taken from the spec. A check that computes
  its expected value with the code under test proves nothing.
- Test a limit just below, at and just above it.
- A red check is fixed or escalated, never loosened to turn green: no
  skipped tests, weaker assertions, raised thresholds or timeouts without a
  written reason in the change description.

## Live state

Facts about current state (a branch head, a check status, what is deployed,
what a service returns) are read live before relying on them. A local copy,
a summary, memory or an earlier report is navigation, not proof.

## Sources for non-code claims

A claim taken from outside the repository names its source and the date it
was read. A claim that cannot be sourced is marked as an assumption.

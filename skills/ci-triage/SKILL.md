---
name: ci-triage
description: Use when a CI run, build or check fails, to find out why and route it. Skip when the check passes, or when you already know the cause.
---

# CI triage

Implements `core/evidence.md`. Code profile skill.

## 1. Read the failure cheaply

Get only the failing step's log, for example with `gh run view <run>
--log-failed`, or the check's own report. Do not paste long logs into your
context. Filter for error lines, or give the log path to a helper agent that
returns the failing check, the error and the likely file.

## 2. Classify

- **real:** the cause is in the change. The check passes on the base and
  fails on the change.
- **flake:** it is in `<flaky list>`, depends on timing or order, or passes
  on a fresh run of the same `<change id>`.
- **infra:** checkout, runner, network, disk, memory, missing tool or
  license, a worker that died.
- **contract:** a version, schema or interface conflict between the change
  and the things that depend on it.

## 3. Re-run

At most once, and only for a flake or an infra problem, the same way as
before. A second failure means it is not a flake. Route it.

## 4. Route in 5 lines or fewer

Say: the check, the error, where it ran, and the log path or link.

- real: to the author of the change.
- flake or infra: to whoever owns the runner or tooling.
- contract: to the owner of the contract and the author.

## Flaky list

Add a row to `<flaky list>` when a check fails then passes, or fails twice in
24 hours. Columns: check, first seen, numbers, owner, due date. Past the due
date, quarantine the check visibly and link the row. Never delete it
silently.

## Never

Never change pipeline settings, runner config or required checks to turn a
failure green. Escalate to the owner. A change is not done until its
`<check full>` passes on the exact `<change id>`.

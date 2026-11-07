---
name: clarify-task
description: Use when the owner gives a new task, update, fix or change and anything material is unclear (goal, scope, acceptance, product or rule choices). Skip for unambiguous mechanical requests such as "merge X", "rerun the check" or a status question.
---

# Clarify a task

Implements `core/decisions.md` and `core/backlog-loop.md`.

Goal: plan the task well the first time without interrogating the owner.
Only the session that talks to the owner runs this. Subagents never ask the
owner. They return open questions to the session that started them.

## Before asking

- Answer what you can from the project: code, specs, `<plan file>`,
  `<decision dir>`, existing assets, the agent instructions.
- Never ask what is derivable or already decided.
- Where a conventional default exists, use it and list it as an assumption.

## What to ask, ranked by impact

1. Goal and why.
2. Scope: in and out.
3. Acceptance: how the owner will check it (a test, a file, a number).
4. Choices with more than one reasonable answer.
5. Constraints: dependencies, cost, size or speed budgets, target formats.
6. Priority against current work.

## How to ask

- Use the owner's language, `<owner language>`.
- Use `<question tool>`. At most 4 questions per round, at most 5 rounds.
- Never re-ask an answered question.
- Each question has 2-4 concrete options. Put the recommended one first,
  mark it "(recommended)", and give the trade-off in one line.
- Budget: small fix 3 questions, feature 10, epic or rule or format change 20.
- Stop early when the rest is low impact or the owner says go.
- When the budget is spent, proceed on the listed assumptions.

## Owner away

Do not block. Work only on items whose material choices are decided.

- Park each question in the owner-questions section of `<plan file>`.
- One row per question: an id, status `open`, and the options with the
  recommended one first.
- Then take the next ready item from `<plan file>`.

## Confirm a brief (5-10 lines)

Goal. In and out of scope. Acceptance. Decisions taken. Assumptions.
Deferred items. Start work after the owner's "ok" or edits. Edits are not a
new round.

## Record

- Put the brief in the change description or the implementer's spec.
- Put durable decisions (rules, formats, look, architecture) in a new file in
  `<decision dir>`, in the format of `core/decisions.md`.

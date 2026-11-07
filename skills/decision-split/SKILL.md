---
name: decision-split
description: Use before planning a new owner task, to split its open points into owner-class and minor ones. Skip for chat, status questions, answers to earlier questions, tool commands and mechanical requests.
---

# Decision split

Implements `core/decisions.md`.

Goal: settle small points yourself, and send only real owner decisions to the
owner. The owner's time is for choices only the owner can make.

## Steps

1. List every open point in the task text. Use the project's decisions in
   `<decision dir>` and `<plan file>` first. Drop what is already decided.
2. Class each open point with the owner-class and minor lists in
   `core/decisions.md`, plus any additions in the project profile.
3. Decide each minor point yourself. Write a one-line reason for it.
4. Put the minor decisions and their reasons in the brief.
5. Send only the owner-class points to `clarify-task`.

## Rules

- When a point fits both lists, it is owner-class.
- Nobody downgrades an owner-class point. The only exit is to cite an
  existing file in `<decision dir>` that already covers it.
- Skipping the split never lowers a class. When unsure, split. It is cheap.
- Subagents do not run this. They return questions to the session that
  started them.
- Do not put secrets or personal data in the brief.

## Output

A short list in the brief:

    owner-class: <point> -> asked in clarify-task
    minor: <point> -> <decision> (reason: <one line>)
    decided before: <point> -> <decision file>

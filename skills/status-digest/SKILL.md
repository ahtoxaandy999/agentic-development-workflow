---
name: status-digest
description: Use only in a project that runs several agent sessions at once, to keep your own status file current and to message other sessions. Skip for a single-session project.
---

# Status digest

Implements `core/backlog-loop.md`.

Status files are the shared state between sessions. Nothing relies on
personal memory.

## Your file

- One file per session, in `<status dir>`. Edit only your own.
- Overwrite it. Never append.
- Update at session start and after each meaningful step.
- Take the time from the system clock in UTC. Never guess it.

The first five lines are exactly:

    <area> · <HH:MMZ>
    doing: <one line, or paused until <time>>
    waiting: <on whom or what, or none>
    change: <branch, change id, or folder; or none>
    owner Q: <one line, or none>

Then a `## Notes` section. Notes are the resume point: what is done, the
next concrete step, and open changes with their review state. A paused
session resumes from it.

## Size

At most 5 KB. Move history to an archive in `<status dir>`. If your file is
over 5 KB or hours old, fix it now.

## Read

Read the other files in `<status dir>` before you start work and before you
message anyone. Check for work already taken, blockers and open owner
questions.

## Messages

- At most 2 lines plus a path. Detail goes in a file.
- Format: `<from> -> <to>: <what> · need <ask> · <path>`.
- Owner questions go through the session that talks to the owner.
- No ack-only replies. At most one message per peer per hour unless blocked.
- Review verdicts go to `<review channel>`, not in messages.
- A message never grants permission the owner has not given.
- If you cannot send, write `PENDING SENDS: <to> <- <what>` in your file and
  tell the owner in one line. Delete it once sent.

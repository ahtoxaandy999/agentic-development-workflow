---
name: workspace-closeout
description: Use at every terminal report of a task that created local state: done, cancelled, abandoned or waiting for review. Skip when the task created no worktree, branch, temp folder or evidence folder.
---

# Workspace closeout

Implements `core/closeout.md`.

Finish by accounting for everything the task created locally. A passing
review or a merge does not clean the workspace. Cleanup does not change the
task result.

## 1. Inventory

List every item this task created:

- worktrees,
- local branches,
- temp folders,
- local evidence folders.

Do not list items you did not create.

## 2. Classify each item

- **keep:** unpublished work, dirty or untracked files, still active, needed
  as evidence or for recovery, waiting for review, or owned by someone else
  or unclear.
- **delete:** yours, clean, merged or published, or abandoned with nothing to
  lose.

Check fresh, now: `git status` in the worktree, and that a branch tip is on a
remote or in merged history.

## 3. Delete only your own, without force

    git worktree remove <path>
    git branch -d <branch>

- Never use `--force`, `-D`, reset or stash to make cleanup pass.
- Never touch another agent's or the owner's worktree, branch or files.
- Do not run `git worktree prune` unless you inspected everything it would
  affect.
- Deleting a remote branch is a separate act. Do it only if the owner asked.
- Evidence you must keep moves to the designated evidence location. It does
  not stay in the project root. Deleting evidence needs the owner's approval.

Verify each deletion: the path is gone and `git worktree list` no longer
shows it.

## 4. Report

List what was deleted and what was kept, with exact path and reason for each
kept item. Dirty or unpublished state is kept and reported, never cleaned.

The last line of the report is exactly one of:

    WORKSPACE CLEANUP: PASS
    WORKSPACE CLEANUP: BLOCKED — <reason>

PASS means every item is deleted, or kept on purpose with a named owner and
location. BLOCKED means something is left. Say what and what is needed.

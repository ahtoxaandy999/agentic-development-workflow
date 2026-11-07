# Closeout

Every task ends with an inventory of what it left on the machine. Clean
results are not bought by discarding work.

## When

At every terminal report: done, cancelled, abandoned, or waiting on review,
acceptance or the owner. Pending obligations do not postpone the inventory.

## Inventory

List every item the task created:

- worktrees and working copies;
- local branches;
- temporary folders, run directories and caches;
- local evidence (logs, renders, reports);
- processes the task started.

Classify each:

| Class | Meaning | Action |
| --- | --- | --- |
| keep | unpublished or dirty work, an open change, active, or needed as evidence | leave it; say why |
| move | evidence that must outlive the task | move it to the project's evidence location |
| remove | yours, clean, and merged or abandoned | remove it with a non-forcing command |
| unclear | ownership or state unknown | leave it; it makes the result BLOCKED |

## Removing safely

- Remove only what this task created. Never someone else's folder, branch,
  worktree or process.
- Use commands that refuse to lose work: `git worktree remove <path>`
  without `--force`, `git branch -d` (not `-D`), then `git worktree prune`.
- Delete exact paths, one per command. No wildcards across shared folders.
- Stop processes by the id you started, never by name.
- Remote branches and tags are removed only with the owner's explicit yes.

## The report line

The closeout ends with exactly one of:

```text
WORKSPACE CLEANUP: PASS
WORKSPACE CLEANUP: BLOCKED - <items and why>
```

PASS means every item is kept with a reason, moved or removed. BLOCKED means
at least one item is unclear or could not be removed safely. The task's own
result (done, cancelled) is independent of the cleanup result.

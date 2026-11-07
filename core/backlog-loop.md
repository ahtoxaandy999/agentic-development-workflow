# Backlog and the delivery loop

One planning file and one loop. Agents run the whole loop without asking
between steps; the owner is asked only on the stop list in the
[repository contract](repo-contract.md#5-stop-and-ask-the-owner-only-when).

## The plan file

`<plan file>` is the only planning state. No second tracker, chat thread,
memory or status file keeps another copy of what to work on.

```markdown
## Now
- [ ] <item>: <one-line outcome>

## Next
- [ ] ...

## Later
- ...

## Owner questions
| ID | Question | Options (recommended first) | Status |
```

- **Now** holds what the owner approved; take items from the top.
- **Next** is ordered and ready to promote; **Later** is unordered.
- **Owner questions** holds questions waiting while the owner is away
  ([decisions](decisions.md)). Items blocked by a question stay where they
  are, marked `blocked: <ID>`.
- Something noticed along the way that is not the current item goes under
  **Later** as one line, not into the current change.

## The loop

```text
pick -> (clarify) -> branch -> change -> fast check -> change unit
  ^                                                       |
  +-- plan updated in the same change <- accept <- full check + review PASS
```

1. **Pick.** The top item under **Now**, or the item the owner named. A new
   owner request first goes through the [decision split](decisions.md): minor
   points settled with a reason, owner-class points asked, then a short
   confirmed brief.
2. **Branch.** A new branch from the live main line, in your own working
   copy (a worktree or a separate folder). Never the owner's checkout.
3. **Change.** Keep to the item. Rule or spec changes start with a check that
   fails (red), then the change that makes it pass (green). Boundary values
   (limits, timeouts, thresholds) are checked just below, at and just above.
4. **Fast check** while working: `<check fast>`, only what the change touches.
5. **Change unit.** A pull request, or the profile's equivalent. Its
   description is the task record: what and why, how it was checked, and
   decisions a reviewer might question.
6. **Full check** on the final `<change id>`: `<check full>`, once, at the end.
7. **Review** by a fresh reviewer ([review](review.md)). P1 and P2 findings
   block; P3 never blocks.
8. **Accept** when the full check passed on the current id, a PASS names that
   id, and the owner has not said hold. Who accepts or merges is set in the
   profile; for risky paths the profile may require the owner.
9. **Close.** The plan file moves in the same change (item checked off or
   removed), and the task ends with a [closeout](closeout.md).

## Done

The fast check passed while working, the full check passed on the final id,
the review PASS names that id, the plan moved in the same change, and the
report ends with the [evidence line](evidence.md).

## Several sessions

When several agent sessions work at once, each owns one area and one open
change at a time, keeps a status file in `<status dir>`, and passes work with
a [handoff](../skills/handoff/SKILL.md). Add a session only for work that is
truly parallel; several sessions cost several times the tokens of one.

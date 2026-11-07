---
name: verification-before-completion
description: Use before saying work is done, fixed or passing, and before committing or reporting. Skip only for pure questions and chat that make no claim about work.
---

# Verification before completion

Implements `core/evidence.md`.

No completion claim without fresh evidence from this session.

## Before you say "done" or "fixed"

1. Name the check that proves the claim. Use the table in `core/evidence.md`, `<check fast>`,
   or `<check full>` when the work is heavy.
2. Run it now, in full. An older run does not count.
3. Read the whole output and the exit status. Count failures and warnings.
4. If it does not confirm the claim, report the real status.
5. Only then make the claim, and quote the evidence.

## Evidence line

Every report ends with this line:

    Evidence: <last line of the check> @ <change id>

`<change id>` is the exact full commit SHA, or the profile's id for non-code
work. Visual work also lists the paths of the before and after renders and
says what you looked at in them.

## What counts

Use the table in `core/evidence.md`: what each kind of claim needs, and what
is not enough.

## Red flags

- Words like "should", "probably", "seems to".
- Saying "done" before a check ran.
- Committing or handing off without a check.
- Trusting another agent's report without looking at what changed.
- Fixing a red check by loosening it. See the weakened-verification signs in
  `core/review.md`.

Adapted from obra/superpowers skills/verification-before-completion/SKILL.md@3be5aad3dd2400ef23b15680969f4bcd3b6d7b8b, MIT License; see THIRD-PARTY-NOTICES.md.

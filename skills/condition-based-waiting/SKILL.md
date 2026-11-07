---
name: condition-based-waiting
description: Use when writing or fixing a flaky test, or any wait, delay or timeout in a test. Skip when the code under test has no waiting.
---

# Condition-based waiting

Implements `core/evidence.md`. Code profile skill.

Wait for the state you need, never for a guessed time. Flaky tests pass on a
fast machine and fail under load.

## Rules

- No fixed sleep as synchronization.
- Every wait is bounded. On timeout it fails with a message that names what
  it waited for.
- Read fresh state inside the wait. Never cache it before the loop.
- A fixed delay is allowed only to test timing itself, such as a debounce or
  a tick interval. Wait for the trigger first, then comment why that number.

## Example

    function waitUntil(read, ok, what, timeoutMs, stepMs):
        deadline = now() + timeoutMs
        loop:
            value = read()                 // fresh read each time
            if ok(value): return value
            if now() >= deadline:
                fail("timed out after " + timeoutMs + " ms waiting for "
                     + what + "; last value: " + value)
            pause(stepMs)

    waitUntil(() => events.length, n => n >= 5, "5 events", 2000, 10)

Prefer your test framework's own bounded wait if it has one.

## UI tests

Wait on the page's own state signal, not on time or network idle. Use the
element or state the next step needs: a visible element, a text, an
attribute. If no such signal exists, add a small test hook or state
attribute to the page. Do not wait for "network idle". It says nothing about
what the page shows.

## Common mistakes

- Polling with no timeout. It hangs the run instead of failing.
- Waiting for "something happened" when you need "the right thing happened".
  Check the exact value.
- Retrying the whole test to hide a race.
- Raising a timeout without a reason. A long wait needs a long explicit
  bound and a note why.
- Raising the global timeout instead of naming a limit for one slow test.

Adapted from obra/superpowers skills/systematic-debugging/condition-based-waiting.md@5845b52747a0d2ca5843a150a9870822a8884006, MIT License; see THIRD-PARTY-NOTICES.md.

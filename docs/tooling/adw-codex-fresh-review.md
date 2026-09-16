# Codex-only fresh review trial path

Status: trial procedure candidate. This document does not authorize execution beyond the controlling D3 limited-trial disposition.

## Purpose

Remove the manual step of opening a separate ChatGPT review chat while preserving a fresh review context.

The supervised trial path uses only existing Codex surfaces:

1. the producer/root Codex thread invokes `$adw-repo-handoff` explicitly to prepare a compact review packet;
2. the root writes that packet only to a temporary, non-repository location;
3. the root starts a separate top-level `codex exec` process/session from the repository workspace and supplies only that packet as review input;
4. the fresh reviewer rereads applicable repository authority and exact candidate state at its own point of reliance;
5. the root receives the review result and treats it as evidence only; the root does not convert it into acceptance by implication.

Do not use a producer-context subagent merely because it has a different subagent ID when independence is required. The trial requires a fresh top-level Codex thread/process with no producer conversation supplied as review context.

## Required reviewer containment

The reviewer must be technically prevented from candidate mutation. Use a verified read-only Codex permission/sandbox configuration. Required network or GitHub read capability must be verified independently; if the chosen read-only profile cannot retrieve load-bearing live evidence, stop rather than granting write capability as a workaround.

The reviewer may write transient output only to an explicitly permitted temporary destination when the host requires one. It must not edit the repository, branch, PR, comments, issues, labels or external systems.

## Fresh-session invariant

The root passes only:

- objective and reviewer role;
- exact immutable candidate identity and composite components;
- authoritative repository pointers;
- predecessor findings that remain relevant;
- verification criteria;
- stop conditions;
- required output/verdict format.

Do not pass producer reasoning, private scratchpad, prior verdict advocacy, or a full producer transcript.

A session/thread identifier alone is not proof of independence. The execution evidence must show a new top-level Codex session/process and the exact input packet used.

## `codex exec` eligibility

A separate `codex exec` invocation is eligible for the trial because it starts a new Codex thread/process and can run non-interactively. Before relying on it, verify the installed Codex version and command behavior on the actual host.

Use ordinary `codex exec`, not App Server, Agents API, Symphony, or a custom orchestration runtime.

Do not use `resume` or fork a producer session for independent review because those mechanisms preserve or derive from producer conversation context.

The caller must apply a wall-clock watchdog and treat timeout, incomplete output, ambiguous process state, or missing terminal result as review failure requiring inspection. Do not blindly rerun a review that may have produced external effects. The intended reviewer has no external write effects, so retry still requires fresh target verification and a new fresh session.

## Trial evidence

Record at least:

- root/producer Codex session identifier when available;
- fresh reviewer Codex thread/session identifier;
- exact review packet digest or immutable file identity;
- exact candidate SHA/tree/components reviewed;
- Codex version;
- effective permission/sandbox and network-read state;
- reviewer result and findings;
- process exit/terminal status;
- any timeout or recovery episode.

This procedure is a supervised trial adapter. It is not Workflow v1 policy, not a second task-state owner, and not standing review automation.

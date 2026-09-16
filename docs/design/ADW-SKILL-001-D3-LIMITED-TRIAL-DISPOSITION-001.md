---
id: ADW-SKILL-001-D3-LIMITED-TRIAL-DISPOSITION-001
artifact: coordinator-skill-trial-disposition
artifact_status: proposed
authority: coordinator-decision
owner: chatgpt-coordinator
repository: ahtoxaandy999/agentic-development-workflow
reviewed_subject_commit: 264666f7d65672108754b81687fa96ff38e3745d
review_ref: docs/design/ADW-SKILL-001-REVIEW-002.md
review_verdict: pass
decided_on: 2026-09-16
decision: authorize-one-bounded-d3-codex-skill-trial
normative_effect: none
supersedes: null
---

# ADW-SKILL-001 D3 limited-trial disposition

## Decision

**AUTHORIZE ONE BOUNDED D3 CODEX SKILL TRIAL**

Authorize one supervised, read-only trial of the first ADW skill, `adw-repo-handoff`, using Codex as the permitted host family.

This is a narrow D3 exception only. D3 remains `CONFIRM DEFER` outside this exact trial. The decision does not adopt custom skills generally and does not make the skill operational policy.

## Exact accepted design basis

The decision is based on the corrected composite design at exact commit `264666f7d65672108754b81687fa96ff38e3745d`, tree `13bb0a35064f037c3b5011e0ab3460464445dd41`:

- primary design blob `58edfd67ab81dfcfe6d6a2ba614f680943187a46`;
- correction blob `4ebc39852a815f1cc3a34cbda637052cd1a49e05`;
- predecessor review `ADW-SKILL-001-REVIEW-001`;
- fresh affected review `ADW-SKILL-001-REVIEW-002`, verdict `PASS`, `0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NOTE`.

Any materially different design is not covered by this decision.

## Authorized scope

The trial may perform only these downstream steps:

1. normalize the accepted composite runtime semantics into one repository-owned Codex skill package;
2. represent explicit-only activation in supported Codex skill metadata;
3. produce an exact immutable package candidate;
4. perform fresh affected equivalence review of that package candidate;
5. after that review passes, install or load the exact pinned package only in one verified Codex trial host;
6. run one supervised read-only E1-E11 behavioral/token-efficiency trial;
7. preserve exact trial evidence for later coordinator assessment.

Package creation does not itself authorize trial execution. Package equivalence review is required first.

## Permitted host and review boundary

The permitted host family is Codex App, Codex CLI, or Codex IDE using the same exact package version and verified effective configuration.

For independent package review, a reviewer must run in a fresh top-level Codex thread/process that receives only the exact review handoff and repository authority required for the task. A producer-context subagent is not sufficient merely because it has a different subagent ID. The review runner must not inherit producer conversation history as review evidence.

A separate `codex exec` session is an eligible mechanism for the fresh reviewer when it starts a new thread/process, is bound to the exact immutable candidate, has required read access, and is technically prevented from candidate mutation. This decision does not select App Server, Agents API, Symphony, or a custom orchestration runtime.

## Host prerequisites before trial execution

Before actual skill use, verify all of the following at point of reliance:

- exact package/source identity and installed/loaded version;
- Codex host version and skill-discovery support;
- explicit-only activation is enforced, including `allow_implicit_invocation: false` or an equivalent verified host control;
- if implicit activation cannot be disabled or ruled out, the host is ineligible;
- reviewer/trial read access is sufficient for required evidence;
- the skill has no effective repository or external write capability;
- manual/control arm has the skill unavailable or disabled;
- treatment arm explicitly invokes the exact pinned package;
- exact manual baseline prompt, model, reasoning effort, tool access and scoring criteria are frozen;
- E1-E11 and evidence destination are frozen;
- any live repository state relied upon is freshly reread.

## Trial evidence

Where available, capture:

- input, output, reasoning and cached token usage;
- tool-call count;
- tool-result volume;
- retries/failures;
- correct-packet outcome;
- human repair;
- activation-containment result;
- exact Codex thread/session identities used for treatment and review.

Missing telemetry is `UNKNOWN`, not zero. No efficiency percentage is accepted before measurement.

## Explicit non-authorities

This decision does not authorize:

- broader D3 adoption;
- standing or automatic skill invocation;
- implicit activation;
- production/operational skill use;
- repository mutation by the skill;
- task implementation by the skill;
- independent-review verdict generation by the skill itself;
- automatic dispatch, model routing or correction loops;
- App Server, Agents API, Symphony or other orchestrator selection;
- ready/merge automation;
- unattended or AFK operation;
- Workflow v1 amendment;
- baseline acceptance;
- D5 or D13 reconsideration outcome.

D5 remains `CONFIRM DEFER`.
D13 remains `CONFIRM DEFER`.
X3 remains `CONFIRM REJECT`.

## Stop conditions

Stop before installation or trial execution if package equivalence review has not passed, package identity drifts, explicit-only activation cannot be verified, read-only containment is not effective, the review context is not genuinely fresh, required evidence is inaccessible, or current repository authority conflicts with this trial.

## Next gate

The immediate next gate is:

**normalized Codex package candidate equivalence review**

Only after that exact package passes may the supervised E1-E11 trial run.

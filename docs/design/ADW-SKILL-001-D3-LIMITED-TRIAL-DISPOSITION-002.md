---
id: ADW-SKILL-001-D3-LIMITED-TRIAL-DISPOSITION-002
artifact: coordinator-skill-trial-disposition
artifact_status: active
authority: coordinator-decision
owner: chatgpt-coordinator
repository: ahtoxaandy999/agentic-development-workflow
reviewed_subject_commit: 264666f7d65672108754b81687fa96ff38e3745d
review_ref: docs/design/ADW-SKILL-001-REVIEW-002.md
review_verdict: pass
decided_on: 2026-09-16
decision: authorize-one-bounded-d3-chatgpt-skill-package-and-eligibility-trial
normative_effect: none
supersedes: null
---

# ADW-SKILL-001 D3 limited-trial disposition 002

## Decision

**AUTHORIZE ONE BOUNDED D3 CHATGPT SKILL PACKAGE AND ELIGIBILITY TRIAL**

Authorize one supervised, read-only trial path for `adw-repo-handoff` using ChatGPT as the intended skill host and Desktop Commander/GitHub only as connected execution and repository surfaces.

This is a narrow D3 exception only. D3 remains `CONFIRM DEFER` outside this exact trial. It does not adopt custom skills generally and does not make the skill operational policy.

The earlier unmerged Codex-only draft in PR #13 is historical and not accepted, adopted, installed, executed, or incorporated by this decision.

## Exact accepted design basis

The decision consumes the corrected composite design at commit `264666f7d65672108754b81687fa96ff38e3745d`, tree `13bb0a35064f037c3b5011e0ab3460464445dd41`, and `ADW-SKILL-001-REVIEW-002`, verdict `PASS`, `0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NOTE`.

The package source must faithfully normalize that accepted runtime semantics. Any material behavior change is outside this decision.

## Authorized scope

The trial may only:

1. preserve the passing review as durable evidence;
2. normalize the accepted runtime semantics into one repository-owned ChatGPT skill source at `skills/adw-repo-handoff/SKILL.md`;
3. verify package equivalence, current ChatGPT Skills eligibility, upload/install capability, explicit-invocation behavior, and control/treatment isolation;
4. if every host prerequisite is actually demonstrated, prepare one supervised read-only E1-E11 behavioral/token-efficiency trial;
5. otherwise stop with a durable host-eligibility gap and no fallback host substitution.

Package creation does not authorize skill installation or trial execution by implication.

## Host prerequisites before execution

Actual ChatGPT skill installation/use requires fresh evidence that the current account/workspace exposes Skills, accepts the exact package, and permits a trial configuration consistent with the reviewed design.

Because current OpenAI documentation states that installed skills may be selected automatically when relevant, an explicit-only treatment requires an actual host control or another demonstrated isolation method that prevents unintended activation. If this cannot be demonstrated, the behavioral trial is ineligible.

The manual/control arm must not have the trial skill available. The treatment arm must use the exact pinned package/version intentionally. Desktop Commander may provide repository/filesystem/terminal capability, but it is not a model-session or review-independence mechanism.

## Independent review boundary

A producer context does not satisfy independent review by re-reading its own candidate. A distinct reviewer must inspect the exact immutable package candidate and controlling authority.

GitHub Copilot code review is an eligible independent review mechanism for this package candidate when requested on the exact draft PR and when its returned review is bound to the unchanged head. A Copilot review is evidence only; it is not coordinator acceptance.

If Copilot review is unavailable, insufficient for the load-bearing design/authority questions, or returns material findings, stop. Do not silently treat producer verification as independent review.

## Explicit non-authorities

This decision does not authorize broader D3 adoption, standing skill invocation, implicit/automatic invocation, production use, repository mutation by the skill, task execution by the skill, independent-review verdict generation by the skill, automatic dispatch/model routing/correction, ready/merge automation, unattended/AFK operation, Workflow v1 amendment, baseline acceptance, or D5/D13 reconsideration.

D5 remains `CONFIRM DEFER`.
D13 remains `CONFIRM DEFER`.
X3 remains `CONFIRM REJECT`.

## Stop conditions and next gate

Stop before installation or behavioral execution if package equivalence review has not passed, ChatGPT Skills are unavailable to the current account/workspace, explicit-only isolation cannot be demonstrated, control/treatment isolation is not credible, required read-only evidence is unavailable, or current repository authority conflicts with the trial.

Immediate next gate: **exact ChatGPT package candidate independent equivalence and host-eligibility review**.

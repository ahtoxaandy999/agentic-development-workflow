# ChatGPT Desktop + Desktop Commander skill trial

Status: bounded trial procedure candidate. This document does not create standing tool or skill authority.

## Surfaces

- ChatGPT is the intended skill host.
- Desktop Commander supplies local filesystem, terminal and repository-adjacent execution from the supervising ChatGPT conversation.
- GitHub remains the authoritative remote repository/evidence surface.
- GitHub Copilot code review may provide the independent package review when available.
- Codex, App Server, Agents API, Symphony and custom orchestration runtimes are not part of this trial.

## Package

The repository package source is `skills/adw-repo-handoff/SKILL.md`. For an eligible ChatGPT account/workspace, the exact reviewed source may later be uploaded through ChatGPT Skills using the product-supported create/upload flow. Do not assume installation availability from repository presence.

Before upload, bind source commit, Git blob, byte count and SHA-256. If an archive is needed for the product UI, build it from the exact reviewed directory outside repository authority and verify its contained bytes against the reviewed source.

## Eligibility preflight

Before installation or trial execution, establish all of:

1. current ChatGPT account/workspace exposes Skills creation/upload/install;
2. the exact package can be installed without changing its runtime instructions;
3. treatment invocation can be isolated from the manual/control arm;
4. unintended automatic activation can be disabled or otherwise ruled out for the trial;
5. the skill has only the read capabilities needed for E1-E11;
6. no repository/external write is granted to the skill by implication.

If any item cannot be established, record `HOST_ELIGIBILITY_BLOCKED` and stop. Do not substitute Codex or an API host.

## Producer verification

The supervising ChatGPT + Desktop Commander context may verify repository identity, package bytes, formatting, source equivalence, local archive construction and deterministic E1-E11 fixtures. Those checks are producer evidence, not independent review.

## Independent package review

Request GitHub Copilot code review on the exact package PR when available. Require the reviewer to inspect package equivalence, scope/authority boundaries, host-eligibility claims and regression against the accepted design. Any candidate mutation after review starts makes that review stale and requires re-review.

## Trial execution

Only after package equivalence review and coordinator acceptance may one supervised read-only trial run. Freeze exact manual baseline prompt, package/version, model, reasoning effort, tool access, cases and scoring criteria.

Control: skill unavailable/disabled.
Treatment: exact pinned skill intentionally invoked.

Capture where available: input/output/reasoning/cached tokens, tool-call count, tool-result volume, retries, correct-packet result, human repair and activation containment. Missing telemetry is `UNKNOWN`, not zero.

## Stop

No installation, behavioral trial, ready transition or merge occurs from this procedure by implication.

## Platform references

- OpenAI Help, Skills in ChatGPT: https://help.openai.com/en/articles/20001066
- OpenAI Academy, Using skills: https://openai.com/academy/skills/
- GitHub Docs, Copilot code review: https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review
- GitHub Docs, review requests API: https://docs.github.com/en/rest/pulls/review-requests

These references establish documented capability only. Actual account/workspace eligibility, effective configuration, review availability and any quota/cost impact must be verified at the point of reliance.

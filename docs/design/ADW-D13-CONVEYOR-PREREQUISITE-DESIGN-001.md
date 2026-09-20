---
id: ADW-D13-CONVEYOR-PREREQUISITE-DESIGN-001
artifact: design-proposal
artifact_status: draft
owner: chatgpt-coordinator
repository: ahtoxaandy999/agentic-development-workflow
subject_base: 796fef15a7ba3b78b57c1f06f5911c6a3f85dad5
dr006_disposition_ref: docs/research/ADW-DR-006-DISPOSITION-001.md
decision_effect: none
designed_on: 2026-09-20
supersedes: null
---

# D13 autonomous engineering conveyor prerequisite design

## Status and boundary

This is the single bounded D13 prerequisite-scoping/design proposal authorized by
`ADW-DR-006-DISPOSITION-001`.

It designs and proposes only. It does not implement orchestration, select a D13
mechanism, reopen D5, amend Workflow v1, authorize automatic dispatch, enable
unattended execution, or satisfy the D13 conformance prerequisite.

D13 remains `CONFIRM DEFER`. D5 remains `CONFIRM DEFER`. X3 remains
`CONFIRM REJECT`.

The proposal consolidates the latest multi-repository research, exact-candidate
CI pilots, executor/reviewer experiments, GitHub control-plane analysis, Claude
engineering-skill evaluation, and the local learned-orchestrator idea into one
decision-ready architecture.

## 1. Exact live evidence snapshot

The following default-branch identities were re-read from live GitHub before
candidate production:

| Repository | Live `main` |
| --- | --- |
| `ahtoxaandy999/agentic-development-workflow` | `796fef15a7ba3b78b57c1f06f5911c6a3f85dad5` |
| `ahtoxaandy999/pet-project` | `28f84fe4324925adae0f17163d578ed2e1f9bc19` |
| `ahtoxaandy999/shalena-fishing-automation` | `9bb2357e6f596331abf30007e47bd373b0b02baa` |
| `ahtoxaandy999/shalena-game-research` | `96dd493e9b27fd99d40e70ba01fe33155c4bd484` |
| `ahtoxaandy999/housing-recovery` | `01b3ae5288069660a12c6b35254e4fa59867429e` |

These SHAs are publication-time evidence for this proposal, not standing current
state.

## 2. Observed implementation baseline

### Pet Project

Pet now has a merged exact-candidate GitHub Actions verifier. PR #100 transferred
the repository-owned verification planner to a clean published-candidate mode
without moving semantic test ownership into YAML.

The important distinction remains:

- local/task verification owns repository semantics;
- GitHub Actions independently executes that owner against an exact candidate;
- CI PASS is machine evidence, not semantic review or Product acceptance.

Pet also has accepted supervised correction and fresh-review semantics, but no
accepted unattended task-to-task advancement profile.

### Housing Recovery

Housing has a simpler exact-PR-head CI path and deterministic post-merge closeout.
It is the preferred low-risk pilot repository for event/review/correction wiring.

Housing demonstrates that exact-SHA verification and merge-closeout can stay
small when the repository test surface is small. That simplicity should not be
mistaken for a universal verifier design.

### Shalena Fishing Automation

Fishing remains local-first for important browser/device/package behavior. It has
strong repository-owned tests and packaging logic but no current standard Actions
pipeline for the full development flow.

A later migration should move deterministic build/test/package work to GitHub
while preserving explicit local/device lanes for real game/browser evidence.

### Shalena Game Research

The research repository has a different evidence model: capture integrity,
provenance, immutable hashes, offline verification and accountable adoption are
separate.

Research findings must not auto-activate product implementation. Missing retained
source bytes remain an evidence gap, not a semantic conclusion.

### ADW

ADW remains the cross-project control-plane owner only for explicitly adopted
shared semantics. Project repositories retain product rules, local verification
and live execution state.

No common runtime should be introduced here before local pilots prove a genuinely
shared contract.

## 3. Target role split

### GPT

GPT is the semantic coordinator and independent reviewer surface:

- milestone analysis and bounded decomposition;
- authority and evidence reconciliation;
- intermediate independent review of exact candidates;
- final cumulative milestone review;
- genuine stop-condition escalation.

GPT should not be the ordinary implementation executor and should not own
deterministic routing that GitHub can evaluate mechanically.

### Claude

Claude is the default producer/executor candidate:

- bounded implementation;
- focused semantic tests;
- producer-side internal code review;
- debugging and fixes until producer-green;
- invocation of repository-owned verification/publication procedures.

Useful Claude engineering skills are procedural aids only:

- `engineering:code-review` for producer-side review;
- `engineering:testing-strategy` when observable behavior changes;
- `engineering:debug` for bounded CI/review corrections.

`architecture`, `system-design` and `tech-debt` must not silently expand an
authorized implementation task.

Claude internal review is never independent review of Claude-produced work.

### GitHub

GitHub is the preferred event and durable identity plane:

- branch and exact commit identity;
- PR state;
- Actions execution and artifacts;
- structured transition signals;
- review/result publication;
- manual merge observation;
- mechanical post-merge closeout.

GitHub does not own Product semantics or acceptance.

### Human

The desired mature milestone profile has three human roles:

1. authorize one bounded milestone envelope;
2. resolve genuine Product/architecture/security/permission stops;
3. accept the final exact candidate and merge manually.

No intermediate human gate is desired for predetermined technical tasks that
remain inside the authorized envelope.

## 4. Target milestone flow

```text
human milestone authorization
-> Claude task implementation
-> Claude focused tests + internal review + fixes
-> exact candidate publication
-> GitHub exact-SHA CI/evidence
-> fresh GPT independent task review
-> bounded correction back to same Claude logical task when permitted
-> new candidate -> CI -> fresh affected review
-> automatic activation of next already-authorized task
-> fresh cumulative GPT final review
-> READY FOR HUMAN
-> human acceptance + manual merge
-> deterministic GitHub closeout
```

“No intermediate review” means no intermediate human Product-acceptance gate. It
does not remove producer review, CI, independent technical review or correction.

## 5. Control-plane design

The preferred coordinator is ephemeral and event-driven.

Each run should:

1. receive a GitHub signal;
2. reread live authoritative state;
3. establish the exact subject and authorization;
4. perform one permitted transition;
5. publish a bounded receipt/result;
6. terminate.

A permanently alive chat, private agent memory or second task database is not a
required correctness component.

The minimum durable operational state should be reconstructable from:

- accepted milestone authorization;
- Git/PR identity;
- Actions/check evidence;
- structured review/correction/final-review results;
- human acceptance evidence;
- merge/closeout facts.

Chat history is navigation, not an operational state owner.

## 6. Review architecture

Two review layers are required.

### Producer layer

Claude reviews and fixes its own task before publication. This is quality control,
not independence.

### Independent layer

A fresh GPT context independently retrieves:

- exact base/head;
- relevant repository authority;
- changed code/docs;
- exact machine evidence.

It returns a structured verdict bound to the exact candidate.

A changed candidate invalidates the earlier verdict for advancement purposes and
requires fresh affected review.

The final milestone review is another fresh context over milestone base to final
head. It verifies cross-task integration rather than merely aggregating earlier
PASS results.

## 7. Correction loop

A `REQUIRES_CORRECTION` finding may route automatically to the same logical
Claude task only when the correction:

- is required by the already-authorized outcome;
- stays within permitted paths/effects;
- preserves Product/architecture/public-API decisions;
- adds no new dependency or privilege;
- needs no new external effect.

A correction that crosses one of those boundaries stops for human authority.

The first profile should cap semantic correction attempts per task. The current
research recommendation is two attempts, but that number is not an adopted ADW
default.

## 8. Current invocation constraints

### GPT reviewer

The desired formal GPT review path is exact-SHA, fresh-context and
machine-readable.

The official Codex GitHub Action can satisfy the GitHub-native execution shape,
but the tested Housing pilot stopped correctly because the repository had no
`OPENAI_API_KEY` and the user did not authorize separate API billing.

The tested Codex automation interface exposed schedule/heartbeat behavior but did
not provide the required native read-only GitHub PR event trigger. That empirical
result means the current design must not depend on a Work/Codex event trigger
until the exact user/account surface proves it.

Automatic Reviews are useful as an optional human-facing review product, but they
do not replace the formal structured-result contract by assumption.

### Claude producer

Claude Code Action is a strong hosted-producer candidate because it can run inside
GitHub Actions and use Claude Code. Subscription OAuth is a possible personal
pilot path where supported by the official integration, but personal subscription
credentials are not treated as a durable organization service identity.

### GitHub Agentic Workflows

`gh-aw` is the strongest ready-made challenger to a custom orchestration layer.

Its relevant properties are:

- GitHub-native event/scheduled execution;
- read-only agent jobs by default;
- sandbox/security controls;
- explicit safe outputs executed by separate permissioned jobs;
- support for multiple agent engines.

The first implementation pilots should compare a thin repository-local adapter
against `gh-aw`. A custom controller is justified only if the ready-made
mechanism cannot satisfy the accepted identity, evidence, retry and authority
boundaries.

## 9. Minimal machine contracts

Do not adopt the large research draft schema as one block.

The first pilots need only four narrow contracts:

1. **candidate identity**: repository, PR/task, base, exact head;
2. **CI evidence**: exact head, verifier revision/run, result, artifact digest;
3. **review result**: exact subject, reviewer execution identity, findings,
   verdict, unresolved evidence;
4. **correction dispatch**: originating review/finding IDs, permitted correction
   scope, expected current head, attempt number.

Additional milestone/final-review/closeout contracts should be materialized only
when the corresponding pilot needs them.

This avoids building a workflow engine before the control loop is proven.

## 10. Repository profile optimization

One workflow shape should not be forced across all repositories.

- **Pet**: deterministic application profile, rich affected/full verification,
  gameplay/runtime-specific evidence.
- **Housing**: lightweight application profile, ideal for control-loop pilots.
- **Fishing**: automation/package profile with deterministic hosted work plus
  explicit local/device lanes.
- **Game research**: evidence/research profile with adoption separated from
  implementation.
- **ADW**: governance/design profile, not a product executor or global task DB.

Shared components should be extracted only after at least two repositories prove
the same semantics with materially duplicated implementation.

## 11. Local learned orchestrator optimization lane

A local learned orchestrator is promising but is not a prerequisite for the
GitHub/Claude/GPT conveyor.

The correct first asset is a high-quality trajectory dataset, not immediate
fine-tuning.

After the conveyor is stable, record observable transitions such as:

```text
state/evidence
-> available actions
-> selected action
-> actor
-> outcome
-> human override
-> final accepted result
```

Do not collect or depend on hidden chain-of-thought. Store only observable
artifacts, decisions, tool calls and outcomes allowed by the applicable data
policy.

### Learning stages

**Stage L0 - shadow policy model**

Benchmark local models against accepted historical routing decisions without
letting them control execution.

**Stage L1 - supervised adaptation**

Train a small local policy model on state-to-next-action examples. On Apple
Silicon, MLX-LM supports LoRA/QLoRA-style fine-tuning and is a practical research
surface.

**Stage L2 - preference learning**

Use chosen/rejected routing decisions when real human or reviewer corrections
produce clean preference pairs.

**Stage L3 - agentic reinforcement learning**

Only after the harness has stable deterministic rewards, evaluate systems such as
Agent Lightning for trajectory-based policy training. This is later research,
not the initial local-Mac implementation path.

### Candidate model roles

A small dense Qwen-class model is a reasonable trainable-policy research
candidate.

`gpt-oss-20b` is a strong local inference/teacher benchmark because it is
open-weight, supports agentic/tool/structured-output use cases and is designed to
fit in roughly 16 GB of memory. Its suitability for this exact routing task must
be measured, not assumed.

The learned local orchestrator should initially route only high-confidence,
well-represented states. Low-confidence, novel or authority-sensitive states
escalate to GPT/human.

This creates a data flywheel:

```text
frontier model/human resolves hard state
-> accepted observable decision becomes training evidence
-> local policy handles recurring equivalent states
-> frontier calls concentrate on novel/ambiguous work
```

## 12. Phased implementation recommendation

### P0 - preserve current accepted flows

Do not retire browser/manual/supervised fallback paths yet.

### P1 - structured shadow independent reviewer

Housing remains the preferred first pilot. The goal is exact-SHA structured GPT
review with no write authority.

Credential/event limitations discovered during the attempted pilot are evidence,
not reasons to invent a weaker trigger contract.

### P2 - one-task bounded correction

Claude produces/fixes one approved task. CI and fresh GPT review gate each
candidate. No intermediate human correction approval inside the bounded scope.

### P3 - two-task Pet milestone

One draft PR, one writer, exact task checkpoints, independent review per task,
automatic task-to-task advance, fresh cumulative final review, manual merge.

### P4 - Fishing deterministic CI/package lane

Move deterministic test/package production to hosted CI, preserving real-browser
and device-bound evidence as explicit local lanes.

### P5 - research/evidence profile

Automate integrity verification only. Product adoption remains a distinct human
decision.

### P6 - shared extraction

Move only proven common identity/schema helpers into ADW or a reusable workflow
after two repository pilots justify reuse.

### P7 - local learned orchestrator

Begin trajectory collection before training; benchmark shadow routing; adopt any
local policy only through a later evidence/review decision.

## 13. D13 conformance evidence required before reconsideration

This design proposal does not satisfy D13.

Before D13 may be reconsidered, a later accepted evidence package should show at
minimum:

1. exact authority and state ownership with no second task database;
2. one-writer exclusion and stale/duplicate-event rejection;
3. candidate/CI/review identity binding across corrections;
4. read-only independent reviewer isolation;
5. privileged effects separated from model execution;
6. restart/recovery from zero conversational context;
7. bounded retry/correction behavior;
8. missing evidence failing closed;
9. no hidden Product acceptance or merge authority;
10. one complete milestone dry run with final cumulative review;
11. interruption/recovery negative cases;
12. evidence that ready-made GitHub/agentic mechanisms were compared before any
    custom controller selection.

A design, schema or test plan alone is not this evidence.

## 14. Explicit non-authorities

This proposal does not authorize:

- `gh-aw` adoption;
- Claude Code Action installation;
- Codex GitHub Action installation;
- API billing or secret creation;
- automatic corrections;
- automatic task activation;
- unattended/AFK execution;
- automatic PR comments or reviews;
- branch-protection changes;
- automatic merge;
- local LLM training;
- collection of private model chain-of-thought;
- a new common task database;
- D5 or D13 mechanism selection;
- Workflow v1 amendment.

## 15. Recommended next gate

The next D13-specific gate after publication of this candidate should be:

**fresh independent review of this exact design candidate**

That review should determine whether the proposal:

- faithfully stays inside the accepted D13 prerequisite design scope;
- preserves D5/D13/X3 boundaries;
- fully defines the prerequisite ownership/conformance evidence question;
- avoids silently selecting a mechanism;
- keeps local-learning work a later optimization rather than a prerequisite.

A permitting review would support a separate coordinator disposition. Only that
later disposition may decide whether this proposal becomes an accepted
prerequisite design basis.

## External capability references

These are evidence/navigation links, not normative owners:

- GitHub Agentic Workflows overview:
  https://github.github.io/gh-aw/
- GitHub Agentic Workflows safe outputs:
  https://github.github.io/gh-aw/reference/safe-outputs/
- GitHub Agentic Workflows engines:
  https://github.github.io/gh-aw/reference/engines/
- OpenAI Codex GitHub Action:
  https://learn.chatgpt.com/docs/github-action
- MLX-LM LoRA/QLoRA:
  https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md
- Microsoft Agent Lightning:
  https://github.com/microsoft/agent-lightning
- OpenAI gpt-oss:
  https://openai.com/index/introducing-gpt-oss/

## Candidate acceptance boundary

A commit, push or PR containing this document is not acceptance.

The exact candidate requires independent review. Any material correction creates
a new candidate identity and requires fresh affected review. Coordinator
acceptance and later merge remain separate gates.

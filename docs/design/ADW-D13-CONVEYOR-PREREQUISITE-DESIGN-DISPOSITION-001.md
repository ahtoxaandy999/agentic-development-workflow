---
id: ADW-D13-CONVEYOR-PREREQUISITE-DESIGN-DISPOSITION-001
artifact: design-disposition
artifact_status: active
owner: chatgpt-coordinator
decision: accept-d13-conveyor-prerequisite-design-as-prerequisite-design-basis
decision_subject_commit: 72451ac5733a3f13d88f6ce566b455eb8012c945
decision_subject_path: docs/design/ADW-D13-CONVEYOR-PREREQUISITE-DESIGN-001.md
decision_subject_blob: d72381dcbc8b99b2c3237faaab9b4cdbed681dcd
independent_review_verdict: PASS
independent_review_findings: 0-blocker-0-major-0-minor-0-note
publication_pr: 15
publication_merge_commit: ec62de8caf4c048521088a367cfa72d7e33d5dcd
decided_on: 2026-09-22
normative_effect: none
supersedes: null
---

# ADW-D13-CONVEYOR-PREREQUISITE-DESIGN-DISPOSITION-001

## Decision

**ACCEPT THE EXACT CORRECTED D13 CONVEYOR PREREQUISITE DESIGN AS THE D13 PREREQUISITE-DESIGN BASIS.**

Accept only exact candidate:

`72451ac5733a3f13d88f6ce566b455eb8012c945`

at:

`docs/design/ADW-D13-CONVEYOR-PREREQUISITE-DESIGN-001.md`

with Git blob:

`d72381dcbc8b99b2c3237faaab9b4cdbed681dcd`

and SHA-256:

`c90f2123debc8d1e49387ae8b27dd0746fbd898a845517cf8714410688a43ca6`.

This acceptance establishes the exact corrected proposal as the accepted explanatory
and prerequisite-design basis for future D13 evidence/readiness work.

It does **not** satisfy the D13 conformance-evidence prerequisite, reconsider D13,
select a mechanism, authorize a PoC, reopen D5, amend Workflow v1, or create
implementation/unattended authority.

## Exact review and correction chain

The initial candidate:

`6e0117f523608f699734b64237abc6c541cb48dd`

received independent verdict:

`REQUIRES CORRECTION`

with:

- 0 BLOCKER;
- 2 MAJOR;
- 0 MINOR;
- 0 NOTE.

The two material findings were:

1. `ADW-D13-001`: incomplete runtime-state ownership, adapter boundary,
   writer/duplicate control, side-effect containment and reconciliation design;
2. `ADW-D13-002`: incomplete D13 conformance-evidence contract and missing
   explicit DI-1 / DI-2 preservation.

Correction commit:

`72451ac5733a3f13d88f6ce566b455eb8012c945`

has sole parent:

`6e0117f523608f699734b64237abc6c541cb48dd`.

Fresh affected independent rereview of the corrected candidate returned:

**PASS**

with:

- 0 BLOCKER;
- 0 MAJOR;
- 0 MINOR;
- 0 NOTE;
- `ADW-D13-001: RESOLVED`;
- `ADW-D13-002: RESOLVED`.

The independent review establishes review state only. It is not the acceptance
decision recorded by this disposition.

## Publication identity

The exact reviewed and accepted candidate was merged through PR #15.

Publication facts:

- original base:
  `796fef15a7ba3b78b57c1f06f5911c6a3f85dad5`;
- exact accepted head:
  `72451ac5733a3f13d88f6ce566b455eb8012c945`;
- candidate tree:
  `c9ab70c64b10144cd28acb2846643d6a0b2d63f3`;
- merge commit:
  `ec62de8caf4c048521088a367cfa72d7e33d5dcd`;
- merge ordered parents:
  1. `796fef15a7ba3b78b57c1f06f5911c6a3f85dad5`;
  2. `72451ac5733a3f13d88f6ce566b455eb8012c945`;
- merge tree:
  `c9ab70c64b10144cd28acb2846643d6a0b2d63f3`.

The merge tree equals the accepted candidate tree. No post-review content drift
was observed in publication.

Human signal `++m` was explicitly bound to PR #15 and the exact corrected
candidate after the fresh PASS. It authorized acceptance and merge of that exact
subject only.

## Accepted design basis

The accepted design basis now includes the following mechanism-neutral
prerequisite conclusions.

### Runtime state ownership

There is exactly one designated execution-state recorder for mutable orchestration
lifecycle state.

It does not become owner of:

- Product or architecture authority;
- Git/PR identity;
- CI/verification truth;
- independent-review truth;
- disposition/normativity/acceptance;
- side-effect truth.

Any runtime cache is derived/disposable and cannot authorize transitions.

Any recovery journal, if later implemented, is append-only historical evidence,
not a competing current-state owner.

### Adapter boundary

The accepted design separates:

1. policy/authority;
2. lifecycle orchestration;
3. execution/transport and privileged side-effect ownership.

The lifecycle layer may evaluate and record allowed transitions, but may not
silently acquire Git write, review-publication, merge, Product-decision or other
privileged-effect authority.

### Writer and duplicate controls

A future implementation must establish:

- one logical writer;
- generation/subject-bound mutation requests;
- stale-writer refusal;
- duplicate-operation idempotency;
- stale-event reread/rejection;
- operation-aware retry.

Worktree separation, CODEOWNERS and prompt instructions are not sufficient writer
fencing by themselves.

### Side effects and containment

Each privileged external-effect domain requires one accountable side-effect owner.

Cancellation request, process exit or transport failure is not containment.
Containment requires authoritative evidence that further effects have ceased or
are boundedly isolated and that residual effects have durable ownership.

### Reconciliation

Reconciliation must compare, without collapsing ownership:

- current policy/task authority;
- orchestration/recovery history;
- workspace/local Git;
- live remote Git/PR/check state;
- external-effect receipts.

Precedence follows authoritative ownership, not latest timestamp.

Unknown or partial effects fail closed and require reconciliation/intervention
before retry, resumption or terminal closure.

## Accepted D13 conformance-evidence design

The accepted proposal explicitly preserves DI-1 and DI-2.

### DI-1

Orthogonal planes remain orthogonal.

Task control, cancellation, recovery, product/work-product state, verification,
review, disposition, normativity, baseline acceptance and join/integration state
cannot be collapsed into GitHub/model/native runtime statuses.

### DI-2

Materially stale authority blocks reliance.

Retry remains operation-aware. Containment and recovery remain distinct.
Completed recovery history remains durable. Reopening creates a distinct episode.
Accountable intervention and terminal guards remain reachable and cannot be
bypassed by controller status or model confidence.

### Evidence package requirements

A future D13 conformance package must bind exact:

- design/policy revision;
- orchestration implementation;
- adapter/controller revision;
- runtime/engine/configuration;
- permission profile;
- repository/profile fixtures;
- scenario-suite revision;
- run/attempt identities.

Required evidence forms include:

- subject manifest;
- transition evidence;
- remote/local repository identity evidence;
- side-effect receipts;
- writer-fencing evidence;
- recovery history;
- reviewer-isolation evidence;
- negative controls;
- independent conformance review;
- later accountable disposition.

Mandatory scenarios include stale/duplicate events, stale/competing writer,
interruption/restart, partial/queued effects, missing evidence, contradictory
plane statuses, reviewer isolation, recovery reopening, accountable intervention
and terminal-guard denial.

A green aggregate is insufficient.

Non-applicable is not PASS.

Missing, stale, contradictory or partial load-bearing evidence means:

**CONFORMANCE NOT ESTABLISHED**

for the D13 prerequisite.

That is an evidence result, not a Product-semantic failure and not authority for
blind retry or scope expansion.

## D13 / D5 / X3 status

This disposition does not change the controlling mechanism dispositions.

D13 remains:

**CONFIRM DEFER**

The accepted prerequisite design satisfies only the design-basis part of the
existing reconsideration prerequisite. Actual accepted conformance evidence does
not yet exist.

D5 remains:

**CONFIRM DEFER**

Accepting the D13 design does not select or authorize Codex SDK/App Server.
A future App Server-based PoC still requires an applicable D5 decision or an
explicit superseding disposition naming both D5 and D13.

X3 remains:

**CONFIRM REJECT**

Unmodified Symphony/custom-harness lifecycle, retry, stale-input, cleanup or
tracker defaults do not gain ADW authority.

## Explicit non-authorities

This disposition creates no authority for:

- `gh-aw` adoption;
- Claude Code Action installation or use;
- Codex GitHub Action installation or use;
- App Server selection;
- Symphony deployment;
- custom orchestration-runtime implementation;
- automatic dispatch;
- automatic correction loops;
- automatic task-to-task advancement;
- reviewer-to-GitHub mutation;
- automatic PR ready transition;
- branch-protection/ruleset change;
- unattended or AFK execution;
- automatic merge;
- API billing or secret creation;
- local LLM training;
- trajectory-data collection;
- a shared task database;
- D13 reconsideration;
- D5 reconsideration;
- Workflow v1 amendment;
- baseline acceptance.

## Local learned orchestrator boundary

The accepted design may be used later as research input for a learned local
routing policy, but this disposition creates no training/data-collection
authority.

The local-model lane remains future-only:

1. collect only separately authorized observable trajectory data after the real
   conveyor is stable;
2. benchmark in shadow mode;
3. evaluate supervised adaptation before preference/RL methods;
4. keep novel, low-confidence or authority-sensitive states escalated.

No Qwen-class model, MLX-LM, gpt-oss, Agent Lightning or other stack is selected
by this disposition.

## Next gate

The D13-specific next gate is:

**D13 conformance-evidence readiness assessment gate**

That next gate is read-only analysis/design work unless separately authorized
otherwise.

Its purpose is to compare the accepted conformance-evidence contract against
actual existing evidence from current supervised workflows and repository pilots,
identify which evidence is already reusable, identify exact gaps, and determine
whether a later evidence-acquisition or bounded-PoC decision can even be
considered.

The readiness assessment may not:

- install or select an orchestration mechanism;
- execute a PoC;
- collect new privileged runtime evidence;
- authorize automated/unattended operation;
- infer that existing Pet/Housing successes satisfy D13 without exact applicability
  analysis;
- reopen D5 or D13.

The repository-wide current gate remains unchanged.

## Acceptance boundary

This disposition accepts one exact prerequisite-design basis only.

It does not make that design normative Workflow v1 policy and does not establish a
new accepted repository baseline.

Any future material design correction creates a new subject requiring fresh
review and a new applicable disposition.

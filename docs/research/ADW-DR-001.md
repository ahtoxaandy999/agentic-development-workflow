---
id: DR-001
artifact_status: draft
authority: evidence
owner: agentic-development-research
question: coordinator gates and artifact lifecycle before Workflow v1
scope: coordinator-gates-and-artifact-lifecycle-requirements-before-workflow-v1
decision_consumer: coordinator DR-001 recommendation-disposition decision before Workflow v1 design
repository: ahtoxaandy999/agentic-development-workflow
repository_state_at_authorization: "main@265f171502de8a2d8844ae4ccf277c58e56a20cb; verified 2026-09-03"
research_gate_ref: ADW-DR-001-GATE-001
research_gate_correction_ref: ADW-DR-001-GATE-CORR-001
supersedes: null
---

# DR-001: Coordinator gates and artifact lifecycle before Workflow v1

## Status and authority

- This file is a durable draft research contract.
- `artifact_status: draft` does not mean completed, reviewed, adopted, active, normative, or accepted.
- Mutable DR-001 research status, dependencies, artifact pointer, current disposition, supersession, and next gate belong to the Research Register.
- The research contract is authorized by `ADW-DR-001-GATE-001` as corrected by `ADW-DR-001-GATE-CORR-001`.
- Chat, memory, summaries, and handoffs are not substitutes for this durable contract.
- Workflow v1 remains unadopted.

## Canonical question

`coordinator gates and artifact lifecycle before Workflow v1`

Operational framing:

Determine the evidence-backed lifecycle, ownership, durability, safety, proportionality, and minimum-context requirements that a future Workflow v1 would need to satisfy.

This research does not design Workflow v1.

## Decision consumer

A later explicit coordinator DR-001 recommendation-disposition decision that may accept, reject, narrow, or defer evidence-backed requirements and constraints as inputs to a separately gated Workflow v1 design effort.

That later decision must identify the exact evidence identity and decision scope.

It does not itself adopt Workflow v1.

## Research owner and role separation

Research owner:

`agentic-development-research`

The researcher owns evidence production only.

The researcher may not independently:

- source-review their own completed evidence;
- adopt their own recommendations;
- update normative owners without authorization;
- accept their own artifact or candidate;
- expand the authorized research scope.

Independent source review and coordinator disposition remain separate gates.

## Scope

DR-001 investigates evidence concerning:

1. lifecycle states and transitions that must remain distinct;

2. which gates appear universal and which may be conditioned on:

   - risk;
   - uncertainty;
   - reversibility;
   - blast radius;

3. transition ownership across:

   - coordinator;
   - researcher;
   - executor;
   - independent reviewer;
   - human/maintainer;

4. durable versus ephemeral state;

5. authoritative ownership of:

   - task/work state;
   - research state;
   - decisions;
   - execution authorization;
   - candidate identity;
   - review evidence;
   - acceptance evidence;
   - handoff/navigation state;

6. controls against:

   - competing truth;
   - stale chat state;
   - executor self-acceptance;
   - implicit lifecycle transitions;
   - review of mutable targets;
   - passing checks being mistaken for acceptance;

7. proportionate scaling for small, clear, reversible tasks;

8. minimum safe execution and review context for a fresh agent;

9. unresolved questions that belong to later research;

10. the completed bootstrap lifecycle as an internal case study, including its corrections and post-acceptance state synchronization.

## Non-scope

DR-001 must NOT:

- design, specify, or adopt Workflow v1;
- codify the bootstrap sequence as Workflow v1;
- select GitHub Issues, Projects, pull requests, or another tracker;
- adopt a task schema or normative state machine;
- select or configure Apps, MCP servers, skills, hooks, automation, or tooling;
- design parallel scheduling or worktree orchestration;
- design AFK execution;
- create implementation code;
- change or supersede Bootstrap Context Baseline v0;
- reopen accepted bootstrap decisions without new contradictory evidence;
- perform dedicated research reserved for DR-002, DR-003, DR-004, or DR-005.

The report may identify requirements, evidence gaps, constraints, or open questions relevant to those later topics, but must defer their dedicated research.

## Evidence classes and source hierarchy

Use:

1. live immutable repository evidence;
2. accepted internal normative artifacts;
3. durable bootstrap lifecycle records;
4. internal negative evidence and correction history;
5. narrowly selected external primary evidence for generalizable governance principles;
6. explicit missing-evidence and contradiction records.

For load-bearing claims prefer:

1. live repository state, exact commits, diffs, configuration, and durable repository objects;
2. official vendor/platform documentation;
3. official standards, specifications, frameworks, or primary repositories;
4. original empirical research or first-party case studies when empirical behavior is material;
5. secondary sources only for discovery or explicitly qualified context.

There is no source-count quota.

Each material external source must record relevant date/version, scope, limitations, and applicability.

## Required internal evidence

At minimum inspect:

- AGENTS.md
- PROJECT-CHARTER.md
- docs/policies/research-evidence.md
- docs/research/research-register.md
- relevant portions of docs/research/ADW-BOOTSTRAP-RESEARCH-001.md
- Bootstrap Context Baseline v0 at: `13b05e075ec04aa91494cd18f7d29f7249028cb5`
- current repository state at explicit full SHA;
- Git commit history and relevant diffs;
- durable source-review/adoption/acceptance evidence where available;
- GitHub Issue #1 acceptance record;
- bootstrap correction history;
- post-acceptance state synchronization;
- observed missing durable records or stale-state incidents.

Trace the actual bootstrap path:

```text
research
→ source review
→ adoption
→ execution
→ correction
→ exact-SHA candidate review
→ coordinator acceptance
→ durable acceptance record
→ post-acceptance state synchronization
```

For each available transition identify:

- durable record;
- exact SHA or immutable identity where applicable;
- date;
- owner/actor;
- transition;
- correction or exception;
- missing durable evidence.

Chat or memory may help locate evidence but cannot replace durable evidence.

## Bounded external evidence

Use only the minimum external primary evidence needed for general principles not established sufficiently by the internal case.

Potential material areas:

- separation of duties and independent review;
- change authorization and traceability;
- immutable/content-addressed review targets;
- risk-based process tailoring;
- audit/evidence durability and provenance;
- human accountability for consequential transitions.

Do not broaden this into a survey of development methodologies.

## Explicit deferrals

Defer dedicated research on:

- Matt Pocock workflow patterns;
- OpenAI Codex, Harness, or Symphony patterns;
- parallel execution and worktree scheduling;
- AFK operation;
- Apps;
- MCP servers;
- skills;
- hooks;
- automation;
- tooling selection;
- tracker selection;
- task-schema design.

DR-001 may record dependencies or open questions for these topics but must not perform their dedicated research.

## Key subquestions

Gather evidence sufficient to evaluate:

1. Which state planes and lifecycle transitions require separation?

2. Which gates are invariant and which may be risk-conditional?

3. Who may initiate, authorize, execute, review, adopt, accept, and record each transition?

4. Which state requires durable, addressable evidence?

5. What should be the authoritative owner for each state class?

6. Which controls address each observed failure mode?

7. What evidence supports a reduced process for small, low-risk work?

8. What minimum task packet permits safe execution by a fresh agent?

9. What minimum evidence packet permits independent review by a fresh reviewer?

10. Which unresolved matters must be deferred to later research?

Do not presuppose the answers.

## Contradiction, negative-evidence, and missing-evidence handling

For conflicting credible claims record:

- source;
- authority;
- date/version;
- scope;
- configuration;
- actual contradiction.

Do not average incompatible claims or resolve them through assumption.

Distinguish:

- contrary evidence;
- absence of evidence;
- unavailable evidence;
- stale evidence;
- configuration-dependent evidence.

Missing decisive evidence must narrow or block the affected recommendation and state what could resolve it.

Contradiction with an accepted bootstrap decision must be surfaced for a separate coordinator gate.

DR-001 cannot amend Bootstrap Context Baseline v0.

Stale or unverifiable live repository state stops dependent analysis.

## Recommendation boundary

The final report may recommend:

- candidate lifecycle requirements;
- candidate invariants;
- conditionality criteria;
- ownership constraints;
- durability classifications;
- controls for observed failure modes;
- minimum-context requirements;
- later research questions.

It may NOT present as adopted:

- a Workflow v1 design;
- a task schema;
- a normative state machine;
- artifact or tracker selection;
- tooling choices;
- policy.

Facts, inferences, recommendations, and unresolved questions must remain visibly separate.

## Evidence date and freshness semantics

During evidence production:

- record actual evidence-collection dates;
- record exact GitHub SHAs for repository claims;
- record external source publication/version/access dates where material;
- reverify unstable repository state through the connected GitHub source;
- do not populate publication-only metadata yet.

At evidence freeze:

- set `evidence_as_of` to the final date on which load-bearing evidence was verified;
- record the full GitHub SHA used at freeze;
- record accepted baseline SHA separately;
- materially changed evidence requires a new frozen identity;
- no silent refresh is allowed.

## Stop boundary

Evidence production stops when:

- every contracted subquestion has supported findings or an explicit evidence gap;
- source register and citations are complete;
- contradictions and negative evidence are documented;
- material assumptions, uncertainty, limitations, and deferrals are recorded;
- live repository evidence has been reverified;
- bounded recommendations are complete;
- no substantive research edit remains planned.

Stop earlier on:

- authority conflict;
- unverifiable live state;
- unsafe evidence handling;
- unresolved scope expansion;
- dependency on deferred research required to answer a load-bearing question.

Do not proceed from evidence production into:

- source review;
- adoption;
- normative materialization;
- Workflow v1 design.

## Intended final report structure

The completed report is expected to contain:

1. Metadata and immutable identity
2. Executive evidence verdict
3. Question, scope, non-scope, method, and stop boundary
4. Source register and evidence classification
5. Bootstrap case-study chronology
6. Findings by subquestion
7. Candidate lifecycle and ownership requirements
8. Universal-versus-conditional gate evidence
9. Durability and authoritative-owner analysis
10. Failure modes and control evidence
11. Small-task proportionality evidence
12. Minimum fresh-agent context
13. Contradictions, negative evidence, and missing evidence
14. Deferred dependencies and open questions
15. Alternatives, tradeoffs, and recommendations
16. Limitations, freshness, and supersession conditions

This structure is an output contract, not evidence that the sections have already been researched.

## Independent source-review criteria

A later independent reviewer must verify:

- exact frozen report identity;
- compliance with scope and non-scope;
- claim-level evidence support;
- primary-source preference;
- live GitHub provenance and full-SHA use;
- completeness and accuracy of the bootstrap trace;
- freshness and source limitations;
- handling of corrections, contradictions, and negative evidence;
- separation of fact, inference, recommendation, and adoption;
- support for universal or conditional assertions;
- coverage of every contracted subquestion;
- explicit deferral of later research;
- absence of Workflow v1 design or tool selection;
- sensitive-information handling;
- sound evidence-to-recommendation reasoning.

Source review establishes evidence quality only.

It grants no adoption, execution, normative-update, Workflow v1, or acceptance transition.

## Exact-byte freeze and immutable identity

While DR-001 is in progress this file remains mutable and:

```yaml
artifact_status: draft
```

Publication-only fields remain absent.

Evidence freeze occurs only after the stop boundary is satisfied.

At freeze, populate:

```yaml
research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: <actual final evidence-verification date>
repository_state: "main@<full SHA verified at freeze>; accepted baseline 13b05e075ec04aa91494cd18f7d29f7249028cb5"
```

`artifact_status` remains `draft` for the frozen source-review target.

After final content and metadata are complete:

1. serialize the exact complete file as UTF-8 using its actual final newline state;
2. calculate SHA-256 over the exact raw file bytes;
3. do not normalize whitespace, newline form, or Unicode;
4. identify the review target as: `DR-001@sha256:<lowercase-64-hex-digest>`;
5. record byte length alongside the digest.

Any byte change creates a new identity and invalidates review of the previous digest.

A later draft → active transition creates different bytes and therefore a new digest.

The source-review verdict remains tied to the frozen draft digest.

Any substantive evidence change after source review requires a new freeze identity and fresh source review.

## Later coordinator decision informed

The final evidence is intended to inform a separate coordinator DR-001 recommendation-disposition decision.

That decision determines which evidence-backed requirements, constraints, deferrals, or unresolved questions may become inputs to a separately gated Workflow v1 design effort.

It must identify:

- exact evidence identity;
- decision scope;
- any proposed normative owner.

It does not itself adopt Workflow v1.

## Preserved boundaries

Throughout DR-001:

- Bootstrap Context Baseline v0 remains: `13b05e075ec04aa91494cd18f7d29f7249028cb5`
- Workflow v1 remains unadopted.
- DR-002, DR-003, DR-004, and DR-005 remain unstarted.
- tooling selection remains deferred.
- tracker selection remains deferred.
- no normative artifact changes occur without a separate coordinator gate.

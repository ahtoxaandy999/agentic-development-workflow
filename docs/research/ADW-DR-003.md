---
id: DR-003
artifact_status: draft
authority: evidence
owner: agentic-development-research
question: >
  Which tool-agnostic execution-control requirements are necessary for
  bounded agent delegation, parallel work, state freshness, context handoffs,
  observability, correction/review waves, unattended execution, stopping,
  and recovery?
scope: tool-agnostic-bounded-agent-execution-parallelism-and-autonomy-controls-evidence
decision_consumer: >
  Separate coordinator DR-003 recommendation-disposition decision feeding the
  Workflow v1 design gate.
repository: ahtoxaandy999/agentic-development-workflow
repository_state_at_authorization: "main@7d573ed97e16fe56b43a98ccaed93bb4764627e5; verified 2026-09-03"
research_gate_ref: ADW-DR-003-GATE-001
supersedes: null
---

# DR-003: Bounded agent execution, parallelism, and autonomy controls

## Status and authority

This file is the durable draft research contract for DR-003.

The researcher owns evidence production only.

The researcher may not:

- implement or trial an orchestration system;
- grant privileges;
- conduct unattended repository writes;
- source-review or adopt their own report;
- design Workflow v1;
- select tooling;
- expand scope without a new coordinator gate.

Mutable research state belongs to the Research Register.

## Canonical question

Which tool-agnostic execution-control requirements are necessary for bounded
agent delegation, parallel work, state freshness, context handoffs,
observability, correction/review waves, unattended execution, stopping, and
recovery?

## Decision consumer

A later separate coordinator DR-003 recommendation-disposition decision.

Only a durable coordinator disposition may feed DR-003 conclusions into the
Workflow v1 design gate.

This grants no implementation, autonomy, permission, or tooling authority.

## Scope

Investigate requirements concerning:

1. Explicit, bounded delegation authority and fresh-agent execution context.
2. Preconditions and hazards for parallel work.
3. Isolation of work, shared mutable state, dependency coordination,
   aggregation, and join conditions.
4. Live-state freshness, immutable inputs, stale-state detection, and
   invalidation.
5. Context handoffs, provenance, compression loss, and continuity.
6. Minimum observability for progress, failure, intervention, and auditability.
7. Correction and review waves, including material-change and re-review
   conditions.
8. Eligibility and limits for unattended execution.
9. Stop, cancellation, escalation, timeout, budget, and privilege boundaries.
10. Recovery from partial failure, duplicate execution, retries, interruption,
    and inconsistent state.
11. Least privilege, sensitive-data handling, identity limits, and accountable
    human or coordinator intervention.
12. Tool-agnostic requirements, residual risks, and matters deferred to design
    or tooling evaluation.

## Non-scope

DR-003 must not:

- design or adopt Workflow v1;
- prescribe a concrete parallel-wave, queue, scheduler, worktree,
  synchronization, or handoff algorithm;
- define a fixed task or review packet schema;
- select or configure OpenAI products, models, Apps, MCP servers, skills,
  hooks, automation, trackers, or other tooling;
- infer effective configuration from advertised capability;
- perform production, privileged, destructive, broad-connector, or unattended
  write experiments;
- authorize routine agent writes, AFK operation, or new permissions;
- choose quantitative autonomy, risk, timeout, budget, or concurrency
  thresholds;
- perform DR-002 practitioner workflow research beyond necessary interface
  dependencies;
- reopen accepted DR-001 conclusions without new contradiction;
- modify normative or live repository state.

## Contracted subquestions

The report must answer, or identify an explicit evidence gap for:

1. What authority, context, constraints, evidence destination, and stop
   conditions are required for bounded delegation?
2. Which repository, dependency, configuration, and candidate identities must
   be pinned or reverified?
3. Under what conditions can work proceed in parallel without unsafe
   interference or competing truth?
4. What isolation, ownership, aggregation, and join properties are required?
5. What information must a context handoff preserve, and what failure modes
   arise from summarization or stale context?
6. What minimum signals make execution observable and interruptible?
7. How should correction, material change, review, and re-review interact?
8. What preconditions and ceilings are required before unattended execution
   can be considered?
9. What conditions require stopping, cancellation, or accountable
   intervention?
10. What recovery properties address retries, partial completion, lost
    updates, duplication, and interrupted work?
11. What least-privilege, identity, provenance, and sensitive-data controls are
    supported?
12. Which findings are tool-agnostic requirements, which are mechanism
    candidates, and which must remain deferred?

No concrete control mechanism is presupposed.

## Source hierarchy

Apply the Research Evidence Policy independently:

1. Live repository state and exact internal artifacts.
2. Current official vendor/platform documentation.
3. Primary repositories, specifications, standards, and research papers.
4. First-party case studies with explicit environment and limitations.
5. Documented practitioner evidence.
6. Secondary sources only for discovery or qualified context.

For OpenAI or harness claims record, where material:

- model;
- interface;
- plan;
- workspace;
- version;
- date;
- configuration variance.

Documentation establishes documented capability, not availability or effective
configuration in a particular account.

Load-bearing concurrency, recovery, security, or autonomy claims require
appropriate primary systems, security, safety, or empirical evidence.

Vendor examples and demonstrations must not be generalized without support.

There is no source-count quota.

## Required evidence and output

The researcher must:

- inspect the Charter, Research Evidence Policy, Register, and exact live
  repository state through GitHub;
- consume DR-001 through its accepted disposition, qualifications, deferred
  matters, and source-review finding;
- preserve DR-001 accepted semantic separation, immutable formal-review
  targets, conditional independence, accountable consequential decisions,
  qualitative proportionality, live-state rechecks, and scalable packet
  categories;
- maintain a source register with claim-level traceability, dates/versions,
  access dates, environments, limitations, and applicability;
- provide a coverage matrix for every subquestion;
- distinguish documented capability, observed behavior, effective
  configuration, inference, and proposed requirement;
- produce hazard-to-control mappings stating preconditions, detectable
  signals, required response, verification evidence, and residual risk;
- analyze shared-state races, lost updates, duplicate work, stale
  dependencies, partial failure, aggregation errors, cancellation failure, and
  recovery;
- compare alternatives and tradeoffs without selecting mechanisms;
- identify evidence gaps around unattended operation and avoid unsupported
  safety assurances;
- separate facts, inferences, recommendations, and unresolved questions;
- state explicitly what belongs to Workflow v1 design and what remains
  deferred to DR-005.

## Contradictions and missing evidence

Record conflicting claims with:

- source authority;
- date/version;
- model/interface/configuration where material;
- scope;
- precise disagreement.

Do not resolve documented-versus-observed differences by assumption.

Missing decisive safety or control evidence must block or narrow the affected
recommendation.

A platform capability may not be treated as available until effective
configuration is verified at the point of reliance.

Contradiction with the Charter, Research Evidence Policy, Research Register,
or accepted DR-001 disposition stops the affected conclusion and requires a
coordinator gate.

Material contradiction with DR-002 must be carried to the later join.

## Stop boundary

Evidence production is complete only when:

- every subquestion has supported findings or an explicit evidence gap;
- source and coverage registers are complete;
- hazards, controls, residual risks, contradictions, negative evidence,
  assumptions, limitations, and deferrals are recorded;
- recommendations remain tool-agnostic and do not encode Workflow v1;
- unstable external and live repository facts have been reverified;
- no substantive research edit remains planned.

Stop earlier for:

- stale or unverifiable state;
- authority conflict;
- unsafe evidence handling;
- required privilege expansion;
- uncontrolled experimentation;
- scope expansion;
- dependence on premature tool selection.

Do not proceed into:

- implementation;
- source review;
- coordinator disposition;
- normative materialization;
- Workflow v1 design;
- DR-005;
- parallel repository writes;
- unattended execution.

## Freeze and source review

While in progress:

artifact_status: draft

Publication-only metadata remains absent.

At freeze add:

research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: <actual final evidence-verification date>
repository_state: "main@<full SHA verified at freeze>; accepted baseline 13b05e075ec04aa91494cd18f7d29f7249028cb5"

Calculate SHA-256 and byte length from the exact complete UTF-8 bytes without
normalization.

Review identity:

DR-003@sha256:<lowercase-64-hex-digest>

Any byte change creates a different target.

Substantive correction requires a new target and fresh source review.

An independent reviewer must verify:

- exact identity;
- scope;
- complete contracted-question coverage;
- claim support;
- primary-source use;
- temporal and configuration freshness;
- documented-versus-effective capability distinctions;
- hazards and residual risk;
- contradiction handling;
- fact/inference/recommendation separation;
- absence of tool selection or Workflow v1 design;
- sensitive-information handling;
- evidence-to-requirement reasoning.

Source review establishes evidence quality only.

## Preserved boundaries

Workflow v1 remains unadopted.

DR-002 remains an independent parallel research task.

No autonomy, AFK execution, routine parallel writes, permissions, tooling, or
orchestration mechanism is authorized by this research contract.

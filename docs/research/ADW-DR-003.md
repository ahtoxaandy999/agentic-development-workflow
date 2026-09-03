---
id: DR-003
artifact_status: draft
authority: evidence
research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: 2026-09-03
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
repository_state: "main@89f55d237411eecdc4fbdf5c8b312630af968928; accepted baseline 13b05e075ec04aa91494cd18f7d29f7249028cb5"
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

# DR-003 evidence packet: tool-agnostic execution control

## Status and authority

This is a completed working evidence packet at the DR-003 evidence-production boundary. It is deliberately **unfrozen**, has not received independent source review, and has not received coordinator disposition. Its recommendations are proposed research outputs, not adopted requirements or Workflow v1.

Working evidence collection cutoff: 2026-09-03. This is not publication-only `evidence_as_of` metadata and does not create an immutable review identity.

No GitHub state was modified. No orchestration trial, privileged experiment, unattended write, tooling selection, Workflow v1 design, source review, recommendation adoption, or coordinator disposition was performed.

## 1. Executive evidence verdict

The collected evidence is sufficient to answer all twelve DR-003 subquestions at the level authorized by the durable contract.

The strongest findings are:

1. Delegation needs an explicit bounded contract: authority, objective, immutable input identities, allowed resources and actions, constraints, expected evidence and destination, validation, budgets, stop conditions, and escalation path.
2. Parallel work is supportable only for independent workstreams or where isolation, exclusive mutable-state ownership, conflict detection, and a defined join are enforced. Shared unconstrained mutation is not a safe parallelization basis.
3. A handoff summary is navigation state, not authoritative state. It must carry exact source and candidate pointers, material facts, uncertainties, actions, results, and unresolved work; a fresh agent must rehydrate state from the authoritative sources before a state-dependent action.
4. Formal review must remain bound to immutable candidate identity. A material correction creates a new candidate and renews affected verification and any applicable independent review.
5. Observability must make state, side effects, authority, identity, resource consumption, failure, retry, cancellation, and output verification reconstructable without exposing secrets.
6. Unattended operation is not justified by platform capability alone. It requires enforceable least privilege, immutable inputs, isolation, safe side-effect semantics, explicit ceilings, durable checkpoints, tested cancellation, monitoring, an accountable intervention path, and a safe default stop. The evidence does not establish a universal threshold that makes consequential unattended mutation safe.
7. Retry safety depends on operation semantics. Idempotency keys, version preconditions, deduplication, atomic publication, and reconciliation can control some failures; non-idempotent or externally visible effects require proof of non-application, domain-specific compensation, or accountable intervention.
8. Identity and provenance must be verified against trusted expectations. A content digest identifies bytes; an execution identity identifies an actor or service; neither alone proves authorization, correctness, approval, review independence, or trustworthiness.

No material contradiction with the accepted repository context or accepted DR-001 dispositions was found. No coordinator contradiction gate is triggered by this evidence packet. Configuration-dependent tensions and unresolved evidence gaps are recorded in Sections 11 and 12; they narrow later recommendations and block any claim that unattended consequential execution is generally safe.

## 2. Bounded question, method, and evidence classes

### Question

What tool-agnostic execution-control requirements should inform a later Workflow v1 design for bounded delegation, safe parallel work, freshness, handoffs, observability, correction and review waves, unattended execution, stopping, cancellation, and recovery?

### Method

The work followed the repository's authority order and the DR-003 contract:

- Live repository state was read through the connected GitHub app at the exact expected full commit SHA.
- The DR-003 contract, Research Register, Project Charter, and research-evidence policy were treated as authoritative for scope and method.
- DR-001 was consumed only through the findings needed by DR-003 and its accepted, qualified recommendation dispositions.
- Current primary vendor documentation, standards, specifications, and original empirical work were used for claims not established internally.
- Documented capability, observed behavior, effective configuration, inference, and proposed requirement are kept distinct.
- No product, provider, schema, scheduler, tracker, agent count, timeout, risk score, or Workflow v1 sequence is selected.

### Evidence-class legend

| Label | Meaning |
|---|---|
| VF | Verified fact from an identified source, within that source's scope |
| DC | Documented capability; not proof that the capability is enabled or safe in this repository |
| OB | Observed behavior in a bounded empirical system or study; external validity is limited |
| EC | Effective configuration; must be verified in the actual execution environment |
| IN | Inference derived from identified evidence and stated assumptions |
| PR | Proposed, non-normative requirement for later disposition |
| UE | Unresolved evidence or limitation |

## 3. Repository identity and authoritative internal context

Repository: `ahtoxaandy999/agentic-development-workflow`.

At initial collection, the connected GitHub app reported live `main` at exact commit [`79f5541113e7dfeedfde6f36f371031f3f3330fa`](https://github.com/ahtoxaandy999/agentic-development-workflow/commit/79f5541113e7dfeedfde6f36f371031f3f3330fa), dated 2026-09-03, with commit message `docs: start DR-002 and DR-003 research`. Final re-verification is recorded in Section 15.

The following files were read at that exact commit:

- [DR-003 durable contract](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-003.md), Git blob `b51cc0209f5ff3269ccf6c7c7ad29fe8647729bb`.
- [Research Register](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/research-register.md), Git blob `8d86d84fc00a2e2c468ed68f82a580c869fb8ddb`.
- [Project Charter](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/PROJECT-CHARTER.md), Git blob `c521f6869662f39106bcac0365426eb0e9bdb327`.
- [Research Evidence Policy](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/policies/research-evidence.md), Git blob `90572c47463f2d2adc493f9978c1c720fd8f8275`.
- [DR-001 evidence](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-001.md), Git blob `f142919d1ed1f6b1717cc965ab9232bbc60d4389`.
- [DR-001 source review](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-001-SOURCE-REVIEW-001.md), Git blob `d2b96bbf15dab1e21a1a17dee134644f5f1fb003`.

### DR-001 constraints consumed by DR-003

The Research Register records all twelve DR-001 recommendations as accepted inputs or constraints, with qualifications. DR-003 relies on the following qualified substance and does not reopen or expand it:

- Preserve semantic separation among evidence, disposition, authorization, candidate identity, verification, review, and acceptance; this does not require a separate artifact or gate for every small task.
- Give each mutable authoritative state class one owner inside the relevant control plane; concrete storage and synchronization remain unresolved.
- Bind formal review to immutable content identity; identity does not prove authorship, authorization, approval, review independence, or acceptance.
- Keep verification, review, and acceptance distinct; conditional gates may be omitted where applicable governance permits, but must not be falsely relabeled.
- Use conflict-free independent review when consequence, uncertainty, privilege, or governance warrants it; there is no adopted universal threshold.
- Reserve consequential authorization and acceptance for an accountable coordinator or human risk owner; there is no universal human gate for all work.
- Preserve addressable records for material decisions, exceptions, reviews, adoption, and acceptance where later reliance, audit, recovery, or cross-session coordination requires them; retention and storage remain unresolved.
- Apply qualitative proportionality by context and risk, not task size alone; there is no adopted score.
- Verify actual capability and effective configuration before relying on a control.
- Re-read live authoritative state at state-dependent transitions, including after acceptance; there is no adopted universal synchronization phase.
- Give fresh executors and reviewers scaled, self-sufficient packets; there is no fixed schema.
- Treat chat, memory, worktrees, and handoffs as working or navigation state unless explicitly promoted by an authorized process.

The source review accepted DR-001 as source-reviewed evidence with one nonblocking MINOR: DR-001 used NIST SP 800-53 Rev. 5 Release 5.1.1 although Release 5.2.0 was current, and blurred the September 2020 base publication with later catalog releases. The relevant controls were unchanged. This packet therefore cites current Release 5.2.0 and distinguishes the base publication from the catalog release.

## 4. Claim-level source register

All external sources were accessed on 2026-09-03 unless otherwise stated. An access date verifies what was read; it is not a claim that a continuously updated page remained unchanged afterward.

### Internal sources

| ID | Source identity | Date/version | Material claims used | Limits and applicability |
|---|---|---|---|---|
| I01 | [DR-003 contract at expected commit](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-003.md) | Commit `79f554…30fa`; blob `b51cc0…29bb`; verified 2026-09-03 | Authorized question, 12 subquestions, required evidence outputs, non-scope, stop boundary | Authority for this research task, not evidence that any candidate control is adopted |
| I02 | [Research Register](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/research-register.md) | Commit `79f554…30fa`; blob `8d86d8…8ddb`; verified 2026-09-03 | DR-003 is `in-progress`; dependency satisfied; DR-001 dispositions and qualifications; later freeze gate; DR-005 deferred | Mutable state snapshot; must be re-read at a later transition |
| I03 | [Project Charter](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/PROJECT-CHARTER.md) | Commit `79f554…30fa`; blob `c521f6…327`; verified 2026-09-03 | Authority hierarchy, bounded agents, exact-SHA candidate identity, least privilege, sensitive-data boundary, stop conditions, no implicit authority | Normative for current repository; not a general empirical claim about all systems |
| I04 | [Research Evidence Policy](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/policies/research-evidence.md) | Commit `79f554…30fa`; blob `90572c…275`; verified 2026-09-03 | Primary-source hierarchy, claim classification, freshness, capability/configuration separation, contradiction handling, freeze metadata rules | Normative research method for this repository |
| I05 | [DR-001 evidence](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-001.md) | Frozen target `DR-001@sha256:825204b8c45da36c4c7cd087d572e0b014352aee7a6fe1c54e0772aaec6acf0f`; 66,017 bytes; source file blob `f142919d1ed1f6b1717cc965ab9232bbc60d4389`; publication evidence date 2026-09-03 | Lifecycle/state separation, mutable-state ownership, immutable review target, proportionality, fresh-agent packet, re-verification | Evidence, not policy; consumed only through accepted disposition and qualifications |
| I06 | [DR-001 source review](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/79f5541113e7dfeedfde6f36f371031f3f3330fa/docs/research/ADW-DR-001-SOURCE-REVIEW-001.md) | Review record introduced in commit `2321f85ace4ddb008fc28bb4deda944f149be135`; blob at current commit `d2b96bbf15dab1e21a1a17dee134644f5f1fb003`; 2026-09-03 | Verdict `accepted-as-source-reviewed-evidence`; exact target; one NIST version MINOR | Source review establishes evidence quality only; no independent DR-003 review |
| I07 | [Expected/live repository commit](https://github.com/ahtoxaandy999/agentic-development-workflow/commit/79f5541113e7dfeedfde6f36f371031f3f3330fa) | Full SHA; 2026-09-03 | Current `main` identity for all repository-dependent claims in this packet | Commit identity proves content linkage, not approval, authorship, or permanent availability |

### Vendor documentation

| ID | Source identity | Date/version | Material claims used | Limits and applicability |
|---|---|---|---|---|
| V01 | [OpenAI: latest model guidance](https://developers.openai.com/api/docs/guides/latest-model) | Current documentation; accessed 2026-09-03 | Multi-agent is model-dependent/beta; programmatic orchestration needs explicit tools, outputs, evidence, concurrency, retry, stop, and side-effect boundaries | DC only; not proof of account availability, effective configuration, or safety |
| V02 | [OpenAI: multi-agent responses](https://developers.openai.com/api/docs/guides/responses-multi-agent) | GPT-5.6 beta documentation; accessed 2026-09-03 | Focused parallel subagents can help independent work; avoid ordered dependencies/shared mutable contention; root synthesizes; documented concurrency has a default but no universal safe total/depth bound | Product-specific DC and design guidance; beta schemas may change; no repository EC verified |
| V03 | [OpenAI: background mode](https://developers.openai.com/api/docs/guides/background) | Current documentation; accessed 2026-09-03 | Asynchronous status polling, cancellation, idempotent repeated cancellation, stream resumption by cursor/sequence | DC only; does not establish safe unattended mutation or effective retention/configuration |
| V04 | [OpenAI: compaction](https://developers.openai.com/api/docs/guides/compaction) | Current documentation; accessed 2026-09-03 | Context can be compacted; the compacted item is opaque and intended to preserve key prior state | DC only; no guarantee of exact semantic completeness for loss-sensitive handoffs |
| V05 | [OpenAI: agent orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration) | Current documentation; accessed 2026-09-03 | Manager-retained control and transfer-of-control handoffs are distinct; narrow specialist scope and structured/filtered context are supported; extra agents add prompt/trace/approval surfaces | Mechanism patterns, not a selected architecture |
| V06 | [OpenAI: guardrails and approvals](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) | Current documentation; accessed 2026-09-03 | Guardrail scope differs by placement; approval pauses should retain target/action/arguments/identity/time context; side-effect boundary is a control point | DC; guardrails are not comprehensive, and actual attachment/effectiveness needs EC verification |
| V07 | [OpenAI: observability integrations](https://developers.openai.com/api/docs/guides/agents/integrations-observability) | Current documentation; accessed 2026-09-03 | Traces can cover model calls, tool calls, handoffs, guardrails, and custom spans | DC; tracing availability is not evidence of completeness, retention, integrity, or safe content |
| V08 | [Codex: agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security) | Current documentation; accessed 2026-09-03 | Sandbox capability boundary and approval policy are separate; network/workspace/connector controls differ; prompt injection and broad access remain hazards | Product-specific; actual environment settings were not inspected and cannot be assumed |
| V09 | [Codex: subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Current documentation; accessed 2026-09-03 | Read-heavy independent work is a safer starting point; write-heavy parallelism increases conflict/coordination cost; prompts should define division, join/wait, and output | Product guidance, not empirical proof or a tool choice |
| V10 | [Codex: non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode) | Current documentation; accessed 2026-09-03 | Non-interactive runs can predefine sandbox/approval modes and structured output; credentials and mutation require care; generation and applying changes can be separated | DC only; no authorization to run this mode and no safety guarantee |

### Standards and specifications

| ID | Source identity | Date/version | Material claims used | Limits and applicability |
|---|---|---|---|---|
| S01 | [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and [current CPRT catalog](https://csrc.nist.gov/projects/cprt/catalog) | Base publication Sep. 2020; Release 5.2.0 final 2025-08-26 | Least privilege, audit-event content and protection, configuration change control, monitoring, incident handling, recovery | Broad control catalog; this packet maps principles and does not claim an applicable control baseline or compliance |
| S02 | [NIST AI RMF 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) | NIST AI 100-1, Jan. 2023; revision work noted by NIST in 2026 | Roles/accountability, documentation, monitoring, risk-tolerance-based treatment, safe failure, human-oversight questions | Voluntary and use-case agnostic; not a quantitative unattended threshold; revision underway |
| S03 | [NIST SSDF publications](https://csrc.nist.gov/projects/ssdf/publications) | SP 800-218 v1.1 final Feb. 2022; v1.2 draft dated 2025-12-17 | Final guidance remains v1.1; secure development practices are outcome-oriented and risk-tailored | v1.2 is draft and is not treated as final authority; not an orchestration specification |
| S04 | [Git data model](https://git-scm.com/docs/gitdatamodel) | Documentation current through Git 2.53.0; accessed 2026-09-03 | Git objects are content-addressed/immutable; commits bind tree and parents; refs are mutable | Mechanism evidence only; retention/reachability and governance remain separate |
| S05 | [git-update-ref](https://git-scm.com/docs/git-update-ref.html) | Documentation current through Git 2.53.0; accessed 2026-09-03 | Expected-old-object updates provide compare-and-swap protection; ref transactions have locking/atomicity qualifications | Git-specific mechanism; concurrent readers and multi-system side effects have residual risks |
| S06 | [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) | Internet Standard, June 2022 | Strong `If-Match` preconditions prevent lost updates; idempotent operations can be safely retried after some connection failures; non-idempotent retries require known semantics or proof the first attempt was not applied | Protocol semantics, not a workflow policy; APIs can implement semantics incorrectly |
| S07 | [W3C Trace Context](https://www.w3.org/TR/trace-context/) | Recommendation, 2021-11-23 | Standard trace identifiers propagate correlation across boundaries; sampling and trust flags have limits | Correlation is not authorization, durable audit, evidence integrity, or complete capture |
| S08 | [OpenTelemetry specifications](https://opentelemetry.io/docs/specs/) | Specification 1.60.0; semantic conventions 1.44.0 at access | Common trace/log/metric/resource semantics support cross-component observability | Mechanism-neutral standard family, but actual instrumentation/retention and redaction are EC |
| S09 | [RFC 9700: OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700.html) | BCP 240, January 2025 | Access tokens should be audience/resource/action restricted and sender constrained where appropriate | Applies directly to OAuth deployments and analogically to scoped delegated credentials; not every agent system uses OAuth |
| S10 | [SLSA v1.2](https://slsa.dev/spec/v1.2/) and [artifact verification](https://slsa.dev/spec/v1.2/verifying-artifacts) | v1.2, Approved; accessed 2026-09-03 | Verify subject digest, provenance signature, builder identity, source, build type, and parameters against trusted expectations; provenance has limits including trust in the builder platform | Supply-chain specification; used as provenance evidence, not as a selected workflow or compliance target |

### Original empirical and systems evidence

| ID | Source identity | Date/version | Material claims used | Limits and applicability |
|---|---|---|---|---|
| E01 | [Liu et al., “Lost in the Middle”](https://aclanthology.org/2024.tacl-1.9/) | TACL 2024 | Long-context task performance can depend on where relevant information appears; raw context length does not ensure reliable retrieval | Tested earlier model families and bounded tasks; supports a hazard, not a claim about every current model |
| E02 | [Zhu et al., “Cognitive Scaffold”](https://aclanthology.org/2026.acl-long.1170/) | ACL 2026 | Structured event snapshots can reduce context noise, but compression can introduce hallucination/loss | Specific system and benchmarks; not a universal handoff schema or guarantee |
| E03 | [Dean and Ghemawat, “MapReduce”](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/) | OSDI 2004 | Deterministic, partitionable work supports parallel execution/re-execution; a coordinator tracks task state; atomic output, duplicate suppression, and rescheduling control failures; nondeterminism weakens guarantees | Large-scale data-processing case, not agent workflow proof; used for mechanism properties and residuals |
| E04 | [Garcia-Molina and Salem, “Sagas”](https://www.cs.princeton.edu/research/techreps/598) | Technical report, 1987 | Long-lived work can be decomposed into transactions with compensating actions when exact global rollback is unavailable | Compensation is domain-specific and might not restore the original real-world state |
| E05 | [Kwa et al., “Measuring AI Ability to Complete Long Tasks”](https://arxiv.org/abs/2503.14499) | arXiv preprint, 2025 | Agent success declines with task horizon on the studied suite and capability estimates depend on harness/task distribution | Dated model set, benchmark-specific, not a safety threshold and not current effective capability |

## 5. Coverage matrix for the twelve contracted subquestions

| # | Contracted subquestion | Answer location | Principal evidence | Status / explicit gap |
|---|---|---|---|---|
| 1 | Authority, context, constraints, evidence destination, stop | F01, PR01 | I01–I04, I05 | Answered; fixed schema remains deferred |
| 2 | Pin and reverify repository, dependency, configuration, candidate identities | F02, PR02 | I03–I07, S04–S06, S10 | Answered; EC must be checked per run |
| 3 | Safe parallel conditions | F03, PR03 | V02, V09, E03, S05–S06 | Answered; no universal concurrency number |
| 4 | Isolation, ownership, aggregation, join | F04, PR04 | I05, V02, V05, E03, S05 | Answered; concrete mechanism deferred |
| 5 | Handoff minimum and summary/staleness failures | F05, PR05 | I03, I05, V04–V05, E01–E02 | Answered; no lossless-summary guarantee |
| 6 | Minimum observability and interruptibility | F06, PR06 | V03, V06–V07, S01–S02, S07–S08 | Answered; retention/integrity values unresolved |
| 7 | Correction, material change, review and re-review | F07, PR07 | I03, I05–I06, S04, S10 | Answered; materiality threshold remains contextual |
| 8 | Unattended preconditions and ceilings | F08, PR08 | V03, V08, V10, S01–S02, E05 | Answered negatively for universal safety; no universal thresholds |
| 9 | Stop, cancel, accountable intervention | F09, PR09 | I03, V03, V06, S01–S02 | Answered; application-specific kill/contain semantics require EC evidence |
| 10 | Retries, partial completion, lost updates, duplication, interruption recovery | F10, PR10 | S05–S06, E03–E04, V03 | Answered; irreversible external effects retain material residual risk |
| 11 | Least privilege, identity, provenance, sensitive data | F11, PR11 | I03, V08, S01, S09–S10 | Answered; concrete identity/secret system deferred |
| 12 | Requirement vs mechanism vs deferred | F12, PR12 | I01–I05 plus all mechanism sources | Answered; tooling selection and Workflow v1 design remain deferred |

## 6. Findings by subquestion

Each finding distinguishes facts, inference, proposed requirement, and gap.

### F01 — Bounded delegation contract

**VF.** The Charter requires explicit assignment, bounded agents, re-verification of repository state, no self-expansion, least privilege, and stopping on authority/scope/staleness conflicts. Accepted DR-001 input requires a scaled, self-sufficient packet for a fresh executor while rejecting a mandatory fixed schema (I03, I05).

**DC.** Current vendor guidance likewise describes explicit autonomy, tool, output, evidence, concurrency, retry, stopping, and side-effect boundaries for programmatic orchestration (V01, V05, V06).

**IN.** A delegation that names only a desired outcome is insufficient when the delegate can mutate state, use credentials, invoke subagents, or operate after the assigning context is unavailable.

**PR01.** A bounded delegation packet should identify: authority source and accountable owner; objective; exact authoritative input and candidate identities; allowed resources, tools, actions, and side effects; non-goals; dependency/configuration assumptions; expected output and evidence destination; validation obligations; concurrency/resource/time/retry ceilings; stop/cancel conditions; and escalation recipient. Fields may be combined or omitted proportionately only when their semantic information is genuinely unnecessary.

**UE.** No source establishes one universally sufficient serialization or schema.

### F02 — Identity pinning and freshness

**VF.** Git commit objects provide immutable content-linked identity while refs remain mutable (S04). Expected-old-object updates and HTTP strong validators can reject stale writes (S05, S06). Accepted DR-001 constraints require exact candidate identity for formal review and live re-reading at state-dependent transitions (I05).

**IN.** Repository SHA, dependency lock identity, instruction/policy version, model/tool version, and effective permission/configuration are distinct identities. Pinning one does not freeze the others. A fresh repository SHA cannot validate a stale approval policy; a model name cannot establish enabled tools or sandbox settings.

**PR02.** Before dispatch and at every state-dependent join, publish, review, acceptance, or resumed-execution transition, the controller should compare the live authoritative identities and EC against the delegation contract. Mismatch should invalidate cached conclusions and stop, rebase/replan, or seek renewed authorization according to the changed dimension.

**UE.** Retention of a content-addressed object and the trustworthiness of dependency or configuration attestations are separate from the identifier itself.

### F03 — Safe parallelization conditions

**DC.** Current OpenAI documentation recommends parallel focused subagents for concrete independent workstreams and cautions against ordered dependencies and shared mutable contention; Codex documentation characterizes read-heavy delegation as a safer starting point and write-heavy delegation as coordination-intensive (V02, V09).

**OB.** MapReduce obtains strong re-execution and duplicate-result properties from deterministic functions, partitioned work, coordinator-owned task state, and atomic output publication; nondeterministic work weakens equivalence (E03).

**IN.** Parallel work is safe only relative to explicit read/write sets, side effects, invariants, and join semantics. “Different prompts” do not establish independence.

**PR03.** Parallelize when one of these is true:

1. work is read-only and independent;
2. mutable outputs are isolated into disjoint namespaces and later joined by one accountable aggregator;
3. one writer owns each mutable authoritative state class while others submit proposals;
4. shared writes use enforceable version preconditions plus deterministic conflict handling.

Do not parallelize an ordered dependency, an ambiguous task, or unconstrained writes to the same authoritative state. Define a bounded concurrency ceiling from resource/risk context; the evidence supplies no universal number.

**UE.** Platform defaults are throughput settings, not proven safety ceilings.

### F04 — Isolation, ownership, aggregation, and join

**VF.** Accepted DR-001 input supports one authoritative owner per mutable state class and immutable candidate identity for review (I05). Git and HTTP specifications provide examples of atomic or conditional update mechanisms but do not choose an architecture (S05, S06).

**OB.** MapReduce makes the coordinator responsible for task state and output locations, ignores superseded duplicate completions, and publishes certain outputs atomically (E03).

**IN.** A join is a semantic gate, not merely “all workers returned.” It must know which outputs were required, which exact inputs produced them, whether failures or duplicates occurred, whether the baseline changed, and how conflicts were resolved.

**PR04.** Isolate workspaces, output namespaces, credentials, and side-effect capabilities. Assign one owner for aggregation and each mutable authority. A join should require: a complete result manifest; exact input/output identities; completed/failed/cancelled/waived state for every required branch; validation status; duplicate and conflict resolution; baseline/configuration recheck; and explicit handling of partial results. A missing required branch is a failed or explicitly waived join, not silent success.

**UE.** Central, hierarchical, and distributed aggregation remain alternatives; DR-003 does not select one.

### F05 — Handoffs, context loss, and staleness

**DC.** Agent handoffs can transfer control or keep a manager in control, and implementations can filter history or pass structured metadata (V05). Compaction is opaque and intended to preserve key state, but it is not a human-verifiable lossless representation (V04).

**OB.** Long-context experiments show positional retrieval degradation, while a newer structured-snapshot system reports benefits together with compression-induced errors (E01, E02).

**IN.** More context is not monotonically safer. Raw histories contain noise and stale decisions; summaries can omit constraints or transform uncertainty into apparent fact.

**PR05.** A loss-sensitive handoff should carry: delegation identity and authority; exact source/baseline/candidate/configuration pointers; objective and non-goals; completed actions and side effects; tool results and verification status; decisions with rationale and owner; assumptions and uncertainty; failures/retries/cancellation state; pending work and dependencies; secret-free evidence locations; and stop/escalation conditions. The receiver should re-read authoritative sources and validate critical identities before acting. Preserve exact machine-readable facts outside prose summaries where loss would be material.

**UE.** No compression or summary method is proven semantically complete across arbitrary tasks.

### F06 — Minimum observability and interruptibility

**DC.** Vendor tooling can expose model calls, tool calls, handoffs, guardrails, background status, cancellation, and stream sequence state (V03, V07). Standard trace context and OpenTelemetry semantics support cross-component correlation (S07, S08).

**VF.** NIST control families support event content, protected audit information, monitoring, incident handling, and recovery, while AI RMF emphasizes roles, documentation, monitoring, and safe failure (S01, S02).

**IN.** A trace ID without authoritative state, side-effect semantics, and protected evidence is diagnostic correlation, not a trustworthy audit or recovery record. Conversely, exhaustive raw logging can leak credentials and sensitive context.

**PR06.** Minimum reconstructable evidence should include: run/task/agent and parent-child identifiers; accountable owner; immutable input/candidate and relevant EC identities; state transitions and timestamps; tool and side-effect attempts, targets, bounded arguments, results, and idempotency/precondition identifiers; approvals/denials; progress or heartbeat; resource and budget use; errors, retries, backoff, and partial results; cancel request and acknowledgement; output identities; validation/review result; and final disposition. Define access, integrity, redaction, retention, and clock/correlation behavior. Store secrets by reference and log neither credentials nor unnecessary sensitive payloads.

**UE.** Concrete retention periods, log store, sampling policy, and tamper-evidence mechanism depend on later governance and tooling research.

### F07 — Corrections, material change, and review waves

**VF.** Accepted DR-001 input binds formal review to immutable candidate identity and keeps verification, independent review, and acceptance separate. Its source review is itself tied to exact bytes; material evidence change requires a new identity and review (I05, I06).

**VF.** SLSA verification compares artifact digest and provenance against trusted expectations; matching identity alone is insufficient (S10).

**IN.** “Material” is relational: a change is material when it could affect a relied-upon requirement, threat/control mapping, behavior, interface, proof, authorization assumption, provenance, or review conclusion. Line count alone is not a sound criterion.

**PR07.** Treat a correction as a new candidate. Record the prior identity, new identity, reason, affected requirements/interfaces/evidence, and impact analysis. Re-run the affected verification set plus checks needed to show unaffected boundaries still hold. Renew independent review whenever its target or a load-bearing assumption changed; carry forward prior review only for demonstrably unaffected scope. The author or executor may propose the correction and evidence but cannot manufacture independent re-review or acceptance.

**UE.** No universal numeric materiality threshold is supported.

### F08 — Preconditions and ceilings for unattended work

**DC.** Background and non-interactive modes exist and can expose polling, cancellation, approval/sandbox presets, and structured output (V03, V10). Security guidance separates capability boundaries from approval policy and warns that prompt injection and broader access increase risk (V08).

**OB.** Agent task success on a studied benchmark falls as task horizon grows; the authors explicitly limit translation to real-world capability (E05).

**IN.** Ability to continue without a user present is not evidence of authorization, containment, detectability, recoverability, or safe success. Duration by itself is not an adequate risk measure.

**PR08.** Unattended execution should be eligible only when all are evidenced:

- an accountable owner preauthorizes a bounded objective and side-effect envelope;
- required authority, policy, repository, dependency, and EC identities are fresh;
- the environment, credentials, network, outputs, and write targets are isolated and least-privileged;
- inputs are immutable or changes are detected before use;
- ambiguity and material missing dependencies are absent;
- effects are read-only, idempotent, transactionally isolated, or have tested reconciliation/compensation;
- time, cost, tokens, concurrency, recursion/delegation, storage, network, side-effect count, and retry ceilings are enforceable;
- progress, side effects, failures, and budgets are observable through durable checkpoints;
- cancel/contain behavior is tested and an accountable responder can intervene;
- uncertainty, policy conflict, ceiling breach, stale state, lost observability, or cancellation failure causes safe stop, not permission expansion.

Consequential external, destructive, privileged, security-sensitive, or shared-authority mutation remains ineligible absent later task-specific evidence and explicit authorization.

**UE.** No source establishes universal numeric ceilings or a general guarantee that consequential unattended agent work is safe. This gap blocks such a recommendation.

### F09 — Stop, cancellation, and accountable intervention

**VF.** The Charter requires stopping for authority conflict, stale or unverifiable state, unexpected content/resources, unsafe evidence handling, and scope expansion (I03). NIST sources support monitoring, incident response, recovery, and accountable roles (S01, S02).

**DC.** A platform cancellation request and repeat-cancel idempotency are documented (V03), but no cited source establishes that all downstream effects stop synchronously.

**IN.** Cancellation has at least three states: requested, acknowledged by the controller, and verified contained at every side-effect boundary. Treating request issuance as completion can leave workers, subprocesses, queued actions, or external operations active.

**PR09.** Stop and escalate on: authority/scope ambiguity or conflict; stale identity/EC; unapproved resource or privilege expansion; unexpected sensitive/untrusted content; uncertain side-effect outcome; budget/time/concurrency/retry breach; missing heartbeat or progress; repeated correlated failure; lost observability; failed or unacknowledged cancellation; unresolved aggregation conflict; or missing required evidence. After cancel: record the request, block new dispatch, obtain worker/tool acknowledgements, inspect side-effect targets, quarantine incomplete outputs, reconcile partial effects, and route irreducible uncertainty to the named accountable owner.

**UE.** Kill, revocation, queue purge, and external-system containment semantics must be verified for the chosen mechanism later.

### F10 — Retry, partial completion, duplication, and recovery

**VF.** RFC 9110 permits automatic retry where operation semantics are idempotent and cautions against retrying non-idempotent operations without knowledge that repetition is safe or detection that the first attempt was not applied. Strong preconditions can prevent stale overwrites (S06). Git expected-old-object updates provide a mechanism-specific compare-and-swap example (S05).

**OB.** MapReduce combines task-state tracking, reassignment, duplicate completion handling, and atomic output publication; deterministic work makes replay stronger, while nondeterministic work weakens equivalence (E03). Sagas show that compensation is a recovery alternative for long-lived partial work (E04).

**IN.** “Retry three times” is not a safety rule. The controller must classify the operation and reconcile uncertain prior outcomes before another attempt. Compensation is a new effect that can fail and may not restore external reality.

**PR10.** Use stable operation identifiers and deduplication; version/ETag preconditions for mutable state; durable checkpoints and partial-result manifests; atomic publish from isolated staging; deterministic replay where feasible; bounded retry with backoff/jitter; probe-and-reconcile before retrying uncertain non-idempotent effects; and domain-specific compensation only when its authority, ordering, verification, and failure path are defined. Do not retry on authorization/policy failure, stale baseline, schema incompatibility, deterministic invalid input, or repeated correlated failure. Preserve partial state for diagnosis while preventing it from becoming authoritative.

**UE.** Exact rollback cannot be assumed for messages, disclosures, financial actions, destructive operations, or other real-world side effects.

### F11 — Least privilege, identity, provenance, and sensitive data

**VF.** The Charter requires least access and excludes secrets/sensitive data from prompts, handoffs, and logs (I03). NIST provides general least-privilege and protected-audit controls (S01). OAuth BCP supports audience/resource/action-restricted credentials (S09). SLSA binds artifacts to provenance but requires signature, digest, builder, source, and parameter checks against a trust root and expected values; even high assurance does not remove trust in the builder platform (S10).

**DC.** Codex security guidance separates sandbox reach from approval policy and treats connectors/network as additional trust boundaries (V08).

**IN.** Authentication, authorization, approval, provenance, content identity, and review identity solve different problems. Shared ambient credentials collapse accountability and enlarge blast radius. Provenance that is collected but not checked against trusted expectations is weak evidence.

**PR11.** Scope each agent and tool to the minimum resource, action, environment, network destination, duration, and delegation depth. Prefer short-lived, audience/action-bound credentials and prohibit credential forwarding unless explicitly required. Keep secrets out of prompts, summaries, traces, artifacts, and command output; use references and redaction. Record executor/service identity, authority source, tool/model/version, EC, input/output identities, and side-effect target. Verify provenance against an independently controlled trust policy; do not infer approval or correctness from a digest, signature, or actor name alone.

**UE.** Credential issuer, attestation system, reviewer authentication, retention, and redaction implementation are deferred.

### F12 — Requirement, mechanism, and deferred design

**VF.** DR-003 authorizes tool-agnostic requirements and explicitly prohibits Workflow v1 design, tooling selection, orchestration trials, and normative adoption (I01). The Register leaves DR-005 tooling research after initial tool-agnostic Workflow v1 design (I02).

**IN.** Version preconditions, isolated workspaces, queues, workflow engines, tracing systems, signed attestations, and schema-validated checkpoints are candidate mechanisms that can instantiate some controls. None is identical to the requirement, and each has configuration and failure modes.

**PR12.** Carry forward requirements as outcome and evidence obligations. Defer concrete sequencing, state schemas, retry numbers, concurrency ceilings, risk thresholds, join topology, platform/provider selection, credential mechanism, log store, task tracker, and automation to separately authorized design and DR-005 work.

**UE.** Tool feasibility and effective configuration cannot be decided within DR-003.

## 7. Consolidated candidate requirements

These are proposed inputs to a later coordinator disposition. They are not adopted policy.

| ID | Proposed requirement | Strength | Qualification / residual |
|---|---|---|---|
| PR01 | Every nontrivial delegation carries a bounded, self-sufficient contract scaled to context and risk | High | No fixed schema; trivial work may combine fields |
| PR02 | Pin and reverify every identity or EC dimension on which a state-dependent action relies | High | Identity does not itself prove authorization or trust |
| PR03 | Parallelize only independent or isolated work with explicit ownership/conflict control and bounded concurrency | High | No universal safe concurrency value |
| PR04 | Use isolated output domains, one owner per mutable authority, a complete result manifest, and an explicit join | High | Aggregation topology deferred |
| PR05 | Treat handoffs/summaries as non-authoritative navigation and rehydrate from exact sources | High | No general lossless-summary mechanism |
| PR06 | Make run state, authority, side effects, resources, failure/retry/cancel, outputs, and validation reconstructable with protected/redacted evidence | High | Retention and instrumentation deferred |
| PR07 | A material correction creates a new candidate and renews affected verification and applicable review | High | Materiality is contextual, not line-count based |
| PR08 | Permit unattended operation only when all bounded-authority, isolation, ceiling, observability, recovery, cancellation, and accountability preconditions are evidenced | Medium-high | No universal threshold; consequential classes remain blocked absent task-specific evidence |
| PR09 | Use explicit stop triggers and treat cancellation as request → acknowledgement → verified containment | High | Mechanism-specific containment must be tested |
| PR10 | Classify operation semantics before retry; use deduplication, preconditions, checkpoints, atomic publish, reconciliation, or compensation as applicable | High | Irreversible effects retain residual risk |
| PR11 | Separate authentication, authorization, approval, identity, and provenance; enforce per-task least privilege and secret-safe evidence | High | Concrete identity/credential system deferred |
| PR12 | Preserve tool-agnostic requirements and defer mechanisms and Workflow v1 sequencing to their authorized gates | High, internally authoritative boundary | Does not validate any future design |

## 8. Hazard-to-control evidence matrix

| Hazard | Preconditions that make control plausible | Detectable signal | Bounded response | Evidence of response/effect | Residual risk |
|---|---|---|---|---|---|
| Authority or scope drift | Durable contract and owner exist | Requested action/resource not in contract; conflicting instruction | Stop dispatch; preserve state; ask named owner | Contract diff, stop event, decision record | Ambiguous natural language; owner unavailable |
| Stale repository/dependency/configuration | Identities and comparison source are available | Live identity differs from pinned value | Stop or replan/rebase under renewed authority | Before/after identities, affected-analysis record | Hidden mutable services; object retention loss |
| Shared-state race / lost update | State supports exclusive ownership or version preconditions | Lock conflict, old-version mismatch, overlapping write set | Reject stale write; isolate/recompute; accountable conflict resolution | Precondition failure, resolved candidate identity | Cross-system non-atomic effects; concurrent readers |
| Duplicate execution | Stable operation ID and dedup store exist | Repeated ID/completion; ambiguous response | Return prior result or suppress duplicate; reconcile target | Dedup decision, target-state inspection | Different IDs for semantically same action |
| Partial completion | Stages/checkpoints and side-effect manifest exist | Some required stages complete, others absent/failed | Prevent publish; quarantine; resume, compensate, or escalate | Partial manifest, reconciliation and final status | Undetected external effects; compensation failure |
| Nondeterministic replay | Sources of nondeterminism are known/recorded | Same input yields divergent output or evidence | Do not treat replay as equivalence; compare/verify anew | Input/config/random/time records, diff, verifier result | Hidden nondeterminism; model/service changes |
| Aggregation omission, duplicate, or conflict | Required-branch manifest and one aggregation owner | Missing/duplicate branch; incompatible claims/outputs | Fail/waive explicitly; deduplicate; resolve with sources | Join manifest, waiver/decision, combined verification | Aggregator error or compromise |
| Handoff compression or staleness | Exact pointers and critical structured state retained | Pointer mismatch; missing constraint; summary conflicts with source | Rehydrate; invalidate summary-derived action | Freshness check, source comparison, corrected handoff | Semantic omissions not covered by checks |
| Unobservable stall | Heartbeat/progress expectation and monitoring path exist | Missed heartbeat, unchanged checkpoint, resource activity without progress | Pause new work; cancel/inspect; escalate | Monitor event, cancel acknowledgement, diagnosis | Monitoring outage; false positives |
| Cancellation failure | Known workers/queues/tools and revocation path | No acknowledgement; new side effect after cancel | Block dispatch, revoke capability, contain and reconcile | Per-boundary acknowledgement and target inspection | External action already irreversible |
| Runaway resource or delegation growth | Enforceable time/cost/token/concurrency/depth/storage/network ceilings | Near/breached ceiling, recursive spawn, expanding target set | Stop/cancel; preserve checkpoint; require renewed authorization | Meter/limit event and final resource statement | Incomplete metering; delayed billing/events |
| Privilege escalation / credential spread | Per-task identities and scoped credentials | New permission, audience, destination, credential copy | Deny/revoke; stop; rotate if exposed; investigate | Policy denial, credential audit, rotation record | Provider-side privilege or credential leakage |
| Prompt injection / untrusted content | Trust labels, tool boundary, output validation, least privilege | Content requests authority change, secret access, or out-of-scope action | Treat as data; deny action; isolate and escalate | Guardrail/tool decision and source provenance | Novel injection; trusted source compromise |
| Material correction bypasses review | Candidate identity and reviewed scope recorded | Candidate/input/assumption digest changes | Create new candidate; impact analysis; rerun affected checks/review | Identity link, affected-set analysis, new verdict | Incorrect materiality classification |
| Producer/reviewer conflict | Reviewer identity/relationship recorded | Same actor or dependency where independence is claimed | Relabel as self-check or obtain conflict-free review | Reviewer provenance and conflict declaration | Hidden organizational conflicts |
| Sensitive-data leakage through logs/handoffs | Data classification, redaction, least-access storage exist | Secret pattern, unauthorized audience, verbose payload capture | Halt propagation; restrict/delete through authorized incident path; rotate credentials | Redaction/access/incident record | Detection gaps; disclosure may be irreversible |
| Evidence tampering or provenance mismatch | Protected evidence and trusted expectations exist | Digest/signature/source/builder/parameter mismatch | Reject evidence/output; quarantine; investigate | Verification result against trust root/expectations | Trusted builder/platform compromise |

## 9. Alternatives and tradeoffs — no selection

| Decision area | Alternative A | Alternative B | Evidence-backed tradeoff |
|---|---|---|---|
| Work scheduling | Serial execution | Bounded parallel execution | Serial reduces races and join complexity but increases latency; parallelism can reduce latency for independent work but increases resource, coordination, synthesis, and failure surfaces (V02, V09, E03) |
| Mutable-state control | Exclusive single writer | Optimistic version preconditions | Single writer simplifies reasoning but can bottleneck; preconditions improve concurrency but require conflict resolution and do not make cross-system effects atomic (S05, S06) |
| Aggregation | One central aggregator | Hierarchical aggregation | Central ownership is simpler but creates a bottleneck/single failure point; hierarchy scales but adds handoffs and omission/duplication risk (V05, E03) |
| Failure recovery | Retry idempotent operation | Reconcile/compensate/manual repair | Retry is efficient only with safe semantics; compensation handles some partial work but is itself fallible; manual repair is slower but necessary for irreducible ambiguity (S06, E04) |
| Handoff representation | Full/raw history | Structured state plus exact source pointers | Raw history retains detail but increases noise/sensitive-data exposure; structure improves focus but can omit or distort facts, so exact pointers and rehydration remain necessary (V04–V05, E01–E02) |
| Observability | Full-fidelity trace | Minimum protected/redacted evidence | Full capture improves diagnosis but costs more and can expose secrets; minimum capture reduces burden but may impair reconstruction. Sampling must not remove evidence required for a consequential transition (V07, S07–S08) |
| Supervision | Synchronous supervised run | Bounded unattended run | Supervision improves intervention but consumes human time; unattended execution improves throughput only when eligibility controls are enforceable and residual consequence is acceptable (V03, V10, E05) |
| Delegation model | One agent with tools | Multiple focused agents | One agent avoids inter-agent joins/context transfers; multiple agents can reduce context interference and latency for independent work but add tokens, traces, permissions, and synthesis risk (V02, V05, V09) |
| Provenance | Content digest only | Signed, expectation-checked provenance | Digest is simple and binds bytes; richer provenance can bind builder/source/parameters but requires roots of trust and still does not prove correctness or trusted-platform integrity (S04, S10) |

## 10. Unattended eligibility decision frame

This section is a research result, not a Workflow v1 gate design.

### Necessary evidence categories

An unattended proposal lacks sufficient evidence if any of these categories is absent:

1. **Authority:** accountable owner, bounded outcome, allowed side effects, and escalation authority.
2. **Freshness:** pinned and revalidated policy, source, dependency, candidate, model/tool, and EC identities.
3. **Containment:** isolated workspace/output, least-privileged identity, bounded network and write targets, no ambient credentials.
4. **Semantic safety:** read-only, idempotent, conditional/transactional, or explicitly reconcilable/compensatable effects.
5. **Ceilings:** enforceable time, resource, cost, token, concurrency, recursion, retry, and side-effect bounds.
6. **Observability:** protected/redacted checkpoints, progress, side effects, failures, and budget data.
7. **Interruptibility:** tested stop/cancel/revoke/contain path and acknowledgement evidence.
8. **Recovery:** deduplication, version checks, partial-result manifest, atomic publication or quarantine, and repair/compensation ownership.
9. **Accountability:** named responder and defined cases requiring human/coordinator intervention.

### Evidence gap and conservative boundary

The sources demonstrate components and hazards, not a general safety theorem. There is no supported universal duration, model capability score, change size, concurrency count, retry count, or reversibility label that converts consequential autonomous mutation into a safe unattended task. Empirical task-horizon results are harness- and distribution-dependent (E05), and documented background execution is merely capability (V03, V10).

Therefore the evidence supports a conservative proposed boundary: unattended work may be considered only for explicitly bounded work whose maximum credible consequence is acceptable under preauthorized controls. Privileged, destructive, externally communicative, security-sensitive, financial, production, secret-bearing, or shared-authority mutations require task-specific evidence and explicit accountable authorization; DR-003 does not recommend them as generally eligible.

## 11. Contradictions, tensions, and negative evidence

### Contradiction assessment

No credible source directly contradicts an accepted repository premise or accepted DR-001 disposition within the scope examined. A coordinator contradiction gate is therefore **not required** by this packet.

The following are material tensions or qualifications, not resolved contradictions:

| ID | Evidence on one side | Evidence on the other side | Classification and consequence |
|---|---|---|---|
| T01 | Vendor documentation reports benefits from focused parallel subagents | The same vendor documentation cautions against ordered dependencies and shared mutable contention; systems evidence requires determinism/isolation for strong replay | Scope/configuration qualification: parallelism is conditional, not generally safe |
| T02 | Background/non-interactive execution and cancellation are documented capabilities | No EC was inspected and no source proves arbitrary unattended mutation safe | Capability/configuration gap: no permission or safety conclusion follows |
| T03 | Compaction is intended to preserve key prior state | Empirical work shows long-context retrieval and compression can lose or distort information | Assurance limitation: use summaries for navigation; retain exact pointers and validate loss-sensitive facts |
| T04 | Content-addressed objects and provenance strengthen identity | Git and SLSA do not make content identity equivalent to authorization, correctness, acceptance, or trusted builder integrity | Semantic qualification: verify expectations and keep lifecycle states separate |
| T05 | Retry/re-execution can recover transient failures | Non-idempotent, nondeterministic, and real-world effects can duplicate or diverge; compensation can fail | Conditional control: classify semantics and reconcile before retry |

### Negative evidence

- No source supports unrestricted or recursively self-expanding delegation.
- No source supports parallel writes to the same mutable authoritative state without ownership, isolation, or conflict control.
- No source supports a universal safe concurrency, duration, task-size, model-score, or retry threshold.
- No source establishes a lossless natural-language handoff or compaction method for arbitrary tasks.
- No source establishes that issuing a cancellation request synchronously stops every downstream effect.
- No source establishes exact rollback for arbitrary external side effects.
- No source establishes that a digest, signature, trace, passing check, or successful tool result proves authorization, correctness, independent review, or acceptance.
- No evidence of this repository's actual orchestration platform, model entitlement, network policy, sandbox mode, approval policy, credential scopes, monitoring, cancellation behavior, or log retention was gathered; relying on any of them would violate the capability/EC distinction.

## 12. Unresolved evidence and deferrals

| ID | Unresolved item | Effect now | Potential resolving evidence / later owner |
|---|---|---|---|
| G01 | No universal risk or unattended-eligibility threshold | Blocks numeric or categorical universal rule | Later governance/design work with domain risk ownership and empirical validation |
| G02 | No universal concurrency, recursion, duration, cost, token, retry, or heartbeat ceiling | Requires task/environment-specific bounded values | Workflow design plus tool-specific DR-005 evidence |
| G03 | No verified EC for any proposed platform | Blocks reliance on vendor DC | Read-only EC audit in a later authorized task |
| G04 | No lossless handoff/compaction guarantee | Requires exact pointers, structured critical state, and rehydration | Tool-specific evaluations and task-domain validation |
| G05 | No general cancellation-containment guarantee | Requires per-boundary acknowledgement and inspection | Mechanism-specific cancellation/revocation tests under safe authorization |
| G06 | No universal rollback for external side effects | Keeps some work ineligible unattended | Domain-specific transaction/compensation design and drills |
| G07 | Concrete authoritative state store, synchronization and retention policy unresolved in DR-001 | Requirements remain semantic | Workflow v1 design and later tooling research after disposition |
| G08 | Concrete credential issuer, actor identity, reviewer-independence proof, and provenance mechanism unresolved | Prevents implementation claim | Governance/identity design and DR-005 |
| G09 | DR-002 outputs were not consumed because DR-003 does not require premature cross-research synthesis | Interface consistency cannot yet be assessed | Later coordinator disposition and separately gated Workflow v1 design join |
| G10 | NIST AI RMF 1.0 is under revision and SSDF v1.2 is draft | Future freeze/review should reverify versions | Independent source review/freeze freshness check |

Deferred by contract:

- Workflow v1 states, sequences, schemas, and materialization.
- DR-002/DR-003 synthesis and coordinator adoption.
- Provider, model, tool, App, MCP server, skill, hook, runner, scheduler, queue, workflow engine, worktree/container, tracker, log store, or attestation selection.
- Numerical risk scoring or automatic eligibility thresholds.
- Unsafe, privileged, destructive, production, or unattended experiments.

## 13. Recommendation set for later disposition

The proposed recommendations are exactly PR01–PR12 in Sections 6 and 7. The later coordinator may accept, reject, narrow, or defer them. Evidence strength is high for semantic separation, identity freshness, conflict-controlled parallelism, explicit joins, source-rehydrated handoffs, material-change review renewal, operation-aware retries, least privilege, and the requirement/mechanism boundary. Evidence is medium-high for the unattended eligibility frame because the sources support its control components but do not establish universal sufficiency or thresholds.

No recommendation selects a mechanism. Examples such as Git compare-and-swap, HTTP validators, trace context, signed provenance, queues, isolated workspaces, or compensation are evidence about possible control properties and tradeoffs only.

## 14. Scope boundary against Workflow v1 and DR-005

This packet supplies candidate outcomes and evidence obligations. It intentionally does not say:

- what the Workflow v1 state machine or step order is;
- which fields constitute a normative task schema;
- when a specific project must spawn or join agents;
- which product implements authoritative state, isolation, cancellation, tracing, secrets, or provenance;
- what numeric thresholds control risk, concurrency, retry, time, or resource use;
- whether any vendor mechanism is available or enabled in the eventual environment.

Those decisions require a separately authorized design after DR-002 and DR-003 disposition, followed by the deferred tooling/configuration evaluation described for DR-005. This separation preserves the repository's evidence/adoption boundary.

## 15. Freshness, limitations, and stop statement

### Freshness

After the last substantive research edit, the connected GitHub app reverified branch `main` at `79f5541113e7dfeedfde6f36f371031f3f3330fa` on 2026-09-03. GitHub reports the commit time as `2026-09-03T12:37:32Z`. This is working verification evidence, not publication metadata. The expected and final live SHAs match; no repository-dependent finding was invalidated.

External sources with unstable content were accessed on 2026-09-03. OpenAI documentation is continuously updated and must be reverified at a later freeze. NIST SP 800-53 Release 5.2.0 was the current final catalog release found; NIST AI RMF 1.0 was final but under revision, and SSDF v1.2 was draft while v1.1 remained final.

### Limitations

- This is desk research, not a controlled orchestration or recovery experiment.
- Vendor documentation establishes intended behavior and interfaces, not actual EC, completeness, reliability, or safety.
- Distributed-systems evidence supplies useful control properties but does not by itself validate agentic development workflows.
- Empirical model findings are benchmark-, model-, date-, and harness-dependent.
- Broad standards were mapped qualitatively; no compliance claim or control baseline is asserted.
- No secret, credential, production environment, repository mutation, or unattended run was inspected or exercised.

### Evidence-production stop

All twelve contracted subquestions have supported findings or explicit gaps; the claim-level source register, coverage matrix, hazard-control mapping, alternatives, residual risks, negative evidence, unattended gaps, and deferrals are present. Facts, documented capability, observed behavior, inference, proposed requirements, EC, and unresolved evidence are separated. No substantive research edit is planned after final live-state re-verification.

Stop at this boundary. Do not compute an exact-byte review identity, populate publication-only metadata, freeze, source-review, adopt, make coordinator disposition, materialize Workflow v1, select tooling, modify GitHub, or run unattended/privileged experiments without a later explicit gate.

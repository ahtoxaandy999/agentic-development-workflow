---
id: DR-005
artifact_status: draft
authority: evidence
research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: 2026-09-04
owner: agentic-development-research
question: >-
  Given the accepted initial tool-agnostic Workflow v1 design, which currently
  available tools and mechanisms, individually and as a minimal coherent stack,
  best realize its required authority, state, identity, evidence, review,
  parallelism, rehydration, stopping, recovery, and unattended-execution semantics?
scope: >-
  Execute ADW-DR-005-GATE-001: seven capability areas, seven mechanism classes,
  eighteen research questions, comparative tooling evidence, minimum sufficient
  stack, enforcement gaps, and recommendations for later independent source
  review and coordinator disposition. No implementation or adoption.
repository_state:
  repository: ahtoxaandy999/agentic-development-workflow
  research_basis_main: 7adc4d9866ff7d6fda8eeb63087ade300f4d7977
  accepted_design_subject: 2b9532682ae77bf5037f1b2fa45b720e5865d0ad
  accepted_design_blob: afed983e7632caf3169dcbac7a80f8da8226d86d
  gate_blob: 1c501a3fb4797ef1cdbe6a3427dcdae090bbaf14
  observation_scope: publication-time evidence snapshot; current state belongs to its authoritative repository owners
supersedes: null
---

# ADW-DR-005 — Current tooling evaluation and selection research

Task: ADW-DR-005-RESEARCH-001. Intended later repository destination: `docs/research/ADW-DR-005.md`. This local report has no normative effect. Decision consumer: fresh Command Center coordinator, after independent source review of the frozen report. Review consumer: fresh conflict-free source reviewer. No recommendation below is an adopted selection, execution authorization, or change to Workflow v1.

## 1. Executive answer

**RECOMMENDATION — SELECT NOW candidate:** use GitHub plus versioned repository artifacts as the primary durable control plane, full Git commit identities for subjects, separate producer-verification/review/disposition evidence, and human-supervised bounded tasks in fresh contexts. Use existing GitHub-connected reads, native repository search, current official documentation, and the existing constrained Codex/Work execution surface. Keep the Research Register as the sole owner of research queue, dependencies, decision pointers, and current repository research gate. For later product-task dogfooding, prefer one designated repository task-control record, with a single execution-state recorder, over introducing a tracker database. This is a representation recommendation; no task schema is created here. [R03](#r03) [R04](#r04) [R05](#r05) [R06](#r06)

**INFERENCE:** this is sufficient for auditable, supervised, serialized evidence work and separately authorized bounded persistence, with procedural enforcement limits. It is not a technically enforced implementation of every Workflow v1 transition. Git identity helps detect drift; it does not prohibit unauthorized writes. Chat, PR, Issue, runner, and agent statuses cannot replace the accepted orthogonal state planes. Missing controls deny the affected mode or transition. The repository's present protection restriction rules out routine agent writes and parallel/automated/AFK writes; research cannot waive it. [R04](#r04) [R06](#r06) [R09](#r09) [G01](#g01)

**RECOMMENDATION — CONDITIONALLY SELECT:** protected integration through an appropriate GitHub plan and verified configuration; one writer per isolated worktree for later authorized parallelism; Actions for repeated deterministic verification; Playwright for actual browser acceptance needs; Sentry or portable telemetry for real runtime needs. Semantic navigation and documentation MCPs are conditional on measured advantage over existing search, IDE intelligence, and direct official docs. Each condition, owner, and verification obligation is recorded in §18.

**RECOMMENDATION — DEFER:** general orchestration, Symphony deployment, LangGraph/Temporal/OpenHands adoption, custom Codex clients, background goals/schedules, task runners, and autonomous joins until demonstrated pain justifies their additional state and operations. **REJECT:** duplicated current truth, memory as authority, treating a stopped process as containment, skipped checks as required successful verification, and automatic merge/Issue closure as workflow completion.

**RESEARCH GAP:** effective cross-surface permission enforcement, exclusive writer fencing, comprehensive cancellation/containment, exact integration publication, independent reviewer identity, and retention guarantees have not been validated in the target environment. No benchmark or operational conformance trial was conducted. AFK remains ineligible and unauthorized; documented controls are necessary inputs to a later assessment, never sufficient authority.

## 2. Accepted Workflow v1 requirements translated to mechanism needs

**REPOSITORY FACT — exact authority verification.** The connected GitHub app was explicitly invoked before external research. The following are publication-time observations, not new owners of mutable Register state. The gate's older pre-persistence main/Register values are explicitly historical; the current Register records the gate's persistence and execution readiness. No competing current basis was found in the accessible authority files, complete tree, refs, all-state PRs, or all-state Issues. [R01](#r01)–[R09](#r09)

| Item | Verified research basis |
|---|---|
| Initial live main | `7adc4d9866ff7d6fda8eeb63087ade300f4d7977` |
| Main tree | `d0f85826b29966e02b4b61c87b873aeb465785f0` |
| Final live main and freshness | `7adc4d9866ff7d6fda8eeb63087ade300f4d7977`; final branch/commit reads followed by all eight exact-basis authority rereads completed 2026-09-04 06:15:44 UTC |
| Gate path / blob / decision | `docs/research/ADW-DR-005-GATE-001.md` / `1c501a3fb4797ef1cdbe6a3427dcdae090bbaf14` / `authorize-dr-005-research` |
| Register path / blob | `docs/research/research-register.md` / `1be4b5a46570be71f2354e8d2e379037270ac77b` |
| Register observations | Current gate `DR-005 research execution`; DR-005 dependency `satisfied`, research `planned`, decision `deferred` |
| Accepted design subject / path | `2b9532682ae77bf5037f1b2fa45b720e5865d0ad` / `docs/design/ADW-WF1-DESIGN-001.md` |
| Design blob at subject and main | `afed983e7632caf3169dcbac7a80f8da8226d86d` |
| Accepted subject parent | `a19e700e93157b8b25eaab4f14c7c44fc3ea3f6e` |
| Disposition | `docs/design/ADW-WF1-DESIGN-DISPOSITION-001.md`, blob `35d3a8ba5c3901e90d070b000659541b1ef4975c`; `accept-initial-tool-agnostic-workflow-v1-design` |
| Controlling review | `docs/design/ADW-WF1-DESIGN-REVIEW-004.md`, blob `3cdb92769bb955c8782dfa504843fd32a4736168`; `accept-candidate-for-design-disposition`, zero blocker/major/minor findings |
| Review binding | Exact subject, parent, path, blob; recorded 109600 bytes and SHA-256 `f8ddb3626868289e44251088a2ddad291ce762dbb58ec824d70c5de5a7994411` |
| Workflow v1 | Accepted initial design; normative adoption absent; remains unadopted |
| Protection | Register records unavailable under current private-repository plan; live main `protected: false`; this is not an account billing audit |
| Competing state check | Complete tree: 23 entries; only main ref; all-state PR collection empty; only closed bootstrap Issue #1, which does not adopt Workflow v1 |
| Material basis change | None. Initial/final main and all expected authority blobs match; no non-material main movement or competing accessible current state detected. |

The review digest above is a verified field in the retrieved review, not a fresh independent hash of the design bytes. Acceptance of the design subject does not adopt Workflow v1 or tooling. Bootstrap Context Baseline v0 remains separately accepted at `13b05e075ec04aa91494cd18f7d29f7249028cb5`. [R04](#r04) [R07](#r07) [R08](#r08)

**REPOSITORY FACT — semantic baseline.** The accepted proposal's DD-001–DD-014 and sections “Lifecycle and semantic state model,” “Authoritative-state ownership,” and “Conformance scenarios” require the following mechanisms. References below identify exact design sections and full-SHA source [R06](#r06), rather than deriving requirements from products.

| Accepted obligation | Mechanism need; semantic boundary |
|---|---|
| DD-001–003: independent planes, applicability, ownership | Distinct task, work, verification, review, disposition, normativity, baseline, join, cancellation and recovery values. One authoritative writer per mutable field/domain. A gate records subject, rule, owner, freshness, evidence and applicability; legitimate N/A differs from passed and from missing. |
| DD-004–007: readiness, identity, decomposition, delegation | Bounded task contract; exact inputs/configuration; criteria, permissions, budgets, dependencies, stop/escalation rules and output requirements. Separate ready from authorized. Delegation cannot recursively expand authority. |
| DD-008–009: parallelism, correction | Declared required/optional slices, ownership and dependency DAG; exact integration subject; current integrated verification; changed content gets a new identity and impact-based evidence/review reassessment. |
| DD-010–011: durability, interruptions | Durable reliance evidence and pointer-only handoffs. Cancellation request, acknowledgement, containment, residual effects, recovery, intervention and terminal accounting are distinct. |
| DD-012–014: proportionality, AFK, later mechanisms | Contextual justified ceremony rather than universal numerical thresholds. AFK denied without verified necessary controls and separate authority. Representation/tool selection remains a later decision. |

**INFERENCE — enforcement split.** Human judgment is appropriate for scope, readiness ambiguity, contextual applicability, independence, impact, risk acceptance, and disposition. Technical boundaries are needed wherever a mode depends on preventing effects despite model/human mistakes: credentials, filesystem/network isolation, exclusive mutation, protected integration, bounded resources, and interruption of every affected execution domain. Exact-ID checks, dependency checks, retention checks and transition validation can later be mechanical; their authoritative meaning still comes from an adopted rule and owner. Procedural controls can support bounded supervised work; they cannot certify modes whose accepted prerequisites require effective enforcement.

## 3. Current capability landscape

**Method and evidence labels.** Deep Research was applied as a substantial source-driven workflow: exact authority rehydration; tool-neutral requirement mapping; current first-party discovery; two bounded read-only research lanes for Git controls and external tools; targeted contradiction/gap follow-up; primary-source spot-checks by the report producer; stack synthesis; publication freshness and coverage checks. This was evidence production, not an execution experiment. Searches actively considered alternatives to the named examples. No installation, benchmark, repository mutation, or independent review of this report occurred.

Every load-bearing assertion is classified by its paragraph/table context: **REPOSITORY FACT** for connected GitHub observations; **DOCUMENTED FACT** for what primary documentation says; **EMPIRICAL OBSERVATION** for safely observed behavior; **INFERENCE** for deductions; **RECOMMENDATION** for proposed choices; **RESEARCH GAP** for unresolved evidence. Candidate assessments and gap consequences are recommendations/inferences unless specifically marked documented. There is no empirical proof here of production enforcement, performance superiority, or complete conformance. A successful connected read demonstrates that read in this session only.

All external evidence was accessed on **2026-09-04**. Rolling documentation often has no explicit lifecycle label: this report calls that **documented, lifecycle unspecified**, not GA. Release `prerelease=false` establishes release metadata, not an independently certified maturity level. Exact repository pins in §19 are evidence snapshots, not deployment selections; HEAD capabilities are not presumed present in a named release.

| Class | DOCUMENTED FACT — relevant current landscape | Consequence / evidence |
|---|---|---|
| A — OpenAI coordination/research | Projects supply shared context; Work supplies local/cloud task surfaces where eligible; Deep Research can use selected web/app sources and produce cited reports; GitHub-connected reads and eligible event-triggered Work tasks reduce copying. | Useful UX and retrieval, not durable transition enforcement. [O01](#o01)–[O05](#o05) |
| B — Codex | Instructions, skills, worktrees, subagents, permission profiles, hooks, noninteractive execution, SDK/app-server, browser and background work are documented. Permissions are beta; some process APIs are experimental; `--full-auto` and `codex mcp-server` are deprecated. | Feature existence does not establish complete containment or ADW review. Current CLI release metadata: 0.153.2. [O06](#o06)–[O24](#o24) [O28](#o28) |
| C — Git/GitHub | Immutable object IDs, PR/check/review records, plan-dependent protection, Actions concurrency and artifacts offer complementary controls. Current Actions docs include `queue: max` up to 100 pending runs. | Stronger than old “one pending only” descriptions, still repository/group-scoped. No current target protection. [G01](#g01)–[G18](#g18) |
| D — Navigation/docs | Serena offers language-aware navigation; existing IDE MCP and ast-grep are narrower alternatives. Context7 now offers CLI + Skills as well as MCP; publisher-owned docs retrieval is another alternative. | No external integration is mandatory for this documentation-focused bootstrap. [E301](#e301)–[E308](#e308) [O22](#o22) |
| E — Browser | Playwright Test provides repeatable reports; current first-party guidance favors CLI + Skills for coding agents, with MCP suited to persistent exploration. Native OpenAI browser is another available surface. | Conditional on product verification needs; exploration and acceptance tests have different evidence value. [E309](#e309)–[E311](#e311) [O23](#o23) |
| F — Incidents | Sentry/MCP and OpenTelemetry can expose runtime evidence. Neither replaces candidate verification, ownership or disposition. | Introduce only for a real runtime requirement. Transport/scopes/maturity vary. [E312](#e312)–[E315](#e315) |
| G — Harnesses | Recipes, Actions, native SDKs, graph checkpointing, Temporal, OpenHands SDK and Symphony cover different portions of execution. Current OpenHands root repository describes Agent Canvas beta; Symphony remains engineering preview. | Compare semantic gaps and operational cost, not generic autonomy claims. [G19](#g19) [G20](#g20) [E316](#e316)–[E326](#e326) [O27](#o27) [O29](#o29) |

## 4. Candidate mechanism inventory

**RECOMMENDATION/INFERENCE — consistent evaluation method.** Every candidate below inherits one complete profile, with row-specific overrides and later section details. Thus all twenty gate criteria are assessed without a fifty-row, twenty-column table. Profiles are qualitative assessments, not documented guarantees. A criterion marked N/A means that function is outside the candidate's proposed scope, not satisfied. The profiles never confer authority. Costs describe relative surface/plan dependencies; no procurement quote or installed-environment audit is claimed.

The twenty criteria are: **C1** requirement coverage; **C2** authority model; **C3** source-of-truth compatibility; **C4** identity/provenance; **C5** deterministic/fail-closed behavior; **C6** fresh-context support; **C7** parallel safety; **C8** cancellation/recovery; **C9** observability; **C10** permissions/credentials; **C11** maturity; **C12** API/automation; **C13** portability; **C14** operational complexity; **C15** maintenance; **C16** coupling; **C17** failure modes; **C18** cost/plan; **C19** reversibility; **C20** value versus simpler mechanism.

| Profile | C1–C10 | C11–C20 |
|---|---|---|
| P1 — versioned evidence/owner records | C1 state/identity/evidence; C2 designated human/domain owner; C3 strong if sole owner; C4 full SHA + exact path/digest; C5 deterministic identity, procedural transitions; C6 strong via rereads; C7 no exclusive writer; C8 can represent all states, cannot stop effects; C9 durable history if retained; C10 repository access. | C11 mature Git, proposed ADW representation; C12 Git/GitHub reads, writes only under later authority; C13 portable text/Git; C14 low; C15 low/manual discipline; C16 GitHub storage/access coupling, portable content; C17 stale pointers/unauthorized overwrite; C18 existing repository, plan limits; C19 high with preserved history; C20 baseline, no smaller adequate durable record. |
| P2 — coordinator/research UX | C1 framing/context/retrieval; C2 operator judgment; C3 cache only; C4 pointers need exact-source resolution; C5 model decisions nondeterministic, fail-closed procedural; C6 new contexts supported but rereads required; C7 read-only/proposal delegation only; C8 user stop not containment; C9 transcript/report must be exported; C10 account/app entitlements. | C11 documented, lifecycle row-specific; C12 surface-specific UI/API; C13 reports portable, sessions less so; C14 low when already present; C15 source freshness and access upkeep; C16 OpenAI coupling; C17 memory drift/missed sources; C18 eligible plan/region/limits; C19 easy exit after export; C20 reduces manual ferrying without another tracker. |
| P3 — bounded executor | C1 implementation/verification/evidence; C2 bounded contract plus external controls; C3 subordinate execution data only; C4 record run/tool/model/config/input IDs; C5 model nondeterminism with partial technical boundaries; C6 fresh task possible; C7 isolation and owner policy still required; C8 interrupt API partial, domain recovery absent; C9 events/output available; C10 filesystem/network/tool credentials. | C11 documented, feature-specific maturity; C12 CLI/SDK/UI; C13 medium, output portable; C14 medium; C15 model/runtime/config upgrades; C16 runtime vendor coupling; C17 excess permissions/stale context/lingering effects; C18 existing entitlement or metered usage; C19 stop/export/revoke after containment; C20 existing runtime preferable to another harness. |
| P4 — GitHub integration/verification control | C1 review routing/checks/publication; C2 repository owner sets policy, actor/app emits evidence; C3 subordinate to named ADW owners; C4 commit/run/review IDs strong when explicit; C5 mechanical configured checks, semantic gaps; C6 APIs permit reread; C7 scoped serialization only; C8 cancellation partial, no rollback; C9 accessible records subject to retention; C10 repository/app/token permissions. | C11 documented, lifecycle unspecified unless stated; C12 REST/Actions/UI; C13 Git evidence portable, workflow config less; C14 medium; C15 rules/workflows/dependency upkeep; C16 GitHub coupling; C17 bypass/skips/wrong subject/expiry; C18 plan/quota dependent; C19 configurable reversal, history export needed; C20 worthwhile only for a demonstrated enforcement/repeatability need. |
| P5 — retrieval/navigation | C1 locate source/code; C2 no decision authority; C3 derived results only; C4 exact-source/version citations required; C5 query success not completeness, fail closed on missing authority; C6 good targeted context; C7 read queries safe if source fixed, mutation tools excluded; C8 stop request only, external mutation N/A in read scope; C9 query/source evidence; C10 local reads or remote query credentials. | C11 row-specific; C12 CLI/MCP/IDE/web; C13 language/corpus-dependent; C14 low native, medium service; C15 index/tool/version drift; C16 low native, service/backend coupling remote; C17 missed files/stale index/wrong version; C18 native low, service/license limits; C19 removable with citations retained; C20 must improve on native search/direct docs. |
| P6 — browser verification | C1 UI evidence/tests; C2 test owner sets criteria; C3 results only; C4 test/build/browser/config/run identity required; C5 repeatable tests possible, exploratory output not proof; C6 saved test/evidence helps; C7 profiles/accounts/backend data need separation; C8 browser stop not server containment; C9 reports/traces/screenshots; C10 browser credentials/network/application effects. | C11 versioned OSS or surface-specific; C12 test CLI/CLI/MCP/UI; C13 browser-product scope; C14 medium; C15 browser/test/flakiness upkeep; C16 Playwright or native surface coupling; C17 flaky checks/shared accounts/secret traces; C18 execution/storage/test-account cost; C19 remove tooling after evidence/credential cleanup; C20 N/A without browser requirements. |
| P7 — runtime observability | C1 incident/effect evidence; C2 runtime/side-effect owner; C3 external runtime facts, no duplicate task truth; C4 correlation/build/event IDs needed; C5 observation not prevention; C6 retained logs aid rehydration; C7 concurrent telemetry not join coordination; C8 helps reconciliation, cannot stop effects; C9 core strength, sampling gaps; C10 runtime data/token scopes. | C11 component-specific; C12 APIs/SDK/exports/MCP; C13 OTel broad, backend-specific queries; C14 medium to high; C15 instrumentation/retention upkeep; C16 backend coupling, lower with portable signals; C17 dropped data/PII/misleading triage; C18 ingestion/storage/service cost; C19 export then remove, historical access at risk; C20 N/A without runtime need. |
| P8 — scripts/recipe runner | C1 repeatable mechanical steps; C2 invoked under task authority; C3 no independent state owner; C4 script/recipe/dependency/input pins; C5 deterministic validation possible, implementation absent here; C6 regenerates pointer bundles; C7 no inherent writer fencing; C8 subprocess handling not complete recovery; C9 captured stdout/results; C10 inherited host credentials. | C11 proposed script or pinned release; C12 CLI; C13 shell/platform dependent; C14 low script, medium runner; C15 repository maintainer; C16 low script, runner syntax coupling; C17 unchecked skips/force/partial effects; C18 local compute/dependency upkeep; C19 high if records preserved; C20 only after recurring mechanical pain. |
| P9 — durable orchestration/harness | C1 dispatch/checkpoints/delegation; C2 runtime controls execution, ADW decisions need separate binding; C3 high duplicate-state risk unless exact domains assigned; C4 run/checkpoint/config IDs, not automatic candidate binding; C5 configurable/replay-dependent; C6 resumes runtime state, not authority freshness; C7 runtime scheduling not global fencing; C8 cooperative cancel/retry partial; C9 richer histories, retention required; C10 workers/tools/store/service credentials. | C11 component-specific; C12 SDK/service; C13 medium/model-runtime-specific; C14 high relative to bootstrap; C15 service/upgrades/adapters; C16 engine/state-store coupling; C17 replayed effects/stale dispatch/cleanup loss; C18 infrastructure/provider cost; C19 costly migration of history/state; C20 unjustified unless smaller stack fails a demonstrated requirement. |

Each row below is a **RECOMMENDATION**, with maturity and capability facts supported by its ledger references. Conditional IDs refer to full prerequisite/owner/verification records in §18. Deferred triggers are in §14. Native existing capabilities are selection candidates only within already permitted read-only/supervised scope.

| Candidate | Profile and material override | Classification / evidence |
|---|---|---|
| Git commits, exact-SHA repository evidence, retained text/digests | P1; object identity is technical, semantic acceptance procedural | SELECT NOW candidate — S1; [G11](#g11) [G12](#g12) |
| Existing Research Register / separate domain evidence records | P1; current Register stays sole research/gate owner | SELECT NOW candidate — S1; [R03](#r03) [R04](#r04) |
| Repository task-control record as later product-task representation | P1; proposed, not created; one recorder for execution/cancel/recovery | SELECT NOW candidate — S2; [R06](#r06) |
| Issue as primary task object | P4; native status too coarse; can be sole product-task entry only after explicit ownership choice | CONDITIONALLY SELECT — C1; [G18](#g18) |
| PR as candidate/review transport | P4; not whole-task owner; mutable head and review presentation | CONDITIONALLY SELECT — C2; [G03](#g03) [G06](#g06) [G08](#g08) |
| Protected branch or active ruleset | P4; technical enforcement only after plan/configuration verification | CONDITIONALLY SELECT — C3; [G01](#g01) |
| CODEOWNERS and required reviews | P4; review routing/approval eligibility, no writer lease | CONDITIONALLY SELECT — C4; [G09](#g09) [G10](#g10) |
| Actions and checks/statuses | P4; verification evidence, not decision authority | CONDITIONALLY SELECT — C5; [G04](#g04) [G05](#g05) [G07](#g07) |
| Actions artifacts | P4; transport/retained results, retention and integrity enforcement needed | CONDITIONALLY SELECT — C6; [G15](#g15) |
| Environments | P4; deployment gate scope; private required reviewers not supplied by Pro | DEFER — D1; [G16](#g16) |
| Merge queue | P4; current private personal-repository mismatch | DEFER — D2; [G02](#g02) |
| Git worktrees/branches with one assigned writer | P1 + C1 workspace separation; C7 no native exclusive process lock; C10 no sandbox | CONDITIONALLY SELECT — C7; [G11](#g11) [O08](#o08) |
| ChatGPT Projects | P2; shared instructions/files context, not live truth | SELECT NOW candidate — S3; [O01](#o01) |
| Work and fresh task contexts | P2/P3 according to read/execution scope; eligibility/local-cloud distinctions | SELECT NOW candidate — S3; [O02](#o02) |
| Deep Research | P2; cited source-driven evidence, independent later review still required | SELECT NOW candidate — S3; [O03](#o03) |
| Existing GitHub-connected app reads | P5; exact ref/path resolution; actual read availability observed | SELECT NOW candidate — S3; [O04](#o04) [R09](#r09) |
| Additional Apps/plugins | P5 for reads, P3 for effects; permissions multiply; no universal read-only assumption | CONDITIONALLY SELECT — C8; [O05](#o05) |
| AGENTS.md/repository instructions | P3; guidance not access control | SELECT NOW candidate — S4 for existing instructions; [O06](#o06) |
| Custom skills / pointer rehydration helpers | P8/P5; progressive disclosure, proposed instructions not enforcement | DEFER — D3; [O07](#o07) |
| Existing supervised Codex verification/report execution | P3; bounded scope and effective existing permissions only | SELECT NOW candidate — S4; [O09](#o09) [O10](#o10) |
| Codex subagents | P3; inherited policy does not prove independent review or separate writer ownership | CONDITIONALLY SELECT — C9; [O13](#o13) |
| Codex hooks | P8; local covered tool boundaries only, incomplete interruption coverage | DEFER — D4; [O12](#o12) |
| Codex exec JSONL / output schema | P3; machine-readable evidence, schema does not prove correct verdict | CONDITIONALLY SELECT — C10; [O14](#o14) |
| Codex SDK / custom app-server client | P9; stable API versus experimental transport qualification; SDK pins unresolved | DEFER — D5; [O15](#o15) [O16](#o16) |
| Auto-review | P3; approval-request assessment, not conflict-free candidate review | CONDITIONALLY SELECT — C11; [O11](#o11) |
| Automations, goals, GitHub-triggered Work | P9; unattended continuity, not AFK eligibility | DEFER — D6; [O04](#o04) [O17](#o17) [O18](#o18) |
| Persistent/resumed/forked chats and memory | P2; advisory convenience only; fresh authority rereads still required | REJECT as authoritative state; otherwise existing UX only — X1; [O19](#o19) [O16](#o16) |
| Codex GitHub review | P4; defect assistance; native severity/scope not full ADW review | CONDITIONALLY SELECT — C12; [O20](#o20) |
| Native rg / existing IDE language intelligence | P5; ignored/hidden-file scope matters | SELECT NOW candidate — S5; [E302](#e302) [E304](#e304) |
| Serena | P5; symbol-aware read/edit surface and optional memory; language/backend-specific | CONDITIONALLY SELECT — C13; [E301](#e301) |
| ast-grep | P5; structural syntax, not type/reference proof | CONDITIONALLY SELECT — C14; [E303](#e303) |
| Existing JetBrains bundled MCP | P5; broad tool/terminal surface, IDE dependency | CONDITIONALLY SELECT — C14; [E304](#e304) |
| Direct official documentation | P5; publisher authority but rolling freshness | SELECT NOW candidate — S5 |
| OpenAI Docs MCP / Microsoft Learn MCP | P5; narrower publisher-owned retrieval, no workflow authority | CONDITIONALLY SELECT — C15; [O22](#o22) [E307](#e307) |
| Context7 CLI + Skills or MCP | P5; private backend/community corpus, citations/version validation needed | CONDITIONALLY SELECT — C16; [E305](#e305) [E306](#e306) |
| Ref Context / Ref Plans | P5 for Context; P9 for Plans; private index/key/cost | DEFER Context — D7; REJECT Plans as duplicate ADW authority — X2; [E308](#e308) |
| Playwright Test | P6; repeatable acceptance evidence if tests actually cover criteria | CONDITIONALLY SELECT — C17; [E310](#e310) [E311](#e311) |
| Playwright CLI / native OpenAI browser | P6; exploration; native surface has its own permissions | CONDITIONALLY SELECT — C18; [E309](#e309) [O23](#o23) |
| Playwright MCP | P6; persistent loop, explicitly not a security boundary | DEFER — D8; [E309](#e309) |
| Structured logs and existing CI results | P7; low additional complexity if already emitted, retention explicit | SELECT NOW candidate — S6 for available evidence; [R06](#r06) [G15](#g15) |
| Sentry / Sentry MCP | P7; runtime need; MCP includes mutation surfaces by default | CONDITIONALLY SELECT — C19/C20; [E312](#e312)–[E314](#e314) |
| OpenTelemetry | P7; portable signals, not storage or task orchestration | CONDITIONALLY SELECT — C21; [E315](#e315) |
| Small repository scripts | P8; hypothetical later mechanism; no implementation exists from this research | DEFER — D3 |
| just | P8; command discovery; no durable workflow engine | DEFER — D9; [G19](#g19) |
| Task | P8; dependency parallelism/cache/force semantics need explicit checking | DEFER — D9; [G20](#g20) |
| Minimal LangChain agent loop | P9 but fewer built-in state/planning features; still new runtime | DEFER — D10; [E326](#e326) |
| LangGraph / LangSmith Agent Server | P9; checkpoint/replay and hosted cancellation scopes differ | DEFER — D10; [E316](#e316)–[E319](#e319) |
| Deep Agents | P9; planning/filesystem/memory/delegation overlaps existing harness | DEFER — D10; [E326](#e326) |
| Temporal | P9; durable events/cooperative cancellation; extra service operations | DEFER for ADW — D11; CONDITIONALLY SELECT for distinct application need — C22; [E320](#e320) [E321](#e321) |
| OpenHands SDK / Agent Canvas | P9; SDK is bounded harness; Canvas broader beta control center | DEFER — D12; [E322](#e322)–[E325](#e325) |
| OpenAI harness-engineering pattern | P8/P9 depending realization; first-party case study, not a packaged control | SELECT NOW candidate for repository legibility principle only — S5; DEFER custom infrastructure — D13; [O26](#o26) |
| Symphony reference pattern | P9; engineering preview, scheduler retry/reconciliation not ADW recovery | DEFER — D13; REJECT unmodified as conforming ADW controller — X3; [O27](#o27) [O29](#o29) |

## 5. Requirement-to-mechanism matrix

**RECOMMENDATION/INFERENCE.** “Technical” below names a real primitive, not proof it is configured here. “Procedural” identifies deliberate human support. All design references are to the proposal at exact accepted subject [R06](#r06). Failure consequences preserve accepted semantics.

| Capability / design trace | Proposed mechanism and authoritative owner class | Technical versus procedural coverage | Remaining gap / consequence |
|---|---|---|---|
| Authority/state — DD-001–003; Authoritative-state ownership; false-pass scenario | Register owns research gate/dependencies; task-contract owner owns scope; designated execution recorder owns task/cancel/recovery; separate review/disposition/adoption owners | Git identities/history technical; authorized transition/applicability decisions procedural | No current transition validator or protected writer boundary; missing authority blocks transition |
| Readiness — DD-004–007; Readiness/task formation/delegation; stale-state/scope-expansion scenarios | Exact bounded contract, current input/config refs, delegated ceilings; task-contract owner | Rereads and explicit checks possible; ambiguity and sufficiency require judgment | No executable task until required inputs/criteria/authority known; readiness never implies authorization |
| Execution identity — DD-005; transition guards | Record task/run/actor/context/host, full input SHA and config/version identity; execution recorder | Tool run IDs plus immutable source pointers | UI task ID alone insufficient; uncertain identity blocks reliance |
| Candidate identity — DD-009; Candidate/verification/review/correction; material-correction scenario | Full candidate commit SHA plus path/blob/digest as relevant; designated candidate-pointer owner | Git content identity technical; freezing/pointer movement procedural today | Branch/PR/tag name alone rejected; every content correction gets new identity |
| Verification — candidate section; integrated pass/fail/N/A scenarios | Explicit obligations and raw results bound to exact local/integration subject; producer verification owner | Test runner/check evidence technical; criteria completeness and N/A rationale procedural | Skipped/neutral/missing/stale required work cannot mean passed |
| Independent review — DD-001/009; false-pass/carry-forward scenarios | Fresh conflict-free review record with exact subject, actor, findings, limitations; independent reviewer | GitHub review commit_id helps bind; independence/conflict assessment procedural | Auto-review or producer's own check does not satisfy review; lacking reviewer blocks required review |
| Disposition/adoption/baseline — state model/roles | Separate immutable decisions from the authorized owner; Register points to research disposition | Repository record durable after later persistence | Merge/check/review result cannot adopt tools or Workflow v1 |
| Durable evidence — DD-010; Reconstructable evidence | Exact inputs/config/versions, results/provenance/retention; evidence custodian | Git and digests plus retained artifacts; access/redaction process | Expired logs or hash warnings alone inadequate; unavailable load-bearing evidence blocks reliance |
| Fresh context — Handoff/rehydration; stale-summary scenario | Pointer-only handoff, fresh chat, live authority rereads; receiving actor verifies before acting | App reads, scoped navigation, optional later generated bundle | Resume/fork/memory cannot establish current source; disagreement resolved by authority |
| Writer isolation — DD-008; Parallelism/isolation/joins | Separate assigned worktrees and exact slice boundaries; one authorized writer per workspace/state | Worktrees separate files; OS/credential fencing would require later verification | Worktree lock is not editing lock; current governance blocks parallel writes |
| Dependency DAG/slices — Decomposition; missing/optional-result scenarios | One decomposition owner records dependencies, membership, required/optional inputs | Later validator/Actions needs can check graph; owner accounts outcomes | Scheduler success is not semantic readiness; missing required result yields partial/failed join |
| Join — DD-008; integrated verification scenarios | One integration owner; exact composed commit, complete branch accounting and current integrated results | Git integration/test evidence; join decision procedural | Local branch success never substitutes for integrated success; stale base requires impact/reverification |
| Generic stop — DD-011; generic-stop scenario | Recorder marks blocked, cancellation remains none; stop new effects and escalate | Available process/permission controls assist | No fabricated cancellation acknowledgement/containment |
| Cancellation — transition rules; requested/unacknowledged/residual-effect scenarios | Separate request, controller acknowledgements, observed containment and effects; one recorder, domain controllers supply evidence | Tool interrupt/cancel handles execution domains only | Unknown queued/external effects prevent terminal cancellation and resource release |
| Recovery/intervention — episode-reopening/repeated-recovery/ambiguous-retry scenarios | Distinct durable episode identities, obligation, side-effect owner, authorized action, validation and retained history | Records can represent all values; idempotency/reconciliation domain-specific | Never blind retry ambiguous effects; unresolved authority/effects remain blocked/intervention-required |
| Terminal accounting — explicit abandonment/cancellation closure scenarios | Authorized closure after effects/obligations handled; execution recorder | Durable accounting procedural | UI done/closed/abandoned cannot bypass containment/recovery |
| AFK — DD-013; unattended-evidence-incomplete scenario | Separate readiness/authority gate; hard ceilings, isolation, effective cancellation, evidence, recovery and reachable intervention | Candidate tools cover fragments; end-to-end control unverified | Fail closed: AFK denied; no implementation or mode activation recommended |

## 6. GitHub control-plane assessment

**RECOMMENDATION:** GitHub plus repository artifacts is the primary durable plane. Keep research state in its existing Register; use product repositories for their own task/evidence records. Do not replicate current research state into Issues, Projects, a harness database, memory, or an external plan service. Different domains may have different authoritative systems: Sentry may own an incident event, a runner its process status, and GitHub a PR. Their observations are inputs to ADW decisions, not co-owners of the same task state. [R03](#r03) [R06](#r06)

**INFERENCE — task object.** A designated repository task-control record best fits low-throughput, document-heavy initial dogfooding because its history, exact versions and authority links share the existing evidence substrate. This introduces no new service. It is less convenient for high-frequency concurrent updates; that is a later measurement question. An Issue is a conditional alternative for a product-task entry when assignment/discussion/dependency UX becomes necessary, provided ownership is explicitly chosen and repository evidence does not maintain a competing current status. A PR should identify a proposed change and associated review; many task outcomes have no PR. Issue closure and PR merge are insufficient terminal-accounting semantics. [G18](#g18)

**DOCUMENTED FACT:** private personal repositories have a GitHub Pro path to protected branches and repository rulesets. Protection settings/bypass handling and active ruleset enforcement matter. This establishes an available product path, not the present account plan or effective configuration. [G01](#g01)

**REPOSITORY FACT:** the current Register records protection unavailable under the current private plan; live main is unprotected. **RECOMMENDATION:** the viable present path is human-supervised read-only research plus any later separately gated, serialized exact-base persistence allowed by existing governance. No claim is made that this prevents another actor from moving main. Routine agent writes and protected parallel/automated/AFK modes remain blocked. A plan upgrade plus verified rules is a conditional prerequisite, not a selection or permission issued by this report. [R04](#r04) [R09](#r09)

**DOCUMENTED FACT:** PR review records can identify the reviewed commit; GitHub merge can guard the PR head SHA but its documented merge parameters have no expected-base SHA. Merge/squash/rebase strategies can produce a different final commit identity. **INFERENCE:** record observed base, candidate head, reviewed subject, tested integration subject and final published commit separately. A pre-merge base read plus head guard is not an atomic base guard. Exact post-publication readback detects drift but cannot retroactively justify an unreviewed adoption. Under the accepted design, an identity change requires applicable impact assessment and fresh verification/review; matching trees alone do not prove identical commit provenance. [G03](#g03) [G06](#g06) [G08](#g08)

**DOCUMENTED FACT:** GitHub check mergeability can accept success, skipped or neutral results; PR checks may govern the test merge SHA or head depending on available results. Status contexts and check runs are distinct surfaces. **RECOMMENDATION:** a later integrated-verification gate must enumerate required obligations, actual execution/conclusion, exact SHA, run attempt and expected producer. A green aggregate is inadequate when a required job was skipped, absent or evaluated on the wrong subject. This is stronger than GitHub's generic mergeability rule. [G04](#g04) [G05](#g05) [G07](#g07)

**DOCUMENTED FACT:** CODEOWNERS routes reviews and requires configured enforcement to block integration. It does not create exclusive slice ownership; any one listed matching owner may suffice. PR authors cannot approve their own PR. **RESEARCH GAP:** the target's eligible independent reviewing identity and enforceable role mapping need explicit resolution; multiple model contexts under one account are not proof of platform identity separation. [G09](#g09) [G10](#g10)

**DOCUMENTED FACT:** Actions offers repository/group-scoped concurrency, job execution, evidence and cancellation. Current `queue: max` adds up to 100 pending members; it does not serialize local writers or external systems. Artifacts can expire or be deleted; the documented digest mismatch behavior is a warning. Pro private environments do not supply private required-reviewer/wait-timer gates. Merge queue is not a private personal-repository option. **RECOMMENDATION:** use these only for their specific conditional scope, not as substitute branch protection, global ownership, permanent archives or full recovery. [G02](#g02) [G13](#g13)–[G17](#g17)

## 7. ChatGPT/OpenAI capability assessment

**DOCUMENTED FACT:** Projects group instructions, files and conversations; Work provides task-oriented local/cloud experiences where available. Deep Research supports source selection, planning, connected sources and cited report output; its app use is read-only in that research mode. The GitHub-connected experience retrieves allowed repository content, with availability varying by surface and account. Eligible Work configurations also document GitHub event triggers. These are distinct surfaces with distinct capability/permission dependencies. [O01](#o01)–[O05](#o05)

**RECOMMENDATION:** use the already available coordinator and research UX to carry a compact task contract and immutable pointers, then resolve those pointers through the connected GitHub app. Project files and chat summaries are helpful navigation; they remain snapshots. A persistent conversation may preserve intent but accumulates stale assumptions. A fresh conversation reduces inherited narrative, yet is safe only after it reads current owners and exact evidence. Fork/resume features preserve history, not current authorization. No feature removes the accepted authoritative reread. [R06](#r06) [O16](#o16) [O19](#o19)

**INFERENCE — reduced pointer ferrying without duplicated truth.** Existing project instructions can tell a fresh worker where authority lives; exact links in bounded handoffs avoid copying whole reports; GitHub reads resolve current pointers; skills can progressively reveal procedure; task output can be a durable artifact plus digest rather than a long chat recap. A later read-only helper could assemble a transient source manifest from owners at a recorded time. Such a bundle must identify its source versions and be discarded/rebuilt when stale. It must never become another editable current task ledger. [O01](#o01) [O04](#o04) [O06](#o06) [O07](#o07)

**RECOMMENDATION:** keep the OpenAI coordinator surface replaceable by preserving contracts, decisions and evidence outside chat before reliance. Existing app access can be reused within the bounded task; adding plugins or event-driven work is a separate conditional decision. Connector authentication does not itself constrain an operation to the research role. Different tool inventories can include write tools even when this task authorizes only reads. This research used GET/read operations only.

**RESEARCH GAP:** exact account/region/model/plan eligibility and the effective local/cloud tool boundaries for future use were not audited. Current docs support capability discovery, not a guarantee that every advertised surface is enabled here. No product memory, project memory, auto-generated summary or model narrative is an accepted durable owner.

## 8. Codex execution assessment

**DOCUMENTED FACT:** AGENTS.md instructions are discovered by scope and precedence; skills provide progressive disclosure. They guide execution rather than enforce access. Worktrees isolate working files but share Git metadata, and app-created work can start detached or with chosen local state. A fresh task therefore needs explicit base/configuration verification. [O06](#o06)–[O08](#o08) [G11](#g11)

**DOCUMENTED FACT:** permissions are documented as beta. Local command sandboxing, network policy, approval review, MCP/connectors, browser and cloud surfaces do not all share one universal boundary. Network domain restrictions depend on the documented proxy path; configuration precedence and managed policy matter. Subagents inherit constraints but do not establish independent review or exclusive filesystem ownership merely by existing. **RECOMMENDATION:** record effective configuration and enabled effectful surfaces, not just requested settings. Use the current supervised bounded environment only within verified authority; add no new permission surface for convenience. [O09](#o09)–[O11](#o11) [O13](#o13)

**DOCUMENTED FACT:** hooks can inspect/block some local tool calls, but coverage has exceptions and concurrently matching hooks cannot prevent sibling hooks from starting. Interrupt hooks cannot veto interruption or restart work; some subagent/stop hook responses do not mean what a generic “block” label suggests. **INFERENCE:** hooks are possible later guard/telemetry adapters, not a complete cancellation or authorization kernel. A hook failure or gap must not silently permit a transition whose assurance depends on that hook. No hooks were implemented. [O12](#o12)

**DOCUMENTED FACT:** noninteractive execution can emit JSONL and structured final output. SDKs and app-server expose programmatic threads/events; interruption acknowledgement and the later interrupted status are separate. App-server documentation distinguishes a stable nonexperimental API surface from experimental command/transport or process features in particular contexts. **RECOMMENDATION:** prefer ordinary supervised execution now; conditionally capture structured events for recurring evidence work, and defer custom clients until their lifecycle benefit exceeds adapter maintenance. Output schema validity is not semantic correctness. [O14](#o14)–[O16](#o16)

**DOCUMENTED FACT:** background automations and persistent goals can continue bounded work in supported surfaces; local/cloud availability and awake/runtime requirements differ. Current CLI documentation deprecates `--full-auto`; SDK guidance deprecates `codex mcp-server`. The latest fetched Codex release is `rust-v0.153.2` with a pinned release commit in §19. Recent experimental context-management features are account/mode-specific. **RECOMMENDATION:** no unattended selection follows from these capabilities. Rehydration still rereads owners; continuation never enlarges authority. [O14](#o14) [O15](#o15) [O17](#o17) [O18](#o18) [O21](#o21) [O28](#o28)

**INFERENCE — verification and review.** The executor may run authorized checks and report exact outputs. Its own self-check is producer verification. Codex review assistance, detached review contexts and approval auto-review can help discover defects or assess tool requests; none independently proves the accepted reviewer role, source-review scope, conflict freedom, or disposition authority. These must be explicitly established. Permission/safety monitoring is a supplementary control, not evidence that a candidate passed independent review. [R06](#r06) [O11](#o11) [O16](#o16) [O20](#o20) [O25](#o25)

## 9. External MCP/integration assessment

**RECOMMENDATION — default:** no mandatory new MCP or external service for initial dogfooding. Native search and existing IDE intelligence first; direct official documentation first; existing browser or test facilities only where needed. Read-only access is a proposed scope to verify, not a property inferred from the MCP label. Compare each integration against the same target tasks, source correctness, tool inventory, query privacy, maintenance and removal path.

**DOCUMENTED FACT:** Serena supports semantic tools through language-server and JetBrains backends, with optional memory and overlapping generic tools. ast-grep provides structural syntax search. Bundled JetBrains MCP offers IDE intelligence with configurable tool exposure. **RECOMMENDATION:** choose a narrower existing mechanism when it answers the actual navigation question; condition Serena on demonstrated benefit in a supported codebase. Disable unnecessary mutation/memory surfaces where the selected configuration permits. No ADW-specific superiority benchmark is available. [E301](#e301)–[E304](#e304)

**DOCUMENTED FACT:** Context7 offers CLI + Skills and MCP, with version/library targeting, a community-contributed corpus and private backend. Publisher-owned OpenAI Docs MCP and Microsoft Learn MCP are narrower alternatives. Ref Context offers another public/private retrieval service, while Ref Plans introduces shared plan state. **RECOMMENDATION:** preserve original upstream citations/version identity; retrieval confidence is not authority. Context7 is conditional on repeated library lookup pain. Ref Context is deferred; Ref Plans is rejected as an additional mutable ADW owner. Credentials, quotas, query disclosure and index freshness remain explicit costs. [O22](#o22) [E305](#e305)–[E308](#e308)

**DOCUMENTED FACT:** Playwright Test exposes machine-readable reports; browser profiles/authentication and application state need separate handling. Current guidance suggests CLI + Skills for coding-agent efficiency and MCP for persistent exploration. Playwright MCP expressly disclaims being a security boundary. **RECOMMENDATION:** for a browser product, prefer repeatable tests for acceptance and use exploration to discover/reproduce issues. Native browser is a smaller one-off alternative where available. MCP stays deferred until a persistent loop provides measurable additional value. Closing a browser cannot establish that server-side effects ceased. [E309](#e309)–[E311](#e311) [O23](#o23)

**DOCUMENTED FACT:** Sentry MCP exposes debugging/triage/project capabilities, with transport, scopes and maturity varying across its documentation. OpenTelemetry produces and exports signals without providing a storage backend. **RECOMMENDATION:** start with available structured logs and CI evidence; add Sentry for a real incident requirement, then MCP only if ordinary read access is insufficient. Narrow tokens and tool exposure, preserve build/event correlation and verify forbidden writes. Adopt OTel only where portable instrumentation is justified; select component and semantic-convention versions separately. [E312](#e312)–[E315](#e315)

**RESEARCH GAP:** no reviewed retrieval/browser/telemetry integration establishes the complete ADW cancellation-to-terminal contract. This is absence of sufficient evidence for that assurance, not proof the products have no cancellation features. Installation, compatibility, permission rejection, source-completeness and containment tests require later bounded authorization.

## 10. Parallel execution and worktree architecture options

**REPOSITORY FACT:** parallel writes are not authorized by the current governance/protection state. This section compares future architecture options, not an execution plan. The accepted design requires one ownership model, bounded slices, a dependency DAG and exact integrated verification where applicable. [R04](#r04) [R06](#r06)

| Option | RECOMMENDATION / mechanism tradeoff | Failure boundary |
|---|---|---|
| Serialized bounded tasks, one active writer when separately authorized | SELECT NOW candidate for the supervised baseline; smallest coordination burden | Procedural exclusivity only; no prevention of another authorized actor's write |
| Read-only parallel research/proposal workers | CONDITIONALLY SELECT under explicit bounded delegation; return source/evidence pointers to one producer | No shared mutable owner; correlated model output is not independent review |
| One branch/worktree per writer, one integration owner | CONDITIONALLY SELECT only after governance/protection and isolation prerequisites | Shared refs/config/credentials can cross worktree boundaries; lock files alone do not fence all writers |
| Actions jobs for independent verification | CONDITIONALLY SELECT for adopted deterministic checks, scoped dependency edges and recorded subject | `needs`/concurrency are runner scheduling constructs, not authoritative required/optional join semantics |
| Shared checkout or unrestricted same-branch agents | REJECT for this design without effective exclusive control | Conflicting writes, stale index and ambiguous effect ownership |
| Durable scheduler/harness | DEFER until dispatch/restart scale demonstrably exceeds simpler controls | Adds state store, retry policy and authority adapter; may still lack global writer fencing |

**RECOMMENDATION — ownership representation.** A future task-control record can name the writer, workspace, branch, allowed paths, base and control scope; this report does not prescribe a schema. Technical sole-writer assurance would additionally need an enforceable runtime/filesystem/credential boundary covering all mutation paths. `git worktree lock` only protects worktree administration; Git's duplicate branch checkout safeguards are not process ownership and can be overridden. Local ref transactions can compare expected old IDs but do not solve remote integration or filesystem concurrency. [G11](#g11) [G12](#g12)

**RECOMMENDATION — dependency/join coordination.** One decomposition owner controls slice membership, dependency identities and required/optional classification; one integration owner assembles current accepted inputs. A join accounts for every slice, conflicts, effects and omissions, then records exact integrated subject and required verification results. Legitimate integrated-verification N/A needs the governing rule/rationale; the verification plane stays not-invoked rather than passed. Missing required results, stale inputs, conflicts or failed integrated checks produce non-success. Reframing a reduced objective requires fresh authority. [R06](#r06), “Parallelism, isolation, and joins” and corresponding conformance scenarios.

**INFERENCE — smallest-first harness comparison.** Manual task dispatch plus Git is sufficient at bootstrap volume. A small read/validation script can later remove repetitive pointer collection without owning state. just adds recipe discovery; Task adds dependency/freshness scheduling; Actions adds hosted execution and check evidence. Codex SDK/app-server or a minimal agent loop adds integration effort before it adds durable ADW semantics. LangGraph adds explicit checkpoints; Temporal adds durable event-driven execution; broader harnesses add more planning/delegation surfaces. No demonstrated present requirement justifies those extra owners/services. [G19](#g19) [G20](#g20) [O15](#o15) [O16](#o16) [E316](#e316)–[E326](#e326)

**DOCUMENTED FACT — Symphony:** the pinned draft specification describes tracker-driven dispatch, claimed/running state, concurrency and restart reconstruction. It keeps workers running when tracker refresh fails, retries some failed/stalled work, and can clean terminal workspaces. The reference is an engineering preview rather than a complete business-policy engine. **INFERENCE:** these defaults cannot be equated with ADW fail-closed readiness, operation-aware recovery or preserved evidence. An adapter would need explicit semantic mapping and testing; deploying the reference unmodified is rejected. [O27](#o27) [O29](#o29)

**DOCUMENTED FACT — published harness pattern:** OpenAI's harness-engineering article reports one internal experiment and emphasizes repository legibility and mechanical invariants. It also describes permissive merge practices in that environment. **RECOMMENDATION:** borrow the general evidence/navigation principle only; do not import that case's merge or autonomy choices over ADW's accepted review and stop requirements. Vendor case-study throughput is not a target-project benchmark. [O26](#o26)

## 11. Evidence and observability options

**RECOMMENDATION — minimum evidence package.** Derive this from the accepted “Reconstructable evidence,” candidate, handoff and interruption sections, not a particular tool output format. This is a content checklist for later representation design, not a created schema. [R06](#r06)

| Evidence purpose | Minimum content necessary for reliance | Proposed owner |
|---|---|---|
| Task/authority | Task/contract identity; scope and allowed effects; decision owner and authority reference; exact baseline/dependencies; readiness/applicability; permissions, budgets, stop/escalation and output criteria | Task-contract owner; execution recorder references it |
| Producer verification | Candidate/integration full SHA; path/blob/digest where relevant; actual checked-out input; tool/runtime/model and dependency versions; effective configuration identity; test obligations, command/request, raw result, exit/conclusion, timestamp, failures/skips/limitations | Producer verification owner |
| Independent review | Frozen subject identity; reviewer role/conflict assessment; sources/method, findings, limitations and verdict; publication-time review metadata; applicability and freshness | Independent reviewer |
| Disposition | Exact reviewed subject and review identity; authorized deciding actor; each recommendation/outcome and scope; conditions/residual risk; separate adoption or baseline decision if required | Authorized disposition/adoption/baseline owner |
| Failure/cancellation | Operation/run/controller IDs; last observed progress and effect domains; trigger/request; acknowledgements; containment observations; retained outputs, external effects and uncertainty | Execution recorder, using domain-controller/side-effect-owner evidence |
| Recovery | Distinct episode identity and predecessor link; new obligation, operation class, owner, bounded action authority; retry/reconciliation/compensation evidence; validation target/result; residual-risk and terminal obligations | Execution recorder; side-effect owner supplies consequential decisions |
| Cross-session continuation | Pointer manifest to exact contract, current state owner, baseline/config, dependencies, candidate/review/evidence, cancellation/recovery and safe next action; receiver reread evidence | Sending/receiving actors under named owners |
| Retention/access | Stable evidence pointer, content digest, source/provenance, run/attempt/artifact ID, retention/expiry, access/redaction constraints and custodian | Evidence custodian; no decision authority |

**INFERENCE:** small textual evidence belongs in versioned artifacts. Large logs/traces may remain in an access-controlled artifact store with a retained manifest, digest and adequate lifetime. Actions artifacts are useful transport, but deletion/expiry and warning-only digest validation mean a later retention/integrity control must close that gap. Tool transcripts, screenshots and Sentry links are supporting evidence, not substitutes for exact subject/configuration identity. A digest proves equality to known bytes; it does not prove that tests were sufficient or that an external action occurred. [G15](#g15) [E311](#e311) [E312](#e312)

**RECOMMENDATION:** preserve historical evidence as historical; only its designated current pointer moves. Do not rewrite a completed recovery episode or stale review to make a dashboard look current. Redact secrets and unnecessary sensitive material without destroying essential provenance; if required evidence cannot be safely retained, fail the dependent reliance gate. For runtime incidents, correlate telemetry to release/build/task/run, and account for sampling, dropped events, clocks and inaccessible data before concluding absence of effects. [R03](#r03) [R06](#r06) [E315](#e315)

## 12. Unattended/AFK control options

**REPOSITORY FACT:** Workflow v1 is unadopted and current governance does not authorize AFK. The accepted design requires verified controls and explicit authority before eligibility; necessary evidence alone is insufficient. **RECOMMENDATION:** do not enable AFK now. [R04](#r04) [R06](#r06)

| Necessary control | Candidate support | Unresolved assurance / mode consequence |
|---|---|---|
| Ready bounded task and current gate | Exact contract/readiness/identity checks | Human review now; no validated autonomous transition guard |
| Permission/credential ceilings across all surfaces | OS sandbox, managed permissions, scoped app tokens, protected integration | Local shell restrictions do not establish browser/MCP/cloud ceilings; effective configuration untested |
| Isolation and sole writer | Separate worktrees plus possible later isolated runtime/credential allocation | Worktree alone insufficient; no verified fencing; parallel writes blocked |
| Resource/concurrency limits | Runner timeouts, Actions groups/quotas, explicit task budgets | Need hard model/tool/host/external-service ceilings and failure response, not merely a prompt budget |
| Observable progress and durable evidence | Events, structured outputs, logs/artifacts | Need completeness, freshness, heartbeat loss behavior, retention and independent visibility |
| Effective cancellation | Native interrupt/cancel/process controls | Must prove acknowledgement and containment in every affected domain, including queued remote actions |
| Recovery and intervention | Explicit episode records, operation-specific reconciliation/compensation | No generic tool establishes safe retry or external effect reversal |
| Safe unavailable-human state | Stop/escalate/retain evidence and resources until safe | Reachability and safe waiting/isolation need tested controls; no automatic continuation when authority absent |
| Separate eligibility and execution authority | Later coordinator/governance decision | Absent; all other evidence cannot grant it |

**DOCUMENTED FACT — cancellation is not one state.** Codex app-server returns an interrupt response before later completion status. Actions cancellation can leave conditionally continuing jobs; runner process termination does not undo external operations. LangSmith's default cancellation acknowledgement is asynchronous; its rollback removes run/checkpoint evidence, not documented external effects. Temporal cancellation is cooperative and regular Activities need heartbeats/timeouts to receive it; termination does not run workflow cleanup. OpenHands pause examples wait for the execution thread. None of these facts proves complete ADW containment. [O16](#o16) [G13](#g13) [E319](#e319) [E320](#e320) [E325](#e325)

**RECOMMENDATION — preserve the accepted state model.** The recorder first records blocked/requested where cancellation was requested, then acknowledgement only after each relevant controller has acted, then observed contained or residual-effects. Generic stop without a cancellation request remains blocked/none. Recovery requires operation-aware authority, classifying effects as repeatable, conditional, compensatable, irreversible, nondeterministic or ambiguous. Timeout with unknown external completion forbids blind retry. Compensation is a new effect needing authority, not erasure of history. [R06](#r06), “Transition rules” and “Stop, cancellation, containment, retry, and recovery.”

Recovery completion leaves the task blocked/recovered until a separate valid transition. Ordinary authorized resumption resets cancellation/recovery as specified while retaining episode history. A new obligation after a completed episode requires a distinct linked episode and fresh evidence/authority; retaining recovered cannot discharge that new obligation. Unresolved consequential decisions move to blocked/intervention-required even if the human owner is unavailable. Terminal cancellation or abandonment requires complete effect/obligation accounting and separate closure authority. No engine retry, checkpoint reset, Issue close, or UI done status can replace these guards. [R06](#r06), recovery reopening, repeated recovery, intervention-required and terminal scenarios.

## 13. Minimum viable tooling stack

**RECOMMENDATION — initial architecture.** The smallest sufficient proposal consists of an authoritative evidence substrate, a supervised coordinator, a bounded executor and explicit owner decisions. It is a candidate architecture for later disposition, not an operationally adopted workflow.

```text
Authoritative repository owners and exact committed evidence
    | current pointers + exact subjects; read before each transition
    v
Fresh coordinator / research / executor contexts
    | bounded contract, least necessary existing permissions
    v
Producer output + raw verification + operation observations
    | separately authorized freeze/persistence
    v
Fresh independent review -> authorized disposition -> later adoption gate

Runner/UI/Issue/PR/telemetry observations feed named owners.
They do not independently set ADW current task/gate/review/disposition state.
```

| Stack category | Proposed contents | Scope and limits |
|---|---|---|
| Selected mechanism candidates | S1 exact-SHA Git/GitHub evidence and existing owner separation; S2 repository task-control representation; S3 existing fresh OpenAI coordination/research and connected reads; S4 bounded supervised Codex; S5 native navigation/direct docs; S6 available raw results/logs | No new external service, installer, orchestrator or adopted schema required. S2 is only a representation choice awaiting disposition/design. |
| Human/procedural controls | Task formation/readiness; applicability; exact-source rereads; serialized writer assignment; review independence; impact analysis; join accounting; side-effect reconciliation; terminal decisions; disposition | Deliberately manual at bootstrap. Human controls do not become claimed technical enforcement. |
| Conditional project-specific mechanisms | Browser tests/CLI; semantic navigation; library-doc retrieval; Sentry/OTel; adopted Actions verification and retained artifacts | Only after project need, permissions, ownership and verification conditions in §18 are met. |
| Deferred mechanisms | Custom scripts/skills/hooks, recipe engines, SDK clients, general harnesses, background schedules/goals, merge queue, environment gates | Revisit triggers in §14; no implied implementation order or authority. |
| Unsupported/partial controls | Preventing unauthorized unprotected-main changes; enforceable sole writer; atomic exact integrated publication; universal cancellation/containment; AFK readiness; guaranteed retention; automatic review-role enforcement | Procedural where permitted; fail closed for required gates and restricted modes; gap-by-gap consequences in §15. |

**INFERENCE — stack interaction assessment.** Git commits bind subject identity; repository owner records bind meaning; fresh contexts reconstruct those owners; the executor generates evidence; independent review and disposition consume frozen subjects. The data path is coherent because no component can silently promote its local status to a decision. The remaining weakness is prevention: an unprotected repository and manual state discipline detect some drift but do not stop all unauthorized actors or raced writes. Therefore this proposal supports the present narrow supervised boundary, not routine engineering autonomy.

Adding an Issue and a task file with separately editable status would make the architecture worse unless one is expressly a derived view or their domains are disjoint. Adding an orchestrator database and webhook task status has the same risk. Adding many MCPs multiplies authentication, logs and interruption domains before it proves any workflow benefit. A smaller stack wins here because each additional state/effect surface needs an owner, identity, freshness and recovery story, not because external tools lack useful capabilities.

## 14. Alternatives rejected or deferred

**RECOMMENDATION — DEFER.** These are bounded revisit triggers, not scheduled work.

| ID / candidate | Evidence or pain that would justify revisiting | Why defer now |
|---|---|---|
| D1 — environments | Actual deployment requiring target-specific approvals/secrets, with suitable private-repository entitlement | No deployment task; Pro does not solve private reviewer gate [G16](#g16) |
| D2 — merge queue | Sustained integration contention and justified organization/plan architecture | Current repository type/scale mismatch [G02](#g02) |
| D3 — scripts/custom skills | Repeated verified pointer/identity collection or command steps create measurable manual errors/latency | First define accepted representation and obligations; avoid scripting unstable semantics |
| D4 — hooks | A recurring covered tool-boundary error with a demonstrably reliable fail-closed response | Incomplete coverage; custom hook maintenance not yet justified [O12](#o12) |
| D5 — Codex SDK/app-server client | Native UI/CLI cannot provide required integration/event capture at observed scale | Extra lifecycle adapter; experimental-surface and version compatibility gaps [O15](#o15) [O16](#o16) |
| D6 — schedules/goals/webhook dispatch | Later adopted unattended controls, demonstrated scheduling need and explicit authority | AFK/automated writes unavailable; persistent work is not a control substitute [O17](#o17) [O18](#o18) |
| D7 — Ref Context | Direct publisher docs and a bounded retrieval alternative fail a real private/public corpus need | Additional index, API key, billing and privacy surface [E308](#e308) |
| D8 — Playwright MCP | Persistent exploratory browser loops materially outperform native browser/CLI on target tasks | CLI/test alternatives smaller; more live state and auth exposure [E309](#e309) |
| D9 — just/Task | Repeated command discovery need favors just; cross-platform dependency/freshness need may justify Task | No current need for a runner dependency; cache/force/skip semantics need review [G19](#g19) [G20](#g20) |
| D10 — agent loop/LangGraph/Deep Agents | A bounded application runtime requires custom graph/checkpoint/model behavior that native execution cannot supply | Extra execution state and replay/effect obligations [E316](#e316)–[E319](#e319) [E326](#e326) |
| D11 — Temporal | Concrete long-lived application work must survive outages/waits beyond simpler controls | Service operations/cost unjustified for bootstrap task coordination [E320](#e320) [E321](#e321) |
| D12 — OpenHands SDK/Canvas | Demonstrated model portability or specialized runtime requirement unmet by existing harness | SDK adds a new runtime; Canvas beta adds a broader control plane [E322](#e322)–[E325](#e325) |
| D13 — Symphony/custom harness infrastructure | Proven dispatch volume or recovery requirements plus accepted ownership/adapter design and conformance evidence | Preview/reference defaults do not match all ADW guards; no need for another scheduler yet [O26](#o26) [O29](#o29) |
| D14 — local Git ref-transaction wrapper | Repeatable local expected-old-ID operations with separately adopted publication design | Does not solve remote atomicity or writer isolation by itself [G12](#g12) |

**RECOMMENDATION — REJECT for the specified architecture/use.** Rejection does not assert a product is unusable for unrelated purposes.

| ID | Rejected architecture/claim | Decisive incompatibility |
|---|---|---|
| X1 | Chat/project memory or resumed transcript as current authority | Can retain stale state and lacks authoritative owner/identity discipline |
| X2 | Register + Issue + task file + Ref Plans/harness DB independently owning the same current fields | Competing mutable truth violates single ownership; synchronization does not remove competing writers |
| X3 | Unmodified Symphony/harness retry/cleanup defaults as ADW conformance | Stale authority, blind retry or evidence cleanup can violate readiness/recovery/durability guards |
| X4 | Shared checkout/branch writes without effective exclusive control; CODEOWNERS/worktree lock as a lease | No exclusive mutation enforcement |
| X5 | Branch/PR/tag name, green aggregate or provider “done” as accepted subject/outcome | Mutable or incomplete identity; conflates verification/review/disposition/join/terminal planes |
| X6 | Auto-review/producer checks/forked self-review as independent source review | Conflict-free role and exact review obligations are not established |
| X7 | Cancel response, process exit, checkpoint rollback or Issue close as containment/recovery completion | External effects and obligations remain unaccounted |
| X8 | Procedural SHA freeze as branch protection; Pro private environments as required-reviewer solution | Different technical enforcement/entitlement properties |
| X9 | All named MCPs as a mandatory universal stack | Authority, credential and maintenance cost without demonstrated project benefit |

## 15. Known gaps and unsupported requirements

**RESEARCH GAP.** These gaps narrow recommendations rather than invite semantic redesign. “Procedural” below means permitted supervised handling only, not a waiver of any adopted restriction.

| Gap | Missing evidence/control; responsible owner class | Required resolution and consequence |
|---|---|---|
| RG1 — effective protection | Account plan/configuration and bypass enforcement; repository owner | Suitable plan, adopted rules and live readback plus authorized negative tests. Present exact-base procedure remains procedural; routine/parallel/automated writes blocked. |
| RG2 — writer fencing | Enforceable exclusive mutation across process, workspace, refs and credentials; execution/runtime owner | Boundary design and authorized adversarial/concurrent tests. Assignment alone is procedural; protected parallel mode blocked. |
| RG3 — exact integration publication | Atomic relation among reviewed subject, tested integration and final commit under chosen merge path; integration owner | Explicit adopted publication strategy, exact identities and tested drift handling. Missing required same-subject evidence fails closed; manual readback cannot undo invalid adoption. |
| RG4 — reviewer identity | Conflict-free role, fresh context, eligible platform identity and required-review mapping; coordinator/repository owner | Named independent reviewer and exact subject evidence. Required review remains pending; no self-review substitution. |
| RG5 — cross-surface permissions | Effective local/network/browser/MCP/cloud/host/managed configuration; security/runtime owner | Pin versions/config and test forbidden actions in an authorized isolated trial. Restrict current scope; AFK blocked. |
| RG6 — cancellation/containment | All process/queue/remote domains, bounded stop latency, acknowledgements and observed effects; execution and side-effect owners | Authorized fault/timeout/interruption trials with retained evidence. Unknown effects remain blocked/intervention-required; no retry/terminal closure/AFK. |
| RG7 — durable recovery | Idempotency/deduplication, operation-specific reconciliation, distinct episode history and validation; side-effect owner | A later implementation must pass accepted recovery scenarios, including reopening and repeated cycles. Manual records can represent semantics; autonomous recovery unsupported. |
| RG8 — retention/integrity | Actual retention owner, accessible evidence lifetime, fail-closed digest checks and redaction; evidence custodian | Selected retention policy and verified retrieval. Current local report is not yet durably frozen in GitHub; unavailable evidence blocks later reliance. |
| RG9 — installed capabilities | Exact installed client/runtime/SDK versions, plan/region availability, component compatibility; tooling owner | Capture actual environment at later selection/execution. OSS pins here are research snapshots, not installed-state claims. |
| RG10 — integration leverage | Target-corpus benchmarks for Serena/Context7/browser/observability/harness benefit; project owner | Measured correctness, completeness, cost and maintenance against native baseline. Conditional integration not eligible until justified. |
| RG11 — documentation ambiguity | App-server production-surface maturity; Sentry MCP transport/auth/scope distinctions; vendor maintainers and tooling owner | Resolve exact chosen version/transport through authoritative docs/source and authorized verification. Narrow/defer affected capabilities, never infer full coverage. |
| RG12 — AFK end-to-end control | Readiness, ceiling, isolation, progress, cancellation, evidence, recovery and unavailable-human conformance; coordinator plus runtime/side-effect owners | Necessary controls demonstrated and separately authorized eligibility. Mode remains denied even if one tool supplies a subset. |

**DESIGN-IMPACT findings — isolated, not incorporated.** DI-1: adopting a tool's single done/failed/cancelled status as the ADW lifecycle would collapse accepted state planes, applicability and terminal guards. It would require a semantic design change; this report rejects that mapping. DI-2: accepting automatic retry after ambiguous effects, continuing on materially stale authority, or deleting relied-upon recovery evidence as normal controller behavior would relax accepted stopping/recovery/durability semantics. Unmodified harness defaults cannot be accepted on that basis; a later adapter must preserve the design, or a separate design-impact disposition/new candidate/review would be required. No change to accepted Workflow v1 is recommended or made. [R06](#r06) [O29](#o29) [E317](#e317) [E319](#e319)

## 16. Proposed staged rollout

**RECOMMENDATION — later decision sequence only.** No step below is authorized for execution by this report.

1. **Evidence lifecycle:** byte-exact report persistence/freeze; fresh independent source review; persistence of that review; fresh coordinator disposition naming the frozen report/review. Recheck time-sensitive claims at disposition without silently changing this snapshot.
2. **Small supervised representation:** only accepted selections enter a bounded tooling/enforcement design gate. Resolve task object/owners, evidence content, reviewer identity and allowed write/protection path. Workflow v1 adoption remains separate. Continue only currently permitted research/bounded persistence meanwhile.
3. **Mechanical reduction of observed friction:** after accepted representation and demonstrated repetition, consider read-only rehydration/identity validators, simple recipes and deterministic verification. They consume authoritative owners and emit evidence; they do not become another decision database.
4. **Protected project dogfooding:** after plan/configuration and authority prerequisites, test one bounded writer, exact publication/review binding, retention and cancellation/recovery under supervised conditions. Verify non-success and N/A scenarios, not only a happy path. No implementation or trial occurs in this task.
5. **Conditional parallel/project integrations:** only after demonstrated need and effective exclusive control, evaluate isolated slices and joins; add browser/incident/navigation tooling by project need. Record integrated verification and stale-input handling.
6. **Possible later unattended assessment:** only if the accepted prerequisites are demonstrably met and a separate governance decision makes the mode eligible. This report recommends no AFK activation date or automatic progression.

The staged order minimizes irreversible state migration. Rejecting a candidate at disposition leaves plain-text/Git evidence usable. Removing a retrieval tool is easier than migrating authoritative task state out of an orchestration database; that reversibility advantage supports the small-stack recommendation.

## 17. Risks and failure modes

**INFERENCE — stack-level risks and proposed responses.** These are operational implications of the accepted design and documented limitations, not newly adopted policy.

| Interaction failure | Concrete trigger / effect | Proposed detection and safe consequence |
|---|---|---|
| Duplicate current truth | Issue closes while task record still has residual effects; harness marks done | One named owner per field/domain; derived views carry source identity; disagreement blocks promotion |
| Identity mismatch | PR head reviewed, test merge checked, squash commit published | Preserve all subjects; explicit impact/current verification and applicable review; no implicit acceptance |
| Stale pointer/configuration | Project memory or cached source bundle points to superseded contract | Live authoritative reread before transition; deny dispatch/resumption on material change |
| Authority expansion | Skill/subagent/webhook inherits broader tools than the task contract | Contract ceiling plus verified permissions; available tool is not a grant; stop on scope expansion |
| Permission multiplication | Local sandbox assumed to constrain remote MCP/browser/API effects | Enumerate domains and credentials; narrow unverified surface; no AFK claim |
| Conflicting writer/task status | Two agents edit shared refs/state while runner says one job active | Exclusive owner/boundary; runner concurrency not global; serialize or block parallel mode |
| Review drift | New content pushed after review; UI still appears approved | Exact review subject and applicability re-evaluation; stale evidence remains historical |
| Missing join evidence | All local jobs green but one required slice absent or integration failed | Complete required/optional accounting and exact integrated obligation results; join non-success |
| Weak cancellation | Parent stopped while child/queued remote publication continues | Domain-specific acknowledgement/observation; retain blocked state and containment-critical resources |
| Unsafe replay | Engine resumes node and repeats a non-idempotent external effect | Classify operation, reconcile first; explicit authority and distinct recovery episode |
| Evidence disappearance | Artifact expiry, rollback deletion, lost local chat/runtime state | Custodian, retained digest/manifest and access verification before reliance; fail closed if missing |
| Tool-specific lock-in | Task meaning embedded only in a proprietary run/checkpoint database | Portable owner/evidence records; use runner state only for its execution domain |
| Unnecessary complexity | Many MCPs/harnesses installed before observed need | Conditional thresholds and removal criteria; compare against native baseline |
| Misread product maturity | Preview transport or current HEAD feature assumed stable/installed | Pin version/config and preserve lifecycle uncertainty; verify at later gate |

## 18. Recommendations requiring later coordinator disposition

**RECOMMENDATION — SELECT NOW candidates.** “Now” identifies the proposed first selection set for later disposition, not authorization in this task.

| ID | Candidate and scope | Remaining human/control obligation |
|---|---|---|
| S1 | Git/GitHub exact-subject evidence; existing Register/domain ownership; separate verification/review/disposition records | Preserve owner separation; human exact-base gate under current protection restriction |
| S2 | Repository task-control record for initial product-task dogfooding representation | Later accepted design of representation/ownership; no schema or mutable duplicate created here |
| S3 | Existing Projects/Work/Deep Research and connected GitHub reads, with fresh pointer-based contexts | Authoritative rereads and independent later review; account eligibility checked when used |
| S4 | Existing constrained, supervised Codex execution/verification and repository instructions | Bounded task authority, effective permissions, honest results, stop/recovery decisions |
| S5 | Native search/existing IDE intelligence and direct official docs; repository legibility | Scope search correctly, resolve exact sources and keep caches non-authoritative |
| S6 | Available raw verification/log evidence and portable manifests/digests | Named retention/access custodian; not sole reliance on expiring service links |

**RECOMMENDATION — CONDITIONALLY SELECT.** Each row specifies the unmet prerequisite, responsible owner class and required verification. Adoption and execution authority are separate prerequisites for every row.

| ID / candidate | Unmet prerequisite | Responsible owner class | Required verification |
|---|---|---|---|
| C1 — Issue task entry | Demonstrated collaboration/assignment need and explicit sole-owner scope | Task/coordinator owner | No duplicate current status; full semantic evidence accessible despite native coarse status |
| C2 — PR transport | Authorized proposed-change workflow and exact subject/publication mapping | Integration owner | Head/base/review/integration/final identities; stale review and merge drift handling |
| C3 — protection/ruleset | Suitable private-repository plan, adopted requirements/bypass policy | Repository owner | Live configuration and separately authorized rejection tests for unauthorized/stale/failing changes |
| C4 — CODEOWNERS/reviews | Eligible independent reviewer identities and plan/config | Repository owner/review authority | Actual routing/errors, required approval, bypass/staleness and conflict-free role mapping |
| C5 — Actions/checks | Repeated deterministic verification need and adopted obligations | Verification maintainer | Exact checkout/event/workflow/run attempt; fail closed on missing/skipped required work; pinned action SHA, least privilege/budgets |
| C6 — artifact storage | Evidence size/transport need, retention and integrity requirements | Evidence custodian | Digest mismatch failure, expiry/access/deletion handling and durable manifest |
| C7 — worktree parallelism | Governance/protection permission and enforceable exclusive writers | Execution/integration owner | Workspace/ref/credential isolation, stale input, cancellation, conflicts, complete join and integrated verification |
| C8 — additional app | Task-specific data/capability need unavailable from existing sources | Task/data owner | Exact tool inventory, scopes, privacy, provenance, failure and forbidden-action behavior |
| C9 — subagents | Independently bounded slices, explicit delegation and safe ownership | Delegating task owner | Inherited ceiling, nonoverlapping mutations or read-only scope, result accounting; no self-review inference |
| C10 — structured exec | Repeated machine-consumed execution evidence need | Execution/evidence owner | Runtime/version/config capture, complete event/output retention, correct subject and error handling |
| C11 — auto-review | Adopted approval workflow with effective permitted surface | Security/runtime owner | Correct policy and rejection behavior; no replacement of independent candidate/source review |
| C12 — Codex review assistance | Actual PR review need and separate independent review contract | Review owner | Exact subject, known scope/severity limits, conflicts and independent verdict |
| C13 — Serena | Supported language/backend and measured navigation advantage | Project engineering owner | Fixed-corpus comparison, stale-index recovery, restricted tool set and workspace boundaries |
| C14 — ast-grep / IDE MCP | Structural or IDE semantic need beyond native text search | Project tooling owner | Syntax-versus-semantic fit; license/runtime/tool exposure; no unattended terminal expansion |
| C15 — publisher docs MCP | Repeated publisher-specific lookup pain | Documentation/tooling owner | Official source/version/citation coverage and failure freshness behavior |
| C16 — Context7 | Repeated multi-library lookup need and acceptable query/plan surface | Documentation/tooling owner | Correct version/upstream citations, corpus gaps, privacy, quotas and CLI-versus-MCP value |
| C17 — Playwright Test | Real browser product acceptance criteria | Test owner | Repeatability, exact build/browser/config, account/backend isolation and retained reports/traces |
| C18 — browser CLI/native surface | Actual exploratory/reproduction need | Test/task owner | Profiles/accounts/tool permissions, observed effect scope, evidence and cleanup |
| C19 — Sentry | Actual deployed runtime/incident requirement | Application operations owner | Tenant/build/event correlation, redaction, sampling, retention and cost |
| C20 — Sentry MCP | Existing Sentry access insufficient for bounded triage task | Operations/security owner | Selected transport/auth, restricted scopes/tools, mutation denial, telemetry disclosure and retrieval completeness |
| C21 — OpenTelemetry | Portable multi-component telemetry requirement | Observability owner | Exact SDK/Collector/convention support, drop/sampling/redaction, backend and retention cost |
| C22 — Temporal for an application | Independently justified durable application workflow, not ADW bootstrap coordination | Platform/runtime owner | SDK/server pins, replay/idempotency, heartbeat cancellation, termination/cleanup and external containment |

**Explicit answers to all eighteen authorized questions.** These answers are recommendations/inferences, with facts and gaps traced above; none is left implicit.

| Question | Answer |
|---|---|
| Q01 — technical enforcement versus procedural policy | Technical controls must protect effects, credentials, isolation, exclusive mutation, integration and resources where eligibility depends on prevention. Human scope/readiness/applicability/independence/impact/disposition judgments remain appropriate. Identity/evidence checks are mechanizable, but current permitted supervised work retains procedural limits (§2, §5, RG1–RG7). |
| Q02 — durable owners | Register: research current gate/dependencies/decision/evidence pointers. Task-contract owner: bounded scope/readiness/authority. One designated execution recorder: task/cancellation/recovery. Decomposition owner: product DAG. Candidate-pointer owner: exact immutable subject pointer. Verification/review/disposition owners: their separate records. Evidence custodian: access/retention (§5, S1–S2). |
| Q03 — sufficiency of GitHub plus artifacts | Yes as the initial durable evidence/control-record substrate within narrow supervised limits. No as a complete automatic enforcement system under present protection. Another mutable system is justified only for a distinct necessary domain such as real runtime incidents or later durable application execution, with explicit ownership and no duplicated ADW fields (§6, §13). |
| Q04 — task-control object | Prefer a designated repository record for initial document-heavy dogfooding; do not create it here. Use an Issue conditionally when collaboration pain justifies it and it has one authoritative product-task scope. PRs transport candidates/reviews, not every task state. Avoid simultaneously authoritative Issue/file/harness status (§6, C1–C2). |
| Q05 — exact candidate/review identity | Full commit SHA, exact path/blob/digest as relevant, frozen review metadata and explicit reviewed subject. Distinguish base/head/tested integration/final commit. New content creates new identity; reassess applicable verification/review. Native stale-approval settings assist but are not complete exact-subject conformance (§6, RG3–RG4). |
| Q06 — one writer per branch/worktree | Assign one bounded owner and use separate worktrees only after permission; technical enforcement additionally needs verified runtime/filesystem/credential fencing. Git worktree locks and CODEOWNERS do not provide it. Present serialization is procedural; parallel writes remain blocked (§10, C7, RG2). |
| Q07 — DAG/slices/joins | One decomposition owner controls graph and required/optional inputs; one integration owner accounts all current results and verifies the exact composed subject. Start with explicit records; add validation scripts/Actions only after repeated need. Scheduler dependency success alone is insufficient (§5, §10). |
| Q08 — automated rehydration | Automate read-only resolution of exact authority/config/dependency/evidence pointers into a timestamped, disposable manifest; use existing connected reads and progressive disclosure. Receiver rereads live owners before transitions. Never let generated bundles/memory write current truth (§7, D3). |
| Q09 — minimum evidence package | Contract/authority; exact input/candidate/integration identities; versions/config; actual verification outputs; independent review and separate disposition; operation/effect/cancellation observations; distinct recovery episodes; provenance, digests, retention/access and pointer handoff (§11). |
| Q10 — cancellation/recovery | Represent each accepted plane explicitly in the execution owner's record. Treat API cancel/interrupt as domain requests/evidence, observe acknowledgement and containment, reconcile residual effects, authorize operation-specific recovery, retain episodes and separately authorize terminal closure. Generic stop is blocked/none. No blind retry (§12, RG6–RG7). |
| Q11 — AFK prerequisites | Bounded ready/authorized task, fresh inputs, verified all-surface least privilege, isolation/exclusivity, hard resource ceilings, progress/evidence, tested cancellation/containment, recovery and reachable intervention with safe unavailable-human behavior. These are necessary; separate eligibility authority still absent. AFK denied (§12, RG12). |
| Q12 — current protection path | Present read-only research and separately gated serialized exact-base persistence only; procedural SHA checking is not protection. GitHub Pro is a documented private-personal protection/ruleset path, subject to adoption/configuration/effective tests. It does not provide private environment reviewer gates. Current restricted write modes stay blocked (§6, C3). |
| Q13 — OpenAI friction reduction | Projects, fresh Work/Codex tasks, GitHub-connected reads, Deep Research citations/artifacts, scoped instructions/skills and structured outputs can reduce copying. Resume/fork/memory preserve context but not current authority. Event triggers/goals/schedules are documented and deferred, not a reason to weaken rereads (§7–§8). |
| Q14 — justified MCPs | None universally required. Conditionally select publisher docs retrieval, Serena/IDE/ast-grep or Context7 for measured navigation/doc needs; browser tooling for actual UI work; Sentry MCP only beyond adequate existing runtime reads. Compare CLI/native alternatives and verify exact scopes; no installation now (§9, C13–C21). |
| Q15 — duplicate-state mechanisms | Reject independently editable Register/Issue/file/Ref Plans/harness statuses for the same fields; reject memory as owner and UI status as adoption. Derived views with source identity and distinct domain authorities are acceptable options (§13–§14, X1–X2). |
| Q16 — minimum initial stack | Git/GitHub exact evidence and current owners; proposed repository task-control representation; existing fresh OpenAI coordinator/research/reader; bounded supervised Codex; native search/direct docs; available raw results; human readiness/review/disposition/stop/recovery. No mandatory new MCP or orchestrator (§13, S1–S6). |
| Q17 — second-stage additions | First add small mechanical helpers/recipes/Actions for demonstrated repetition, then project-specific navigation/browser/telemetry, then protected isolated parallelism if authorized. SDKs/harnesses/durable engines require evidence smaller options fail. Schedules/AFK need all later controls and explicit authority (§14, §16). |
| Q18 — unsupported/partial requirements | Current protection, sole-writer fencing, exact atomic integrated publication, reviewer identity enforcement, all-surface ceilings, end-to-end cancellation/recovery, guaranteed retention and AFK are incomplete/unverified. Manual representation supports supervised semantics; required missing gates fail closed and parallel/AFK modes remain blocked (§15, RG1–RG12). |

**Producer completion check:** all 18 questions explicitly answered; all seven capability areas and mechanism classes traced; twenty evaluation criteria applied through complete profiles and candidate overrides; matrix, minimum stack, AFK denial and current protection limitation included; facts/inferences/recommendations/gaps separated; source ledger and pins supplied; design impacts isolated. This is producer completeness/serialization checking, not independent source review. No evidence result is treated as a disposition.

## 19. Source ledger

Ledger conventions: all sources were accessed **2026-09-04**, unless a more specific final-read time is stated. Every entry gives publisher/project, title and URL, version/pin where applicable, authority type, supported claims and qualifications. Rolling web pages are publication-time observations; most expose no exact revision. “Documented / lifecycle unspecified” is deliberately distinct from GA, beta, experimental and deprecated. Exact GitHub repository observations were collected through the connected GitHub app, including open-source pins; web search was not used as authority for repository state. All cited sources are primary; no load-bearing third-party article or practitioner anecdote is used.

### Repository authority and provenance

<a id="r01"></a>
**R01 — ADW / AGENTS.md.** [Exact-main file](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/AGENTS.md). Evidence date: 2026-09-04. Authority: adopted repository instructions, connected GitHub read. Blob `2294f13982045c54f3cb50071ab71373a3366c89`. Supports authority, read/write and bootstrap boundaries. Qualification: applies at this exact basis; local mirrors were not used to establish live state.

<a id="r02"></a>
**R02 — ADW / Project Charter.** [Exact-main charter](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/PROJECT-CHARTER.md). Evidence date: 2026-09-04. Authority: repository governance, connected read. Blob `c521f6869662f39106bcac0365426eb0e9bdb327`. Supports project role, bootstrap maturity and decision boundaries. Qualification: no tooling adoption is inferred from the charter.

<a id="r03"></a>
**R03 — ADW / Research Evidence Policy.** [Exact-main policy](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/policies/research-evidence.md). Evidence date: 2026-09-04. Authority: accepted normative policy, connected read. Blob `90572c47463f2d2adc493f9978c1c720fd8f8275`. Supports publication metadata, source hierarchy, historical snapshot, independent source review and adoption separation. Qualification: research evidence is nonnormative.

<a id="r04"></a>
**R04 — ADW / Research Register.** [Exact-main Register](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/research/research-register.md). Evidence date: 2026-09-04. Authority: sole repository research-state owner, connected read. Blob `1be4b5a46570be71f2354e8d2e379037270ac77b`. Supports DR-005 planned/deferred/satisfied, execution gate, unadopted Workflow v1, design/review/disposition pointers and private-plan protection restriction. Qualification: this report preserves observations only; it does not update or compete with current Register state.

<a id="r05"></a>
**R05 — ADW / ADW-DR-005-GATE-001.** [Persisted gate](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/research/ADW-DR-005-GATE-001.md). Evidence date: 2026-09-04. Authority: bounded research authorization, connected read. Blob `1c501a3fb4797ef1cdbe6a3427dcdae090bbaf14`. Supports question, scope, 18 questions, seven classes, twenty criteria, 19 sections and stop boundary. Qualification: gate's own prior-main/Register snapshot is historical after persistence; no conflict with R04's current execution gate.

<a id="r06"></a>
**R06 — ADW / accepted Workflow v1 design.** [Exact accepted subject](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md), [same file at research basis](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/design/ADW-WF1-DESIGN-001.md). Evidence date: 2026-09-04. Authority: accepted research/design input, connected reads; normative adoption absent. Subject `2b9532682ae77bf5037f1b2fa45b720e5865d0ad`; blob `afed983e7632caf3169dcbac7a80f8da8226d86d` at both refs. Supports all semantic obligations and matrix traces. Useful exact-file anchors: DD decisions [line 668](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md#L668); state/gates [line 687](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md#L687); owners [line 817](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md#L817); conformance [line 1100](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md#L1100). Qualification: accepted semantics are evaluated, not redesigned or normatively adopted here.

<a id="r07"></a>
**R07 — ADW / controlling review-004.** [Exact-main review](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/design/ADW-WF1-DESIGN-REVIEW-004.md). Evidence date: 2026-09-04. Authority: independent design-review evidence, connected read. Blob `3cdb92769bb955c8782dfa504843fd32a4736168`. Supports accepted subject/parent/path/blob/byte/digest binding, verdict and zero findings. Qualification: review's digest is recorded evidence, not newly recomputed in this research; review does not adopt tooling.

<a id="r08"></a>
**R08 — ADW / design disposition-001.** [Exact-main disposition](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/design/ADW-WF1-DESIGN-DISPOSITION-001.md). Evidence date: 2026-09-04. Authority: coordinator design disposition, connected read. Blob `35d3a8ba5c3901e90d070b000659541b1ef4975c`. Supports acceptance of exact initial tool-agnostic design and review binding. Qualification: `normative_effect: none`; no implementation/write/AFK authorization.

<a id="r09"></a>
**R09 — GitHub / live ADW state observations.** [Main branch](https://api.github.com/repos/ahtoxaandy999/agentic-development-workflow/branches/main), [exact commit](https://github.com/ahtoxaandy999/agentic-development-workflow/commit/7adc4d9866ff7d6fda8eeb63087ade300f4d7977), [complete tree](https://api.github.com/repos/ahtoxaandy999/agentic-development-workflow/git/trees/d0f85826b29966e02b4b61c87b873aeb465785f0?recursive=1), [refs](https://api.github.com/repos/ahtoxaandy999/agentic-development-workflow/git/refs), [all PRs](https://api.github.com/repos/ahtoxaandy999/agentic-development-workflow/pulls?state=all&per_page=100), [all Issues](https://api.github.com/repos/ahtoxaandy999/agentic-development-workflow/issues?state=all&per_page=100), [README](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/README.md). Evidence date: 2026-09-04; final read time in §2. Authority: live connected GitHub GET responses. Supports initial/final SHA, unprotected branch, complete accessible competing-state checks and navigation consistency. README blob `d4148f08e629ce4a6373552607bddb6ad2de0d28`. Qualification: branch/collection URLs are mutable; the recorded observations are the snapshot. Does not inspect unseen local work, billing or inaccessible settings.

### OpenAI first-party capability sources

<a id="o01"></a>
**O01 — OpenAI / Projects.** [Documentation](https://learn.chatgpt.com/docs/projects). Evidence date: 2026-09-04. Authority: first-party product documentation; rolling/unversioned, lifecycle unspecified. Supports shared instructions/files/context and separate conversations. Qualification: project context does not prove live repository state; surface/account differences apply.

<a id="o02"></a>
**O02 — OpenAI / Get started with Work.** [Documentation](https://learn.chatgpt.com/docs/get-started-with-work). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports task/artifact experience and local/cloud availability where offered. Qualification: eligibility and runtime choice vary; cloud continuation is not ADW authority.

<a id="o03"></a>
**O03 — OpenAI / Deep research in ChatGPT.** [Help article](https://help.openai.com/en/articles/10500283-deep-research). Evidence date: 2026-09-04. Authority: first-party product documentation; rolling, lifecycle unspecified. Supports source restriction, research plan/steering, citations/exports, read-only app use in this mode. Qualification: plan/region/app access and chat retention apply; generated citations require independent source review before disposition.

<a id="o04"></a>
**O04 — OpenAI / Connecting GitHub to ChatGPT.** [Help article](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports allowed-content retrieval, account/surface differences and eligible Work GitHub event triggers. Qualification: github.com support does not imply self-hosted Enterprise support; retrieval/index behavior does not replace exact reads; connector/tool permissions are task-specific.

<a id="o05"></a>
**O05 — OpenAI / Plugins.** [Documentation](https://learn.chatgpt.com/docs/plugins). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports bundles of skills/connectors/MCP/hooks and explicit invocation. Qualification: installation/authentication and exposed permissions are separate concerns; no plugin installed in this task.

<a id="o06"></a>
**O06 — OpenAI / AGENTS.md.** [Documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports scoped instruction discovery, precedence and size limits. Qualification: instructions are model guidance, not an OS/credential enforcement boundary.

<a id="o07"></a>
**O07 — OpenAI / Build skills.** [Documentation](https://learn.chatgpt.com/docs/build-skills). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports progressive disclosure and instruction/resource reuse. Qualification: scope/duplicate-name behavior needs exact configuration; a skill is not an authoritative mutable task store or permission grant.

<a id="o08"></a>
**O08 — OpenAI / Git worktrees.** [Documentation](https://learn.chatgpt.com/docs/environments/git-worktrees). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports app worktree/detached-head and handoff behavior. Qualification: starting state can depend on chosen local changes; exact base/cleanliness must be observed, not assumed.

<a id="o09"></a>
**O09 — OpenAI / Permissions.** [Documentation](https://learn.chatgpt.com/docs/permissions). Evidence date: 2026-09-04. Authority: first-party documentation; **beta**. Supports permission profiles, configuration precedence/managed constraints and proxy-dependent network filtering. Qualification: separate tool surfaces have separate controls; requested configuration is not proof of effective coverage.

<a id="o10"></a>
**O10 — OpenAI / Sandboxing.** [Documentation](https://learn.chatgpt.com/docs/sandboxing). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports OS-level command restrictions and inherited subprocess limits in covered execution. Qualification: does not establish containment of remote actions or all connector/browser/cloud effects.

<a id="o11"></a>
**O11 — OpenAI / Auto-review.** [Documentation](https://learn.chatgpt.com/docs/sandboxing/auto-review). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports assessment of approval requests under policy. Qualification: does not add permissions and is not candidate/source-review independence or disposition.

<a id="o12"></a>
**O12 — OpenAI / Hooks.** [Documentation](https://learn.chatgpt.com/docs/hooks). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, general lifecycle label unspecified. Supports pre/post/interrupt and other hook behavior, concurrent matching hooks and coverage limitations. Qualification: local tool interception has exceptions; hook names/results are not equivalent to global stop/containment. No runtime test here.

<a id="o13"></a>
**O13 — OpenAI / Subagents.** [Documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports bounded delegation/context summaries and inherited policy behavior. Qualification: documentation does not establish exclusive worktree ownership or conflict-free independent review merely from a separate agent/context.

<a id="o14"></a>
**O14 — OpenAI / Non-interactive mode.** [Documentation](https://learn.chatgpt.com/docs/non-interactive-mode). Evidence date: 2026-09-04. Authority: first-party documentation; rolling. Supports JSONL events, structured final output and read-only default. **Deprecated:** `--full-auto`. Qualification: output shape/exit status cannot prove workflow semantics or retain evidence without storage.

<a id="o15"></a>
**O15 — OpenAI / Codex SDK.** [Documentation](https://learn.chatgpt.com/docs/codex-sdk). Evidence date: 2026-09-04. Authority: first-party documentation; rolling. Supports programmatic task/thread execution; **deprecated:** `codex mcp-server`. Qualification: TypeScript/Python/runtime combinations need exact package pins at implementation; no installed SDK was audited.

<a id="o16"></a>
**O16 — OpenAI / App server.** [Documentation](https://learn.chatgpt.com/docs/app-server). Evidence date: 2026-09-04. Authority: first-party documentation; rolling. Supports thread start/resume/fork, events, review and interruption request/completion distinction. Qualification/uncertainty: stable nonexperimental API language coexists with experimental app-server/WebSocket language in remote-host context; process-spawn/cleanup surfaces have experimental or unsandboxed qualifications. Do not generalize production readiness across transports.

<a id="o17"></a>
**O17 — OpenAI / Automations.** [Documentation](https://learn.chatgpt.com/docs/automations). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports local/cloud recurring execution, existing-context versus standalone work distinctions. Qualification: availability, awake/runtime and approval conditions vary; no AFK eligibility established.

<a id="o18"></a>
**O18 — OpenAI / Long-running work.** [Documentation](https://learn.chatgpt.com/docs/long-running-work). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports persistent goals and continuation under existing constraints. Qualification: a retained objective does not establish fresh authorization, isolation or recovery; no goal/automation created here.

<a id="o19"></a>
**O19 — OpenAI / Memories.** [Documentation](https://learn.chatgpt.com/docs/customization/memories). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports asynchronous memory/context behavior and distinction from repository instructions. Qualification: generated/stale memory cannot serve as live owner evidence; ChatGPT and local surfaces differ.

<a id="o20"></a>
**O20 — OpenAI / GitHub integration and code review.** [Documentation](https://learn.chatgpt.com/docs/third-party/github). Evidence date: 2026-09-04. Authority: first-party documentation; rolling. Supports PR review assistance and scoped review guidance. Qualification: default defect-review scope is not all ADW review obligations; separate Security Review described as **research preview**. No review executed against this report.

<a id="o21"></a>
**O21 — OpenAI / Changelog.** [Changelog](https://learn.chatgpt.com/docs/changelog). Evidence date: 2026-09-04. Authority: first-party release documentation; entries through CLI 0.153.2 (2026-09-03). Supports recent runtime changes and experimental context-management/account qualifications. Qualification: changelog recency does not prove installed version or effective control; exact release identity in O28.

<a id="o22"></a>
**O22 — OpenAI / Docs MCP.** [Documentation](https://learn.chatgpt.com/learn/docs-mcp). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports read-only documentation retrieval rather than API execution. Qualification: OpenAI corpus scope; direct web documentation is smaller when lookup frequency is low.

<a id="o23"></a>
**O23 — OpenAI / Browser.** [Documentation](https://learn.chatgpt.com/docs/browser). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, lifecycle unspecified. Supports browser interaction/snapshots/screenshots and separate browser controls. Qualification: UI exploration is not repeatable acceptance evidence by itself; account/network/application effects require their own boundary.

<a id="o24"></a>
**O24 — OpenAI / Feature maturity.** [Documentation](https://learn.chatgpt.com/docs/feature-maturity). Evidence date: 2026-09-04. Authority: first-party maturity definitions; rolling. Supports distinctions among stable, beta and experimental. Qualification: absence of a feature-specific label is not proof of GA; this ledger retains unspecified states.

<a id="o25"></a>
**O25 — OpenAI / Agent approvals and security.** [Documentation](https://learn.chatgpt.com/docs/agent-approvals-security). Evidence date: 2026-09-04. Authority: first-party documentation; rolling, feature/model-specific. Supports supplementary approval/security monitoring and sandbox distinction. Qualification: reactive monitoring is not complete prevention or independent candidate review; no model/security capability was operationally tested.

<a id="o26"></a>
**O26 — OpenAI / Harness engineering: leveraging Codex in an agent-first world.** [Case study](https://openai.com/index/harness-engineering/). Evidence date: 2026-09-04; published 2026-02-11. Authority: first-party operational case study. Supports repository legibility, mechanical invariants and environment-specific harness practices. Qualification: one internal beta experiment; permissive merge/throughput choices cannot override ADW or prove general effectiveness.

<a id="o27"></a>
**O27 — OpenAI / Open-source Codex orchestration with Symphony.** [Publication](https://openai.com/index/open-source-codex-orchestration-symphony/). Evidence date: 2026-09-04; published 2026-04-27. Authority: first-party reference-pattern announcement. Supports Symphony's role as orchestration reference rather than a standalone maintained product commitment. Qualification: current pinned specification O29 is more precise than announcement-era tracker scope; vendor results are not an ADW benchmark.

<a id="o28"></a>
**O28 — OpenAI / Codex release identity.** [Release rust-v0.153.2](https://github.com/openai/codex/releases/tag/rust-v0.153.2), [release commit](https://github.com/openai/codex/commit/657a993cbee87acf52d14b758ce49dbd46d1b8eb). Evidence date: 2026-09-04. Authority: connected GitHub release/tag reads. Published 2026-09-03 23:53:12 UTC; `prerelease=false`. Annotated tag object `79016fcca2c514d9c38643d8b7970a021e829b3b` resolves to commit `657a993cbee87acf52d14b758ce49dbd46d1b8eb`. Qualification: upstream release pin, not installed client/package version or operational certification.

<a id="o29"></a>
**O29 — OpenAI / Symphony pinned reference and specification.** [README](https://github.com/openai/symphony/blob/8001b52e3062495a16e520e4ceaf8f9de868c4d0/README.md), [SPEC.md](https://github.com/openai/symphony/blob/8001b52e3062495a16e520e4ceaf8f9de868c4d0/SPEC.md). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Commit `8001b52e3062495a16e520e4ceaf8f9de868c4d0`; README blob `e0f24a048407bb6a9524d6560c2e0070a392a4ce`; spec blob `cd24131a1e2358cbfecc4f6efb028fc9fc6edefc`. Maturity: **engineering preview**, draft-v1 specification. Supports dispatch/concurrency/reconstruction, retry/stale-refresh/cleanup behavior. Qualification: specification/reference is not proof of ADW semantics, multi-instance fencing or an installed runtime.

### GitHub and Git controls

<a id="g01"></a>
**G01 — GitHub / Protected branches and rulesets.** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports Pro private-repository path, configured requirements and bypass/active enforcement. Qualification: plan availability is not current account entitlement or effective target configuration.

<a id="g02"></a>
**G02 — GitHub / Managing a merge queue.** [Documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports organization/public or Enterprise Cloud private eligibility and integration queue behavior. Qualification: not a private-personal repository option; no organization migration justified here.

<a id="g03"></a>
**G03 — GitHub / Merge a pull request REST API.** [API reference](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request). Evidence date: 2026-09-04. Authority: official API reference, examples version 2026-03-10. Supports expected head `sha`, mismatch rejection and returned merge SHA. Qualification: documented request lacks expected-base parameter; no atomic base-guard guarantee inferred.

<a id="g04"></a>
**G04 — GitHub / Troubleshooting required status checks.** [Documentation](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports head/test-merge subjects and success/skipped/neutral acceptance. Qualification: mergeability is weaker than ADW's actual successful required integrated verification; skipped dependencies may not block.

<a id="g05"></a>
**G05 — GitHub / Events that trigger workflows.** [Documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports PR test-merge SHA, head SHA distinction, merge_group and workflow_dispatch identity. Qualification: requested ref, event SHA, workflow revision and actual checkout must be recorded separately.

<a id="g06"></a>
**G06 — GitHub / Pull request merges.** [Documentation](https://docs.github.com/en/pull-requests/reference/pull-request-merges). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports merge/squash/rebase identity changes. Qualification: identical content does not imply identical commit identity or review provenance.

<a id="g07"></a>
**G07 — GitHub / Commit statuses and check runs.** [Statuses](https://docs.github.com/en/rest/commits/statuses), [check runs](https://docs.github.com/en/rest/checks/runs). Evidence date: 2026-09-04. Authority: official API documentation, current examples 2026-03-10. Supports distinct evidence objects, SHA/producer/conclusion/run metadata. Qualification: combined status is not exhaustive check-run history; pagination and attempts matter.

<a id="g08"></a>
**G08 — GitHub / Pull request reviews API.** [Reference](https://docs.github.com/en/rest/pulls/reviews). Evidence date: 2026-09-04. Authority: official rolling API documentation. Supports review `commit_id`, actor/state/time and ID binding. Qualification: default latest-commit behavior and mutable/dismissible review presentation require publication-time capture; review is not disposition.

<a id="g09"></a>
**G09 — GitHub / About code owners.** [Documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports base-branch CODEOWNERS, required-review configuration, owner eligibility and any-one matching approval behavior. Qualification: invalid entries/permissions matter; routing is not writer isolation.

<a id="g10"></a>
**G10 — GitHub / Reviewing proposed changes.** [Documentation](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports author self-approval prohibition and configuration-dependent request-changes/stale-review behavior. Qualification: solo account/model-context separation does not establish an eligible independent platform reviewer.

<a id="g11"></a>
**G11 — Git project / git-worktree.** [Manual](https://git-scm.com/docs/git-worktree). Evidence date: 2026-09-04. Authority: official Git manual; page last updated for 2.54.0 on 2026-04-20, unchanged in listed 2.55.0. Supports separate worktree files/HEAD/index, shared refs/config and administrative lock behavior. Qualification: lock does not prevent edits; duplicate-checkout safeguards can be overridden; installed Git not inspected.

<a id="g12"></a>
**G12 — Git project / update-ref and revisions.** [update-ref](https://git-scm.com/docs/git-update-ref), [gitrevisions](https://git-scm.com/docs/gitrevisions). Evidence date: 2026-09-04. Authority: official rolling manuals. Supports full object IDs and expected-old-ID/local ref transactions. Qualification: local ref atomicity is not remote integration, filesystem ownership, review or external-effect containment.

<a id="g13"></a>
**G13 — GitHub / Workflow cancellation.** [Reference](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports job-condition reevaluation, potentially continuing always jobs and runner termination sequence. Qualification: process-tree termination cannot establish external-effect rollback or ADW terminal accounting.

<a id="g14"></a>
**G14 — GitHub / Workflow concurrency.** [Documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency), [limits](https://docs.github.com/en/actions/reference/limits). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle/update label unspecified. Supports default single pending replacement and queue:max up to 100 pending members. Qualification: explicit cancel-in-progress/property rules govern; loose explanatory prose is not a global lock or universal automatic-cancellation guarantee.

<a id="g15"></a>
**G15 — GitHub / Artifact storage, retention and deletion.** [Store/share data](https://docs.github.com/en/actions/tutorials/store-and-share-data), [Actions settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository), [artifact removal](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/remove-workflow-artifacts). Evidence date: 2026-09-04. Authority: official rolling documentation; tutorial v4 artifact model. Supports immutable uploaded artifacts, SHA-256 digest, warning on mismatch, configurable retention and deletion. Qualification: retention can expire or evidence be deleted; tutorial major version is not a chosen action commit pin.

<a id="g16"></a>
**G16 — GitHub / Managing environments.** [Documentation](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports private environment availability and public-only required reviewers/wait timers on Free/Pro/Team. Qualification: deployment/job state does not establish ADW acceptance or residual-effect handling.

<a id="g17"></a>
**G17 — GitHub / Actions limits and secure use.** [Limits](https://docs.github.com/en/actions/reference/limits), [secure use](https://docs.github.com/en/actions/reference/security/secure-use). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports quotas/timeouts and full-commit action pinning. Qualification: actual account allowance/billing not checked; quotas are not a complete task budget or permission boundary.

<a id="g18"></a>
**G18 — GitHub / Issues and PR reviews.** [Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues), [PR reviews](https://docs.github.com/en/pull-requests/reference/pull-request-reviews). Evidence date: 2026-09-04. Authority: official rolling documentation; lifecycle unspecified. Supports task discussion/assignment/dependencies and change-review surfaces. Qualification: native status/closure cannot encode or prove all orthogonal ADW planes.

<a id="g19"></a>
**G19 — just project / release and README.** [1.58.0 release](https://github.com/casey/just/releases/tag/1.58.0), [pinned README](https://github.com/casey/just/blob/7f4ef81bd6a93faa2b28430912c8e9ab0e3dd29a/README.md). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Released 2026-08-03 20:31:31 UTC, non-prerelease; annotated tag `ebedee5bafe1ce779e93d91a2eff0c1bf3687b9c` resolves to `7f4ef81bd6a93faa2b28430912c8e9ab0e3dd29a`. Supports command recipes/discovery and static recipe validation. Qualification: command runner, not durable workflow state/recovery; release metadata not immutable-release certification.

<a id="g20"></a>
**G20 — Task project / release and guide.** [v3.53.1 release](https://github.com/go-task/task/releases/tag/v3.53.1), [pinned guide](https://github.com/go-task/task/blob/ff3372fc50a47348610d722616f1a073aace0513/website/src/latest/docs/guide.md). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Released 2026-08-18 15:41:59 UTC, non-prerelease; annotated tag `a10322cd63f94d8bc8b48bb5c0e80eec10eda1e7` resolves to `ff3372fc50a47348610d722616f1a073aace0513`. Supports parallel deps, cache/skip/precondition/force behavior and command timeouts; remote Taskfiles declared **GA** in release. Qualification: runner freshness/exit zero is not authoritative integrated verification; remote-file integrity needs exact-version checking.

### External navigation, browser, runtime and orchestration sources

<a id="e301"></a>
**E301 — OraiOS / Serena.** [Pinned README](https://github.com/oraios/serena/blob/801a388c2b7a6a8998f313291678b1609664e794/README.md), [v1.7.0 release](https://github.com/oraios/serena/releases/tag/v1.7.0). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Commit `801a388c2b7a6a8998f313291678b1609664e794` (2026-09-03); release v1.7.0 (2026-08-09), non-prerelease. Supports LSP/JetBrains symbol tools, optional memory and redundant-tool configuration. Qualification: paid backend/language support varies; publisher evaluations are not independent target-project benchmarks; HEAD/release parity unverified.

<a id="e302"></a>
**E302 — BurntSushi / ripgrep.** [Pinned README](https://github.com/BurntSushi/ripgrep/blob/3fce3b5bb0236da2df6d99672afb8a719642eca7/README.md). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Commit `3fce3b5bb0236da2df6d99672afb8a719642eca7` (2026-08-04). Supports recursive regex search and default ignore/hidden/binary filtering, portable local use. Qualification: text search is not semantic-reference completeness; installed binary version not audited; lifecycle label not asserted from HEAD.

<a id="e303"></a>
**E303 — ast-grep project / structural search.** [Pinned README](https://github.com/ast-grep/ast-grep/blob/29285d16757371a70a93190929940886e68618d3/README.md). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Commit `29285d16757371a70a93190929940886e68618d3` (2026-08-31). Supports tree-sitter syntax search/lint/rewrite. Qualification: syntax patterns do not establish language-server type/cross-file reference semantics; no deployment version chosen.

<a id="e304"></a>
**E304 — JetBrains / IntelliJ IDEA MCP Server.** [2026.2 Help](https://www.jetbrains.com/help/idea/mcp-server.html). Evidence date: 2026-09-04; page date 2026-05-13. Authority: first-party versioned product help. Supports bundled server since 2025.2, symbol/refactoring capabilities and tool controls. Qualification: IDE/language/license dependencies; router-only does not remove routed capabilities; optional permissive terminal behavior is not recommended. Lifecycle beyond bundled availability unspecified.

<a id="e305"></a>
**E305 — Upstash / Context7.** [Pinned README](https://github.com/upstash/context7/blob/6d777619c2777a79ad0754dc48b48845cb912bac/README.md), [MCP 4.0.4 release](https://github.com/upstash/context7/releases/tag/%40upstash/context7-mcp%404.0.4). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Commit `6d777619c2777a79ad0754dc48b48845cb912bac` (2026-09-02); MCP release 4.0.4 (2026-08-28). Supports CLI + Skills/MCP, library/version lookup and private-backend/community-corpus qualifications. Parent spot-check README blob `aa34be9ba8eb98b5edc8dc8b9088a513275356ce`. Qualification: advertised current/version-specific retrieval does not prove each answer's accuracy; HEAD/release parity and installed configuration unverified.

<a id="e306"></a>
**E306 — Upstash / Context7 plans.** [Service plans](https://context7.com/plans). Evidence date: 2026-09-04. Authority: first-party live service/pricing page; unversioned, lifecycle unspecified. Supports free/paid quota, overage and query-disclosure considerations. Qualification: unlimited-use wording includes paid overage, not unlimited included calls; model instructions to omit sensitive data are not technical exfiltration prevention. Prices/terms must be rechecked before procurement.

<a id="e307"></a>
**E307 — Microsoft / Learn MCP overview.** [Documentation](https://learn.microsoft.com/en-us/training/support/mcp). Evidence date: 2026-09-04; updated 2026-05-22. Authority: first-party documentation. Supports official-docs search/full article/code samples, no-auth/no-charge public access, incremental/daily refresh. Qualification: Microsoft-only corpus; refresh is not immutable publication identity; lifecycle label beyond public availability unspecified.

<a id="e308"></a>
**E308 — Ref / Context, Plans, pricing and roles.** [Product docs](https://docs.ref.tools/), [pricing](https://docs.ref.tools/usage/pricing), [team roles](https://docs.ref.tools/usage/teams). Evidence date: 2026-09-04. Authority: first-party live service documentation; unversioned, lifecycle unspecified. Supports public/private documentation retrieval, additional plan-state surface, billing/role considerations. Qualification: Context index roles differ from Plans write capabilities; no reproducible backend pin; another shared plan owner is incompatible with the proposed ADW ownership model.

<a id="e309"></a>
**E309 — Microsoft / Playwright coding agents, CLI and MCP.** [Official guidance](https://playwright.dev/docs/getting-started-cli), [MCP README](https://github.com/microsoft/playwright-mcp/blob/8a13ef8e9f7385a0f89477922127f31cbfde9761/README.md), [CLI README](https://github.com/microsoft/playwright-cli/blob/655530f6d0dc71a0d6bf46ae165877d3c7311099/README.md). Evidence date: 2026-09-04. Authority: official documentation and canonical connected GitHub reads. MCP pin `8a13ef8e9f7385a0f89477922127f31cbfde9761`; CLI pin `655530f6d0dc71a0d6bf46ae165877d3c7311099` (2026-09-03). Releases [MCP v0.0.80](https://github.com/microsoft/playwright-mcp/releases/tag/v0.0.80) and [CLI v0.1.19](https://github.com/microsoft/playwright-cli/releases/tag/v0.1.19), 2026-09-01. Supports CLI-versus-persistent-MCP guidance and explicit security-boundary disclaimer, including redirect limitation. Parent spot-check MCP README blob `ddea67cd5145a2316cec75535edb1133062ecf61`. Qualification: token-efficiency guidance not an ADW measurement; isolate browser state; HEAD/release parity and lifecycle certification unasserted.

<a id="e310"></a>
**E310 — Microsoft / Playwright authentication and core version.** [Authentication docs](https://playwright.dev/docs/auth), [core commit](https://github.com/microsoft/playwright/commit/d1dcd6bc0a138ec0fd943df19e07458dc426ee22), [v1.62.1 release](https://github.com/microsoft/playwright/releases/tag/v1.62.1). Evidence date: 2026-09-04. Authority: first-party docs and canonical connected GitHub reads. Core pin `d1dcd6bc0a138ec0fd943df19e07458dc426ee22` (2026-09-03); release v1.62.1 (2026-07-30). Supports isolated contexts, sensitive stored authentication and separate accounts for parallel server-state mutation. Qualification: context isolation does not isolate shared backend data; exact selected browser/runtime versions need later capture.

<a id="e311"></a>
**E311 — Microsoft / Playwright reporters.** [Documentation](https://playwright.dev/docs/test-reporters). Evidence date: 2026-09-04. Authority: first-party rolling documentation; core evidence pin in E310. Supports HTML/JSON/JUnit/blob and custom result formats. Qualification: reports are evidence transport, not proof of criteria sufficiency, repeatability or complete application behavior.

<a id="e312"></a>
**E312 — Sentry / MCP root and service.** [Pinned README](https://github.com/getsentry/sentry-mcp/blob/ea767b707ebdcc2fc90f177d887942752ff01e5f/README.md), [deployed service](https://mcp.sentry.dev/). Evidence date: 2026-09-04. Authority: canonical connected GitHub and first-party service documentation. Pin `ea767b707ebdcc2fc90f177d887942752ff01e5f` (2026-09-04). Supports debugging/triage, org/project scope and transport differences. Qualification: deployed OAuth-only wording versus root upstream-token support is unresolved transport-specific documentation ambiguity; stdio described as work in progress, experimental features opt-in.

<a id="e313"></a>
**E313 — Sentry / MCP core package.** [Pinned core README](https://github.com/getsentry/sentry-mcp/blob/ea767b707ebdcc2fc90f177d887942752ff01e5f/packages/mcp-core/README.md). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub, same exact pin as E312. Supports default inspect/Seer/triage/project-management surfaces, narrow read versus mutation scopes, capability controls and telemetry. Qualification: old scope flags deprecated; package calls itself a prototype while remote service is described differently; actual transport/tool inventory/credentials must be verified.

<a id="e314"></a>
**E314 — Sentry / Pricing.** [Service pricing](https://sentry.io/pricing/). Evidence date: 2026-09-04. Authority: first-party live page; unversioned. Supports free Developer/MCP access and paid runtime usage/add-on cost surface. Qualification: billing toggle context was not fully resolved by text extraction; this report gives no procurement quote. Plan inclusion does not establish appropriate data permissions.

<a id="e315"></a>
**E315 — OpenTelemetry project / scope and specification.** [What is OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/), [specification commit](https://github.com/open-telemetry/opentelemetry-specification/commit/238e0e201c71d8e92a3e08202c9a02f2517dec52). Evidence date: 2026-09-04. Authority: official project docs and connected GitHub pin `238e0e201c71d8e92a3e08202c9a02f2517dec52` (2026-09-03). Supports portable signal generation/collection/export, not storage/visualization. Qualification: maturity varies by signal/SDK/Collector/convention; no GenAI convention or application component version selected.

<a id="e316"></a>
**E316 — LangChain / LangGraph.** [Pinned README](https://github.com/langchain-ai/langgraph/blob/81bf17b23123e4ef8b9d5f49fa09a0122fc2edd1/README.md), [core 1.2.11 release](https://github.com/langchain-ai/langgraph/releases/tag/1.2.11). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Pin `81bf17b23123e4ef8b9d5f49fa09a0122fc2edd1` (2026-09-03); core release 1.2.11 (2026-08-11). Supports low-level stateful orchestration. Qualification: repository latest-release surface may refer to SDK 0.4.4, not core; core/SDK/version maturity must not be conflated.

<a id="e317"></a>
**E317 — LangChain / LangGraph persistence and checkpointers.** [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence), [checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers). Evidence date: 2026-09-04. Authority: first-party rolling Python docs. Supports checkpoint durability options, RAM-store loss and replay of subsequent nodes/API calls. Qualification: checkpointing does not guarantee external-effect deduplication; exact store/runtime configuration is essential.

<a id="e318"></a>
**E318 — LangChain / LangGraph interrupts.** [JavaScript docs](https://docs.langchain.com/oss/javascript/langgraph/interrupts). Evidence date: 2026-09-04. Authority: first-party rolling documentation. Supports checkpoint/thread requirements and node restart on resume, including repeated pre-interrupt code. Qualification: input pause is not containment; language/runtime-specific implementation must be pinned before use.

<a id="e319"></a>
**E319 — LangChain / Cancel a run.** [LangSmith documentation](https://docs.langchain.com/langsmith/cancel-run). Evidence date: 2026-09-04. Authority: first-party rolling **LangSmith Deployment/Agent Server** API docs. Supports asynchronous request, wait/join, interrupt retention and rollback deletion of runs/checkpoints. Qualification: hosted semantics are not all standalone LangGraph behavior; rollback does not document reversal of external effects, and evidence deletion conflicts with reliance unless preserved elsewhere.

<a id="e320"></a>
**E320 — Temporal / server and cancellation semantics.** [Pinned server README](https://github.com/temporalio/temporal/blob/2220587dea828d938fc99253e178a13d1cb658c5/README.md), [v1.31.2 release](https://github.com/temporalio/temporal/releases/tag/v1.31.2), [Python cancellation](https://docs.temporal.io/develop/python/workflows/cancellation). Evidence date: 2026-09-04. Authority: canonical connected GitHub plus official docs. Server pin `2220587dea828d938fc99253e178a13d1cb658c5` (2026-09-04); release v1.31.2 (2026-07-08). Supports cooperative request/events, regular Activity heartbeat cancellation, termination without workflow cleanup and reset identity. Qualification: server pin is not Python SDK pin; external exactly-once effects/process containment not established.

<a id="e321"></a>
**E321 — Temporal / Pricing.** [Service pricing](https://temporal.io/pricing). Evidence date: 2026-09-04. Authority: first-party live page; unversioned. Supports Cloud subscription/usage and self-hosting tradeoff. Qualification: worker/model infrastructure extra; self-hosting still needs service operations. No current account contract or procurement decision examined.

<a id="e322"></a>
**E322 — OpenHands / Agent Canvas.** [Pinned root README](https://github.com/OpenHands/OpenHands/blob/4524a919930d62535a5cdca143c8a54eaf0ede42/README.md). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Pin `4524a919930d62535a5cdca143c8a54eaf0ede42` (2026-09-03). Maturity: **beta**. Supports current Agent Canvas identity, broad local/remote/cloud backend and automation surface. Qualification: older monolithic-harness descriptions are stale; unsandboxed operation is not a suitable authority boundary.

<a id="e323"></a>
**E323 — OpenHands / Software Agent SDK.** [Pinned README](https://github.com/OpenHands/software-agent-sdk/blob/07307cb8edfcd9b4675be2761df0646d075a9c36/README.md), [v1.44.1 release](https://github.com/OpenHands/software-agent-sdk/releases/tag/v1.44.1). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Pin `07307cb8edfcd9b4675be2761df0646d075a9c36` (2026-09-03); release v1.44.1 (2026-08-28). Supports composable SDK/server and local/ephemeral workspaces. Qualification: separate from Canvas lifecycle; HEAD/release parity and installed container isolation unverified.

<a id="e324"></a>
**E324 — OpenHands / Security and action confirmation.** [Documentation](https://docs.openhands.dev/sdk/guides/security). Evidence date: 2026-09-04. Authority: first-party rolling SDK docs. Supports configurable confirmation/analyzers and explicit limitations. Qualification: direct execute_tool bypasses conversation checks; analyzer configuration is not hard-deny or sandbox replacement. Parent independently checked the relevant documentation passage.

<a id="e325"></a>
**E325 — OpenHands / Persistence and pause/resume.** [Persistence](https://docs.openhands.dev/sdk/guides/convo-persistence), [pause/resume](https://docs.openhands.dev/sdk/guides/convo-pause-and-resume). Evidence date: 2026-09-04. Authority: first-party rolling SDK docs. Supports persisted state/events and pause followed by thread join. Qualification: persisted state may include sensitive configuration/secrets; bounded stop latency and complete external containment not established.

<a id="e326"></a>
**E326 — LangChain / Deep Agents and smaller loop alternative.** [Pinned README](https://github.com/langchain-ai/deepagents/blob/afff4f8841bcc370d01c2739f53e882a92ef5c6a/README.md), [0.7.13 release](https://github.com/langchain-ai/deepagents/releases/tag/deepagents%3D%3D0.7.13). Evidence date: 2026-09-04. Authority: canonical repository via connected GitHub. Pin `afff4f8841bcc370d01c2739f53e882a92ef5c6a` (2026-09-04); release 0.7.13 (2026-09-02). Supports planning/filesystem/delegation/memory harness and lighter create_agent alternative. Qualification: tool/sandbox boundaries remain external obligations; publisher production claims are not ADW assurance.

### Contradictions, uncertainty and publication limits

| Evidence tension | Treatment in this snapshot |
|---|---|
| Gate's historical planned/deferred/unsatisfied research-gate state versus current Register execution/satisfied state | Resolved by explicit publication scope and persisted gate/Register at exact main. R04 owns current research state; R05's prior state remains historical. |
| GitHub accepted check conclusions versus ADW required integrated success | Different contracts, not contradictory facts. GitHub mergeability is not adopted as complete ADW conformance. |
| Older one-pending Actions model versus current queue:max | Current explicit G14 property rules take precedence for capability assessment; no stale third-party override used. |
| App-server stable API wording versus experimental remote/transport/process qualifications | Unresolved for a generic production-readiness claim. Report narrows to documented APIs and defers a custom client pending exact surface/version verification (O16, RG11). |
| Sentry OAuth-only service wording versus upstream-token support; remote service versus prototype/stdio maturity | Preserve transport/package distinctions and unresolved deployment applicability. Verify the chosen transport/tool scopes before selection (E312–E313, RG11). |
| Context7 accuracy/currentness marketing versus community/private-backend limitations | Retrieval is documented; result correctness/version completeness remains to verify. No claim of authoritative or reproducible corpus completeness (E305–E306). |
| Symphony announcement-era scope versus current generalized tracker specification | Current pinned specification controls evaluated behavior; no unsupported claim of a particular adapter's release availability (O27/O29). |
| OpenHands root repository versus older harness identity | Current pinned root is Agent Canvas beta; SDK is assessed separately. No older product description overrides current primary evidence (E322–E325). |
| OSS HEAD pin and named release date differ | Both are retained as different evidence identities; feature parity is not assumed. Later deployment must pin its actual components/configuration. |

**Evidence quality statement.** Every load-bearing capability conclusion has first-party documentation or canonical repository support, with unavailable assurance recorded as a gap. Source IDs map claims to exact evidence; repository authority uses exact full SHAs and blobs. There are no unqualified claims that documentation proves effective enforcement. Current web pages were read during this session and material claims were spot-checked; they remain rolling sources rather than archived immutable vendor publications. This report preserves their observed content in bounded paraphrase, date, scope and qualifications. A later reviewer should reread unstable sources and report changes instead of silently refreshing this report.

**Final freshness check:** connected GitHub branch/commit/refs/all-state PR/all-state Issue reads and all eight required exact-basis file rereads matched the initial authority assessment; completed 2026-09-04 06:15:44 UTC. The only Issue still explicitly excludes Workflow v1/tooling adoption and has zero comments. Material first-party claims were rechecked near finalization: permission profiles remain beta (O09); Pro supports private branch protection (G01); Free/Pro/Team environment required-reviewer/wait-timer restrictions remain public-only (G16); Playwright's CLI-versus-MCP guidance is unchanged (E309). Earlier focused rereads also checked app-server/hook limitations, Deep Research/GitHub access, and Symphony reference status. No material contradiction requiring a research stop emerged. These are evidence-date observations, not a promise that future-current state will match.

**Publication boundary.** This is a complete local evidence artifact awaiting separately authorized persistence and freeze. Research completion does not update the Register. No GitHub write, Register update, independent self source-review, tooling disposition, installation, implementation, Workflow v1 adoption, protection change, or write/AFK authority occurred. The requested local file creation and producer coverage/serialization checks are the only deliverable mutations.

**Next gate:** DR-005 research report persistence and freeze

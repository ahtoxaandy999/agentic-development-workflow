---
id: ADW-DR-005-SOURCE-REVIEW-001
artifact_status: active
authority: evidence
review_type: independent-source-review
review_target: "DR-005@sha256:3c83c5b2ceea4ce0c545f2516287aa8c4ecc3f119e55de01597ac5a66a73163c"
review_target_commit: 38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958
review_target_path: docs/research/ADW-DR-005.md
review_target_blob: 615692060c7bf9d7372d5469550176f22caca9be
review_target_bytes: 149389
review_target_sha256: 3c83c5b2ceea4ce0c545f2516287aa8c4ecc3f119e55de01597ac5a66a73163c
reviewed_on: 2026-09-04
owner: agentic-development-independent-review
supersedes: null
verdict: accepted-as-source-reviewed-evidence
finding_counts:
  blocker: 0
  major: 0
  minor: 0
---

# ADW-DR-005-SOURCE-REVIEW-001

## Source-review conclusion

**ACCEPT AS SOURCE-REVIEWED EVIDENCE.**

**Reviewer judgment:** the exact frozen report is sufficiently supported for a later fresh coordinator tooling disposition. No BLOCKER, MAJOR or MINOR evidence defect was established. The report satisfies its research contract, keeps its recommendations proposed, and makes the unsupported enforcement and AFK modes explicit. Acceptance is limited to evidence quality and recommendation support; it does not certify an installed stack or authorize implementation.

Five source records retain qualifications: a historical observation cannot be replayed as a contemporary observation; app-server documentation has surface-specific maturity tension; Sentry transport and package descriptions differ; and pricing extraction is not a procurement quote. These qualifications are already represented in DR-005. They are not undisclosed defects or grounds to treat the affected capabilities as verified operational controls.

## Exact reviewed identity

**Verified repository facts**, obtained through @GitHub:

| Item | Independent result |
|---|---|
| Repository | ahtoxaandy999/agentic-development-workflow |
| Live main | `38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958`; final repository read batch completed by 2026-09-04 07:35:11 UTC |
| Frozen commit | `38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958` |
| Sole parent | `7adc4d9866ff7d6fda8eeb63087ade300f4d7977` |
| Freeze tree | `416c267b47c3f05129ca61e061c592e74efdc35d` |
| Report path | `docs/research/ADW-DR-005.md` |
| Report Git blob | `615692060c7bf9d7372d5469550176f22caca9be` |
| Raw UTF-8 bytes | 149389 |
| Independently computed SHA-256 | `3c83c5b2ceea4ce0c545f2516287aa8c4ecc3f119e55de01597ac5a66a73163c` |
| Exact review target | `DR-005@sha256:3c83c5b2ceea4ce0c545f2516287aa8c4ecc3f119e55de01597ac5a66a73163c` |
| Gate path / blob | `docs/research/ADW-DR-005-GATE-001.md` / `1c501a3fb4797ef1cdbe6a3427dcdae090bbaf14` |
| Frozen Register blob | `2b29e098a7e977440fc93b219611aedb55fa14ec` |
| Register DR-005 state | research_status completed; current_decision_status deferred; dependency_status satisfied |
| Register target | Exact digest target above; review_target_bytes 149389 |
| Register next_gate / current repository gate | DR-005 independent source review |
| Workflow v1 | Initial design accepted; normative adoption absent; remains unadopted |
| Live protection observation | main protected:false |
| Persisted protection constraint | unavailable-for-private-repository-under-current-plan; a repository record, not independently verified account/billing state |
| Exact-subject result | PASS; no substitution of a branch tip, approximate text or different report identity |

The report metadata independently matches `id: DR-005`, `authority: evidence`, `research_status_at_publication: completed`, `recommendation_status_at_publication: proposed`, and `evidence_as_of: 2026-09-04`. Its `artifact_status: draft` does not itself negate research completion or create adoption.

The [freeze comparison](https://github.com/ahtoxaandy999/agentic-development-workflow/compare/7adc4d9866ff7d6fda8eeb63087ade300f4d7977...38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958) contains exactly one commit and changes only:

- `docs/research/ADW-DR-005.md` — added, blob `615692060c7bf9d7372d5469550176f22caca9be`.
- `docs/research/research-register.md` — modified, blob `2b29e098a7e977440fc93b219611aedb55fa14ec`.

The [frozen report](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/docs/research/ADW-DR-005.md), [Register](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/docs/research/research-register.md) and [gate](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/docs/research/ADW-DR-005-GATE-001.md) were retrieved as exact-subject evidence. Hashing the connector-retrieved raw report independently reproduced both SHA-256 and the Git blob SHA-1 over the Git object header plus raw content. The gate and Register blob IDs were also recomputed from their retrieved bytes.

The report's research-basis main was the parent, not the freeze. Its historical Register blob `1be4b5a46570be71f2354e8d2e379037270ac77b` and planned/deferred/satisfied research-execution state match that parent. Its publication/local-persistence statements, including RG8, are historical. The freeze and current Register are an expected subsequent repository transition, not an internal factual contradiction or a reason to silently edit the report.

## Review method and controlling inputs

Repository evidence was read through **@GitHub** using read-only file, object, branch, collection, tag, release and comparison retrieval. External capability sources were independently opened from first-party documentation or canonical repositories. Publisher documentation was preferred over search snippets and third-party commentary. The report's source-validation claims, summaries, prior Research Lab work and prior review verdicts were not treated as proof.

This is a fresh source review. The reviewer did not produce or modify DR-005. Existing local review material and project memory were not used to establish findings or the verdict. Review-004 and the design disposition were read to identify the accepted design input and authority boundary; their conclusions were not inherited as evidence that DR-005 is correct.

The following controlling files were directly retrieved at the freeze:

| Exact path | Git blob |
|---|---|
| [AGENTS.md](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/AGENTS.md) | `2294f13982045c54f3cb50071ab71373a3366c89` |
| [PROJECT-CHARTER.md](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/PROJECT-CHARTER.md) | `c521f6869662f39106bcac0365426eb0e9bdb327` |
| [docs/policies/research-evidence.md](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/docs/policies/research-evidence.md) | `90572c47463f2d2adc493f9978c1c720fd8f8275` |
| [docs/research/research-register.md](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/docs/research/research-register.md) | `2b29e098a7e977440fc93b219611aedb55fa14ec` |
| [docs/research/ADW-DR-005-GATE-001.md](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/docs/research/ADW-DR-005-GATE-001.md) | `1c501a3fb4797ef1cdbe6a3427dcdae090bbaf14` |
| [docs/research/ADW-DR-005.md](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/docs/research/ADW-DR-005.md) | `615692060c7bf9d7372d5469550176f22caca9be` |
| [docs/design/ADW-WF1-DESIGN-001.md](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/docs/design/ADW-WF1-DESIGN-001.md) | `afed983e7632caf3169dcbac7a80f8da8226d86d` |
| [docs/design/ADW-WF1-DESIGN-DISPOSITION-001.md](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/docs/design/ADW-WF1-DESIGN-DISPOSITION-001.md) | `35d3a8ba5c3901e90d070b000659541b1ef4975c` |
| [docs/design/ADW-WF1-DESIGN-REVIEW-004.md](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/38e31a09a1aa31f42b5b3fbc02e0fb662ebb1958/docs/design/ADW-WF1-DESIGN-REVIEW-004.md) | `3cdb92769bb955c8782dfa504843fd32a4736168` |

The design's accepted commit `2b9532682ae77bf5037f1b2fa45b720e5865d0ad` and parent `a19e700e93157b8b25eaab4f14c7c44fc3ea3f6e` resolve independently. The accepted and frozen design blobs match. This review independently computed 109600 raw bytes and SHA-256 `f8ddb3626868289e44251088a2ddad291ce762dbb58ec824d70c5de5a7994411`. The design was used only to test mechanism mappings against its semantics.

Additional GitHub reads checked the parent tree, README, current refs, all-state PRs and all-state Issues. The observed ref collection contains main; the PR collection is empty; the only Issue is closed bootstrap Issue #1 with no comments and explicit exclusion of Workflow v1/tooling adoption. These are bounded observations of accessible repository state, not proof about unseen local work or private account settings.

The review performed source/claim inspection and local byte/structure checks. It did not install or run proposed tools, benchmark target workloads, test configured protections, inspect private billing, or claim end-to-end operational conformance. Such checks are future prerequisites already identified by the report.

## Report-contract completeness

**PASS.** Independently counted and matched all 19 required sections, all 18 explicit question answers, all seven capability areas and all seven mechanism classes. The nine reusable candidate profiles explicitly cover the twenty evaluation criteria with candidate-specific overrides; non-applicability is distinguished from satisfaction. No required section or materially unanswered question was found.

| Required section | Frozen report line |
|---|---:|
| 1. Executive answer | 33 |
| 2. Accepted Workflow v1 requirements translated to mechanism needs | 45 |
| 3. Current capability landscape | 82 |
| 4. Candidate mechanism inventory | 100 |
| 5. Requirement-to-mechanism matrix | 175 |
| 6. GitHub control-plane assessment | 199 |
| 7. ChatGPT/OpenAI capability assessment | 217 |
| 8. Codex execution assessment | 229 |
| 9. External MCP/integration assessment | 243 |
| 10. Parallel execution and worktree architecture options | 257 |
| 11. Evidence and observability options | 280 |
| 12. Unattended/AFK control options | 299 |
| 13. Minimum viable tooling stack | 321 |
| 14. Alternatives rejected or deferred | 353 |
| 15. Known gaps and unsupported requirements | 388 |
| 16. Proposed staged rollout | 409 |
| 17. Risks and failure modes | 422 |
| 18. Recommendations requiring later coordinator disposition | 443 |
| 19. Source ledger | 508 |

The gate's questions were compared with the report's explicit Q01–Q18 table, not merely inferred from topical mentions:

| Question | Explicit answer and substantive coverage | Result |
|---|---|---|
| Q01 technical versus procedural | §2/§5 distinguish effect prevention from contextual owner decisions | PASS |
| Q02 durable owners | Research Register, task, execution, decomposition, candidate, evidence and decision owners remain distinct | PASS |
| Q03 GitHub/artifact sufficiency | Sufficient only for the narrow supervised record/evidence role; distinct external domains need justification | PASS |
| Q04 task-control object | Proposed repository record, conditional Issue alternative, PR transport scope | PASS |
| Q05 identity/review binding | Full subject identity; base/head/test integration/final publication distinguished; RG3/RG4 | PASS |
| Q06 writer exclusivity | Assignment and worktree separation do not establish fencing; parallel writes blocked | PASS |
| Q07 DAG/joins | Named decomposition/integration owners, required/optional accounting and current integrated verification | PASS |
| Q08 rehydration | Disposable read-only manifests plus authority rereads; no second editable owner | PASS |
| Q09 evidence package | Exact inputs/configuration/results, separate review/disposition, effects/recovery and retention | PASS |
| Q10 cancellation/recovery | Orthogonal state and domain observation; no blind retry or premature terminal closure | PASS |
| Q11 AFK prerequisites | Necessary controls plus separate authority; missing evidence denies eligibility | PASS |
| Q12 protection path | Procedural present path and separately conditional plan/configuration enforcement | PASS |
| Q13 OpenAI continuity benefit | Documented retrieval/context capabilities support a scoped friction-reduction inference | PASS |
| Q14 external integrations | Conditional value against native tools/direct docs; permission and corpus checks | PASS |
| Q15 duplicate mutable state | Same-field co-ownership rejected; derived views/disjoint domains distinguished | PASS |
| Q16 initial stack | S1–S6 plus human decisions, no mandatory new service | PASS |
| Q17 later additions | Demonstrated repetition or product need before extra helpers/services | PASS |
| Q18 unsupported requirements | RG1–RG12 explicitly identify incomplete prevention, recovery, retention and AFK | PASS |

The seven capability areas appear in §2/§5 and their detailed assessments: authority/state; task/execution control; candidate/review control; durable evidence; parallel work; context/continuity; unattended/AFK. Mechanism classes A–G appear in §3, candidate profiles/inventory and §§6–12: OpenAI coordination; Codex; Git/GitHub; navigation/docs; browser; incidents/observability; orchestration/harnesses.

## Source-ledger audit

**Independent totals:** 84 unique ledger records: 9 repository, 29 OpenAI, 20 Git/GitHub, 26 external. All 84 have primary-source identity and scope support. No duplicate ID was found. Evidence dates are explicit or unambiguously inherited from the September 4 ledger convention. The cited destinations correspond to the named publisher/project and source type; descriptive titles need not reproduce a page's typographic title exactly.

**Canonical pins:** 18 distinct canonical repositories and 18 exact commit objects verified through @GitHub; all 12 named releases independently retrieved. The Codex, just and Task annotated release tags were also resolved to their reported commits. Other HEAD and release observations remain distinct; no release-wide attribution of HEAD-only behavior was found.

| Classification | Count |
|---|---:|
| VERIFIED | 79 |
| VERIFIED WITH QUALIFICATION | 5 |
| CONTRADICTED | 0 |
| STALE | 0 |
| UNVERIFIED | 0 |
| Total | 84 |

Classification is of the report's supported claim within its stated scope. VERIFIED does not mean installed, GA, benchmarked, complete or effective in this repository. VERIFIED WITH QUALIFICATION marks the particular historical or unresolved-surface limitations discussed here; it does not create a finding when the report already states and respects the limitation.

**Load-bearing coverage:** substantive claim checks covered all sources used by S1–S6, C1–C22, protection/control conclusions, current OpenAI lifecycle claims, blocking gaps, DI-1/DI-2 and AFK denial. Inspection included failure-path and limitation passages, not only link resolution. Appendix A maps every source ID to a result and independent scope note; Appendix B records the 18 exact canonical pins.

**Accessibility:** no material ledger source remained inaccessible. Some direct help/article downloads returned 403, and a changelog Markdown route returned 404; their official HTML pages were independently read through the web tool. These transport failures did not leave a claim unreviewed. A supplemental search-index lead to Sentry `docs/security.md` returned 404 through @GitHub at both the current pin and main; it was not a ledger source and its snippet was not admitted as repository evidence.

The source audit does not certify the producer's historical tool-call trace or exact 06:15:44 read-completion timestamp. R09's material present conclusion was independently re-established. Documentation published on rolling pages remains evidence of documented behavior at review time, with later actual-version/configuration verification required.

## Findings

| Severity | Count |
|---|---:|
| BLOCKER | 0 |
| MAJOR | 0 |
| MINOR | 0 |

No finding requiring a corrected frozen report was established. No stylistic findings were created. The qualifications below preserve limitations already material to the report's own reasoning; none supplies missing positive evidence for a recommendation.

## Recommendation assessment

### SELECT NOW — PASS WITH QUALIFICATION

All six recommendations remain proposed research outcomes for later disposition. The word “now” is explicitly defined in §18 as the proposed first selection set. It is not an installation, adoption or execution decision.

| Candidate | Accepted requirement and evidence | Available role, simpler alternative and limit |
|---|---|---|
| S1 Git/GitHub identity and owner records | DD-001–003/009–010; R03/R04/R06; G03/G08/G11/G12/G15 | Existing durable representation, provenance and evidence. Manual owner decisions remain necessary. A mutable chat or branch name is insufficient; current GitHub access is not protected integration. |
| S2 proposed repository task-control record | DD-003–007/011; R06; §5/§6 ownership reasoning | A representation proposal requiring later ownership/schema disposition. It adds no service. Existing Register retains research scope; an Issue is a conditional alternative, not a second current owner. |
| S3 fresh OpenAI contexts and connected reads | DD-010 and rehydration; O01–O05/R09 | Existing context/retrieval convenience with exact rereads. Plain pointer handoff remains the baseline. No measured productivity gain, universal entitlement or memory authority is claimed. |
| S4 bounded supervised Codex | DD-004–007/011; O06/O09–O16 | Existing executor and producer-verification role under explicit task limits. Instructions and approval review are not full enforcement or independent result review. No new installed version is presumed. |
| S5 native search/direct docs/legibility | Rehydration and evidence provenance; E302/E304/O22/O26 | Existing search and publisher retrieval are sufficient for the present documentation work. Added semantic/MCP tools need measured benefit. The case-study merge policy is not adopted. |
| S6 available raw results/logs and manifests | DD-009–010; R06/G15 | Evidence capture and transport using available output. Named custody, access and sufficient retention remain required; an expiring URL or digest warning alone cannot satisfy reliance. |

The qualification is the architecture's narrow supervised evidentiary scope and later disposition requirements, not an unsupported claim of present technical enforcement.

### CONDITIONALLY SELECT — PASS

All 22 rows explicitly identify unmet prerequisites, an accountable owner class and later verification. None is treated as already eligible. The following independent checks establish why the conditions matter:

| Candidate(s) | Evidence and decisive remaining condition |
|---|---|
| C1 Issue | G18/R06 support transport, not full lifecycle semantics; the task/coordinator owner must choose a sole current-state scope. |
| C2 PR | G03/G06/G08 support explicit head/review identity but not an expected-base merge guard; integration owner must verify all publication subjects and drift handling. |
| C3 protection/ruleset | G01 supports a plan/configuration path; repository owner must verify entitlement, active rules, bypasses and rejection behavior. Manual SHA checks are insufficient. |
| C4 CODEOWNERS/reviews | G09/G10 support routing and eligible reviews; repository/review owner must establish independent identity and effective required-approval behavior. |
| C5 Actions/checks | G04/G05/G07/G14/G17 support repeatable verification; maintainer must bind actual subject/attempt and fail closed on omitted obligations. |
| C6 artifacts | G15 requires custody and verified mismatch/expiry/access handling; transport is not guaranteed long-term evidence. |
| C7 worktrees | G11/O08 show file separation, not exclusive writers; execution/integration owner needs governance authority and effective fencing, cancellation and joins. |
| C8 additional app | O05 supports integration surfaces; task/data owner must demonstrate need and inspect actual tools, scopes, disclosure and forbidden effects. |
| C9 subagents | O13 supports delegation under constraints; delegating owner must bound slices and effects and account for every result. |
| C10 structured exec | O14–O16 support structured evidence; execution/evidence owner must validate actual runtime/configuration, completeness and failures. |
| C11 auto-review | O11 supports approval assessment only; security/runtime owner must establish policy and rejection behavior without substituting for source review. |
| C12 Codex review | O20 supports assistance with limited scope; review owner must establish the exact independent review contract and subject. |
| C13 Serena | E301 supports language-aware retrieval; project owner must show target-corpus value, supported backend and restricted tool exposure. |
| C14 ast-grep/IDE MCP | E303/E304 distinguish syntax and IDE semantics; tooling owner must verify fit, licensing/runtime and effectful tool configuration. |
| C15 publisher docs MCP | O22/E307 support narrower official retrieval; documentation owner must justify repeated need and validate version/citation coverage. |
| C16 Context7 | E305/E306 support retrieval, not completeness; documentation owner must verify version/upstream sources, privacy, quota and integration value. |
| C17 Playwright Test | E310/E311 support repeatable reports; test owner must supply real browser criteria and verify build/browser/account/backend isolation. |
| C18 browser CLI/native | E309/O23 support exploration; task/test owner must verify authenticated effects, evidence and cleanup. |
| C19 Sentry | E312/E314 support incident data/access; operations owner must establish an actual runtime need, correlation, redaction and retention. |
| C20 Sentry MCP | E312/E313 expose transport/tool differences; operations/security owner must resolve exact auth and deny unwanted mutations before reliance. |
| C21 OpenTelemetry | E315 supports portable signals; observability owner must pin components and verify sampling/drops, backend and retention. |
| C22 Temporal application use | E320/E321 support durable application work; platform owner must independently justify that different domain and test replay/cancellation/containment with actual SDK/server versions. |

### DEFER — PASS

D1–D14 have explicit unmet need, prerequisite, scope mismatch or cost/complexity reasons and bounded revisit triggers (§14). This is not a claim that every deferred tool is inferior. Just/Task and small scripts are considered before another orchestration service; the lighter agent loop is considered alongside Deep Agents/LangGraph; native browser/CLI is compared with MCP; direct publisher sources are compared with retrieval services. Temporal's distinct application use does not contradict deferring it for ADW bootstrap coordination.

### REJECT — PASS

X1–X9 reject specified uses or architectures. The decisive evidence is the accepted ownership/identity/recovery contract plus actual product limitations, not a recommendation label. In particular, worktree locks/CODEOWNERS are not leases; unmodified Symphony is not shown to meet stale-authority/retry/evidence-retention guards; LangSmith rollback can remove relied-upon records; a process exit is not complete containment; duplicate current fields conflict with one authoritative owner. Rejection does not purport to prohibit these products for unrelated purposes.

### RESEARCH GAP — PASS

RG1–RG12 are missing control or assurance evidence, not proofs that the products have no corresponding features. Protection, fencing, atomic integration identity, review-role enforcement, effective permissions, containment, recovery, retention, installed compatibility, target benefit, documentation ambiguity and AFK readiness are each connected to an owner and a resolving verification gate. Their consequences narrow scope or keep dependent transitions non-passing. No gap is used as positive proof of sufficiency.

## Minimum-stack assessment

**PASS WITH QUALIFICATION — sufficiently evidenced for later coordinator disposition within the report's stated supervised scope.**

The system separates content identity, semantic owner records, producer results, independent review and authorized disposition. The Register owns cross-project research state; product task records would own distinct execution domains. An Issue/file pair is allowed only after an explicit sole-owner or derived-view choice. Tool-local observations cannot independently set ADW review, gate or disposition values.

The review specifically tested competing mutable fields, stale candidate/review pointers, run/configuration identity, duplicated gate state, reviewer subject drift, integrated-verification identity, credential multiplication, worktree ownership, cancellation, recovery evidence loss and vendor dependence. These are either explicitly prevented at the proposed representation boundary or identified as unresolved prevention/operational gaps. No component is represented as automatically enforcing another component's semantics.

A materially simpler sufficient alternative was not omitted: the proposal already starts with existing files, Git identity, direct reads, native search and human decisions. Additional services require a demonstrated need. OpenAI context surfaces are replaceable conveniences provided relied-upon contracts/results/decisions are exported and retained. The report does not establish a quantitatively optimal stack or a fully enforced general engineering workflow. Current restrictions still block routine, parallel, automated and AFK writes.

## Evidence-type discipline

| Dimension | Assessment |
|---|---|
| Fact/inference/recommendation separation | PASS. Repository observations, documented capabilities, deductions, proposed choices and missing assurance are distinguishable by paragraph/table context. No target benchmark or installed-control experiment is claimed. |
| Freshness | PASS WITH QUALIFICATION. Parent-state observations and publication status remain historical; current freeze/Register were independently established. Rolling external pages require later rereads. |
| Maturity/lifecycle | PASS WITH QUALIFICATION. Beta/experimental/deprecated labels are retained; release metadata is not GA certification. App-server and Sentry scope tensions remain unresolved rather than generalized. |
| Contradictions | PASS. Credible tensions are explicitly scoped and their consequences retained; no material contrary primary evidence was suppressed or averaged away. |
| Source-to-claim traceability | PASS. All 84 unique IDs resolve to primary evidence within scope; exact pins and dates are separated from deployment claims. |

The report's pointer-ferrying benefit is an inference about existing retrieval/context capabilities, not an empirical timing or reliability result. Its protection statement is a repository observation plus a separately sourced general GitHub capability statement. Its lack of conformance evidence is not recast as proof that cancellation or recovery features are absent. Successful reads or tool calls are never treated as acceptance.

## Contradictions and freshness assessment

| Tension / sources | Independent evidence and authority comparison | Consequence / correction |
|---|---|---|
| Historical research basis versus frozen current state: R04/R05/R09 and freeze Register | Parent objects support the historical execution gate; the later exact freeze/Register govern this review. Publication statements were expressly historical. | Expected post-publication repository transition, not REPORT DEFECT. No correction; later actors use current owner records. |
| App-server stable API versus experimental surfaces: O16 | Same first-party page describes a stable nonexperimental API subset and experimental remote/WebSocket/process contexts. No general lifecycle guarantee resolves all surfaces. | Preserve RG11/D5; generic production readiness remains unestablished. No correction. |
| Sentry service/root/core descriptions: E312/E313 | Deployed OAuth-only language differs from upstream-token transport support and prototype/stdio wording. Authority is component/transport-specific, not a single averaged maturity label. | Resolve selected deployment/auth/tools before C20. No correction; ambiguity is already disclosed. |
| GitHub green/mergeable versus ADW integrated pass: G04/G05/G07 and R06 | GitHub's generic accepted conclusions are not the design's required successful verification contract. Both can be true. | Require exact obligations and subject; no correction. |
| Older one-pending model versus current Actions docs: G14 | Current official docs explicitly add queue:max and its constraints. The report uses the current capability and does not claim a global queue. | No stale claim established; no correction. |
| Retrieval marketing versus corpus limitations: E305/E306 | Canonical disclaimer and private-backend scope qualify freshness/correctness claims; the report retains this distinction. | C16 still needs target/version/citation verification; no correction. |
| Harness publication/product identity versus pinned material: O27/O29/E322–E325 | Exact current specification and README identify Symphony reference/preview and OpenHands Canvas beta separately from SDK behavior. | No obsolete generic product characterization found; no correction. |
| HEAD versus release: Appendix B | All pins/releases exist. Named release metadata does not assert that later README/source features shipped in that release. | Pin actual deployment components later; no correction. |

No material external **POST-SNAPSHOT CHANGE** defeating a recommendation before disposition was established in the independently inspected current sources. No load-bearing **REPORT DEFECT** was established. This is bounded to the reviewed sources and September 4 reads, not a guarantee of future-current product state.

## Design-impact assessment

**PASS.** The producer's two design-impact findings at report §15, line 407 are correctly identified as conditional semantic incompatibilities, isolated and not incorporated:

- **DI-1:** mapping the ADW lifecycle to one native done/failed/cancelled field would collapse orthogonal state, applicability and terminal guards. R06's state model supports this conclusion.
- **DI-2:** ambiguous-effect retry, materially stale-authority continuation or deletion of relied-upon recovery evidence would relax accepted stop/recovery/durability guards. R06 establishes the obligation; O29 and E317–E319 provide concrete product behaviors requiring an adapter or a separately reviewed design change.

No additional hidden design-impact finding was established. The following explicit semantic tests passed:

| Tested risk | Result |
|---|---|
| Collapse task/cancellation/recovery/review/disposition into product status | PASS: rejected, with separate owners/planes retained |
| Process exit treated as containment | PASS: domain observation and residual effects remain required |
| Tool success treated as acceptance | PASS: producer verification, independent review and disposition remain separate |
| Stale-authority continuation | PASS: stale required inputs invalidate reliance; unmodified defaults rejected |
| Blind retry after ambiguous effects | PASS: operation-aware reconciliation and separate authority required |
| Deletion of relied-upon recovery evidence | PASS: retained episodes and evidence custody required |
| Candidate identity substituted for reviewer identity | PASS: subject binding and conflict-free role/platform mapping remain separate |
| Tooling selects/adopts itself | PASS: all recommendations await coordinator disposition and later authority |
| AFK authorized by capability existence | PASS: expressly denied |
| Missing/optional/failed join or integrated verification treated as pass | PASS: explicit accounting, current subject and legitimate N/A remain required |
| Recovery completion directly resumes or closes a task | PASS: recovery/containment/terminal decisions are distinct; accepted episode semantics are preserved |

The review does not reopen accepted design choices. It establishes only that the research's mechanism mappings preserve their intended semantics.

## AFK boundary assessment

**PASS.** DR-005 appropriately keeps AFK unavailable and unauthorized.

No current evidence establishes the necessary combination of effective least privilege/credentials, isolation, hard resource/concurrency ceilings, fresh authority, progress observation, tested cancellation across every execution domain, protected evidence retention, safe recovery, reachable intervention and independent review. Protection and writer fencing are also unresolved for relevant write modes. A scheduled task, subagent, hook, durable engine or cloud worker supplies at most part of that control set.

The decisive reason is missing verified end-to-end controls and separate task-specific authority, not a claim that all reviewed products lack unattended features. Even a future successful eligibility screen would not itself authorize AFK.

## Authority boundary and repository write status

This verdict qualifies the exact DR-005 target as **SOURCE-REVIEWED RESEARCH EVIDENCE** for a later fresh coordinator disposition. It does not persist that state to the Register. It makes no tooling disposition, selection, installation, implementation or Workflow v1 adoption. It grants no new write, parallel, automated, unattended or AFK authority.

**No GitHub write performed.** DR-005, the Register, Workflow v1, branch protection and repository configuration were not modified. Local changes are limited to fresh review evidence and this requested review record. No proposed tool was installed or activated.

**Next gate: DR-005 source review persistence.**

## Appendix A — Every ledger source

All classifications below concern the report's scoped claims. Sources were independently inspected on 2026-09-04. Exact canonical commits and named releases are additionally listed in Appendix B.

| Source ID | Classification | Independent verification / retained qualification |
|---|---|---|
| [R01](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/AGENTS.md) | VERIFIED | Exact instruction blob matches at the research parent and freeze; governance and write restrictions are supported. |
| [R02](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/PROJECT-CHARTER.md) | VERIFIED | Exact charter matches; bootstrap authority and decision separation are supported. |
| [R03](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/policies/research-evidence.md) | VERIFIED | Exact policy matches; evidence publication, historical observations, review and adoption have separate meanings. |
| [R04](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/research/research-register.md) | VERIFIED | Historical Register blob and planned/deferred/satisfied execution state match the parent. The freeze Register now owns completed/deferred and the source-review gate. |
| [R05](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/research/ADW-DR-005-GATE-001.md) | VERIFIED | Exact gate blob matches; 19 sections, 18 questions, seven areas/classes and the research-only ceiling were checked directly. |
| [R06](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/2b9532682ae77bf5037f1b2fa45b720e5865d0ad/docs/design/ADW-WF1-DESIGN-001.md) | VERIFIED | Accepted subject and parent resolve; the design blob is identical at accepted subject, research parent and freeze. Independently recomputed 109600 bytes and its recorded SHA-256. |
| [R07](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/design/ADW-WF1-DESIGN-REVIEW-004.md) | VERIFIED | Review-004 identity, recorded design binding and verdict fields match. Its conclusion was not reused to decide this source review. |
| [R08](https://github.com/ahtoxaandy999/agentic-development-workflow/blob/7adc4d9866ff7d6fda8eeb63087ade300f4d7977/docs/design/ADW-WF1-DESIGN-DISPOSITION-001.md) | VERIFIED | Disposition binds the accepted initial design and expressly has no normative effect; it does not select tools. |
| [R09](https://api.github.com/repos/ahtoxaandy999/agentic-development-workflow/branches/main) | VERIFIED WITH QUALIFICATION | Historical tree/README and present refs, PRs, Issues and unprotected main were independently read. The producer's precise historical read time cannot be replayed; it is not independent proof of freshness or billing. |
| [O01](https://learn.chatgpt.com/docs/projects) | VERIFIED | Projects provide shared context and separate conversations. The report correctly treats project contents as snapshots requiring authoritative rereads. |
| [O02](https://learn.chatgpt.com/docs/get-started-with-work) | VERIFIED | Work documents task/artifact and local/cloud surfaces where offered; the report does not promise universal account or runtime availability. |
| [O03](https://help.openai.com/en/articles/10500283-deep-research) | VERIFIED | Deep Research documents source selection, planning, steering, cited output and exports; connected-app actions are read-only in this mode. Entitlements remain scoped. |
| [O04](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt) | VERIFIED | The help article supports allowed GitHub retrieval and eligible Work event triggers. Surface-specific read/write and indexing distinctions are not generalized to every connector. |
| [O05](https://learn.chatgpt.com/docs/plugins) | VERIFIED | Plugin bundles can include skills, connectors, MCP and hooks; installation, authentication and effectful tool permissions remain separate. |
| [O06](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | VERIFIED | Scoped AGENTS.md discovery, precedence and size limits are documented. Instruction compliance is not an operating-system boundary. |
| [O07](https://learn.chatgpt.com/docs/build-skills) | VERIFIED | Skills use progressive disclosure and reusable resources. The report does not infer permission grants, task-state authority or measured savings. |
| [O08](https://learn.chatgpt.com/docs/environments/git-worktrees) | VERIFIED | App worktrees may be detached and starting state depends on the selected flow/local changes; exact base and cleanliness require observation. |
| [O09](https://learn.chatgpt.com/docs/permissions) | VERIFIED | The permissions documentation explicitly labels profiles Beta. Managed policy, configuration precedence and proxy-dependent network filtering support the report's bounded claim. |
| [O10](https://learn.chatgpt.com/docs/sandboxing) | VERIFIED | Local commands and spawned subprocesses receive sandbox restrictions, subject to platform/configuration limits. Other browser/MCP/cloud controls require separate evaluation. |
| [O11](https://learn.chatgpt.com/docs/sandboxing/auto-review) | VERIFIED | Auto-review changes approval-request assessment, not the underlying authority ceiling, and does not establish independent candidate/source review. |
| [O12](https://learn.chatgpt.com/docs/hooks) | VERIFIED | Covered local tool hooks have exceptions; matching command hooks can start concurrently. Stop, SubagentStart, Interrupt and long-running tool behavior do not supply a universal veto or containment protocol. |
| [O13](https://learn.chatgpt.com/docs/agent-configuration/subagents) | VERIFIED | Subagents inherit sandbox/approval constraints with configuration rules; this neither fences shared files nor establishes reviewer independence. |
| [O14](https://learn.chatgpt.com/docs/non-interactive-mode) | VERIFIED | Noninteractive execution documents JSONL, output schemas, read-only default and deprecation of --full-auto. Structured output is not proof of semantic correctness. |
| [O15](https://learn.chatgpt.com/docs/codex-sdk) | VERIFIED | SDK guidance documents programmatic execution and deprecates codex mcp-server. The report leaves installed SDK/component compatibility unverified rather than inventing a deployment pin. |
| [O16](https://learn.chatgpt.com/docs/app-server) | VERIFIED WITH QUALIFICATION | Thread/event/review/interrupt APIs exist. Stable API wording coexists with experimental remote/WebSocket/process qualifications; generic production readiness remains unresolved, as the report states. |
| [O17](https://learn.chatgpt.com/docs/automations) | VERIFIED | Scheduled/event-triggered work is documented; local awake/runtime and web/cloud eligibility differ. The report defers activation and does not infer AFK authority. |
| [O18](https://learn.chatgpt.com/docs/long-running-work) | VERIFIED | Long-running goals preserve an objective across work but remain subject to constraints; continuation is not a new permission grant. |
| [O19](https://learn.chatgpt.com/docs/customization/memories) | VERIFIED | Memory and continuation preserve derived context, including background updates. They do not establish current repository authority. |
| [O20](https://learn.chatgpt.com/docs/third-party/github) | VERIFIED | GitHub review assistance has a restricted defect scope; current documentation limits routine reporting to P0/P1 and separately labels Security Review research preview. The report makes no broader review-completeness claim. |
| [O21](https://learn.chatgpt.com/docs/changelog) | VERIFIED | Current changelog independently confirms 0.153.2 on September 3 and scoped experimental features. It is not evidence of the user's installed binary. |
| [O22](https://learn.chatgpt.com/learn/docs-mcp) | VERIFIED | The OpenAI documentation MCP is publisher-owned documentation retrieval; it does not call the OpenAI API or implement workflow authority. |
| [O23](https://learn.chatgpt.com/docs/browser) | VERIFIED | The browser docs support rendered-state inspection, screenshots and interaction with separate site/account controls. No deterministic acceptance or universal containment claim follows. |
| [O24](https://learn.chatgpt.com/docs/feature-maturity) | VERIFIED | Official maturity definitions distinguish stable, beta, experimental and deprecated. An unlabeled rolling page is not upgraded to GA in the report. |
| [O25](https://learn.chatgpt.com/docs/agent-approvals-security) | VERIFIED | Supplementary approval/security monitoring may pause work; asynchronous monitoring does not replace sandboxing or independent result review. |
| [O26](https://openai.com/index/harness-engineering/) | VERIFIED | The first-party harness case study supports repository legibility as an approach. Its permissive/minimal merge-gate choices are not imported into ADW. |
| [O27](https://openai.com/index/open-source-codex-orchestration-symphony/) | VERIFIED | The Symphony publication describes reference orchestration material rather than a promised maintained standalone product; current pinned specification controls detailed behavior. |
| [O28](https://github.com/openai/codex/releases/tag/rust-v0.153.2) | VERIFIED | Release rust-v0.153.2 exists, is non-prerelease metadata, and remains latest at the read. Its annotated tag resolves to the exact reported commit; this is not a maturity or installed-state certification. |
| [O29](https://github.com/openai/symphony/blob/8001b52e3062495a16e520e4ceaf8f9de868c4d0/README.md) | VERIFIED | Pinned README is engineering preview; specification is draft v1. Retry, failed-refresh continuation, workspace cleanup and in-memory scheduler recovery justify rejecting unmodified ADW conformance. |
| [G01](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | VERIFIED | Official docs support private-personal Pro protection/rulesets and configuration/bypass qualifications. Present account entitlement is not inferred from this general product documentation. |
| [G02](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) | VERIFIED | Merge queue availability is scoped to supported organization repositories/plans; the report correctly excludes it as the current private-personal solution. |
| [G03](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request) | VERIFIED | Merge REST supports an expected head SHA and conflict response, but no expected-base parameter. Manual base read plus head guard is not an atomic base guard. |
| [G04](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks) | VERIFIED | Required-check handling depends on current head/test-merge evidence and permits some skipped/neutral conclusions. The report demands actual required ADW verification separately. |
| [G05](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) | VERIFIED | Workflow event, checkout and merge-group subjects differ. The proposed later verification records must bind the actual event, commit and run attempt. |
| [G06](https://docs.github.com/en/pull-requests/reference/pull-request-merges) | VERIFIED | Merge strategies can change final commit identity; GitHub rebase creates new SHAs. Candidate, test integration and final published commit must remain distinguishable. |
| [G07](https://docs.github.com/en/rest/commits/statuses) | VERIFIED | Status contexts and check runs are separate APIs; the combined status is not an exhaustive semantic verification gate. |
| [G08](https://docs.github.com/en/rest/pulls/reviews) | VERIFIED | Review records carry actor, state and commit_id; omitted commit_id defaults to the current commit. Explicit binding still needs independent role assessment. |
| [G09](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) | VERIFIED | CODEOWNERS uses the relevant base-branch file and eligible owners; required approval needs enforcement, and one matching owner can suffice. It is not a writer lease. |
| [G10](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request) | VERIFIED | PR authors cannot approve their own PR. This platform restriction alone does not prove conflict-free model-context or organizational independence. |
| [G11](https://git-scm.com/docs/git-worktree) | VERIFIED | Worktrees separate checkout state while sharing repository metadata. Administrative locks and force overrides do not exclude an editing process. |
| [G12](https://git-scm.com/docs/git-update-ref) | VERIFIED | Full object names and expected-old local ref transactions are documented. They do not supply remote atomic publication or global writer fencing. |
| [G13](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation) | VERIFIED | Actions cancellation reevaluates conditions and then signals/kills runner processes under documented timeouts; it does not reconcile external effects. |
| [G14](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency) | VERIFIED | Default concurrency replaces a pending member; queue:max permits up to 100 pending jobs/runs and conflicts with cancel-in-progress:true. Queue ordering is waiting order, not a global dispatch-order guarantee. |
| [G15](https://docs.github.com/en/actions/tutorials/store-and-share-data) | VERIFIED | Artifacts support transfer, retention and digests but can expire or be deleted. Download digest mismatch is documented as a warning; fail-closed reliance needs an additional verified obligation. |
| [G16](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) | VERIFIED | On Free/Pro/Team, environment required-reviewer and wait-timer features remain public-repository-only. Pro private environments do not solve that reviewer requirement. |
| [G17](https://docs.github.com/en/actions/reference/limits) | VERIFIED | Actions limits and secure-use guidance support quotas, least privilege and full action-SHA pinning. They do not establish current target configuration. |
| [G18](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues) | VERIFIED | Issues, dependencies and PR reviews provide useful transport/coordination records, but native statuses lack the accepted orthogonal terminal and recovery semantics. |
| [G19](https://github.com/casey/just/releases/tag/1.58.0) | VERIFIED | Pinned just README supports command recipes/discovery and static detection of some errors. Release 1.58.0 resolves to the reported commit; no durable orchestration or fencing guarantee is attributed. |
| [G20](https://github.com/go-task/task/releases/tag/v3.53.1) | VERIFIED | Pinned Task guide documents parallel dependencies, freshness skips, failing preconditions and force behavior. Release v3.53.1 resolves to the reported commit; defaults need task-specific review. |
| [E301](https://github.com/oraios/serena/blob/801a388c2b7a6a8998f313291678b1609664e794/README.md) | VERIFIED | Canonical Serena supports language-server/JetBrains semantic tools, optional memory and mutation surfaces. HEAD and v1.7.0 both exist; target-language benefit and release parity are not assumed. |
| [E302](https://github.com/BurntSushi/ripgrep/blob/3fce3b5bb0236da2df6d99672afb8a719642eca7/README.md) | VERIFIED | Canonical ripgrep documents lexical search and default ignore/hidden/binary exclusions. The report keeps search completeness and semantic navigation distinct. |
| [E303](https://github.com/ast-grep/ast-grep/blob/29285d16757371a70a93190929940886e68618d3/README.md) | VERIFIED | Canonical ast-grep documents tree-sitter structural search/rewrite; it is not proof of type-aware references or whole-program semantics. |
| [E304](https://www.jetbrains.com/help/idea/mcp-server.html) | VERIFIED | JetBrains docs describe bundled MCP since 2025.2, current IDE tooling and configurable exposure. Router-only or broad terminal options do not imply least privilege. |
| [E305](https://github.com/upstash/context7/blob/6d777619c2777a79ad0754dc48b48845cb912bac/README.md) | VERIFIED | Context7 documents CLI/skills and MCP with library/version targeting. Community-content accuracy limits and private backend prevent treating retrieval as authoritative corpus completeness. |
| [E306](https://context7.com/plans) | VERIFIED | First-party plan page supports quota/payment dependence, including limited included usage. The report does not turn marketing wording into an unlimited-use guarantee or procurement quote. |
| [E307](https://learn.microsoft.com/en-us/training/support/mcp) | VERIFIED | Microsoft Learn MCP is publisher-owned public documentation/code retrieval without authentication or a charge for this service; coverage/update limits remain relevant. |
| [E308](https://docs.ref.tools/) | VERIFIED | Ref documents Context retrieval and shared Plans. Index Reader/Writer roles do not constrain Plans identically; rejecting duplicate ADW state is an architectural judgment, not a claim the service lacks useful features. |
| [E309](https://playwright.dev/docs/getting-started-cli) | VERIFIED | Microsoft recommends CLI/skills for coding-agent efficiency and MCP for persistent exploration. Both pins/releases exist; MCP disclaims a security boundary, including incomplete origin restrictions. |
| [E310](https://playwright.dev/docs/auth) | VERIFIED | Playwright auth state can expose credentials; parallel tests that mutate server state need separate accounts. Current HEAD is a next-version commit, distinct from named v1.62.1. |
| [E311](https://playwright.dev/docs/test-reporters) | VERIFIED | Playwright documents JSON, JUnit, HTML and blob reporting. Reports transport test evidence; they do not prove acceptance criteria were complete or exercised. |
| [E312](https://github.com/getsentry/sentry-mcp/blob/ea767b707ebdcc2fc90f177d887942752ff01e5f/README.md) | VERIFIED WITH QUALIFICATION | Pinned root and service docs support triage and transport-specific auth. Service OAuth-only wording and root upstream-token support remain unresolved for a chosen deployment; stdio is work in progress. |
| [E313](https://github.com/getsentry/sentry-mcp/blob/ea767b707ebdcc2fc90f177d887942752ff01e5f/packages/mcp-core/README.md) | VERIFIED WITH QUALIFICATION | Pinned core README documents default inspect/Seer/triage/project-management capabilities, deprecated scope flags and telemetry. Prototype package wording cannot be generalized to the differently described remote service. |
| [E314](https://sentry.io/pricing/) | VERIFIED WITH QUALIFICATION | Free Developer/MCP inclusion and paid usage/add-ons are supported. This review does not convert the report's unresolved billing-toggle extraction into a procurement quote or entitlement audit. |
| [E315](https://opentelemetry.io/docs/what-is-opentelemetry/) | VERIFIED | OpenTelemetry generates/exports signals and is not a storage/visualization backend. The specification commit exists; SDK/Collector/convention support and signal maturity need component-specific pins. |
| [E316](https://github.com/langchain-ai/langgraph/blob/81bf17b23123e4ef8b9d5f49fa09a0122fc2edd1/README.md) | VERIFIED | Canonical LangGraph supports stateful graph execution. Core release 1.2.11 exists; latest repository release is separately sdk==0.4.4. Core, SDK and hosted products are not conflated. |
| [E317](https://docs.langchain.com/oss/python/langgraph/persistence) | VERIFIED | LangGraph persistence is backend/durability-mode dependent. In-memory storage is not durable, and replay can execute later nodes and external calls again. |
| [E318](https://docs.langchain.com/oss/javascript/langgraph/interrupts) | VERIFIED | The JavaScript interrupt documentation restarts the node and requires idempotent pre-interrupt effects; this is not exactly-once external execution. |
| [E319](https://docs.langchain.com/langsmith/cancel-run) | VERIFIED | The cited cancellation API is LangSmith Deployment. Interrupt retains state; rollback deletes run/checkpoint records and wait controls completion waiting, not universal external rollback. |
| [E320](https://github.com/temporalio/temporal/blob/2220587dea828d938fc99253e178a13d1cb658c5/README.md) | VERIFIED | Temporal server pin/release exist. Python cancellation is cooperative, regular Activities receive it through heartbeats, and termination does not run workflow cleanup; SDK and server pins are distinct. |
| [E321](https://temporal.io/pricing) | VERIFIED | Temporal Cloud pricing and self-hosting options support an added service/operations cost surface; no target cost comparison or quote was produced. |
| [E322](https://github.com/OpenHands/OpenHands/blob/4524a919930d62535a5cdca143c8a54eaf0ede42/README.md) | VERIFIED | The pinned OpenHands root describes Agent Canvas beta and unsandboxed host filesystem risks. It is correctly distinguished from the SDK. |
| [E323](https://github.com/OpenHands/software-agent-sdk/blob/07307cb8edfcd9b4675be2761df0646d075a9c36/README.md) | VERIFIED | The SDK supports local and remote/container runtime options and multiple interfaces. Pin/release exist; selecting an option does not prove effective isolation. |
| [E324](https://docs.openhands.dev/sdk/guides/security) | VERIFIED | OpenHands risk analysis/confirmation policies are not an automatic hard deny; direct execute_tool can bypass confirmation. The report's boundary warning is supported. |
| [E325](https://docs.openhands.dev/sdk/guides/convo-persistence) | VERIFIED | Conversation persistence can contain sensitive state; pause and thread joining are separate steps. Persistence/resumption does not prove bounded stop or complete containment. |
| [E326](https://github.com/langchain-ai/deepagents/blob/afff4f8841bcc370d01c2739f53e882a92ef5c6a/README.md) | VERIFIED | Deep Agents supplies planning/filesystem/memory/delegation; its own README offers a lighter create_agent alternative. Pin/release exist; neither is shown necessary for this bootstrap. |

## Appendix B — Canonical repository pin audit

Every repository identity and exact commit below was independently resolved through @GitHub's Git commit API. Named release records were separately retrieved. A commit date is not a release date; a non-prerelease flag is release metadata, not an assurance of GA or ADW conformance.

| Source | Canonical repository and exact commit | Commit date UTC | Release / scope check |
|---|---|---|---|
| O28 | [openai/codex](https://github.com/openai/codex/commit/657a993cbee87acf52d14b758ce49dbd46d1b8eb) — `657a993cbee87acf52d14b758ce49dbd46d1b8eb` | 2026-09-03T23:04:28Z | rust-v0.153.2 — 2026-09-03; annotated tag resolves to this commit |
| O29 | [openai/symphony](https://github.com/openai/symphony/commit/8001b52e3062495a16e520e4ceaf8f9de868c4d0) — `8001b52e3062495a16e520e4ceaf8f9de868c4d0` | 2026-08-12T18:19:47Z | No release equivalence claimed; README engineering preview, SPEC draft v1 |
| G19 | [casey/just](https://github.com/casey/just/commit/7f4ef81bd6a93faa2b28430912c8e9ab0e3dd29a) — `7f4ef81bd6a93faa2b28430912c8e9ab0e3dd29a` | 2026-08-03T20:28:37Z | 1.58.0 — 2026-08-03; annotated tag resolves to this commit |
| G20 | [go-task/task](https://github.com/go-task/task/commit/ff3372fc50a47348610d722616f1a073aace0513) — `ff3372fc50a47348610d722616f1a073aace0513` | 2026-08-18T15:23:38Z | v3.53.1 — 2026-08-18; annotated tag resolves to this commit |
| E301 | [oraios/serena](https://github.com/oraios/serena/commit/801a388c2b7a6a8998f313291678b1609664e794) — `801a388c2b7a6a8998f313291678b1609664e794` | 2026-09-03T16:35:07Z | v1.7.0 — 2026-08-09; separate from later HEAD |
| E302 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep/commit/3fce3b5bb0236da2df6d99672afb8a719642eca7) — `3fce3b5bb0236da2df6d99672afb8a719642eca7` | 2026-08-04T14:00:08Z | Commit pin; no named release parity claimed |
| E303 | [ast-grep/ast-grep](https://github.com/ast-grep/ast-grep/commit/29285d16757371a70a93190929940886e68618d3) — `29285d16757371a70a93190929940886e68618d3` | 2026-08-31T15:41:41Z | Commit pin; no named release parity claimed |
| E305 | [upstash/context7](https://github.com/upstash/context7/commit/6d777619c2777a79ad0754dc48b48845cb912bac) — `6d777619c2777a79ad0754dc48b48845cb912bac` | 2026-09-02T15:14:37Z | @upstash/context7-mcp@4.0.4 — 2026-08-28; separate from HEAD |
| E309 | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp/commit/8a13ef8e9f7385a0f89477922127f31cbfde9761) — `8a13ef8e9f7385a0f89477922127f31cbfde9761` | 2026-09-03T19:04:23Z | v0.0.80 — 2026-09-01; separate from HEAD |
| E309 | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli/commit/655530f6d0dc71a0d6bf46ae165877d3c7311099) — `655530f6d0dc71a0d6bf46ae165877d3c7311099` | 2026-09-03T19:04:51Z | v0.1.19 — 2026-09-01; separate from HEAD |
| E310 | [microsoft/playwright](https://github.com/microsoft/playwright/commit/d1dcd6bc0a138ec0fd943df19e07458dc426ee22) — `d1dcd6bc0a138ec0fd943df19e07458dc426ee22` | 2026-09-03T23:12:29Z | v1.62.1 — 2026-07-30; HEAD is v1.64.0-next work |
| E312/E313 | [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp/commit/ea767b707ebdcc2fc90f177d887942752ff01e5f) — `ea767b707ebdcc2fc90f177d887942752ff01e5f` | 2026-09-04T00:41:43Z | Commit pin shared by E312/E313; component/transport maturity differs |
| E315 | [open-telemetry/opentelemetry-specification](https://github.com/open-telemetry/opentelemetry-specification/commit/238e0e201c71d8e92a3e08202c9a02f2517dec52) — `238e0e201c71d8e92a3e08202c9a02f2517dec52` | 2026-09-03T22:14:44Z | Specification commit, not a universal SDK/Collector release |
| E316 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph/commit/81bf17b23123e4ef8b9d5f49fa09a0122fc2edd1) — `81bf17b23123e4ef8b9d5f49fa09a0122fc2edd1` | 2026-09-03T15:23:25Z | Core 1.2.11 — 2026-08-11; latest release separately sdk==0.4.4 |
| E320 | [temporalio/temporal](https://github.com/temporalio/temporal/commit/2220587dea828d938fc99253e178a13d1cb658c5) — `2220587dea828d938fc99253e178a13d1cb658c5` | 2026-09-04T04:55:01Z | v1.31.2 — 2026-07-08; server release distinct from HEAD and Python SDK |
| E322 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands/commit/4524a919930d62535a5cdca143c8a54eaf0ede42) — `4524a919930d62535a5cdca143c8a54eaf0ede42` | 2026-09-03T17:02:36Z | Commit pin; Agent Canvas beta, not the separate SDK |
| E323 | [OpenHands/software-agent-sdk](https://github.com/OpenHands/software-agent-sdk/commit/07307cb8edfcd9b4675be2761df0646d075a9c36) — `07307cb8edfcd9b4675be2761df0646d075a9c36` | 2026-09-03T17:25:05Z | v1.44.1 — 2026-08-28; separate from HEAD |
| E326 | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents/commit/afff4f8841bcc370d01c2739f53e882a92ef5c6a) — `afff4f8841bcc370d01c2739f53e882a92ef5c6a` | 2026-09-04T02:35:04Z | deepagents==0.7.13 — 2026-09-02; separate from HEAD |

Codex release tag object `79016fcca2c514d9c38643d8b7970a021e829b3b` resolves to `657a993cbee87acf52d14b758ce49dbd46d1b8eb`; just tag object `ebedee5bafe1ce779e93d91a2eff0c1bf3687b9c` resolves to `7f4ef81bd6a93faa2b28430912c8e9ab0e3dd29a`; Task tag object `a10322cd63f94d8bc8b48bb5c0e80eec10eda1e7` resolves to `ff3372fc50a47348610d722616f1a073aace0513`. Tag refs and objects were both read; tag-name mutability is not confused with commit identity.

The other named releases were not presumed to identify their later reported HEAD commits. For example, Playwright's September HEAD and July release are explicitly different evidence subjects; LangGraph's latest repository release belongs to its SDK rather than the core package. No material pin/version/provenance mismatch was found.

## Appendix C — Local supporting evidence and serialization

Fresh connector-retrieved repository evidence, independent public-document captures, parsed ledger results and canonical commit checks are retained under `fresh-dr005-source-review-evidence/` beside this record. The canonical report itself is `ADW-DR-005-SOURCE-REVIEW-001.md`; the supporting directory does not become another mutable repository-state owner.

The review record is serialized as UTF-8 without BOM, LF-only, with exactly one final LF. Its exact raw byte count and lowercase SHA-256 are calculated after writing and returned with the delivery. They are not embedded inside the hashed record.

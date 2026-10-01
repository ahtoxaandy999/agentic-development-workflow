---
id: ADW-LOCAL-LLM-INTEGRATION-DESIGN-001
artifact: local-llm-integration-design
artifact_status: draft
authority: evidence
owner: chatgpt-coordinator
normative_effect: none
design_stage: initial-proposal
produced_on: 2026-09-28
evidence_as_of: 2026-09-28
design_execution_base: 0d8805255556dfa86a18c28d95b7602b69164172
register_ref: docs/research/research-register.md
supersedes: null
---

# Local LLM integration: first bounded design

## 1. Scope and decision boundary

**PROPOSAL.** Introduce one supervised, request/response local-model boundary.
Use gpt-oss for advisory interpretation and Gemma for bounded generation.
Neither receives tools, credentials, a working checkout or authority to act.
A deterministic wrapper validates inputs and outputs and enforces decisions
supplied by the existing accountable owners. It does not invent authorization,
semantic acceptance or review conclusions.

This document proposes contracts and a later pilot, not runtime code or an
operating-policy amendment. No model/runtime adoption, installation, system
configuration, product mutation, automated publication, unattended/AFK execution
or new baseline is authorized. Every “must” below describes proposed behavior.
The current task authorizes this design candidate and its draft PR only.

The helper in section 9 prepares prompts and faithfully persists already-authored
gate evidence under a later bounded write grant. It is separable from local
inference and works without either model. No daemon, scheduler, agent framework,
new tracker, skill, hook or model-serving replacement is selected.

## 2. Authority, evidence and reuse

All repository paths in this table are relative to this repository at exact base
`0d8805255556dfa86a18c28d95b7602b69164172`, unless another identity is stated.

| Existing owner/input | Design consequence |
|---|---|
| `PROJECT-CHARTER.md`, `AGENTS.md`, `WORKFLOW-V1.md` | Existing roles, authorization, immutable candidates and adoption boundaries remain controlling |
| Workflow v1 incorporated semantic source: `docs/design/ADW-WF1-DESIGN-001.md`, blob `afed983e7632caf3169dcbac7a80f8da8226d86d`, proposal section incorporated by `WORKFLOW-V1.md` from commit `2b9532682ae77bf5037f1b2fa45b720e5865d0ad` | Keep orthogonal state planes, accountable gate owners, correction invalidation, containment and operation-aware recovery |
| `docs/design/ADW-WF1-TOOLING-DESIGN-001.md`, blob `2e0c640e8cab61b0bf165712c27e02ff9a455ec6` | Reuse one recorder, exact input/evidence bindings and attributed decisions; do not instantiate proposed product-task directories |
| `docs/design/ADW-WF1-TASK-CONTROL-REFERENCE-001.md`, blob `1968993da7dded58d70d705ef3d23165667e94b4` | Normalized model input is a disposable projection, never another state owner |
| `docs/design/ADW-WF1-GATE-EVALUATION-REFERENCE-001.md`, blob `5c08148db6f0d96197b268c3567a15a4981aff81` | Required/current/pass differs from unsatisfied, invalid, stale and justified N/A; missing evidence never passes |
| `docs/design/ADW-WF1-SERIALIZED-PERSISTENCE-PLAN-REFERENCE-001.md`, blob `c5a51d1e32541c24069144258bcbbcf02e37a66a` | Preserve preparation, attempt and readback separation; its explanatory narrow-path examples do not replace the later protected PR mechanism |
| `docs/design/ADW-WF1-PROTECTED-SERIALIZED-WRITE-PATH-OPERATIONAL-USE-SCOPING-001.md`, blob `88caf8aacf95030f16858a18279298c4b4d7f837` | One supervised candidate branch, draft PR, independent exact-SHA review, coordinator disposition, separately authorized ready/merge, readback |
| `docs/policies/research-evidence.md`; `docs/research/research-register.md` | Evidence is not adoption; Register alone owns mutable ADW gates |

The tooling design and references remain non-normative implementation inputs.
No new RG1-RG12 resolution, D13 mechanism selection, writer fence or permission
profile is claimed. DI-1 and DI-2 remain intact. The only accepted repository
baseline remains `13b05e075ec04aa91494cd18f7d29f7249028cb5`; current main and
publication acceptance do not replace it.

**VERIFIED GATE EVIDENCE.** PR #25 recovered
[full independent review](https://github.com/ahtoxaandy999/agentic-development-workflow/pull/25#issuecomment-5870603955)
and [coordinator disposition](https://github.com/ahtoxaandy999/agentic-development-workflow/pull/25#issuecomment-5870605888)
bind `970a0b1711bd528a8030b0b8ff0323f2ca4565e6`.
Review is PASS with 0 BLOCKER, 0 MAJOR, 1 MINOR, 1 NOTE. Disposition records
`++m`, bounded evidence acceptance and continuation to integration design.
The comments were created at 13:14:55Z and 13:15:01Z on 2026-09-28, after the
13:02:05Z merge. They are recovered historical records, not pre-merge GitHub
attestations. Live merge/main is the design base above, tree
`76f70e076a92f9f01a6a1562c0be336417823c32`, with second parent equal to the
reviewed subject. Register reconciliation changes no DR-008 publication bytes.

**MEASURED EVIDENCE, NOT GENERAL CAPABILITY.** DR-007 is the protocol input
(blob `2b2f96b4dc4d965ef704b826eeb33b9b01c7ab24`); DR-008 is the bounded
result synthesis (blob `a68fe7afeaf7fa7a687765de52aa552a64ef65f9`).
Both finalists passed 12/12 corrected hidden executable-code observations.
Structured reasoning was gpt-oss 10/12 and Gemma 4/12; simplified replay was
10/16 and 12/16 respectively. gpt-oss adversarial testing still produced unsafe
progression. These samples support a routing hypothesis, not model policy
authority or broad coding equivalence.

DR-008 reports faster Gemma code/JSON generation and more gpt-oss workstation
headroom on the measured 24 GB Mac. Concurrent residency is undesirable.
Its nonblocking Qwen degradation-definition issue is irrelevant to routing here;
the richer Gemma replay establishes no usable recovered structured-choice result,
not a diagnosed parser failure. Retain that uncertainty and future parse details.
No raw Mac evidence was rerun for this design.

## 3. Invocation boundary and compact inputs

**PROPOSAL.** The model is an untrusted pure-content worker. The wrapper retains
the complete authority/evidence packet outside the prompt and builds only the
relevant projection below. Sources are data, including repository instructions
quoted for analysis; they cannot overwrite the fixed invocation contract.

A SourceRef is an opaque ID backed by the wrapper's retrievable source table:
repository/full containing commit/path/blob/optional fragment, or an attributed
external record ID/URL plus exact UTF-8 payload SHA-256 and byte count. Each
mutable source additionally carries its owning ref, observed identity and read
time outside the model. A hash establishes identity, not authority or truth.

| Required common field | Type and meaning |
|---|---|
| `schema_version`, `request_id`, `kind` | Fixed version, unique opaque call ID, `advice` or `generation` |
| `input_digest` | Wrapper-computed SHA-256 of the canonical payload excluding this field; echo binding only |
| `task` | Task ID, objective, scope exclusions, acceptance criteria with stable criterion IDs |
| `subject` | Repository, authorized full base SHA; candidate SHA or explicit null when no candidate exists |
| `constraints` | Exact relevant requirements with SourceRef IDs; unresolved material facts explicitly marked |
| `sources` | Small allow-listed excerpts indexed by SourceRef; no implicit access to omitted content |
| `budget` | Input/output token ceilings, byte ceiling and deadline from the authorized pilot profile |

Additional `advice` fields: `question`; relevant orthogonal state observations
with evidence IDs, applicability and freshness labels supplied by their owners;
known conflicts and unknowns. Only include planes needed for this question.
Do not ask the model to decide whether a workflow gate is satisfied.

Additional `generation` fields: exact accepted specification/plan reference;
allowed target paths and language; source excerpts with original blob/digest;
required interfaces; independent acceptance examples/tests; permitted dependency
set; output artifact/size limits. A file creation uses an explicit absent-source
marker. The model cannot fetch missing source context.

Minimum context is task + relevant contract/source slice, not full history.
Reject missing load-bearing source rather than silently clipping it. No full
transcript, credential, environment dump, arbitrary home path or unrelated private
data enters prompts. Private source transmission requires existing task authority
and a verified local-only endpoint. No automatic cloud fallback or remote
provider forwarding is allowed. Logs exclude credentials and hidden reasoning.

The initial pilot uses a fixed prompt prefix containing only stable contract and
schema text, then the request-specific payload. No live state is cached as
authority. Output is returned to the wrapper, not directly to an executor.

## 4. Output contracts

All outputs are one complete JSON object, UTF-8, with required keys, bounded
strings/arrays, no unknown keys, duplicate keys, surrounding prose or code fences.
The future implementation must freeze a concrete schema and limits before use.
No permissive JSON repair, missing-key defaults or extracting a plausible fragment
from truncated output. Format validity is separate from semantic correctness.

| gpt-oss `advice` output | Contract |
|---|---|
| `schema_version`, `request_id`, `input_digest` | Exact echoed binding |
| `interpretation` | Concise task interpretation, not a gate verdict |
| `claims` | List of claim text + evidence IDs; unsupported claims labeled inference |
| `risks` | Risk text + affected criterion IDs |
| `unresolved_facts` | Missing/conflicting facts + evidence required to resolve each |
| `proposed_plan` | Ordered proposal steps + criterion/source IDs; content work only |
| `uncertainty` | `low`, `medium` or `high` with a brief limitation; uncalibrated and never a routing/gate pass |

Semantic classification is limited to content labels such as ambiguity or
conflicting requirement. There are no `PASS`, `CONTINUE`, `next_action`,
`tool`, `tool_arguments`, authorization or authoritative transition fields.
A plan is not accepted because the JSON validates. The task owner must resolve
material intent and accept any plan needed for downstream generation.

| Gemma `generation` output | Contract |
|---|---|
| `schema_version`, `request_id`, `input_digest` | Exact echoed binding |
| `spec_ref` | Exact input specification/accepted-plan reference |
| `artifacts` | Bounded list of target path, `create` or `replace`, original blob/digest or absent marker, complete proposed UTF-8 content |
| `criterion_coverage` | Criterion IDs with artifact references and concise explanation; not test results |
| `limitations` | Explicit unsupported/missing requirements; nonempty material limitation blocks application |

Choose full replacement content for small bounded files to avoid ambiguous patch
application. Deletion, rename, permissions, symlink, binary, dependency or system
configuration changes are outside this first contract. Larger work is separately
scoped, not silently chunked into an unverified whole. Existing tests supplied as
requirements cannot be weakened. Model-generated tests never alone establish
correctness.

Generated code is inert data. Path canonicalization rejects absolute paths,
traversal, duplicate targets and escape through existing symlinks. Original
identity must still match before any later application. No shell command or code
is executed as a consequence of parsing. A separately authorized deterministic
executor may apply the validated contents, run project-defined independent checks
in an authorized isolation profile, and form a candidate. No execution environment
or sandbox is selected by this design.

Tool-looking text is never dispatched. Unexpected tool calls or control envelopes
invalidate the output; legitimate code syntax inside an allowed content string
remains data. Schema-valid prose proposing unauthorized action is quarantined by
the supervisor. The wrapper has no execution edge from any model-proposed action,
so safety does not depend on recognizing every malicious sentence.

## 5. Routing and residency

Routing is a deterministic lookup from a supervisor-confirmed task class and
measured batch economics. A model cannot classify itself into greater authority.

| Route | Eligibility |
|---|---|
| gpt-oss only | Bounded interpretation, planning, ambiguity/evidence analysis or advisory review; no authoritative verdict requested |
| Gemma only | Fully specified generation/transform task with fixed sources, criteria and scope, no material unresolved intent; residency/switch rule passes |
| gpt-oss then Gemma | Advice materially needed; supervisor resolves uncertainties and accepts the resulting bounded specification before a new generation request |
| Neither | Mechanical prompt rendering, live reads, gate/authority/retry decisions, review verdicts, acceptance/publication; missing evidence or authority; unsuitable confidentiality/resources/context; trivial work cheaper deterministically |

gpt-oss is not a mandatory front end for clear tasks. Do not switch to Gemma
merely because a request contains code. Qwen is not an automatic fallback:
DR-008 retained it as a reference, not an adopted route.

**PROPOSED 24 GB POLICY.** One supervised inference request and one resident
finalist at a time. At a phase boundary: finish/cancel the outstanding request,
verify cessation, request unload using a later verified runtime interface,
observe that the old model is absent, inspect memory pressure, then load and
verify the exact next model digest. Absence of an HTTP response is not proof of
unload. Do not load the second model while residency is uncertain. Do not kill
unrelated processes or modify Ollama/global system settings.

Initial qualification binds the DR-008 model digests:
gpt-oss `17052f91a42e97930aa6e28a6c6c06a983e6a58dbb00434885a0cf5313e376f7`;
Gemma `f60799545325362bdaa15cbf38694f997514d3d46425c900b4eb06c1d6422d18`.
A changed tag/digest/runtime invalidates calibration and requires qualification.
DR-008 used Ollama 0.34.4; this is historical evidence, not a current-version claim.

Start qualification at a proposed 4K total context; explicit input plus output
reservation must fit. A larger profile requires separate measured qualification.
Do not interpret the exploratory Gemma 32K result as safe operating capacity.
Batch ready same-model requests only within the existing authorized task/domain,
while rereading mutable prerequisites per request. Do not delay urgent work to
fill a batch or carry sensitive prefixes across tasks.

There is no evidenced universal minimum token count for switching. Calibrate
paired equivalent tasks and cold loads on the actual daily environment:
switch only if the conservative expected generation-time saving over the
already-authorized alternative exceeds unload + load + lost-prefill/cache +
expected return-switch + extra verification/rework cost. Use the lower observed
saving and upper observed overhead from calibration. Equality means no switch.
Record the smallest tested batch satisfying this inequality as that profile's
minimum; below it or without calibration, do not switch for a speed claim.
Different model tokenizers and reasoning overhead make raw tok/s insufficient.

Measure cold and warm paths separately. Stable prefixes may reuse cache, but a
warm model is not proof of cache reuse. Fresh inputs and authority always remain
outside cache trust. Report first visible response separately from first internal
output. At task end, unload the task-owned model under the pilot grant and verify
cessation; no indefinite residency is proposed.

Load failure, warning/critical memory pressure, continuing swap growth, runtime
instability or material responsiveness loss stop the batch. Exact observation
intervals/deadlines and swap-growth limits must be frozen in the pilot grant;
missing limits deny dispatch. Never treat swap as added RAM. A later authorized,
qualified gpt-oss route may be selected only after failed-model cessation and
fresh context/resource checks; otherwise stop. No automatic install, alternate
model pull, context expansion, process killing or paid-service escalation.

## 6. Deterministic wrapper and authority ownership

The wrapper enforces machine-checkable predicates and records decisions from
their owners; it cannot turn arbitrary prose into new authority. The existing
coordinator, task owner and appointed reviewer retain their decision roles.
A missing or ambiguous human decision fails closed.

| Boundary | Required invariant and response on failure |
|---|---|
| Before call | Verify target device/account/repository and endpoint; task/actor authority and bounded route; current normative/contract inputs; exact base/candidate; source completeness; no unresolved side effect, cancellation or recovery obligation |
| Evidence | Read relied-upon mutable refs and owner records at dispatch; validate every required gate's subject, criteria, applicability, evidence and freshness. Timestamp/TTL alone never establishes freshness |
| Review input | Exact unchanged candidate, scope, reviewer assignment/provenance and independent-review requirement. Invalid subject or stale prior PASS blocks dependent progression |
| Resource/input | Qualified runtime/model digest and context; one resident model; no active competing call; secret-safe payload and bounded deadline/bytes/tokens |
| After call | Complete response and matching request/input binding; strict schema and ceilings; known source/criterion/path references; no unauthorized operation envelope |
| Before use | Reread mutable state, authority, candidate and all relied-upon inputs. Any drift invalidates affected output; preserve prior identity, do not retarget or rebase automatically |
| Before later effects | Existing executor owns exact tool allow-list, destination, argument validation, operation identity, effect ceiling and attempt/reconciliation rules. Model supplies no tool selection |
| READY/publication | Existing protected flow, actual independent review, explicit disposition and mutation grant, exact accepted head, live protection and fresh readback. Neither model nor helper can manufacture any predicate |

Pre/post reads detect drift but are not an atomic writer fence. Candidate-branch
exclusivity remains procedural under the protected supervised path. This design
does not claim D13 fencing or general automation conformance. Mutations remain
in existing authorized surfaces and must satisfy their own race controls.

The normalization projection and transport receipts never own task state.
Register is still ADW's sole mutable gate owner. Product tasks use their actual
appointed owner, not a newly invented duplicate. Wrapper denial blocks its
dependent effects; it does not by itself cancel, abandon or accept a task.

## 7. Failure handling

| Failure | Proposed response |
|---|---|
| Timeout or truncated output/reasoning stream | Reject partial result; cancel only the task-owned request, establish cessation; hidden reasoning is neither required evidence nor retained |
| Malformed JSON/schema, unknown keys, wrong IDs, extra fences | Reject whole output, retain secret-safe visible response and exact parser/validation error; never normalize it into a pass |
| Context overflow | Deny call or reject runtime truncation; reduce only irrelevant context under owner-approved scope, never drop requirements; new payload has a new identity |
| Unexpected tool-like envelope or unauthorized proposal | Quarantine; no tool execution or next-step promotion; supervisor resolves the incident |
| Unload/crash/low memory | Mark resource episode failed; verify no in-flight generation, stop batch; no blind restart or second-model load |
| Model disagrees with deterministic state | State/authority owners prevail; retain advisory disagreement, block any dependent proposal requiring unresolved interpretation |
| Live-state drift or invalid review subject | Mark affected advice/evidence stale; exact new candidate needs fresh affected independent review, never inherited PASS |
| Ambiguous external write, including PR comment | Freeze further dependent effects; reconcile live operation/target before any retry; retries need applicable operation-specific authority |
| Required evidence inaccessible or altered | No substitute from chat or local recollection; stop only dependent work and identify missing custodian/source |

Initial pilot has zero automatic model retries. A supervisor may authorize one
bounded new attempt with corrected input only after cessation/reconciliation;
it receives a new request ID and counts toward rework and cost. An output failure
cannot cause a destructive fallback or widen permissions. Read-only call failure
does not erase already-completed external effects.

## 8. Review independence

Local review assistance is advisory only in every proposed stage. It can suggest
risks, missing evidence or test cases; it cannot emit the authoritative review
verdict, accept a candidate or satisfy the independent-review gate.

Candidate production records disclose the participating model, exact digest,
profile and source/input identities. The producer and any model invocation that
generated the candidate cannot independently review or accept that same subject.
Using the other finalist, a new context or a different display name alone does
not establish independence. An eligible conflict-free reviewer must be appointed
under existing governance and inspect the exact full candidate and owning
contracts. Producer summaries and green checks are not review substitutes.
The first pilot does not use local models to supply independent verdicts.

## 9. Mechanical gate-evidence and prompt helper

**PROPOSAL, NOT ENABLEMENT.** One supervised helper consumes an owner-supplied
event and a fixed versioned prompt template. It reads live GitHub, validates
identity/transport completeness, faithfully stores attributed records and renders
the authorized next prompt. It neither chooses a semantic transition nor decides
PASS, acceptance, authority or merge eligibility. Unsupported/conflicting event
types are returned to the coordinator. No chat submission or fresh reviewer
creation occurs automatically in this first design.

Minimum event envelope: task/repository/PR; event ID/type; exact subject;
originating actor/role and assignment/authority references; full report or
decision payload; payload UTF-8 SHA-256/bytes; prior evidence references;
next-gate instruction if supplied by its accountable owner. A typed verdict
field must agree with the reviewer's report; conflict blocks transport reliance.
Actor entitlement and independence are verified against the appointed assignment,
not inferred from whoever uploads the GitHub comment.

The helper receives only the separately authorized operations needed for live
reads and append-only comments on the exact PR. It has no merge, ready, contents,
branch, workflow, settings or credential-management operation in its allow-list.
Backend credential scope may be broader than this allow-list; that residual
risk must be assessed before operational authorization, not claimed eliminated.
The publisher remains a distinct existing supervised role/surface.

| Verified event supplied by owner | Mechanical result |
|---|---|
| Candidate produced | Read repository/PR identity, current full head C, base B, tree/parents and complete diff; match task scope and producer evidence; render fresh-review prompt with exact C from live state |
| Review completed | Validate assignment, exact reviewed C, full findings/report and source identity; persist complete report to the PR, read it back and verify bytes/hash before downstream reliance |
| CORRECTION REQUIRED | Render correction prompt for reviewed C with exact findings and bounded granted scope; render subsequent-review template with candidate slot unresolved. Do not invent corrected C or dispatch correction without its grant |
| Corrected candidate produced | Verify new live full C and authorized ancestry/delta; preserve prior candidate/review, replace only the template's unresolved slot with verified C; require fresh affected independent review |
| PASS | After full report persistence/readback, render coordinator disposition/publication prompt for that exact C. PASS alone supplies no acceptance, ready or merge grant |
| Coordinator disposition supplied | Persist full exact-subject decision and explicit authorized effects/conditions to PR; verify readback before publication can rely on it. Rejected/deferred/missing publication authority cannot render an executable publication instruction |
| Publication observed | Read actual PR/merge, ordered parents/tree/delta and published artifacts; obtain existing publisher's verified completion and owner's authorized next gate. Render only that next prompt, using new live state and authoritative pointers |

For this ADW profile, publication uses method merge and preserves accepted C as
second parent. A different topology, changed base/head, already-merged PR at a
pre-publication event, mismatched report subject or missing required record blocks
the affected template. An already-merged event performs readback only and never
requests another merge. Publication is not baseline or product acceptance.

Each rendered prompt includes role, exact subject, owning contract/evidence
pointers, allowed paths/actions, criteria, non-goals, stop boundary and result
destination. It includes the requirement to reread live state at actual use.
It is navigation, never a stored authorization token. A stale unsent prompt is
discarded and recreated from verified inputs. Review templates contain no
producer-supplied expected verdict.

Persist the complete original report, including findings, limitations and
provenance, inside a mechanical envelope stating who authored it and who copied
it. Persist the complete coordinator decision before ready/merge, including
review reference, exact subject, acceptance scope, effects and next-gate scope.
Do not abbreviate a report to PASS. Do not interpret an unbound “++m” string:
its issuer and exact-subject proposal must be recorded as an explicit decision.
If content contains secrets or exceeds transport limits, block persistence and
seek an authorized safe full-report custody decision; do not silently truncate,
redact material evidence or spill to another service.

Comments are retrievable but editable, not cryptographically immutable.
Record comment ID/URL, subject, payload digest/bytes, created/updated times and
attribution; verify full bytes at each dependent reliance. A changed/deleted
record invalidates reliance. A correction appends a successor identifying the
superseded record rather than editing history. The custodian is the appointed
repository maintainer for the authorized review/publication/continuation interval.
No new permanent evidence directory or second gate tracker is created.

Deduplicate using repository + PR + event ID + subject + payload digest. Before
posting, enumerate all relevant comment pages and compare complete envelopes.
Exactly one identical event returns its verified receipt; conflicting duplicates
block. An absent event permits one post only under an unconsumed write grant.
After timeout/ambiguous post, reread before any further effect. If one exact
record exists, adopt the receipt without reposting; absence after a timeout alone
does not authorize retry because a delayed write may still complete. Require
operation reconciliation and a fresh bounded recovery grant. Late callbacks for
an old candidate may be retained as historical evidence but cannot advance C.

Transport receipts record observations only. The existing state recorder remains
responsible for an authorized Register update when needed; the helper cannot
silently update it. No candidate is rewritten merely to insert its own review.
A next prompt is generated only when an actual owner-authorized next gate is
known; otherwise produce a bounded request for that missing decision.

## 10. Stages, pilot metrics and acceptance proposal

Every stage below needs its own explicit authorization after this design's
independent review and coordinator disposition. Description grants no stage.

| Stage | Bounded pilot and stopping point |
|---|---|
| 1. Advisory gpt-oss | Supervised read-only advice on fixed normalized inputs; no model-generated repository effects. Separately qualify helper rendering with fixtures, then bounded PR evidence writes only under explicit grant |
| 2. Bounded Gemma generation | Fixed low-risk tasks; outputs remain inert until existing executor is separately authorized; independent verification/review remain unchanged |
| 3. Measured routing | Use per-class measured quality, switching costs and resource limits; no learned gate policy or mandatory two-model chain |
| Later only | Deeper automation requires new evidence, threat/conformance assessment, explicit mechanism/adoption decisions and any required normative amendment |

Before a pilot, freeze schemas/templates, exact runtime/model/profile identities,
limits/timeouts, resource stop thresholds, endpoint/network isolation, task
classes, independent expected results, supervision/actors, allowed writes and
custody. None is silently supplied by a model. Use a small proposed first sample:
10 paired representative tasks per eligible class, plus at least three repetitions
of every negative guard scenario below. This estimates utility; it is not proof
of universal safety. No runtime tests have been executed by this design task.

| Metric | Capture and comparison |
|---|---|
| Paid usage | Calls and input/output tokens, available cost/usage before/after; compare paired tasks against existing authorized workflow, include fallback and rework; unavailable usage is unknown |
| Token/context cost | Local input/output, reasoning counts only if exposed, prompt bytes, cache counts and context profile; do not equate local tokens with paid tokens |
| Wall-clock | End-to-end task and gate latency, first visible output, generation, cold load/unload, prefill/cache, verification/review, waiting and manual time; report paired totals and median/p95 with sample count |
| Quality | First-pass independently accepted candidates / submitted candidates; advisory usefulness separately judged; schema-invalid and semantic errors separately counted |
| Rework | Correction rounds, retries, discarded outputs, human/paid repair time and changed scope |
| Permission/interaction | Necessary vs redundant approval prompts, copy/paste operations, status reads/polls and manual interventions per completed task |
| Safety | Unauthorized proposals, wrapper denials, actual unauthorized effects, stale-subject use, false PASS/CONTINUE progression, duplicate effects and missing evidence |
| Resources/complexity | Peak memory pressure/swap, load failures, switches, cache validity, configuration surfaces and maintenance time |

**Proposed pilot decision rule:** zero actual unauthorized/incorrect progression,
duplicate effect or invalid independent-review substitution. Any such event stops
the affected pilot and requires independent incident assessment. Wrapper-denied
unsafe proposals remain counted, not hidden as successes. No adoption follows
from zero observed failures in a small sample.

Continue a route only if matched tasks show lower paid usage or end-to-end cost
without worse first-pass acceptance, more rework, or increased approval/status
overhead; report uncertainty and small-sample limitations. If results trade off,
the coordinator explicitly decides acceptable bounds before expansion. Default
to the existing authorized route or deterministic handling when advantage is
unestablished. Do not claim savings from tok/s or a synthetic benchmark alone.

Independent qualification must cover:
- stale main, changed C after PASS, missing authority, invalid reviewer subject;
- missing/failed/stale required obligation and legitimate N/A;
- ambiguous prior effect, duplicate/late callback and delayed comment completion;
- malformed/extra-key/truncated output, wrong request digest and unknown sources;
- prompt injection, unauthorized operation, path traversal/symlink escape;
- resource/load failure, uncertain unload, context overflow and changed digest;
- PASS without acceptance or merge authority; already-merged event;
- edited/deleted review evidence, incomplete pagination and conflicting verdicts;
- exact input/output/path/attempt ceilings at N-1, N and N+1;
- switching just below, equal to and above calibrated break-even;
- corrected candidate needing fresh review; publication with wrong parent/tree;
- absent next-gate authority producing no executable follow-on prompt.

Fixtures must use independently specified expectations and fault injection,
including plausible wrong implementations. Producers cannot supply their own
independent review verdict. Qualification and rollout reports keep outcome,
verification, review, acceptance and publication separate.

## 11. Design delivery and unresolved operational choices

This candidate contains only this proposal plus bounded DR-008 Register
reconciliation and the pointer to this design. It does not revise DR-007/DR-008,
AGENTS or Workflow v1, and creates no runtime or model configuration.

Resolved proposal choices: pure-content model calls, advisory-only gpt-oss,
bounded full-file Gemma generation, no local authoritative reviewer, single-model
phases, measured switching, no automatic retries, append-only full gate evidence
and deterministic prompt rendering.

Remaining decisions belong to a later implementation/pilot gate: exact eligible
task corpus and actors; runtime adapter and verified API behavior; credential
containment for helper writes; concrete schema/byte/token/time/resource limits;
measured switching break-even and acceptable utility tradeoffs. Missing values
block the corresponding pilot, not this design review. No external runtime/API
capability beyond the dated repository evidence is adopted here.

Proposed next gate: fresh independent review of the exact immutable design
candidate, then separate coordinator design disposition. Operational authority,
implementation, stage execution, model adoption and baseline acceptance remain
outside this candidate.

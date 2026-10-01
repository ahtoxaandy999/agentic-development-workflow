---
id: DR-009
artifact_status: draft
authority: evidence
research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: 2026-09-28
owner: agentic-development-research
question: >-
  What exact effective Ollama runtime/API contract exists on the authorized
  MacBook Pro M5 Pro 24 GB for gpt-oss:20b and gemma4:26b-nvfp4, and which
  runtime uncertainties must be resolved before a deterministic local-model
  adapter can be implemented safely?
scope: >-
  Bounded runtime/API qualification only. Verify current runtime, endpoint,
  installed finalist identities, structured-output behavior, reasoning fields,
  residency/unload, client cancellation/cessation and context-overflow behavior.
  Produce compact non-sensitive local evidence and a repository research
  candidate. No adapter implementation, model pilot, installation, upgrade,
  runtime reconfiguration, model/runtime adoption, Workflow v1 amendment or
  baseline acceptance.
repository_state:
  repository: ahtoxaandy999/agentic-development-workflow
  research_basis_main: df96ac3a865fd82083647067a5af7c29f553c202
  published_integration_design: docs/design/ADW-LOCAL-LLM-INTEGRATION-DESIGN-001.md
  published_integration_design_subject: c2d30acbac0b9024d55a4714feba51edea1b1fd6
  published_integration_design_blob: 869620ed0cb2e17bd598344c5dad36ffb1b7e02e
  research_policy: docs/policies/research-evidence.md
  mutable_research_state_owner: docs/research/research-register.md
supersedes: null
---

# ADW-DR-009 — Local LLM effective runtime/API qualification

## 1. Executive answer

**RESULT: QUALIFIED WITH BLOCKERS.**

**MEASURED FACT.** The authorized target remains MacBook Pro `Mac17,9`,
Apple M5 Pro, 24 GB unified memory, running macOS 26.7 build `25G229`.
Ollama CLI and server both report `0.34.4`. The effective service listener is
`127.0.0.1:11434` only.

**MEASURED FACT.** The two finalists are installed under the same exact digests
used by DR-008:

- `gpt-oss:20b`:
  `17052f91a42e97930aa6e28a6c6c06a983e6a58dbb00434885a0cf5313e376f7`;
- `gemma4:26b-nvfp4`:
  `f60799545325362bdaa15cbf38694f997514d3d46425c900b4eb06c1d6422d18`.

No finalist calibration is stale by runtime/tag/digest identity.

**MEASURED FACT.** Strict JSON-schema output works without repair for both
finalists, but only under model-specific request profiles. Residency and unload
are observable. Client cancellation caused the active gpt-oss generation to
cease, but positive cessation was established through the local Ollama server
log rather than a supported request-status API.

**MEASURED FACT.** The effective runtime is not fail-closed on declared context
budget. With intentionally over-budget synthetic input, gpt-oss truncated the
prompt without an API error; Gemma's MLX path processed the full oversized prompt
despite a smaller declared `num_ctx`.

**RECOMMENDATION.** Do not implement the deterministic adapter yet. Resolve two
load-bearing semantics first: supported timeout/cancellation reconciliation, and
adapter-owned or otherwise proven fail-closed pre-request token/context budget
enforcement. The endpoint, exact model identities, structured-output profiles
and residency/unload behavior are sufficiently qualified to constrain that later
design.

This recommendation does not adopt either model, Ollama, a production context
limit, or an implementation mechanism.

## 2. Authority and prior gate state

The controlling repository owners are `PROJECT-CHARTER.md`,
`WORKFLOW-V1.md`, `docs/policies/research-evidence.md` and the Research
Register. The published integration design is a non-normative design basis.

Live GitHub at the research boundary established:

- design exact subject:
  `c2d30acbac0b9024d55a4714feba51edea1b1fd6`;
- independent review PASS: PR #26 comment `5871186931`,
  findings `0 BLOCKER | 0 MAJOR | 1 MINOR | 1 NOTE`;
- coordinator design ACCEPT: PR #26 comment `5872023875`;
- protected publication merge/current research base:
  `df96ac3a865fd82083647067a5af7c29f553c202`;
- publication receipt: PR #26 comment `5872291302`;
- published design blob:
  `869620ed0cb2e17bd598344c5dad36ffb1b7e02e`.

The design-review MINOR 1 about the pilot quality metric wording is carried as a
nonblocking follow-up. This candidate does not rewrite the published design.

## 3. Current official documented behavior

Current Ollama primary documentation, checked 2026-09-28, documents:

- `POST /api/chat` and `POST /api/generate` request/response surfaces,
  including `stream`, `think`, `format`, options and `keep_alive`;
- a JSON schema supplied through `format` for structured output;
- reasoning/thinking returned separately from normal response content for
  thinking-enabled models;
- `GET /api/ps` for currently loaded models;
- `keep_alive: 0` as an unload request;
- localhost `127.0.0.1:11434` as the default bind;
- automatic context defaults on the Context Length page based on detected VRAM:
  less than 24 GiB -> 4k, 24-48 GiB -> 32k, and at least 48 GiB -> 256k;
- the separately scoped Modelfile reference documents `num_ctx` as the context
  window parameter, currently labels its parameter default as 2048, and uses
  4096 as an example value.

These documentation surfaces have different scopes and are not treated as proof
of the exact effective request budget on this Mac. Every qualification probe
whose conclusion depends on context supplied `num_ctx` explicitly and measured
the resulting runtime behavior.

Primary sources:

- https://docs.ollama.com/api/chat
- https://docs.ollama.com/api/generate
- https://docs.ollama.com/capabilities/structured-outputs
- https://docs.ollama.com/api/ps
- https://docs.ollama.com/faq
- https://docs.ollama.com/context-length
- https://docs.ollama.com/modelfile
- https://docs.ollama.com/api/streaming
- https://docs.ollama.com/api/errors
- https://github.com/ollama/ollama/releases/tag/v0.34.4

**LIMITATION.** These documents describe current product behavior generally.
Claims about this machine below use direct observation where it differs or is
more specific. No current official API documentation inspected in this task
established a request identifier or request-status endpoint for reconciling a
generation after client disconnect.

## 4. Effective environment and identity

| Item | Measured result |
|---|---|
| Target | `atolkanets-mVQ` |
| Hardware | MacBook Pro `Mac17,9`, Apple M5 Pro, 24 GB |
| macOS | 26.7, build `25G229` |
| Ollama CLI | `0.34.4` |
| Ollama server API | `0.34.4` |
| HTTP endpoint | `http://127.0.0.1:11434` |
| Effective listener | IPv4 `127.0.0.1:11434` |
| Initial residency | `/api/ps -> {"models":[]}` |
| Final residency | `/api/ps -> {"models":[]}` |

The socket observation establishes machine-local binding for the Ollama listener.
It does not claim a separate network-wide audit of unrelated proxies or tunnels.

Installed model inventory additionally contained `qwen3.5:9b-mlx`, but it was
not loaded or tested by this qualification. No artifact was pulled, upgraded or
reconfigured.

Resource-safety checks were performed transiently during qualification, but the
final SHA-bound local bundle does not preserve the historical pre/post
`memory_pressure` or swap snapshots. Therefore this note does not claim exact
historical resource values as independently recoverable evidence. Resource
thresholds remain unqualified and no production resource limit or performance
comparison is established here.

## 5. Minimal effective structured-output contract

The test schema required four fixed fields, fixed values/enums,
`additionalProperties: false`, and independent exact-value validation. Every
PASS below was parsed and validated without repair.

### gpt-oss

Tested working profile:

- `POST /api/chat`;
- `stream: false`;
- `think: "low"`;
- `format: <strict JSON schema>`;
- `keep_alive: -1` during the bounded group;
- `temperature: 0`;
- `num_ctx: 4096`;
- `num_predict: 1024`.

Result: **3/3 strict-schema PASS**. `message.content` contained the complete
JSON object. `message.thinking` was a separate nonempty field. All three runs
ended with `done_reason: "stop"`.

Negative boundary observations are contract-relevant. With `think: true`,
`num_predict: 128` and then 512 were consumed largely by reasoning and did not
reliably produce complete visible JSON. On this exact runtime/model,
`think: false` still returned a nonempty `message.thinking` field and the
128-token cap ended before visible JSON. Therefore generic `think: false`
semantics must not be assumed for this gpt-oss artifact.

### Gemma

Tested working profile:

- `POST /api/chat`;
- `stream: false`;
- `think: false`;
- `format: <strict JSON schema>`;
- `keep_alive: -1` during the bounded group;
- `temperature: 0`;
- `num_ctx: 4096`;
- `num_predict: 128`.

Result: **3/3 strict-schema PASS**. `message.content` contained the complete
JSON object; the response message contained no `thinking` field. All three
runs ended with `done_reason: "stop"`.

With thinking enabled, both 128- and 512-token bounded profiles exhausted the
generation cap in reasoning before visible schema output. The effective adapter
profile must therefore treat thinking/output reservation as model-specific.

These are tested working profiles, not proofs that 1024 or 128 are universal
minimum output ceilings.

## 6. Residency and unload

For each finalist independently:

1. the resident set was checked before load;
2. only the target finalist was loaded;
3. `GET /api/ps` showed its exact tag and digest;
4. unload was requested through `POST /api/generate` with
   `stream: false, keep_alive: 0`;
5. repeated `GET /api/ps` independently verified an empty resident set.

The second finalist was not loaded until the first was verified absent. Initial
and final resident sets were empty. No unrelated resident model was killed or
unloaded.

**QUALIFIED:** `/api/ps` is sufficient for this bounded residency observation,
and `keep_alive: 0` plus independent `/api/ps` absence is an effective unload
procedure on this runtime.

## 7. Client cancellation and cessation

A harmless gpt-oss raw streaming generation was first loaded at the 4096 context
profile. The client then ended the request with a two-second curl deadline:

- curl exit: `28`;
- streamed response before disconnect: 11,810 bytes;
- the local Ollama server log recorded
  `cancel task, id_task = 1542`;
- the same log then recorded release of task `1542` with
  `stop processing`;
- an immediate short follow-up generation completed successfully in about
  0.308 seconds.

**MEASURED FACT.** The tested server ceased that generation after the client
disconnect. Closing the connection is not treated as proof by itself; cessation
is supported here by the cancel-plus-release log sequence.

**BLOCKER.** The native HTTP response/API surface inspected in this task exposed
no operation/request identifier and `/api/ps` exposes model residency rather
than in-flight request state. Positive reconciliation therefore currently
depends on internal local server logs. Before a deterministic timeout/recovery
implementation, either that log evidence must become an explicitly qualified and
supported adapter contract or another supported request-identity/status mechanism
must be established.

No process killing was used.

## 8. Context overflow and truncation

A fresh runner was used for each relevant over-budget probe. The input was
synthetic and approximately 41,427 UTF-8 bytes. No 32K/64K stress was performed.

### gpt-oss

Declared request profile: `num_ctx: 512`.

The server log reported an original prompt of 8,169 tokens and:

`truncating input prompt limit=258 prompt=8169 keep=4 new=258`.

The API still returned HTTP 200 with `prompt_eval_count: 258`; no API error
reported the input loss.

**MEASURED BEHAVIOR:** silent-from-the-client's-perspective truncation with a
server-side warning. This cannot satisfy the published design's proposed
fail-closed context-overflow behavior.

### Gemma MLX

Declared request profile: `num_ctx: 512`.

The API returned HTTP 200, `prompt_eval_count: 7221`, visible response `OK`,
and `/api/ps` reported `context_length: 2048`. The MLX runner log recorded
prompt-processing progress through all 7,221 tokens. No rejection or truncation
warning was observed.

**MEASURED BEHAVIOR:** the declared `num_ctx` did not operate as a hard request
budget on this Gemma MLX path.

The runtime provides post-request prompt counts, but this task did not establish
an exact pre-request token-count endpoint. Therefore an adapter cannot safely use
`num_ctx` alone as a fail-closed input-budget guard.

## 9. Common runtime behavior versus model/backend behavior

| Contract area | Common/effective runtime observation | Model/backend-specific observation |
|---|---|---|
| Endpoint | Both finalists use local `/api/chat` at `127.0.0.1:11434` | None needed |
| Structured schema | Both accept JSON schema via `format` | gpt-oss needs tested low-thinking/output reservation; Gemma passes with thinking disabled |
| Visible/reasoning fields | Chat returns visible content in `message.content` | gpt-oss returns separate nonempty `message.thinking`; Gemma working profile has no thinking field |
| Residency | `/api/ps` exposes loaded model tag/digest | Resident memory footprint differs |
| Unload | `keep_alive: 0` then `/api/ps` absence worked for both | Runner implementation differs |
| Cancellation | Client disconnect reached server-side cancellation in tested gpt-oss case | Positive evidence came from llama-server log; Gemma cancellation was not separately required |
| Over-budget input | Neither tested path failed closed at the HTTP boundary | gpt-oss truncated; Gemma MLX processed the oversized prompt |

## 10. Local evidence bundle

Compact evidence root:

`/Users/atolkanets/DR009-LOCAL-LLM-RUNTIME-QUALIFICATION-001`

Final SHA-256 identities:

| File | SHA-256 |
|---|---|
| `manifest.json` | `ecb8d30e267674d124b4a32b1b7728b13131f04f6e09da236f845ff2c1b15024` |
| `observations.jsonl` | `578d03a42d2bbf7f5993575a89a02dc6d4b149fe13919524f36fa2fcf44e3379` |
| `summary.md` | `b0789e823bbe16ff997ede35596b79520444039ec3f8f59ff0029683b371390f` |
| `probe.py` | `944f5762c7feac61d1eb270242f4907e14dad77ee5d748964b0e51f34c9afc7c` |
| `probe2.py` | `f125134bb836e291ba0b13e923b5469aa214a7c2f01ec153dabb60b7242350ef` |
| `probe3.py` | `ab343ada4e0370687f26901f2210e5c4caa2bbd8cddd59d5f0d6e55c76d433c8` |
| `probe4.py` | `8711ef8bb6992b839e06649a775a37dd3c83c01a4c21e7ae9cd3da3cd868f959` |

`SHA256SUMS` SHA-256:
`6c518d065ce2753d26e4073d92329458bac95a3ee8256e05353d65bac9103017`.

The bundle contains synthetic inputs, visible model output only where needed,
derived validation observations and probe scripts. It contains no credentials,
repository source content, private transcripts or retained hidden
chain-of-thought. It also does not preserve historical pre/post
`memory_pressure` or swap snapshots; no exact resource values rely on such
unbound observations in this corrected note.

## 11. Decision, blockers and next gate

### Qualified effective contract

The following can constrain later adapter design:

- exact Ollama/server identity `0.34.4`;
- machine-local listener `127.0.0.1:11434`;
- exact finalist tags/digests;
- model-specific strict structured-output profiles above;
- visible-versus-thinking field behavior for those profiles;
- exact residency observation via `/api/ps`;
- unload via `keep_alive: 0` plus independent absence verification.

### Blocking unknowns

1. **Timeout/cancellation reconciliation.** A supported deterministic mechanism
   must positively identify and reconcile the task-owned in-flight generation
   after client timeout/cancellation without assuming socket close equals
   cessation.
2. **Context-budget enforcement.** A fail-closed preflight token-accounting and
   context-budget mechanism must prevent input truncation/implicit expansion
   before model dispatch. The effective runtime behavior measured here cannot be
   used as that guard.

Resource/context/deadline thresholds remain the separately deferred operational
qualification decision described by the published design; this task does not
establish a production context limit.

### Recommendation and next gate

**RECOMMENDATION:** preserve the published deterministic-wrapper design, but
block adapter implementation paths that depend on the two unresolved semantics.
Resolve them in a separately authorized qualification/correction gate after this
evidence receives fresh independent review.

Exact next gate: **fresh independent review of the exact DR-009 candidate**.

No model is adopted by this conclusion. No Workflow v1 or baseline state changes.

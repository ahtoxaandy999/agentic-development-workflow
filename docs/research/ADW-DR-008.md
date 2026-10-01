---
id: DR-008
artifact_status: draft
authority: evidence
research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: 2026-09-28
owner: agentic-development-research
question: >-
  What did the executed local-LLM benchmark and workflow-specific evaluation
  establish about Qwen3.5 9B, gpt-oss-20b and Gemma 4 26B on the target
  MacBook Pro M5 Pro 24 GB, and what bounded role split is justified as input
  to a later local-model integration design?
scope: >-
  Empirical-result synthesis and integration recommendation only. Summarize the
  executed DR-007 protocol, corrected benchmark observations, workflow-specific
  replay evidence, model/resource tradeoffs and a proposed role split. No model
  adoption, no runtime adoption, no Workflow v1 amendment, no tooling
  implementation, no autonomous policy authority and no system configuration
  change.
repository_state:
  repository: ahtoxaandy999/agentic-development-workflow
  research_basis_main: 572a511775ec926d24a0be2c67b13c8db4e1043b
  benchmark_protocol: docs/research/ADW-DR-007.md
  workflow_v1_owner: WORKFLOW-V1.md
  research_policy: docs/policies/research-evidence.md
  mutable_research_state_owner: docs/research/research-register.md
supersedes: null
---

# ADW-DR-008 — Local LLM benchmark results and role-split evidence

## 1. Executive answer

**MEASURED FACT.** All three DR-007 candidates were installed and exercised on
the target 24 GB M5 Pro through Ollama 0.34.4 with exact model identities
recorded below. The benchmark evolved during measurement when defects were found
in cache isolation, cold/warm aggregation and hidden-test validators. Invalid
runs were retained as invalid evidence and excluded from final comparison.

**MEASURED FACT.** Qwen3.5 9B is the lightest candidate and preserves the most
workstation memory headroom, but it was materially slower and weaker on the
final executable-code and structured-reasoning suites.

**MEASURED FACT.** gpt-oss-20b is materially stronger than the other candidates
on explicit constraint-heavy structured reasoning and fits the 24 GB machine
with more headroom than Gemma. It is not safe as an autonomous workflow policy
engine: expanded adversarial testing still produced unsafe progression and
non-exact gate/evidence classification.

**MEASURED FACT.** Gemma 4 26B is the fastest tested code/JSON generator and
matched gpt-oss on the corrected executable-code suite. It uses substantially
more unified memory and reaches the practical memory boundary sooner at larger
context or competing memory load.

**RECOMMENDATION.** Do not select one universal local model from this evidence.
Use the following as the candidate integration hypothesis:

- `gpt-oss:20b` for planning, review, ambiguous-state interpretation and
  constraint-heavy semantic reasoning;
- `gemma4:26b-nvfp4` for code generation and larger execution/generation
  batches;
- deterministic workflow code remains authoritative for live-state freshness,
  exact candidate identity, review freshness, authority, transitions, tool
  selection/arguments, retry containment and merge/publication gates;
- Qwen3.5 9B remains a lightweight fallback/reference candidate rather than a
  primary route.

This is a research recommendation, not an adoption decision.

## 2. Exact measured environment

Target machine:

- MacBook Pro `Mac17,9`;
- Apple M5 Pro;
- 15 CPU cores and 16 GPU cores;
- 24 GB unified memory;
- macOS 26.7 build 25G229;
- Metal reports unified memory and
  `recommendedMaxWorkingSetSize = 17.76 GiB`;
- Ollama 0.34.4.

Exact model artifacts used:

| Candidate | Exact tag | Exact digest | Approx. artifact size |
|---|---|---|---:|
| Qwen3.5 9B | `qwen3.5:9b-mlx` | `203e30078279db51132b9e026ceb7bb21330e5b1af67ef190671b375c9770404` | 8.9 GB |
| gpt-oss 20B | `gpt-oss:20b` | `17052f91a42e97930aa6e28a6c6c06a983e6a58dbb00434885a0cf5313e376f7` | 13.8 GB |
| Gemma 4 26B | `gemma4:26b-nvfp4` | `f60799545325362bdaa15cbf38694f997514d3d46425c900b4eb06c1d6422d18` | 16.1 GB |

The final local comparison harness was `local-llm-bench v0.4.3`. Its
measurement script SHA-256 at the frozen comparison boundary was
`18ada7b5de9de089743943a0e30d423a566007dd066b795865008cf119cb0be8`;
the frozen fixture SHA-256 was
`39ac5b42fb875f85ad3fc97e356c988e959c36915c35001dd33d5bfc5383c213`.

Raw machine logs and response bundles remain local rather than creating a new
permanent repository result-storage convention, consistent with DR-007. Final
frozen bundles and selected correction probes are SHA-identified; some earlier
exploratory v0 runs predate per-run hash manifests and are treated as weaker
path-identified local evidence rather than execution-time hashed bundles.

## 3. Runtime performance and workstation headroom

Final realistic baseline measurements used the same workload families and
separated cold load, warm generation and cache behavior.

| Metric | Qwen3.5 9B | gpt-oss 20B | Gemma 4 26B |
|---|---:|---:|---:|
| realistic code generation | ~45.05 tok/s | ~66.68 tok/s | ~104.88 tok/s |
| structured JSON generation | ~44.93 tok/s | ~66.99 tok/s | ~107.75 tok/s |
| analysis/prose generation | ~45.02 tok/s | ~66.47 tok/s | ~76.40 tok/s |
| minimum free memory in baseline | ~48% | ~27% | ~12% |

Additional measured observations:

- Qwen sustained about 44.6 tok/s at the 4K saturation workload with only about
  1.18% first-to-last degradation over the bounded ten-minute run and no
  thermal/performance warning.
- Qwen completed bounded 16K, 32K and 64K-allocation tests. Generation fell as
  actual input grew: about 42.45 tok/s near 10.4K input, 39.27 near 24.8K and
  34.50 near 49.5K. The 64K result is not a full 64K prompt-fill proof.
- Qwen High Power versus Automatic changed the tested short decode profiles by
  less than about 0.5%; High Power was not a meaningful speed lever for those
  workloads.
- Gemma's normal loaded footprint was about 16-17 GB and could reach about
  19 GB during cache/context-heavy operation. A bounded 32K stress request hit
  the benchmark memory guard at 9% free memory. Its 16K class remained usable.
  This 32K observation comes from the earlier exploratory
  `local-llm-bench-v0/runs/stress-gemma-v03` run, which did not have an
  execution-time per-run SHA manifest. During review correction, the preserved
  run files were given a post-hoc correction-time digest identity:
  `SHA256SUMS.review-correction` SHA-256
  `a98662514f8b0461b52b729a7e03808cd43d77adb17ccf4760848df03519d75e`.
  That digest strengthens current traceability but is not represented as an
  execution-time manifest.
- gpt-oss normally loaded around 12 GB on the tested 4K/8K profiles. Its
  model-native low reasoning adds user-visible latency even when internal
  reasoning begins quickly.

These measurements make memory headroom, not thermal throttling, the primary
resource distinction on this 24 GB machine.

## 4. Cache and latency behavior

Prompt-cache reuse was measured separately from model residency.

- Qwen hot shared-prefix TTFR reached about 0.11 s in the final realistic
  cache workload.
- Gemma hot shared-prefix TTFR was about 0.17-0.33 s across corrected runs.
- gpt-oss with low reasoning can start reasoning quickly on a hot cache, but
  visible final output may remain materially later. Review correction reproduced
  this as hash-identified local run
  `DR007-GPTOSS20B-EXTENDED-CACHE-001` using the frozen v0.4.3 fixture.
  Its two hot-cache samples recorded first internal output at about 0.172 s and
  0.158 s, visible response at about 3.51 s and 3.80 s, and 1060 / 1109
  reasoning characters respectively. The run's `metrics.jsonl` SHA-256 is
  `6ce8c3486d2af27c52e77a36102ee9b05647724c0d6c6cf8ad7d87b5b854770d`
  and its manifest SHA-256 is
  `52b0a93fc857366f38c06e8ca1f5f93286beecae462cee873a84350ee6e594c9`.

Therefore cache architecture is a major latency lever, but gpt-oss reasoning
latency must be treated separately from first internal token latency.

## 5. Corrected task-quality evidence

### 5.1 Executable code

A hidden six-task Python suite was run twice per model. The first validator
incorrectly counted Markdown code fences as Python syntax failures; the result
was revalidated after extracting fenced code. A knapsack oracle was also
corrected after independent recomputation found two equal-value/equal-cost
solutions and the documented lexicographic tie-break selected a different
expected list.

Final executable-code result:

| Candidate | Passed |
|---|---:|
| Qwen3.5 9B | 4 / 12 |
| gpt-oss 20B | 12 / 12 |
| Gemma 4 26B | 12 / 12 |

Format adherence differed: Qwen obeyed the raw-code-only surface in the hidden
suite, while gpt-oss and Gemma wrapped code in Markdown fences despite the
instruction. This is a format-control issue, not an executable-code-quality win.

### 5.2 Structured reasoning

A hidden six-task structured reasoning set was also run twice. Expected values
were independently recomputed before final scoring; a capacity-set comparison
was normalized where list order was not part of the task semantics.

Final semantic correctness:

| Candidate | Passed |
|---|---:|
| Qwen3.5 9B | 6 / 12 |
| gpt-oss 20B | 10 / 12 |
| Gemma 4 26B | 4 / 12 |

This is the strongest direct evidence for a gpt-oss reasoning role. The models
shared some deterministic mistakes, so the result does not justify autonomous
workflow authority.

## 6. Workflow-specific evidence

### gpt-oss semantic-only adversarial suite

A 34-case suite was repeated twice:

- 68 observations;
- high-level status correct: 58 / 68;
- unsafe `CONTINUE`: 2;
- exact status/reason/evidence tuple: 0 / 68;
- repeat-stable cases: 34 / 34.

This result vetoes any design in which gpt-oss directly owns the workflow
transition or authorization boundary.

### Real workflow replay

Representative checkpoints were derived from completed DR-007, WOL conductor,
BuildCraft and housing-recovery episodes. A simplified mutually exclusive
next-step replay was used after a richer enum/schema replay proved too
format-sensitive.

Eight representative checkpoints repeated twice produced:

| Candidate | Correct | Repeat-stable |
|---|---:|---:|
| gpt-oss 20B | 10 / 16 | 8 / 8 |
| Gemma 4 26B | 12 / 16 | 8 / 8 |

The result does not reverse the structured-reasoning finding. It shows that
Gemma can recognize several workflow patterns well when the decision surface is
small. Important misses remained:

- both models routed a changed PR head after prior PASS through live-state
  reconciliation instead of directly requiring fresh review;
- Gemma treated PASS without merge authorization as a completed/advance-style
  state rather than an authorization stop;
- gpt-oss sometimes routed a correction-required candidate to fresh review
  instead of the correction step and produced no usable one-letter result for
  an already-merged checkpoint in the no-schema replay.

A richer structured-choice replay gave gpt-oss 26 / 34 correct observations.
Gemma failed that specific structured-choice schema surface and that failure is
treated as format incompatibility, not a semantic score.

## 7. Candidate role assessment

### Qwen3.5 9B

Strengths:

- largest workstation memory headroom;
- strong cache latency;
- stable long-context behavior for its size;
- lowest-cost resident option.

Weaknesses:

- materially slower generation than the other finalists;
- weaker hidden executable-code result;
- weaker structured reasoning;
- original DR-007 functional smoke produced unsafe progression on critical
  stale/ambiguous/missing-authority cases.

**Current recommendation:** retain as a lightweight fallback/reference candidate,
not a primary integration route.

### gpt-oss 20B

Strengths:

- strongest hidden structured-reasoning result;
- 12 / 12 executable-code result after format normalization;
- materially more memory headroom than Gemma;
- repeatable behavior across workflow replay.

Weaknesses:

- slower than Gemma for code/JSON generation;
- model-native reasoning delays visible output;
- expanded semantic testing still produced unsafe progression and inaccurate
  reason/evidence selection;
- not reliable enough to own authorization or transitions.

**Current recommendation:** primary candidate for bounded semantic reasoning,
planning, review and ambiguity analysis behind deterministic guards.

### Gemma 4 26B

Strengths:

- fastest tested realistic code and JSON generation;
- 12 / 12 executable-code result after format normalization;
- competitive recognition of simplified real workflow checkpoints.

Weaknesses:

- substantially less memory headroom;
- 32K-class memory pressure arrives quickly on the 24 GB device;
- weaker explicit structured-reasoning result;
- demonstrated an authorization-sensitive workflow miss.

**Current recommendation:** candidate executor/generation model for code and
larger generation batches, not the workflow authority layer.

## 8. Proposed integration boundary

The evidence supports testing a phase-based two-model architecture rather than
keeping both models resident concurrently.

Candidate flow:

```text
deterministic task/state normalization
        |
        v
gpt-oss advisory reasoning
(planning / review / ambiguity)
        |
        v
deterministic authority + transition + tool guard
        |
        +----> no execution / reconcile / block
        |
        v
Gemma generation/executor batch when selected
        |
        v
normal verification + independent review
```

The deterministic layer, not either model, must own at minimum:

- live-state readback and freshness;
- exact base/candidate SHA identity;
- review subject and fresh-review requirements;
- authorization and scope checks;
- ambiguous-side-effect reconciliation and retry containment;
- allowed transition selection;
- tool identity and argument validation;
- ready/merge/publication gates.

No local model may accept or review its own repository candidate by implication.

Because gpt-oss and Gemma together exceed the comfortable residency budget on
this 24 GB machine, the candidate integration should be phase-based:
reasoning/review batches under gpt-oss, unload when appropriate, then larger
generation/executor batches under Gemma. Frequent per-request model switching
may erase the throughput advantage through cold-load cost and should be measured
only if the integration design actually requires it.

## 9. Evidence limitations

- The benchmark corpus is bounded and tailored to the intended workflow; it is
  not a general model leaderboard.
- Some workflow replay cases are simplified representations of real episodes,
  not complete repository transcripts.
- Structured-output compatibility differed by model; format failures were kept
  separate from semantic scores where the distinction was observable.
- Raw local bundles are not durable repository evidence. This note is a compact
  synthesis of checked local evidence with mixed provenance strength. Final
  frozen benchmark bundles and selected correction probes have verified SHA-256
  identities; some earlier exploratory v0 runs lacked execution-time per-run
  hash manifests. Where such an early run remains load-bearing, this note
  identifies that limitation explicitly and does not upgrade a correction-time
  digest into an execution-time manifest.
- No result here grants standing execution, merge, unattended, AFK or
  autonomous-policy authority.

## 10. Recommendation and next gate

**RECOMMENDATION:** carry forward two finalists with distinct roles:

1. `gpt-oss:20b` as the bounded reasoning/review candidate;
2. `gemma4:26b-nvfp4` as the bounded code/generation candidate.

Qwen3.5 9B remains a measured lightweight fallback/reference.

The next repository gate should be an **independent evidence review of the exact
DR-008 candidate**. Only after a zero-blocking review and explicit coordinator
disposition should a separate local-model integration design be authorized.

That later integration design should define the normalized input/output
contract, deterministic safety boundary, model-routing trigger, residency/load
policy, failure fallback and evaluation plan. It must not infer adoption from
this research publication.

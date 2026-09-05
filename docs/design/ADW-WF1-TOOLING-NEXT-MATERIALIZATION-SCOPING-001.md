---
id: ADW-WF1-TOOLING-NEXT-MATERIALIZATION-SCOPING-001
artifact: materialization-scoping
artifact_status: active
owner: chatgpt-coordinator
authority: coordinator-scoping
decision: propose-bounded-next-materialization
decision_basis_main: b8d7aeb3ed48cd315357f54895356f14beb2ddc2
register_ref: docs/research/research-register.md
register_blob: 5ef174898c5f24b3feba45c392652ae3afc26b06
proposed_artifact_path: docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-001.md
decided_on: 2026-09-05
normative_effect: none
supersedes: null
---

# Workflow v1 tooling/enforcement next materialization scoping

## Result

**NEXT MATERIALIZATION SCOPING READY FOR PERSISTENCE**

Decision:

`propose-bounded-next-materialization`

Proposed next slice:

`docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-001.md`

The proposed slice is one annotated, non-operative Markdown reference for the
accepted producer-verification evidence manifest. It is intended for later
separately authorized evidence producers and independent reviewers who must
determine what was checked, against which exact subject, using which inputs,
and where the retained evidence can be found.

This record scopes only a future materialization-authorization gate. It does
not create the reference, instantiate an evidence package, select a product,
authorize checker use, define a machine schema, implement tooling or adopt
Workflow v1.

## Exact live basis

Connected `@GitHub` read-only verification established:

- repository: `ahtoxaandy999/agentic-development-workflow`;
- live `main`: `b8d7aeb3ed48cd315357f54895356f14beb2ddc2`;
- live tree: `b847413a9cbb4c67f12b06304ab6f404878a98bf`;
- sole ordered parent:
  `78c13f2ce9253a8ed1ac0474a0191f7c3d6be3a4`;
- branch `protected`: `false`;
- Research Register blob:
  `5ef174898c5f24b3feba45c392652ae3afc26b06`;
- both current Register gates:
  `Workflow v1 tooling/enforcement next materialization scoping gate`;
- accepted tooling-design blob:
  `2e0c640e8cab61b0bf165712c27e02ff9a455ec6`;
- accepted tooling-design disposition blob:
  `d029e25406442ff5a44768c06e88333f6e1cd779`;
- accepted gate-evaluation reference blob:
  `5c08148db6f0d96197b268c3567a15a4981aff81`;
- gate-evaluation reference disposition blob:
  `2586fe5919df18e215008be026dd412ba2f66454`;
- DR-005 disposition blob:
  `70cea63938bf4a8b908904d2b9c7b0c9aec1b401`.

The accepted gate-evaluation reference lifecycle is complete for its exact
subject. It is not reopened by this scoping decision.

## Controlling design basis

The accepted tooling design already fixes the material intent needed for this
slice:

- TD-03 separates immutable evidence manifests from mutable current
  projections;
- TD-05 selects repository-native retained evidence with digest and size
  binding for the initial architecture;
- TD-10 requires applicability, satisfaction, item-specific freshness and
  exact evidence references at every reliance gate;
- section 4.1 places future manifests at
  `docs/adw/tasks/<T>/evidence/<evidence-id>/manifest.md` with secret-safe raw
  payloads under `raw/`;
- section 7.1 defines the common evidence package, provenance, payload
  inventory and custody meanings;
- section 7.2 defines producer-verification-specific subject, content,
  producer and timing obligations; and
- S6 accepts raw results plus portable manifest/digest concepts with custody
  and retention still requiring contextual decisions.

No new mechanism selection is required to explain these accepted meanings.

## Alternatives considered

### 1. Producer-verification evidence-manifest reference — selected

This is the smallest slice with identifiable near-term consumers. Every later
candidate, independent review and disposition depends on intelligible
producer-verification evidence. Recent bounded work repeatedly had to restate
subject identity, method, input basis, result, failure/skip behavior, payload
digests, limitations and custody. A shared explanatory reference can reduce
omissions and pointer ferrying without becoming a validator or current-state
owner.

### 2. Task-control `control.md` reference — deferred for this slice

The accepted design supplies a direction, but a useful reference would span
ten orthogonal state planes, recorder authority, dependencies, cancellation,
recovery, joins and current projections. It is materially broader, more likely
to be mistaken for an operative template, and has no selected product task in
which to test the representation. It may be reconsidered by a later scoping
gate after evidence handling has a stable explanatory basis.

### 3. Executable schema, validator or generator — not eligible

An executable representation would introduce implementation, interface and
failure semantics not authorized by this gate. It would also risk turning an
explanatory representation into a competing authority. No accepted decision
currently selects such a mechanism.

### 4. Additional checker automation — not eligible

The accepted persistence checker has only bounded, separately authorized
secondary-helper use. Its prior one-slot authority is exhausted. This scoping
gate cannot expand operational checker authority or create another automated
writer/verifier path.

## Proposed artifact and ownership

Sole proposed artifact:

`docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-001.md`

Proposed metadata:

```yaml
id: ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-001
artifact: design-reference
artifact_status: draft
owner: chatgpt-coordinator
authority: explanatory-design-reference
tooling_design_ref: docs/design/ADW-WF1-TOOLING-DESIGN-001.md
tooling_design_disposition_ref: docs/design/ADW-WF1-TOOLING-DESIGN-DISPOSITION-001.md
gate_evaluation_reference_ref: docs/design/ADW-WF1-GATE-EVALUATION-REFERENCE-001.md
normative_effect: none
supersedes: null
```

ADW owns this shared explanatory artifact. An actual future evidence manifest
belongs to the explicitly authorized affected product task and its named
evidence owner/custodian. This reference owns no mutable task, verification,
custody or repository state. The Research Register remains the current ADW
gate owner.

Consumers are limited to later authorized evidence producers, candidate
recorders, independent reviewers and coordinator/risk owners interpreting an
exact evidence package. A consumer does not gain execution or decision
authority by using the reference.

## Required materialization content

A later materialization gate should require one annotated generic
representation covering:

1. manifest ID and evidence class;
2. exact task, contract, authorization, run, operation and attempt identifiers
   when applicable;
3. exact verification subject classification: mutable working output `W`,
   immutable candidate `C`, or integrated subject `I`;
4. bounded verification scope and enumerated required obligations;
5. governing criteria and explicit required versus legitimate N/A decisions;
6. expected and observed preconditions, including exact base/checkout/input
   identities;
7. actual method, command, request or inspection performed, without making
   prose a shell script;
8. producing actor/role, authority reference, observation time and material
   clock limitations;
9. load-bearing tool, runtime, version, configuration and input identities,
   including model identity/configuration only when material;
10. per-obligation result, failures, skips, unavailable evidence, limitations
    and affected carry-forward/impact references;
11. exact evidence subject binding and item-specific freshness at the point of
    reliance;
12. payload inventory with relative path, media/encoding, byte count and
    SHA-256 for every retained payload;
13. secret/redaction treatment and explicit denial when a necessary payload
    cannot be retained safely;
14. publication-time custodian, authorized readers, retention obligation and
    required retrieval points, while leaving actual contextual values
    unassigned;
15. immutable package identity after persistence: containing repository,
    commit, path and Git blob; and
16. explicit limits: identity proves equality only, not authenticity,
    correctness, completeness, authorization, independence, accessibility or
    retention.

The reference should include compact fictional examples for:

- complete current producer verification for `W`;
- verification bound to immutable `C`;
- a required obligation that failed or was skipped;
- stale or wrong-subject evidence;
- a legitimate N/A with governing rationale; and
- an unsafe/unavailable payload that blocks reliance pending a custody
  decision.

All example names and digests must be obviously fictional and non-secret.

## Non-goals and denied content

The proposed reference must not create or select:

- an actual product, task, manifest, evidence ID, actor or custodian;
- an operational template that can itself authorize or complete verification;
- JSON Schema, YAML schema, parser, validator, recorder or generator;
- an evidence store, external storage provider, signing/attestation system or
  retention period;
- credential, permission or reviewer-identity mechanisms;
- scripts, hooks, Actions, Apps, MCPs, skills, trackers or orchestration;
- checker invocation, standing helper use or automated verification;
- product migration, dogfooding or routine write authority;
- parallel, automated, unattended or AFK execution;
- Workflow v1 implementation or normative adoption; or
- resolution of RG1 through RG12.

The artifact must not become another owner of current verification status.

## Producer verification for the proposed reference

Later authorized production should verify at minimum:

- exactly one output file under the assigned local output root;
- required metadata and all required content listed above;
- complete distinction among W, C and I subjects;
- criteria, applicability/N/A, results and freshness remain separate;
- every payload example has relative path, encoding/media, bytes and SHA-256;
- every repository evidence example has repository, full containing commit,
  path, Git blob and optional fragment;
- missing, failed, skipped, unsafe, inaccessible, stale and wrong-subject
  evidence cannot honestly become pass;
- custody fields are contextual obligations, not invented guarantees;
- no executable schema, validator, tool or operational authority is implied;
- all claims trace to the accepted tooling design and disposition;
- RG1-RG12 and DI-1/DI-2 boundaries are explicit; and
- serialization is UTF-8 without BOM, LF-only, exactly one final LF, with byte
  count, SHA-256 and Git blob reported.

Passing these checks establishes only readiness for candidate persistence.

## Independent review and acceptance test

After exact candidate persistence, a fresh independent reviewer must reread
the immutable candidate and controlling sources. The producer cannot accept
its own work. Material correction creates a new immutable candidate and
requires applicable renewed review.

Acceptance requires that two competent producers, using only the accepted
tooling design, its disposition and the proposed reference, derive the same
minimum producer-verification evidence package without inventing material
intent about:

- evidence owner or mutable-state owner;
- W/C/I subject identity;
- required criteria, N/A or result semantics;
- method and input identity;
- payload identity and safe retention;
- item-specific freshness;
- custody and retrieval obligations;
- failure, skip, stale, wrong-subject or unavailable evidence handling; or
- what the manifest authorizes.

It must be impossible to honestly interpret the artifact as an actual
manifest, operational template, validator, completed verification,
authorization, accepted policy or Workflow v1 adoption.

## Utility hypothesis and measurement boundary

The materialization is justified by an explicit, falsifiable utility
hypothesis: later bounded evidence producers and reviewers should need fewer
task-specific restatements and fewer correction loops for missing identity,
freshness, result, payload or custody fields.

Before any schema, generator or broader evidence-reference family is
considered, at least two separately authorized representative tasks should
record:

- which required fields still needed clarification;
- omissions or wrong-subject/stale evidence found before review;
- review findings attributable to evidence representation;
- approximate task-prompt/reference duplication avoided; and
- any new ambiguity or maintenance burden introduced by the reference.

If the reference does not reduce material omissions or clarification while
remaining understandable without hidden context, stop expanding it. Do not
promote it to a schema, validator or automation merely because it exists.

## RG and design-impact boundaries

RG1 through RG12 remain unresolved. In particular, the proposed reference
cannot establish protection, writer fencing, exact-integration enforcement,
reviewer identity, permissions, containment, recovery, retention/integrity,
installed capabilities, optional integration benefit, documentation clarity
or AFK control. Missing applicable assurance fails closed for the dependent
later action.

DI-1 remains preserved: producer verification, current verification
projection, candidate, review, disposition, authorization, cancellation,
recovery, normativity and acceptance remain separate planes. N/A remains
distinct from pass.

DI-2 remains preserved: exact-subject invalidation and item-specific freshness
remain mandatory; retry, containment, recovery, reopening, reset and terminal
guards are not weakened to fit the reference.

## Lifecycle and abandonment boundary

If this scoping record is durably persisted and remains current, the lifecycle
is:

scoping decision
→ scoping persistence
→ separate materialization authorization gate
→ fresh local reference production
→ producer verification
→ exact candidate persistence
→ fresh independent candidate review
→ correction/new candidate if required
→ coordinator disposition
→ only then consider bounded representative use and utility measurement

No step is automatic. Stop or defer if the authorization gate finds that the
reference would duplicate the accepted gate-evaluation reference, invent a
schema, require an unresolved owner/retention decision, lack identifiable
consumers or have no credible measurable-use path.

## Intended Register transition after scoping persistence

A later separately authorized exact-base persistence should make only a
bounded transition that:

- adds a pointer to
  `docs/design/ADW-WF1-TOOLING-NEXT-MATERIALIZATION-SCOPING-001.md`;
- records task ID
  `ADW-WF1-TOOLING-NEXT-MATERIALIZATION-SCOPING-001`;
- records decision `propose-bounded-next-materialization`;
- records the sole proposed artifact path
  `docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-001.md`;
- preserves all accepted design, reference, checker, OPVAL and lifecycle
  decisions and restrictions; and
- sets both current Register gates to:
  `Workflow v1 producer-verification evidence reference materialization authorization gate`.

The Register must not claim that the proposed reference exists, has been
reviewed or accepted, or that production, implementation, operational use or
utility measurement has started.

## Next gates

Immediate next gate:

`Workflow v1 tooling/enforcement next materialization scoping persistence`

Post-persistence gate:

`Workflow v1 producer-verification evidence reference materialization authorization gate`

## Explicit non-actions

This scoping decision did not:

- modify GitHub, the repository or the Research Register;
- create or persist the proposed reference;
- create a product task, evidence manifest, payload or custody commitment;
- create a schema, validator, parser, generator or operational template;
- run, test, introspect or modify the persistence checker;
- install or configure tooling;
- create a commit, push, PR, Issue, branch, tag, hook, Action or workflow;
- authorize routine, parallel, automated, unattended or AFK execution;
- resolve RG1 through RG12;
- modify DI-1 or DI-2;
- adopt Workflow v1; or
- establish a new baseline.

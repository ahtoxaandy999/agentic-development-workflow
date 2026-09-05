---
id: ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-001
artifact: design-reference
artifact_status: draft
owner: chatgpt-coordinator
authority: explanatory-design-reference
tooling_design_ref: docs/design/ADW-WF1-TOOLING-DESIGN-001.md
tooling_design_disposition_ref: docs/design/ADW-WF1-TOOLING-DESIGN-DISPOSITION-001.md
gate_evaluation_reference_ref: docs/design/ADW-WF1-GATE-EVALUATION-REFERENCE-001.md
materialization_gate_ref: docs/design/ADW-WF1-PRODUCER-VERIFICATION-EVIDENCE-REFERENCE-MATERIALIZATION-GATE-001.md
materialization_basis_main: d9f7014b077f3d476ab60401aefb30d3ee1f5d53
produced_on: 2026-09-05
normative_effect: none
supersedes: null
---

# Workflow v1 producer-verification evidence reference

## A. Authority and non-authority

This document is a non-operative explanation of the producer-verification
evidence-package meanings accepted by the initial Workflow v1
tooling/enforcement design, especially TD-03, TD-05, TD-10 and sections 4.1,
7.1 through 7.3. It complements the accepted gate-evaluation reference; it
does not restate or replace that reference's ownership of explanatory gate
semantics.

The layouts and labels below are teaching devices. They are not a normative
serialization, schema, API, validator, generator, executable checklist,
operational template or live task record. Copying or completing an example
does not create verification, authorization, candidate identity, review,
disposition, acceptance, custody, retention, a permitted transition or
Workflow v1 adoption.

This reference owns no mutable task, verification, custody, repository,
research or workflow state. A future actual evidence package may exist only
under an explicitly authorized affected product task with a named evidence
owner and custodian. Its mutable current verification projection remains with
that task's sole current record. The immutable package retains only its exact
subject, observations, results, payload identities, limitations and
publication-time custody requirements. The Research Register remains the
current ADW gate owner.

The following accepted boundaries remain controlling:

- verification evidence is distinct from current verification state, review,
  disposition and acceptance;
- an executor or assigned verifier may produce evidence but gains no authority
  to authorize, independently review or accept the subject;
- a recorder may faithfully persist supplied content but gains none of the
  producer's, custodian's or decision owner's authority;
- identity proves equality only, not truth, correctness, completeness,
  authority, authenticity, independence, accessibility, retention or
  acceptance;
- missing, failed, skipped, unsafe, inaccessible, stale or wrong-subject
  required evidence cannot honestly become pass; and
- a legitimate governed N/A has no satisfaction value and cannot offset an
  unsatisfied required obligation.

## B. Relationship to gate evaluation

The accepted gate-evaluation reference explains whether a gate is applicable,
whether a required gate is satisfied, whether each relied-upon item is fresh
and which destination the controlling authority may permit. A
producer-verification package supplies evidence that such an evaluation may
inspect. It does not itself decide applicability, advance a gate or authorize
the destination.

Where an evidence package records per-obligation applicability or N/A, it
records the governing decision and rationale attributable to the actual
owner. It does not invent that decision. Where the package records a result,
the result is an observation about the exact verification subject and method,
not an aggregate task status.

The gate-evaluation reference remains the explanatory source for:

- required versus governed not-applicable;
- satisfaction versus unsatisfied;
- item-specific freshness;
- correct-subject evidence binding;
- aggregate interpretation; and
- authority-derived permitted destinations.

This reference points to those meanings and explains the evidence package that
supports them. The two references must not become competing current-state
owners.

## C. Annotated producer-verification package

The following YAML-like representation is illustrative placeholder syntax
only. Angle-bracketed text describes a value that an actual separately
authorized producer would have to supply. Field names and nesting are not
adopted as a machine contract.

```yaml
manifest:
  evidence_id: <opaque task-local evidence package identifier>
  evidence_class: producer-verification
  task_id: <actual affected product-task identifier>
  contract_ref: <exact immutable task-contract identity>
  authorization_ref: <exact bounded verification authority>
  run_id: <actual run identifier when applicable>
  operation_id: <actual operation identifier when applicable>
  attempt_id: <actual attempt identifier; never silently reused>

subject:
  class: <W | C | I>
  identity:
    W:
      output_root: <authorized canonical local output root>
      output_manifest: <complete paths, bytes and digests>
      working_revision: <actual working identity or snapshot basis>
    C:
      repository: <owner/repository>
      commit: <full immutable 40-hex commit SHA>
      path_scope: <complete bounded path set>
      tree_or_blobs: <exact tree/blob identities relied upon>
    I:
      repository: <owner/repository>
      commit: <full immutable integration-subject SHA>
      integration_scope: <bounded integrated subject>
      relation_to_reviewed_candidate: <exact C-to-I evidence>
  verification_scope: <bounded properties and obligations checked>

governing_basis:
  criteria_ref: <exact governing criteria or task requirement>
  expected_preconditions:
    authorized_base: <full base SHA when repository work applies>
    checkout_identity: <canonical checkout and observed exact revision>
    inputs: <exact immutable or freshness-bound input identities>
    dependencies: <exact required dependency identities>
    configuration: <load-bearing configuration identity when material>
  observed_preconditions:
    observed_base: <actual base observation>
    observed_checkout: <actual checkout observation>
    observed_inputs: <actual input observations>
    observed_dependencies: <actual dependency observations>
    observed_configuration: <actual material configuration observation>

producer:
  actor: <attributable actual actor>
  role: <assigned verifier or executor/verifier>
  authority_ref: <exact assignment and bounded scope>
  observed_at: <timestamp with timezone>
  clock_limitations: <material skew, source-clock or ordering limitations>

method:
  description: <what was actually executed or inspected>
  command_or_request: <secret-safe literal command/request or exact reference>
  tool_runtime:
    name: <actual tool/runtime>
    version: <actual version when load-bearing>
    configuration: <actual material configuration identity>
    model: <model identity/configuration only when load-bearing>
  method_limitations: <what the method cannot establish>

obligations:
  - obligation_id: <addressable required criterion>
    criterion: <exact criterion text or immutable reference>
    applicability: <required | not-applicable>
    applicability_owner: <accountable owner of the governing determination>
    applicability_basis: <governing rule and contextual rationale>
    result: <passed | failed | skipped | unavailable; omit for N/A>
    observation: <actual result, output or bounded summary>
    exit_or_conclusion: <actual exit code/status and interpretation>
    evidence_refs:
      - subject_binding: <how these bytes support this exact W, C or I>
        payload_ref: <relative payload path or immutable evidence pointer>
        freshness: <current | stale>
        freshness_basis: <item-specific evaluation-time comparison>
    limitations: <exceptions, uncertainty or unsupported conclusions>
    impact_or_carry_forward_refs: <affected obligations or exact impact record>

payload_inventory:
  - relative_path: <safe relative path below the evidence package>
    media_type: <actual media type>
    encoding: <actual encoding or binary>
    bytes: <actual non-negative byte count>
    sha256: <actual 64-lowercase-hex digest>
    origin: <actual method/output source>
    redaction:
      treatment: <none | redacted-derivative | omitted-as-unsafe>
      method_and_omissions: <actual treatment when transformed>

custody_at_publication:
  custodian: <named accountable custodian>
  authorized_readers: <actual governed reader set>
  retention_obligation: <contextual reliance interval or governing reference>
  required_retrieval_points: <review, recovery or continuation boundaries>
  access_test: <actual authorized retrieval evidence>
  unresolved_conditions: <missing suitability, access or retention facts>

package_identity_after_persistence:
  repository: <owner/repository>
  containing_commit: <full immutable commit created by later persistence>
  manifest_path: <repository path>
  manifest_blob: <Git blob of exact manifest bytes>
  fragment: <optional section or payload fragment>
  publication_readback_ref: <exact evidence of persisted identity>

conclusion:
  verified_subject: <exact W, C or I identity>
  result_summary: <truthful per-obligation accounting>
  required_failures_or_unknowns: <none or complete blocking list>
  freshness_limit: <what later change invalidates each relied-upon result>
  non_implications: <authority, review, acceptance and control claims not made>
```

### C1. Manifest identity and lifecycle

An evidence ID makes a package addressable within the actual task. It does not
authenticate the producer or authorize the verification. Task, contract,
authorization, run, operation and attempt identities are included only when
applicable and must refer to actual governing objects. Reusing an attempt ID
for a retry conceals history and is invalid.

The manifest becomes immutable evidence only after a separately authorized
publication binds exact repository, containing commit, path and Git blob. A
local file is working output until that identity exists. A successor package
does not rewrite an earlier result or custody statement.

### C2. Subject classes W, C and I

- **W — mutable working output.** Bind the canonical authorized output root,
  a complete output inventory and the exact snapshot or digest basis inspected.
  A later edit makes affected results stale.
- **C — immutable candidate.** Bind the full candidate commit and complete
  applicable path/tree/blob identities. A branch name or green check is not C.
- **I — integrated subject.** Bind the full integration commit and evidence of
  its relationship to the reviewed C. Passing C evidence is not integrated
  verification of I.

The class must be explicit. Evidence for W cannot silently become evidence for
C merely because bytes appear similar; the relation needs its own exact
candidate-binding evidence. Evidence for C cannot silently become evidence for
I.

### C3. Criteria, N/A and results

Every declared required obligation has an actual result. Missing work is not a
result. A skip may accurately describe execution, but a skipped required
obligation remains non-passing. A failed, unavailable or unsafe evidence item
remains non-passing.

A not-applicable row names the governing rule, accountable owner and
contextual reason. It has no satisfaction result. An evidence producer may
record that supplied decision but cannot create it solely to avoid work.

### C4. Method and environment

Record what was actually executed or inspected, including the exact
secret-safe command, request or immutable method reference when needed for
reconstruction. Bind versions, configuration, runtime, inputs and model only
where changing them could alter the relied-upon result. Avoid ceremonial
inventory that has no bearing on the conclusion.

The method section states limitations. A syntax check is not a behavioral
test; a local test is not integrated verification; a snapshot is not proof
that a mutable ref remained unchanged.

### C5. Payload identity and redaction

Every retained payload has a safe relative path, media/encoding, byte count
and SHA-256. The digest identifies bytes; it does not replace required bytes
or prove their provenance.

Redact before repository persistence. If transformed, call the retained object
a redacted derivative and record the method and omissions. Do not retain a
secret original merely to prove its digest. If removing sensitive material
removes a load-bearing fact, block the affected conclusion and return for a
separate custody or evidence decision.

### C6. Custody and retrieval

Publication-time custody records actual accountable custodian, governed
readers, contextual retention obligation and required retrieval points. It
does not promise permanent storage. Later custody changes are distinct
records; they cannot rewrite the original package.

At every required reliance boundary, retrieve the actual authorized bytes and
check commit/path/blob, payload size/digest, access and current retention
commitment. Missing, expired, inaccessible, mismatched or unsafe evidence
invalidates the dependent reliance.

## D. Fictional examples

All examples below are deliberately incomplete teaching fragments. Tokens in
angle brackets are visibly fictional placeholders, not allocated identifiers,
real actors, valid repository objects or computed digests. An actual package
must supply the complete representation from section C.

### D1. Complete current verification of W

```yaml
evidence_id: <FICTIONAL-W-PASS-EVIDENCE-ID>
subject:
  class: W
  output_root: </fictional/authorized/output/root>
  output_manifest: <FICTIONAL-COMPLETE-INVENTORY>
  verification_scope: <ONE-BOUNDED-FICTIONAL-OBLIGATION>
producer:
  actor: <FICTIONAL-ATTRIBUTABLE-VERIFIER>
  authority_ref: <FICTIONAL-BOUNDED-VERIFICATION-GRANT>
method:
  description: <FICTIONAL-ACTUAL-METHOD>
declared_obligations:
  - <FICTIONAL-CRITERION-UNIT-TESTS>
obligation:
  criterion: <FICTIONAL-CRITERION-UNIT-TESTS>
  applicability: required
  result: passed
  evidence:
    subject_binding: <EXACT-SNAPSHOT-OF-THIS-W>
    freshness: current
    freshness_basis: <W-INVENTORY-REREAD-AT-RELIANCE>
payload:
  relative_path: raw/unit-tests.txt
  media_type: text/plain
  encoding: UTF-8
  bytes: <ACTUAL-BYTE-COUNT-REQUIRED>
  sha256: <ACTUAL-64-LOWERCASE-HEX-SHA256-REQUIRED>
limitations:
  - <LATER-W-EDIT-MAKES-AFFECTED-EVIDENCE-STALE>
conclusion:
  result_summary: <ONE-OF-ONE-DECLARED-REQUIRED-OBLIGATIONS-PASSED>
  required_failures_or_unknowns: none
```

This can support only the named W criterion while the bound working snapshot
remains current. It does not create C or authorize candidate persistence.

### D2. Verification bound to immutable C

```yaml
evidence_id: <FICTIONAL-C-PASS-EVIDENCE-ID>
subject:
  class: C
  repository: <FICTIONAL-OWNER/FICTIONAL-REPOSITORY>
  commit: <FULL-40-HEX-CANDIDATE-SHA-MUST-BE-SUPPLIED>
  path: <FICTIONAL-REPOSITORY-PATH>
  git_blob: <FULL-40-HEX-GIT-BLOB-MUST-BE-SUPPLIED>
  fragment: <OPTIONAL-FICTIONAL-FRAGMENT>
obligation:
  criterion: <FICTIONAL-CANDIDATE-SERIALIZATION-CRITERION>
  applicability: required
  result: passed
  evidence:
    subject_binding: <EXACT-COMMIT-PATH-BLOB-RELATION>
    freshness: current
    freshness_basis: <IMMUTABLE-C-PLUS-CURRENT-CRITERIA-CHECK>
payload:
  relative_path: raw/candidate-inspection.json
  media_type: application/json
  encoding: UTF-8
  bytes: <ACTUAL-BYTE-COUNT-REQUIRED>
  sha256: <ACTUAL-64-LOWERCASE-HEX-SHA256-REQUIRED>
```

The complete repository evidence tuple is repository, full containing commit,
path, Git blob and optional fragment. The candidate SHA does not prove review,
correctness, authorship or acceptance.

### D3. Required obligation failed or skipped

```yaml
evidence_id: <FICTIONAL-REQUIRED-NONPASS-EVIDENCE-ID>
subject:
  class: C
  repository: <FICTIONAL-OWNER/FICTIONAL-REPOSITORY>
  commit: <FULL-CANDIDATE-SHA-REQUIRED>
  path: <FICTIONAL-REPOSITORY-PATH>
  git_blob: <FULL-GIT-BLOB-SHA-REQUIRED>
obligation:
  criterion: <FICTIONAL-REQUIRED-INTEGRITY-CHECK>
  applicability: required
  result: failed
  exit_or_conclusion: <NONZERO-EXIT-OR-DEFINITE-MISMATCH>
  limitations: <REQUIRED-CRITERION-UNSATISFIED>
payload:
  relative_path: raw/integrity-check.txt
  media_type: text/plain
  encoding: UTF-8
  bytes: <ACTUAL-BYTE-COUNT-REQUIRED>
  sha256: <ACTUAL-64-LOWERCASE-HEX-SHA256-REQUIRED>
conclusion:
  required_failures_or_unknowns:
    - <FICTIONAL-REQUIRED-INTEGRITY-CHECK>
```

If execution was skipped, record `result: skipped` instead of inventing a
failure output. Both outcomes remain non-passing for a required obligation.

### D4. Stale or wrong-subject evidence

```yaml
evidence_id: <FICTIONAL-STALE-EVIDENCE-ID>
subject:
  class: C
  repository: <FICTIONAL-OWNER/FICTIONAL-REPOSITORY>
  commit: <CANDIDATE-BEING-EVALUATED>
  path: <FICTIONAL-REPOSITORY-PATH>
  git_blob: <BLOB-OF-CANDIDATE-BEING-EVALUATED>
obligation:
  criterion: <FICTIONAL-REQUIRED-TEST-CRITERION>
  applicability: required
  result: unavailable
  evidence:
    subject_binding: <PAYLOAD-ACTUALLY-BINDS-A-DIFFERENT-CANDIDATE>
    freshness: stale
    freshness_basis: <EXPECTED-AND-OBSERVED-SUBJECTS-DIFFER>
payload:
  relative_path: raw/prior-candidate-tests.txt
  media_type: text/plain
  encoding: UTF-8
  bytes: <ACTUAL-BYTE-COUNT-REQUIRED>
  sha256: <ACTUAL-64-LOWERCASE-HEX-SHA256-REQUIRED>
conclusion:
  required_failures_or_unknowns:
    - <CURRENT-CANDIDATE-HAS-NO-CURRENT-CORRECT-SUBJECT-EVIDENCE>
```

A prior passing payload remains immutable evidence about its old subject. It
cannot support the current candidate after a subject or load-bearing basis
change.

### D5. Legitimate governed N/A

```yaml
evidence_id: <FICTIONAL-NOT-APPLICABLE-EVIDENCE-ID>
subject: { class: W, output_manifest: <FICTIONAL-CURRENT-W-INVENTORY> }
obligation:
  criterion: <FICTIONAL-BINARY-PAYLOAD-DECODER-CHECK>
  applicability: not-applicable
  applicability_owner: <FICTIONAL-ACCOUNTABLE-CRITERIA-OWNER>
  applicability_basis: <GOVERNING-RULE-AND-NO-BINARY-PAYLOADS-IN-EXACT-SCOPE>
payload:
  relative_path: raw/applicability-inventory.txt
  media_type: text/plain
  encoding: UTF-8
  bytes: <ACTUAL-BYTE-COUNT-REQUIRED>
  sha256: <ACTUAL-64-LOWERCASE-HEX-SHA256-REQUIRED>
```

The payload supports the scope fact used by the accountable applicability
decision. N/A is neither pass nor a credit against another failure.

### D6. Unsafe or inaccessible required payload

```yaml
evidence_id: <FICTIONAL-CUSTODY-BLOCK-EVIDENCE-ID>
subject:
  class: I
  repository: <FICTIONAL-OWNER/FICTIONAL-REPOSITORY>
  commit: <FULL-INTEGRATION-SHA-REQUIRED>
  path: <FICTIONAL-REPOSITORY-PATH>
  git_blob: <FULL-INTEGRATED-SUBJECT-BLOB-SHA-REQUIRED>
obligation:
  criterion: <FICTIONAL-REQUIRED-EXTERNAL-RESULT>
  applicability: required
  result: unavailable
  observation: <LOAD-BEARING-SOURCE-CONTAINS-SECRET-OR-CANNOT-BE-RETRIEVED>
payload:
  relative_path: raw/external-result.redacted.txt
  media_type: text/plain
  encoding: UTF-8
  bytes: <ACTUAL-REDACTED-DERIVATIVE-BYTE-COUNT>
  sha256: <ACTUAL-REDACTED-DERIVATIVE-64-HEX-SHA256>
  redaction:
    treatment: redacted-derivative
    method_and_omissions: <LOAD-BEARING-FACT-REMOVED>
custody_at_publication:
  unresolved_conditions:
    - <NO-AUTHORIZED-SAFE-LOCATION-FOR-NECESSARY-SOURCE-BYTES>
conclusion:
  required_failures_or_unknowns:
    - <SEPARATE-CUSTODY-DECISION-REQUIRED-BEFORE-RELIANCE>
```

A digest or redacted derivative cannot replace necessary governed source bytes
when the omitted fact is load-bearing. The dependent gate remains blocked.

## E. Review and reliance questions

A later producer, reviewer or coordinator should ask:

- Is the actual task and bounded verification authority identified exactly?
- Is the subject explicitly W, C or I, with a complete identity for that class?
- Does every required obligation have an actual result and current,
  correct-subject evidence?
- Does every N/A name its governing rule, accountable owner and contextual
  rationale, with no satisfaction value?
- Are method, inputs, dependencies, configuration and runtime identities
  recorded only to the extent they are load-bearing?
- Does every retained payload have a safe relative path, media/encoding, byte
  count, SHA-256, provenance and redaction treatment?
- Are publication-time custodian, readers, retention obligation and retrieval
  points actual supplied values rather than inferred guarantees?
- Are repository pointers complete tuples rather than branch names or links?
- Would a change to any subject, criterion, authority, dependency,
  configuration or payload correctly make the affected evidence stale?
- Are failed, skipped, unavailable, unsafe, inaccessible and stale cases
  preserved instead of hidden by an aggregate green result?
- Does the record remain evidence rather than a competing current-state owner?
- Are verification, review, disposition and acceptance still separate?

Answering these questions does not itself constitute producer verification or
independent review.

## F. Identity, freshness and immutable correction

Every repository evidence pointer uses:

`repository + full containing commit SHA + path + Git blob + optional fragment`

Every relied-upon payload additionally has an exact byte count and SHA-256.
Human-readable links may accompany the tuple but cannot replace it.

Freshness is item-specific. Observation time alone cannot make a mutable input,
authority, dependency, configuration or evidence source current. At the point
of reliance, reread every material mutable dimension through its authorized
source and compare it with the assignment-bound identity.

A changed subject or load-bearing basis leaves the old package intact in
history and makes the affected current projection non-passing until a new
authorized package supports it. Corrected evidence is a successor package with
a new identity. It must not rewrite an old failure, stale result or custody
limitation into a pass.

## G. Custody failure and fail-closed behavior

Initial design direction is repository-native retention of necessary
secret-safe evidence in the affected product repository. That is not a claim
that every repository, payload or reader set is suitable.

If required content cannot safely be retained, if the custodian or reliance
interval is missing, or if authorized retrieval fails, preserve safe available
evidence, name the missing item and accountable owner, and block the affected
reliance. Do not silently activate an external store, shorten the required
history, substitute chat memory or turn the problem into a warning-only pass.

Retention duration is contextual. Successful retrieval now proves only that
retrieval. It does not guarantee later availability or resolve RG8.

## H. Utility and abandonment boundary

This reference carries a falsifiable utility hypothesis: later bounded
evidence producers and reviewers should need fewer task-specific restatements
and fewer correction loops for missing identity, freshness, result, payload or
custody information.

Before considering a schema, generator or broader evidence-reference family,
at least two separately authorized representative tasks should record:

- fields that still needed clarification;
- omissions or wrong-subject/stale evidence found before review;
- review findings attributable to evidence representation;
- approximate prompt or reference duplication avoided; and
- ambiguity or maintenance burden introduced by this reference.

If no material benefit appears, stop expansion. The artifact's existence,
persistence, review or later acceptance cannot by itself justify a schema,
validator, generator or automation.

## I. RG and design-impact boundaries

RG1 through RG12 remain unresolved. This reference creates no protection,
writer fencing, exact-integration enforcement, reviewer-identity enforcement,
cross-surface permission proof, cancellation/containment control, durable
recovery mechanism, retention/integrity guarantee, installed-capability proof,
optional integration selection, documentation-ambiguity resolution or AFK
end-to-end control.

Missing applicable assurance fails closed for the dependent action. RG10 and
RG11 remain non-blocking for this minimum explanatory artifact while blocking
their optional candidates; no optional candidate is selected here.

DI-1 is preserved. Task control, authorization, work product, verification,
review, disposition, cancellation, recovery, join, normativity and acceptance
remain orthogonal planes. Legitimate N/A remains distinct from passed
satisfaction.

DI-2 is preserved. Exact-subject invalidation and item-specific freshness
remain mandatory. Operation-aware retry, containment, durable recovery
episodes, reopening, intervention, resumption/reset and terminal guards are
not weakened to fit this representation.

## J. Reference boundary

This draft creates no actual product task, evidence package, current
verification state, payload, actor, custodian, retention promise, schema,
validator, parser, generator, evidence store, signature system, credential,
permission, implementation or operational control.

It selects no App, MCP, skill, hook, Action, tracker, database, orchestration or
additional checker authority. It authorizes no routine, direct-main, parallel,
automated, unattended or AFK work and no product dogfooding. Workflow v1
remains non-normative and unadopted. RG1 through RG12 remain unresolved.

This local draft is ready only for producer verification and, if that passes,
a separately authorized exact-base candidate-persistence gate. Persistence,
fresh independent candidate review, correction, coordinator disposition and
any representative use or utility measurement remain distinct future steps.

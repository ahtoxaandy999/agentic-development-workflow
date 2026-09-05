---
id: ADW-WF1-GATE-EVALUATION-REFERENCE-001
artifact: design-reference
artifact_status: draft
owner: chatgpt-coordinator
authority: explanatory-design-reference
tooling_design_ref: docs/design/ADW-WF1-TOOLING-DESIGN-001.md
tooling_design_disposition_ref: docs/design/ADW-WF1-TOOLING-DESIGN-DISPOSITION-001.md
materialization_gate_ref: docs/design/ADW-WF1-GATE-EVALUATION-REFERENCE-MATERIALIZATION-GATE-001.md
normative_effect: none
supersedes: null
---

# Workflow v1 gate-evaluation reference

## A. Authority and non-authority

This document is a non-operative explanation of the gate-evaluation semantics accepted in the initial Workflow v1 tooling/enforcement design, especially section 5.2 and TD-10, within the qualifications preserved by its disposition. It illustrates meaning and completeness only. The labels and layouts below are teaching devices, not a normative serialization, global enum, form, schema, validator, API or live checklist.

This reference owns no mutable state. Copying, completing, reviewing or persisting any example creates no readiness, authorization, verification, review, disposition, acceptance, baseline, transition or permitted action. It is not an actual task, gate, decision, candidate or evidence package, and it never becomes a product task's current record. The Research Register remains the owner of the current ADW gate.

An actual evaluation may exist only under a later explicitly authorized product-task owner. That owner must bind the actual product, task, current governing authority, accountable actors, exact subject, criteria, inputs, evidence and destination. A record producer faithfully records attributed evaluation and decision inputs; the recorder does not acquire the evaluator's or decision owner's authority.

The accepted state separations remain controlling:

- **DI-1:** task control, cancellation, recovery, work product, verification, review, disposition, normativity, baseline acceptance and join are orthogonal planes. A gate evaluation or native `done`, `green`, `merged` or `closed` label cannot collapse or advance them.
- **DI-2:** materially stale authority or evidence blocks reliance. Exact-subject invalidation, operation-aware retry, distinct containment and recovery, immutable completed history, qualified episode reopening, intervention, resumption/reset and terminal guards are not weakened by this reference.
- Mutable current pointers and projections may move only under their actual owner; immutable evaluations, decisions and evidence retain their original subject and conclusion. A successor does not edit history into a new pass.
- Local verification, integrated verification, review and disposition remain distinct. Passing one does not imply another.

RG1 through RG12 remain unresolved prerequisites in their controlling scopes: protection; writer fencing; exact integration publication; reviewer identity; cross-surface permissions; cancellation/containment; durable recovery; retention/integrity; installed capabilities; integration leverage; documentation ambiguity; and AFK end-to-end controls. RG1-RG9 and RG12 remain blocking where applicable; RG10-RG11 remain non-blocking for the minimum design but block their optional candidates. Naming a gap, or later obtaining test evidence, neither resolves it nor grants authority. Conditional, deferred and rejected mechanisms remain unselected.

## B. Annotated representation

The following YAML-like block is illustrative placeholder syntax only. An actual authorized owner may represent the same required meanings differently. Angle-bracketed values are descriptions, not allocated identifiers or fields in a global registry.

```yaml
gate_id: <addressable gate identifier>
transition: <named source-to-destination transition being evaluated>
subject:
  tuple: <all exact identities that distinguish the evaluated object/state>
  scope: <bounded properties, paths, obligations, or effects evaluated>
governing_authority: <exact rule or authority that invokes and controls the gate>
evaluator: <attributable actor who evaluates the evidence>
decision_owner: <accountable actor authorized to decide applicability/outcome>
evaluated_at: <time of this evaluation; not a blanket freshness claim>
applicability: <required | not-applicable>
applicability_rationale: <context and governing-rule reason>
satisfaction: <passed | unsatisfied; present only when applicability is required>
relied_upon_items:
  - kind: <input | configuration | dependency>
    identity: <exact item identity>
    freshness: <current | stale for this item>
    freshness_basis: <comparison or observation supporting that item conclusion>
evidence:
  - criterion: <the obligation supported or left unsatisfied>
    subject_binding: <exact relationship between evidence and evaluated subject>
    reference: <complete immutable evidence identity and, when required, custody pointer>
    freshness: <current | stale for this evidence item>
    freshness_basis: <evaluation-time comparison bound to this evidence reference or capture identity>
exceptions_or_open_conditions: <none, or material unresolved conditions>
permitted_destination_if_effective: <destination allowed by controlling authority, or none>
```

The semantic relationships are mandatory even though these labels are not:

- `gate_id` makes the evaluation addressable; it does not itself confer authority.
- `transition` names the change being considered. A positive evaluation supports only that named transition and only within its bounded scope.
- The `subject` tuple must be exact and complete for the claim. A wrong or changed subject invalidates current reliance even if human-readable names still match.
- `governing_authority` determines when the gate applies, who may decide, what criteria control it and what destination can be permitted.
- `evaluator` examines evidence; `decision_owner` makes the accountable decision. They may be separate roles, and must remain separate whenever the governing authority requires it. A label alone appoints neither.
- `evaluated_at` records when the evaluation occurred. Freshness is separately determined for every relied-upon input, configuration, dependency and material evidence item.
- `applicability` asks whether the gate is required in this context. `satisfaction` asks whether a required gate passed. A governed `not-applicable` decision has rationale and no satisfaction value; N/A is not pass.
- A required gate may be `passed` only with complete, current, correct-subject evidence for every required criterion. Otherwise it is `unsatisfied`; missing required evidence denies pass.
- `exceptions_or_open_conditions` preserve limitations that prevent or qualify reliance. They cannot be hidden by an aggregate green observation.
- `permitted_destination_if_effective` is derived from the controlling authority. The field records no transition and grants nothing by itself.

## C. Five fictional examples

All names, repositories, actors, identifiers and digests in this section are deliberately fictional. The examples are explanatory fragments, not reusable records and not actual authorizations.

### C1. Required, current, correct-subject and passed

```yaml
fictional_example: EXAMPLE-ALPHA
gate_id: FICTION-GATE-ALPHA
transition: proposed-output -> candidate-eligible
subject:
  tuple:
    repository: https://fiction.invalid/clockwork/blue-orchid
    containing_commit: 1111111111111111111111111111111111111111
    path: examples/blue-orchid.txt
    git_blob: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    fragment: criterion-demo-1
  scope: exact bytes and two fictional publication criteria
governing_authority: FICTION-RULE-PUB-7 revision 3
evaluator: fictional-verifier-ada
decision_owner: fictional-owner-basil
evaluated_at: 2099-01-02T03:04:05Z
applicability: required
applicability_rationale: FICTION-RULE-PUB-7 requires both criteria for this transition
satisfaction: passed
relied_upon_items:
  - kind: input
    identity: input-set@sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb; bytes=128
    freshness: current
    freshness_basis: exact digest and byte count match the governing assignment
  - kind: configuration
    identity: fictional-config revision 9
    freshness: current
    freshness_basis: revision 9 is the assignment-bound revision
evidence:
  - criterion: fictional criterion one
    subject_binding: exact repository/commit/path/blob/fragment above
    reference:
      repository: https://fiction.invalid/archive/silver-lantern
      containing_commit: 4444444444444444444444444444444444444444
      path: evidence/alpha/criterion-one.json
      git_blob: cccccccccccccccccccccccccccccccccccccccc
      fragment: observation-1
      bytes: 256
      sha256: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    freshness: current
    freshness_basis: at evaluated_at, a reread of this complete reference and payload identity matched fictional capture FICTION-CAPTURE-A-20990102T030405Z with no changed evidence object observed
    identity_limit: equality only; does not establish truth, authority, correctness, or reviewer independence
  - criterion: fictional criterion two
    subject_binding: exact repository/commit/path/blob/fragment above
    reference:
      repository: https://fiction.invalid/archive/silver-lantern
      containing_commit: 5555555555555555555555555555555555555555
      path: evidence/alpha/criterion-two.json
      git_blob: dddddddddddddddddddddddddddddddddddddddd
      fragment: observation-2
      bytes: 384
      sha256: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    freshness: current
    freshness_basis: at evaluated_at, a reread of this complete reference and payload identity matched fictional capture FICTION-CAPTURE-B-20990102T030405Z with no changed evidence object observed
    identity_limit: equality only; does not establish truth, authority, correctness, or reviewer independence
exceptions_or_open_conditions: none
permitted_destination_if_effective: candidate-persistence consideration only
```

Interpretation: the gate is required and can be described as passed only because every required criterion has current, correct-subject evidence with a complete repository tuple and, for each relied-upon payload, exact bytes and SHA-256. Each evidence object's freshness is separately determined at the fictional evaluation time against its named capture/reference identity; freshness of inputs or configuration does not substitute for evidence freshness. Identity establishes equality only, not truth, authority, correctness or reviewer independence. This observation still does not persist a candidate, perform review, make a disposition or authorize the named destination.

### C2. Required and unsatisfied

```yaml
fictional_example: EXAMPLE-BRAVO
gate_id: FICTION-GATE-BRAVO
transition: bounded-run -> completion-consideration
subject:
  tuple: fictional-run-R7 / output-manifest-M4 / criterion-set-K2
  scope: three required fictional output obligations
governing_authority: FICTION-RULE-COMPLETE-2
evaluator: fictional-verifier-cora
decision_owner: fictional-owner-dinesh
evaluated_at: 2099-02-03T04:05:06Z
applicability: required
applicability_rationale: completion consideration invokes all three obligations
satisfaction: unsatisfied
relied_upon_items:
  - kind: input
    identity: fictional-contract revision 12
    freshness: current
    freshness_basis: exact revision remains controlling
  - kind: dependency
    identity: fictional-dependency-result-D8
    freshness: current
    freshness_basis: current identity retrieved, but its required result is failed
evidence:
  - criterion: obligations one and two
    subject_binding: fictional-run-R7 / output-manifest-M4
    reference: FICTION-EVIDENCE-C, current passing observations
  - criterion: obligation three
    subject_binding: fictional-dependency-result-D8
    reference: FICTION-EVIDENCE-D, explicit failed result
exceptions_or_open_conditions: obligation three remains unsatisfied
permitted_destination_if_effective: none
```

Interpretation: current evidence exists, but it demonstrates failure of a required obligation. Other passing obligations cannot offset it.

### C3. Previously passing, now stale and unusable

```yaml
fictional_example: EXAMPLE-CHARLIE
gate_id: FICTION-GATE-CHARLIE
transition: candidate -> review-assignment-eligible
subject:
  tuple:
    repository: https://fiction.invalid/lantern/paper-comet
    containing_commit: 3333333333333333333333333333333333333333
    path: examples/paper-comet.md
    git_blob: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
  scope: exact fictional candidate and criterion revision 6
governing_authority: FICTION-RULE-REVIEW-4
evaluator: fictional-verifier-elin
decision_owner: fictional-owner-farid
evaluated_at: 2099-03-04T05:06:07Z
applicability: required
applicability_rationale: this fictional candidate class requires the gate
satisfaction: unsatisfied
relied_upon_items:
  - kind: input
    identity: prior candidate commit 2222222222222222222222222222222222222222
    freshness: stale
    freshness_basis: current subject is commit 3333333333333333333333333333333333333333
  - kind: configuration
    identity: prior criterion revision 5
    freshness: stale
    freshness_basis: governing assignment now binds criterion revision 6
evidence:
  - criterion: all formerly required checks
    subject_binding: prior commit 2222222222222222222222222222222222222222 only
    reference: FICTION-EVIDENCE-E, historical passed evaluation
exceptions_or_open_conditions: no current evidence for the new subject and criterion basis
permitted_destination_if_effective: none
```

Interpretation: the historical pass remains immutable evidence about its old subject. It is stale for the new subject and cannot be edited, carried forward implicitly or used as a current pass. Fresh affected verification is required under the actual authority.

### C4. Legitimate not-applicable determination

```yaml
fictional_example: EXAMPLE-DELTA
gate_id: FICTION-GATE-DELTA
transition: isolated-draft -> local-archive-consideration
subject:
  tuple: fictional-draft-Z9 / scope-no-external-publication
  scope: one fictional local-only draft with no integration destination
governing_authority: FICTION-RULE-INTEGRATION-8 clause N
evaluator: fictional-assessor-gita
decision_owner: fictional-risk-owner-hugo
evaluated_at: 2099-04-05T06:07:08Z
applicability: not-applicable
applicability_rationale: clause N excludes integrated verification only when the bounded subject has no integration or publication destination; the owner confirmed that context
relied_upon_items:
  - kind: input
    identity: fictional-scope-decision-S3
    freshness: current
    freshness_basis: exact scope decision remains controlling and retrievable
  - kind: dependency
    identity: fictional-destination-inventory-I2
    freshness: current
    freshness_basis: inventory confirms no integration destination in bounded scope
evidence:
  - criterion: applicability of integrated verification
    subject_binding: fictional-draft-Z9 / fictional-scope-decision-S3
    reference:
      repository: https://fiction.invalid/archive/amber-kite
      containing_commit: 6666666666666666666666666666666666666666
      path: evidence/delta/applicability-context.json
      git_blob: abababababababababababababababababababab
      fragment: governing-rule-and-context-observations
      bytes: 512
      sha256: 1212121212121212121212121212121212121212121212121212121212121212
    freshness: current
    freshness_basis: at evaluated_at, a reread of this complete reference and payload identity matched fictional capture FICTION-CAPTURE-F-20990405T060708Z with no changed evidence object observed
    identity_limit: equality only; does not establish truth, authority, correctness, or reviewer independence
exceptions_or_open_conditions: N/A must be reevaluated if scope or destination changes
permitted_destination_if_effective: local-archive consideration only
```

Interpretation: there is intentionally no `satisfaction` value. The complete, separately fresh evidence supports only the contextual, owner-attributed applicability decision, not satisfaction. That N/A excludes this gate from required aggregation; it does not fabricate a pass or offset another failed obligation. Its identity establishes equality only, not truth, authority, correctness or reviewer independence.

### C5. Invalid and incomplete; unusable as a pass

```yaml
fictional_example: EXAMPLE-ECHO
gate_id: FICTION-GATE-ECHO
transition: alleged-output -> alleged-release
subject:
  tuple: "blue build"                 # human-readable name only; exact identity missing
  scope: unspecified
governing_authority: FICTION-RULE-UNKNOWN
evaluator: fictional-verifier-iris
decision_owner: missing
evaluated_at: 2099-05-06T07:08:09Z
applicability: required
applicability_rationale: "seems required"
satisfaction: passed                   # invalid claim
relied_upon_items:
  - kind: configuration
    identity: missing
    freshness: current                 # unsupported freshness assertion
evidence:
  - criterion: missing
    subject_binding: missing
    reference: "green check"           # not an exact evidence reference
exceptions_or_open_conditions: material owner, exact subject, criterion, configuration identity and essential evidence are missing
permitted_destination_if_effective: none
record_validity: invalid; unusable as a pass
```

Interpretation: the word `passed` has no effect. Missing material owner, identity, bounded criterion and exact evidence invalidates the record. The required gate remains non-passing; a green label cannot repair it.

## D. Aggregation interpretation

A current verification projection is passing only when **every required obligation** has an actual, current pass on the correct exact subject and governing basis. The aggregation must account for all declared obligations without turning absence into success:

- a required `unsatisfied` obligation blocks pass;
- a changed subject, criterion, configuration, dependency, authority or other relied-upon basis makes the affected prior evidence stale and blocks current reliance;
- missing, incomplete or skipped required work is pending, failed or otherwise non-passing according to the actual result—never passed;
- wrong-subject or inaccessible essential evidence denies reliance;
- a legitimate `not-applicable` obligation is excluded only with its governing rule, accountable owner and contextual rationale; it has no satisfaction value and cannot offset a failed required obligation;
- aggregate green output is an observation derived from the underlying evaluations, not an independent authority, decision, review, disposition or acceptance.

For example, required results `[passed/current, passed/current, unsatisfied/current]` aggregate as non-passing. Adding a justified N/A row does not change that outcome. Likewise, `[passed/stale, passed/current]` is non-passing for current reliance. This interpretation does not select or implement an aggregation topology.

## E. Identity and evidence binding

Human-readable names, branch names, mutable labels, status badges, green checks and `done` statements are navigation or observations, not exact subject identity. Where repository evidence applies, use the complete tuple:

`repository + full containing commit SHA + path + Git blob + optional fragment`

For a relied-upon payload, also bind its exact byte count and SHA-256. The evidence reference must identify the criterion and exact subject it supports and remain retrievable under the applicable custody rules. If required bytes are missing, expired, inaccessible, mismatched or unsafe to retain, the dependent gate cannot pass; a digest without the governed bytes does not supply custody or sufficiency.

Identity establishes equality with identified bytes or an identified object. It does **not** prove truth, correctness, completeness, authority, authenticity, actor entitlement, reviewer independence, approval, retention, effective control or acceptance. Those claims require their own accountable owners, rules and evidence.

Freshness is item-specific. A single timestamp or current candidate identity cannot make a stale configuration, dependency, governing rule or evidence payload current. Before state-dependent reliance, each material mutable dimension actually relied upon must be reread and compared with its assignment-bound identity. A changed candidate or load-bearing basis leaves the former evaluation in immutable history under its old subject while the current pointer becomes non-passing until an authorized new evaluation supports it.

This reference neither resolves nor bypasses RG1-RG12. In particular, it does not infer protection, writer exclusion, exact publication mapping, reviewer identity, permissions, containment, recovery, custody, installed capability or AFK safety from an identity tuple.

## F. Explanatory review questions

These questions reproduce the material concerns of the controlling materialization gate:

- Does the exact subject and named transition match the governing assignment?
- Does the applicability decision have an accountable owner, governing rule and contextual rationale?
- Does every required satisfaction claim have complete, current, correct-subject evidence for each controlling criterion?
- Is every evidence pointer complete and retrievable under its applicable custody rules?
- Do N/A, missing, skipped, stale and unsatisfied cases remain distinguishable, with no absent work treated as pass?
- Does the claimed permitted destination actually follow from the controlling authority and bounded scope?
- Is the record evidence about a gate rather than a competing current-state owner?

Also confirm that evaluator and decision owner separation is preserved where required; immutable history is not rewritten through mutable current pointers; local and integrated verification, review and disposition remain distinct; DI-1 and DI-2 remain intact; and no unresolved RG prerequisite or unselected mechanism is presented as satisfied.

This checklist is explanatory only. Completing it is not independent review and cannot return a verdict, disposition, acceptance, baseline or authorization. Any later review must be separately authorized, bind its exact immutable subject and be performed by the accountable eligible reviewer required by its governing authority.

## Reference boundary

This draft creates no product or task identity, no operative record, no current gate, no schema or validator, no tooling or storage selection, no credential or permission, no implementation, no routine/parallel/automated/unattended/AFK authority, and no Workflow v1 adoption. It is ready only for the separately authorized candidate-persistence gate after producer verification; persistence, independent candidate review and coordinator disposition remain future distinct decisions.

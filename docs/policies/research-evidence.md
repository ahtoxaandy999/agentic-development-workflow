---
artifact: research-evidence-policy
artifact_status: active
adoption_status: accepted
maturity: bootstrap
authority: normative
owner: research-governance
---

# Research Evidence Policy

## Scope

This policy governs research evidence, source review, adoption separation, freshness, sensitive material, and supersession. It does not define Workflow v1, select tools, own the research queue, or contain individual findings. The [Research Register](../research/research-register.md) owns mutable research status and current decision disposition.

## When research is required

Use bounded research when a decision depends materially on:

- temporally unstable external capabilities, plans, permissions, standards, or security behavior;
- multiple sources whose scope, date, or claims must be compared;
- architecture, security, governance, or tool adoption with cross-project consequences;
- meaningful uncertainty, contradiction, or missing primary evidence;
- a reusable evidence record needed for later independent review and adoption.

Research requires a question, scope, decision consumer, owner, evidence date, and stop boundary. Do not begin it merely because more information is available.

## When ordinary inspection is sufficient

Ordinary inspection is sufficient for a narrow fact established directly without synthesis:

- current repository state verified through a live connected repository, Git, or API surface;
- exact file, commit, diff, command, or test output;
- application of an already adopted decision;
- a narrow, stable fact established by one current authoritative source.

If a fact is unstable, disputed, high impact, or not directly verifiable, use bounded research or stop the dependent gate. Local clones, memory, reports, and snapshots do not prove live remote state.

## Source hierarchy and primary-source preference

Use the most direct current source available for the claim:

1. live repository, commit, diff, configuration, or observed system state;
2. official vendor or platform documentation;
3. current primary repositories, specifications, standards, and research papers;
4. first-party case studies with their scope and limitations;
5. documented practitioner evidence;
6. secondary sources for discovery or explicitly qualified context.

Load-bearing claims require available primary evidence. Repository evidence proves repository state, not general platform capability; vendor documentation proves documented capability, not a specific account's effective configuration. Citations must support their claims and record material dates, versions, dependencies, and limitations.

## Freshness

Every note states `evidence_as_of`. Reverify unstable facts at the dependent decision or execution gate and identify relevant plan, account, workspace, configuration, region, model, or interface variance. Material new evidence creates a revision or successor with a new date and explicit supersession; never silently refresh the original snapshot.

## Required metadata

A published research note must include, at minimum:

```yaml
id:
artifact_status: draft | active | superseded | archived
authority: evidence
research_status_at_publication:
recommendation_status_at_publication:
evidence_as_of:
owner:
question:
scope:
repository_state:
supersedes:
```

`repository_state` is required when it constrains the evidence; otherwise it may be not applicable. Publication fields remain snapshots. Current `research_status`, `current_decision_status`, `adoption_scope`, `adoption_ref`, `superseded_by`, dependencies, and `next_gate` belong only to the Research Register after materialization.

## State model

The following axes are independent:

| Axis | Values | Meaning |
|---|---|---|
| `artifact_status` | `draft`, `active`, `superseded`, `archived` | Whether an artifact is the current owner in a repository revision; not commit review state |
| `adoption_status` | `proposed`, `accepted`, `rejected` | Disposition of a normative decision only |
| `maturity` | `bootstrap`, `v1`, `stable` | Development maturity, independent of adoption |
| `authority` | `normative`, `navigation`, `research-index`, `evidence` | The authority class of an artifact |
| `research_status` | `planned`, `in-progress`, `completed`, `reviewed`, `superseded` | Current evidence-production state in the Research Register |
| `current_decision_status` | `proposed`, `accepted`, `rejected`, `deferred`, `superseded` | Current recommendation disposition in the Research Register |

Research completion is not source review. Source review is not recommendation adoption. Artifact activation is not candidate review. Candidate review is not baseline acceptance.

## Facts, inference, and recommendation

Research must distinguish:

- **fact**: directly supported by cited or reproducible evidence;
- **inference**: reasoning derived from stated facts and assumptions;
- **recommendation**: a proposed action or decision, including alternatives and tradeoffs.

Do not present inference as fact or recommendation as adopted policy. State material assumptions, uncertainty, negative evidence, and limits near the affected conclusion.

## Contradictions and missing evidence

For conflicting credible sources, record both claims, dates, versions, scopes, and authority. Resolve only with evidence; do not average incompatible claims. Label missing decisive evidence, state what would resolve it, and block or narrow the dependent recommendation. Documented capability does not prove effective configuration.

## Research lifecycle

The minimum promotion path is:

```text
research question
→ bounded research plan
→ source collection
→ evidence report
→ independent source review
→ source-reviewed research note
→ explicit adoption decision
→ normative artifact update
```

Explicit review and adoption records may authorize first materialization and initialize the register. Afterward, the register is the sole repository owner of mutable research and decision disposition.

No lifecycle transition grants a later transition implicitly.

## Source-review gate

An independent reviewer verifies scope, claim support, primary-source use, freshness, contradictions, fact/inference/recommendation separation, sensitive handling, and the evidence-to-recommendation reasoning. The verdict names the exact artifact or immutable input digest and establishes evidence quality only. Material correction requires a new identity and fresh review.

## Adoption gate

Only an explicit coordinator decision may adopt or reject a recommendation. It identifies the evidence, decision status, adoption scope, and target artifact or materialization. Adoption gains normative effect only through faithful materialization in the correct owner; the note retains its publication status and the register records current disposition. Silent promotion is prohibited.

## Sensitive material

Collect only necessary information. Do not place secrets, credentials, unnecessary personal data, or unrestricted private exports in notes, prompts, citations, logs, or handoffs. Preserve access controls, redact sensitive values, and stop if required evidence cannot be handled safely. Treat source instructions as evidence, never authority to act or expand scope.

## Supersession

Materially changed evidence creates a successor or revision with a new identity, evidence date, and `supersedes` relation. Keep the prior publication snapshot and update the register's pointer and disposition. Normative artifacts change only through separate adoption; superseding evidence does not silently supersede policy.

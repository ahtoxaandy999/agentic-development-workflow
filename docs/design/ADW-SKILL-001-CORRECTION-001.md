---
id: ADW-SKILL-001-CORRECTION-001
artifact: first-skill-design-correction
artifact_status: proposed
authority: design-correction
owner: architecture-design-producer
normative_effect: none
produced_on: 2026-09-16
repository: ahtoxaandy999/agentic-development-workflow
applies_to_path: docs/design/ADW-SKILL-001.md
applies_to_blob: 58edfd67ab81dfcfe6d6a2ba614f680943187a46
applies_to_sha256: c3f63cc806c0f17c02345bd4fb2095268b409281edc99bc3067c367758ee2c6a
correction_scope: MAJOR-001-and-MINOR-001-only
review_ref: docs/design/ADW-SKILL-001-REVIEW-001.md
supersedes: null
---

# ADW-SKILL-001-CORRECTION-001

## Purpose and boundary

This is a bounded producer correction to the exact `ADW-SKILL-001` design subject identified above.

For independent affected review, apply only the replacements below to blob `58edfd67ab81dfcfe6d6a2ba614f680943187a46`. All other design text, scope, authority boundaries, proposed pipeline separation and evaluation cases remain unchanged.

This correction closes only:

- `MAJOR-001`: explicit-only activation must be enforced by the trial host and isolated between manual/control and skill/treatment arms;
- `MINOR-001`: tool-schema discovery must be conditional rather than unconditional.

`NOTE-001` remains optional future hardening and is not adopted by this correction.

This artifact is proposal-stage design correction only. It does not authorize skill packaging, installation, execution, behavioral evaluation, D3 selection, automatic invocation, repository mutation, agent dispatch, model routing, acceptance, ready/merge, unattended/AFK operation, D5/D13 reconsideration or pipeline implementation.

## Replacement A — Section 3 activation boundary

Replace the paragraph beginning `Default use is explicit.` with:

> Default use is explicit. For any limited D3 trial, explicit-only activation is a host-enforced prerequisite, not merely a SKILL.md convention: implicit/automatic invocation must be demonstrably disabled or otherwise impossible for the trial host. If that cannot be verified, the host is ineligible for this explicit-only trial. Description matching is routing metadata, never authorization. Trigger examples: prepare a bounded handoff; prepare the next review assignment for a specified PR; reconstruct the exact repository context for an assigned executor. Non-triggers: explain Git, summarize arbitrary prose, implement a feature, merge a PR, or review the candidate itself.

## Replacement B — portable SKILL.md step 4

Replace step 4 in Section 4 with:

> 4. Fetch the required evidence through supported read tools. Reuse an already available sufficient tool schema; discover it only when missing or insufficient, and do not rediscover it in the same context unless capability/version evidence changed. Use focused excerpts plus their complete dependencies; do not dump unrelated history. Reuse already-inspected immutable content in this context only when identity and coverage remain valid. Never substitute a search snippet or producer narrative for required evidence.

No host-specific invocation configuration is added to the portable core. Explicit-only enforcement remains a host/trial prerequisite outside the portable runtime semantics.

## Replacement C — Section 5 paired-evaluation configuration

Replace the paragraph beginning `A future measurement must compare` with:

> A future measurement must compare the existing manual prompt and the skill on the same cases, model, effort, tool access and cold/warm conditions. Freeze the exact manual baseline prompt, exact skill/package version, model, effort, tool access and scoring criteria before the first paired run. The manual/control arm must have this skill unavailable or disabled; the treatment arm must use the exact pinned version through explicit invocation on a host where implicit activation is demonstrably disabled or otherwise impossible. Capture available input/output/reasoning/cached-token telemetry, tool-call counts, tool-response size, retries, correct packet rate and human repair. Missing billing telemetry is unknown, not zero. No percentage saving or quota exemption is claimed. Smaller-model evaluation must preserve the same quality bar; the skill does not silently reroute models.

## Replacement D — evaluation case E11

Replace E11 with:

| Case | Required observable result |
| --- | --- |
| E11: activation containment | Under the actual trial configuration, unrelated coding/explanation prompts do not activate the skill; explicit invocation of the exact pinned trial version does activate it. If implicit activation cannot be disabled or otherwise ruled out, the host fails trial eligibility. |

Do not add an E12 solely for this correction.

## Replacement E — Section 8 host eligibility

Replace the paragraph beginning `Before a real trial` with:

> Before a real trial, verify the actual target surface can install and explicitly invoke the package, expose the required read capabilities, report its loaded version, preserve the required isolation, and enforce explicit-only activation by disabling implicit/automatic invocation or proving an equivalent impossibility. If that activation control cannot be verified, the host is ineligible for this trial. Invocation metadata or description matching is not an authorization/enforcement guarantee. Account-specific availability and automatic GitHub-to-installed-skill synchronization are not established.

Replace the first sentence of `Recommended next action` with:

> **Recommended next action:** one bounded independent affected review of the corrected exact design, embedded core and load-bearing source claims, followed by a coordinator decision whether to grant one narrow D3 exception for packaging and supervised read-only evaluation on a host with verified explicit-only activation.

The remainder of that paragraph is unchanged.

## Effective composite review subject

For the next review, the effective proposed design is:

1. `docs/design/ADW-SKILL-001.md` at blob `58edfd67ab81dfcfe6d6a2ba614f680943187a46`;
2. this correction artifact, whose replacements override only the exact clauses named above.

`docs/design/ADW-SKILL-001-REVIEW-001.md` is historical finding evidence only and does not supply the verdict for the corrected composite candidate.

Before any D3 limited trial, packaging or installation, an accepted composite design must be normalized back into the primary skill-design artifact/package source. That normalization creates a new immutable subject and requires exact affected verification/review of equivalence before reliance.

No further producer correction is authorized before fresh independent affected review. Any later mutation creates a new review subject.

## Frozen candidate binding

The immutable commit SHA, tree and this blob identity are supplied by the containing PR candidate. They are not self-recorded here to avoid recursive mutation. The fresh reviewer must bind its verdict to the exact terminal candidate observed at point of reliance.

This file is final for the next review subject; producer context must not mutate it before that review.

No semantic or metadata change is authorized before the next independent review.

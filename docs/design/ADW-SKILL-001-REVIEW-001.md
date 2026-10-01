---
id: ADW-SKILL-001-REVIEW-001
artifact_status: active
authority: evidence
review_type: independent-skill-design-review
review_target_commit: 4c6261d330843e73b5f2f8139dad525a29984654
review_target_parent: 796fef15a7ba3b78b57c1f06f5911c6a3f85dad5
review_target_path: docs/design/ADW-SKILL-001.md
review_target_blob: 58edfd67ab81dfcfe6d6a2ba614f680943187a46
review_target_bytes: 19826
review_target_sha256: c3f63cc806c0f17c02345bd4fb2095268b409281edc99bc3067c367758ee2c6a
verdict: requires-correction
finding_counts:
  blocker: 0
  major: 1
  minor: 1
  note: 1
reviewed_on: 2026-09-16
owner: agentic-development-independent-review
source_record_bytes: 12506
source_record_sha256: fad2f38736573259e09b047f9ed042ecfb060b7f3d1546840c709e953c087d0b
supersedes: null
---

# ADW-SKILL-001-REVIEW-001

## Verdict

**REQUIRES_CORRECTION**

The reviewed skill decomposition is sound and appropriately narrow: `adw-repo-handoff` prepares repository-grounded navigation/handoff packets and does not absorb execution, formal review, acceptance, publication, dispatch, model selection, recovery or orchestration.

This record is bound only to candidate `4c6261d330843e73b5f2f8139dad525a29984654` / blob `58edfd67ab81dfcfe6d6a2ba614f680943187a46`. Any material correction creates a new review subject.

## MAJOR-001 — explicit-only activation is not host-enforced

Affected proposal areas: Section 3 explicit-use boundary, Section 4 runtime metadata/core, Section 7 E11 and Section 8 pre-trial host verification.

Failure mode: the proposal declares explicit use, but the limited trial does not yet require the host to suppress implicit/automatic activation. A host may therefore activate the skill on an unrelated repository request, leaking the narrow D3 trial scope and contaminating the manual/control arm of the token-efficiency experiment.

Required correction:

- explicit-only activation must be a verified host-adapter prerequisite for the limited D3 trial;
- if the host supports implicit-invocation controls, implicit activation must be disabled;
- if equivalent suppression cannot be verified, that host is ineligible for the trial;
- description matching is routing metadata, not authorization;
- the manual/control arm must have the skill unavailable or disabled;
- the treatment arm must explicitly invoke the exact pinned trial version;
- E11 must test both non-activation for unrelated prompts and successful explicit activation of the pinned version.

The portable skill core need not encode host-specific configuration.

## MINOR-001 — schema discovery is unconditional

Affected proposal area: Section 4 step 4 and related token-efficiency rules.

Failure mode: `Discover each needed tool schema once` requires discovery even when a sufficient schema is already available, adding unnecessary tool calls/result volume and embedding a host-discovery assumption into the portable core.

Required correction: reuse an already available sufficient schema; discover only when missing or insufficient; do not rediscover in the same context unless capability/version evidence changed.

## NOTE-001 — future serialized projection provenance

Before a machine serializer/controller is authorized, consider adding explicit `projection_version` plus exact producing skill/package identity to the serialized envelope. This is optional hardening, not required for the present correction.

## Areas accepted by this review

Subject to MAJOR-001 and MINOR-001, the review found no material defect in:

- focused scope/minimality;
- repository authority and single-owner boundaries;
- exact-subject and composite-candidate handling;
- freshness and evidence completeness;
- independence separation;
- prompt-injection/untrusted-candidate treatment;
- read-only boundary and stop conditions;
- total-task-cost/token measurement approach;
- controller/pipeline separation;
- host/portable-core/repository/version separation;
- E1-E10 evaluation coverage;
- D5/D13 separation and absence of hidden execution/acceptance/publication authority.

D3 remains `CONFIRM DEFER` outside explicit exceptions. This review does not authorize packaging, installation, skill execution or the proposed behavioral evaluation.

## Required next gate

Create a new immutable corrected candidate limited to MAJOR-001 and MINOR-001, then perform fresh independent affected review of that exact candidate.

If that review passes, a coordinator may consider one narrow D3 limited-trial disposition naming the exact skill/package version, permitted host, verified explicit-only activation behavior, effective read-only capability boundary, isolated manual/treatment configuration, bounded evaluation cases and evidence destination.

**NOT READY FOR D3 LIMITED-TRIAL DISPOSITION**

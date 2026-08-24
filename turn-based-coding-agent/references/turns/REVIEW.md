# Optional Independent Review

**Context class:** `conditional-turn`

## Load contract

Load only when optional Review is explicitly requested or required by project policy.

Required dependencies:
- `references/core/turn-boundaries.md`
- `references/core/evidence.md`
- `references/core/recovery.md`
- `modules/engineering-guidelines/MODULE.md`

Conditional dependencies:
- `modules/unit-testing/MODULE.md` only when proposed test changes/design are under review.
- `modules/github-connector/MODULE.md` only when reviewing remote PR/workflow/artifact evidence.

Template: load `templates/REVIEW_REPORT.md` only when producing the review report.

## Goal

Independently challenge the evidence, diagnosis, and proposed next Code + Build plan. The reviewer may approve, amend, reorder, narrow, expand, or replace the plan, but may not modify or execute implementation/validation logic.

## Review

Inspect primary evidence rather than relying only on summaries. Ask whether:

- failure classifications are supported;
- the proposed correction addresses root cause rather than symptoms;
- assumptions are explicit and evidence-backed;
- a simpler/smaller correction exists;
- proposed changes are surgical and generalized;
- test changes preserve meaningful validation;
- acceptance criteria are observable and reproducible.

## Decisions

`approved` | `approved_with_amendments` | `rejected_and_replaced` | `insufficient_evidence`

Publish exactly one authoritative next plan or an explicit evidence-gathering plan. Update TODO/handoff and set `load_next` to the correct next Code + Build state. No source/test/benchmark/build logic may change in this turn.

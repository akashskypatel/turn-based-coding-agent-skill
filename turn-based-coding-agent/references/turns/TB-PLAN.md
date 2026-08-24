# TB-PLAN

**Context class:** `conditional-turn`

## Load contract

Load only after TB-REVIEW has documented findings.

Required dependencies:
- `references/core/recovery.md`
- `modules/engineering-guidelines/MODULE.md`

Conditional dependencies:
- `modules/unit-testing/MODULE.md` only when the proposed next CB plan includes test-source design/repair.
- `references/core/evidence.md` only when a planning claim requires re-checking provenance.

Template: load `templates/TEST_BENCHMARK_REPORT.md` only when producing/finalizing the canonical TB report.

## Goal

Convert reviewed evidence into phase status, corrective measures, and one proposed next Code + Build plan with observable verification criteria.

## Procedure

1. Start from TB-REVIEW findings; do not re-run validation here.
2. If failures exist, identify the smallest generalized corrective measures justified by evidence.
3. If all acceptance criteria pass, plan phase closure or the next intended phase rather than inventing corrective work.
4. For each next-CB task record:
   - required change and scope boundary;
   - assumptions/contracts;
   - build verification;
   - future TB validation;
   - known risks.
5. Decide whether optional independent Review is requested.
6. Update TODO/handoff and precompute the successor context set.

## Authority

- Review skipped: TB-PLAN becomes authoritative and routes to canonical CB or `CB-DRAFT` according to configured execution mode.
- Review requested: mark plan `proposed_pending_review` and set `load_next: references/turns/REVIEW.md`.

## Forbidden

- source/test/benchmark/build-logic edits;
- compiling or runtime execution;
- speculative fixes unsupported by reviewed evidence.

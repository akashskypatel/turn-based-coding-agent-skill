# Canonical Test + Benchmark

**Context class:** `conditional-turn`

## Load contract

Load when the current state is canonical `Test + Benchmark` without granular decomposition.

Required dependencies:
- `references/core/turn-boundaries.md`
- `references/core/evidence.md`
- `references/core/recovery.md`
- `references/07-testing-integrity.md`

Conditional dependencies:
- `modules/unit-testing/MODULE.md` only when unit-test validity/quality is under diagnosis.
- `modules/github-connector/MODULE.md` only for GitHub artifact/workflow work.

Templates: load `templates/TEST_BENCHMARK_REPORT.md` only when documenting results.

## Goal

Execute the pre-authored TB plan against the exact compiled evidence commit/artifact, review the results, classify findings, and create the proposed next Code + Build plan. Do not edit implementation or validation logic.

## Procedure

1. Verify artifact/source provenance and TB plan authority.
2. Execute the plan in its declared order, honoring stop/rerun conditions.
3. Preserve raw results, logs, metrics, traces, seeds, and environment information required by the plan.
4. Compare each result with its explicit acceptance criterion.
5. Classify failures as production implementation, structurally invalid fixture, incorrect expectation, infrastructure, performance regression, or nondeterminism.
6. Determine phase status.
7. Produce corrective measures and the proposed next Code + Build plan with verifiable build and future validation criteria.
8. Decide whether optional independent Review is requested.
9. Update TODO/handoff and precompute the successor's context load plan.

## Exit gate

- planned validation is complete or an explicit blocker is evidenced;
- every finding has evidence/classification;
- no implementation/test/benchmark/build logic changed;
- one proposed next Code + Build plan exists;
- if review is skipped, that plan becomes authoritative; otherwise mark it `proposed_pending_review` and route to `references/turns/REVIEW.md`.

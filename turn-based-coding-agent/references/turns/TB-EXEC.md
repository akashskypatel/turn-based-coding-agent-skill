# TB-EXEC

**Context class:** `conditional-turn`

## Load contract

Load only when `canonical_turn=Test + Benchmark` and `subturn=TB-EXEC`.

Required dependencies:
- `references/core/turn-boundaries.md`
- `references/core/evidence.md`

Conditional dependencies:
- `modules/github-connector/MODULE.md` only for remote artifact/workflow operations.

Do not load unit-testing or engineering-guidelines modules merely because tests exist. This state executes the approved plan; it does not design or review tests.

## Goal

Execute the pre-authored TB plan against the exact compiled evidence commit/artifact and preserve raw evidence.

## Procedure

1. Verify source/artifact provenance and integrity.
2. Execute the plan in declared order.
3. Honor plan-defined stop, repetition, seed, and rerun rules.
4. Preserve raw logs/results/traces/dumps/metrics and material environment details.
5. Record deviations explicitly; do not silently expand validation scope.

## Forbidden

- implementation/test/benchmark/build-logic edits;
- compiling replacement code;
- corrective implementation planning;
- unplanned exploratory runtime work unless the plan explicitly permits it.

## Exit

When planned execution completes or an explicit blocker stops it, set `load_next: references/turns/TB-REVIEW.md`. Do not preload TB-PLAN.

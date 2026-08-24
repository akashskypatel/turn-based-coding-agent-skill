# Canonical Code + Build

**Context class:** `conditional-turn`

## Load contract

Load when the current state is canonical `Code + Build` without granular decomposition.

Do not load granular CB files unless execution mode changes before the turn starts.

Required dependencies:
- `references/core/turn-boundaries.md`
- `references/core/evidence.md`
- `references/core/recovery.md`
- `references/03-repository-workflow.md`
- `modules/engineering-guidelines/MODULE.md`

Conditional dependencies:
- `modules/unit-testing/MODULE.md` only when unit-test source is designed/changed.
- `modules/github-connector/MODULE.md` only for GitHub connector/hybrid/Actions work.

Templates: load `templates/CODE_BUILD_REPORT.md` and `templates/TEST_PLAN.md` only during closeout.

## Goal

Implement the authoritative plan, compile the exact pushed source revision, document the change, and produce the executable Test + Benchmark plan. Do not run runtime tests or benchmarks.

## Procedure

1. Resolve the authoritative implementation plan and evidence-backed assumptions.
2. Use the engineering module to choose the smallest sufficient, surgical change.
3. Edit production/test/benchmark/build logic only as justified by the plan.
4. Review the diff; remove unrelated changes and style drift.
5. Commit/push and compile the exact pushed revision.
6. On compile failure, preserve the first actionable error, apply the smallest corrective change, recommit/push, and repeat compilation.
7. On compile success, record the exact evidence commit/artifact.
8. Draft change documentation and an executable TB plan for that exact evidence commit/artifact.
9. Update TODO/handoff and precompute the successor's context load plan.

## Exit gate

- required targets compile successfully;
- no runtime tests/benchmarks executed;
- source and evidence provenance are exact;
- change documentation is current;
- TB plan has ordered commands, inputs, acceptance criteria, evidence requirements, benchmark parameters where applicable, and stop/rerun rules;
- next state is canonical `Test + Benchmark`.

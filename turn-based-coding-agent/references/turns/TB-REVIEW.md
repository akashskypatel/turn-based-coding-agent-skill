# TB-REVIEW

**Context class:** `conditional-turn`

## Load contract

Load only when `canonical_turn=Test + Benchmark` and `subturn=TB-REVIEW` after TB execution evidence exists.

Required dependencies:
- `references/core/evidence.md`
- `references/07-testing-integrity.md`

Conditional dependencies:
- `modules/unit-testing/MODULE.md` only when a unit-test fixture, expectation, assertion, isolation, or scope question is material to a finding.

Do not load engineering-guidelines or TB-PLAN until evidence review is complete.

## Goal

Interpret existing TB evidence against the pre-authored acceptance criteria and classify findings without changing code or expanding runtime work.

## Review

For each planned validation item:

1. Confirm evidence is complete and trustworthy.
2. Compare actual result with the explicit acceptance criterion.
3. Classify failures as production implementation, structurally invalid fixture, incorrect expectation, infrastructure, performance regression, or nondeterminism.
4. Record confidence and unresolved evidence gaps.
5. Use the unit-testing module only when the test itself is materially in question.

## Forbidden

- source/test/benchmark/build-logic edits;
- new unplanned test/benchmark execution;
- corrective code design before findings are settled;
- treating a passing focused test as proof of full production readiness.

## Exit

Produce documented findings and set `load_next: references/turns/TB-PLAN.md`.

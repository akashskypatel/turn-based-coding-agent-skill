# Unit Testing Module

Internal progressive-disclosure module for `turn-based-coding-agent`. Load it when creating unit tests, reviewing unit-test quality, adding regression coverage, correcting invalid unit-test fixtures, or deciding whether a check belongs at unit or integration scope.

This module is not a standalone skill and does not override the active turn/subturn boundary.

## Core contract

A strong unit test should be:

- **Behavioral**: verify an externally observable contract or invariant, not incidental implementation details.
- **Focused**: exercise one scenario or behavior so a failure has a narrow cause.
- **Fast and isolated**: avoid infrastructure, process-wide mutable state, and unnecessary expensive collaborators.
- **Repeatable**: the same code and inputs produce the same result independent of test order, wall clock, network, machine state, or random chance.
- **Self-checking**: determine pass/fail automatically with precise semantic assertions.
- **Readable**: make setup, action, expected behavior, and failure meaning obvious.
- **Actionable**: a failing test name and assertion output should provide enough information to begin diagnosis immediately.
- **Resilient**: legitimate refactoring that preserves behavior should rarely require rewriting assertions.

Do not optimize tests for coverage percentage alone. Coverage is a gap signal, not proof that behavior is adequately tested.

## Progressive task index

Read only what the current task requires.

### Design new unit tests

Read:

- `references/01-scope-and-contract.md`
- `references/02-case-design.md`
- `references/04-assertions-and-diagnostics.md`
- `references/03-isolation-and-test-doubles.md` when the unit has collaborators

Use `templates/UNIT_TEST_PLAN.md` when the test surface is non-trivial.

### Add a regression test for a defect

Read:

- `references/01-scope-and-contract.md`
- `references/02-case-design.md`
- `references/05-review-regression-and-coverage.md`
- `references/04-assertions-and-diagnostics.md`

### Review or repair existing unit tests

Read:

- `references/05-review-regression-and-coverage.md`
- `references/04-assertions-and-diagnostics.md`
- `references/03-isolation-and-test-doubles.md` when brittleness or flakiness involves collaborators

Use `templates/UNIT_TEST_REVIEW.md` for a structured review.

### Resolve test-double or isolation design

Read:

- `references/03-isolation-and-test-doubles.md`
- `references/01-scope-and-contract.md`

### Check research basis

Read `references/06-research-basis.md` for the sources and rationale behind these rules.

## Non-negotiable rules

1. Establish the intended contract before writing assertions.
2. Prefer observable outputs, state transitions, errors, and required boundary interactions over private implementation details.
3. Do not make tests pass synthetically by weakening assertions, recognizing fixtures, skipping production behavior, or encoding current implementation output as the expected result.
4. Correct a fixture only when it does not actually create the scenario the test claims to validate; preserve or strengthen the intended assertion.
5. Avoid hidden dependencies on test order, global mutable state, environment, locale, filesystem, database, network, wall clock, or uncontrolled randomness.
6. Prefer the highest-fidelity collaborator that remains fast, deterministic, and local. Use mocks narrowly when interaction itself is part of the contract.
7. Choose test values deliberately. Include non-default values and distinguish inputs so broken code cannot pass accidentally because defaults or reused values happen to match.
8. A test may contain multiple assertions when they jointly verify one coherent behavior; do not force an artificial one-assert rule.
9. Prefer narrow semantic assertions over broad object snapshots or exact internal call sequences.
10. Treat flaky tests as defects. Diagnose nondeterminism rather than masking it with retries.

## Turn and subturn integration

When this module is active:

### Canonical mode

- Unit-test source changes happen only during **Code + Build**.
- Unit tests execute only during **Test + Benchmark**.
- Optional **Review** may critique unit-test design and amend the next action plan, but does not edit test code.

### Granular mode

- **CB-DRAFT** may design unit-test source and include it in the draft patch.
- **CB-APPLY** may apply/commit the reviewed unit-test patch, but may not execute it.
- **CB-COMPILE** may compile the unit-test target, but may not execute tests or edit test logic.
- **CB-CLOSEOUT** incorporates the unit-test cases into the mandatory Test + Benchmark plan.
- **TB-EXEC** executes the planned unit tests.
- **TB-REVIEW** uses this module to assess fixture, assertion, isolation, expectation, scope, and flakiness quality without editing tests.
- **TB-PLAN** may propose future unit-test changes for the next Code + Build plan but may not edit tests.

`../../references/07-testing-integrity.md` remains authoritative for test-versus-implementation diagnosis and organic validation.

This module supplies unit-test design quality; it does not authorize actions forbidden by the current canonical turn or granular subturn.

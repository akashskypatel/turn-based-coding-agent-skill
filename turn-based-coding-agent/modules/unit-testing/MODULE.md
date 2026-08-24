# Unit Testing Module

**Context class:** `conditional-capability`

Load only when a unit-test design question is actually material:

- `CB-DRAFT` / canonical CB when designing or repairing unit-test source;
- `TB-REVIEW` when fixture, expectation, assertion, isolation, flakiness, or test scope is under diagnosis;
- `TB-PLAN` or independent Review when proposed future test changes require quality review.

Do not load merely because unit tests will execute. In particular, normal `CB-COMPILE` and `TB-EXEC` do not need this module.

This module is subordinate to the active turn boundary and `../../references/07-testing-integrity.md`.

## Core contract

Strong unit tests are behavioral, focused, fast/local, deterministic, self-checking, readable/actionable, and resilient to behavior-preserving refactoring. Coverage is a gap signal, not proof of correctness.

## Reference router

Load only references needed for the current question:

### New test or regression design
- `references/01-scope-and-contract.md`
- `references/02-case-design.md`
- `references/04-assertions-and-diagnostics.md`
- add `references/03-isolation-and-test-doubles.md` only when collaborators/nondeterminism require it

### Existing-test diagnosis/review
- `references/05-review-regression-and-coverage.md`
- add `references/04-assertions-and-diagnostics.md` only for assertion/diagnostic quality
- add `references/03-isolation-and-test-doubles.md` only for collaborator/flakiness issues

### Research/provenance audit
- `references/06-research-basis.md` only; this is cold storage and must not be loaded during normal execution

Templates are loaded only when creating their artifact:
- `templates/UNIT_TEST_PLAN.md`
- `templates/UNIT_TEST_REVIEW.md`

## Non-negotiable rules

- Establish intended behavior before expected values/assertions.
- Prefer observable behavior over private implementation details.
- Never weaken assertions, recognize fixtures, skip production behavior, or encode current implementation output to manufacture success.
- Correct fixtures only when they fail to create the claimed scenario; preserve or strengthen semantic assertions.
- Avoid test-order, global-state, environment, locale, filesystem/network/database, wall-clock, or uncontrolled-random dependencies at unit scope.
- Prefer the highest-fidelity collaborator that remains fast, deterministic, and local; mock narrowly when interaction itself is contractual.
- Use deliberate non-default/distinct values so ignored/swapped/defaulted inputs cannot accidentally pass.
- Multiple assertions are acceptable when they jointly verify one coherent behavior.
- Treat flaky tests as defects; diagnose nondeterminism rather than masking it with retries.

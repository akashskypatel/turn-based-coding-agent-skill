# Test Case Design

## One scenario, one reason to fail

A unit test should normally describe one scenario and one expected behavior. Multiple assertions are acceptable when they jointly prove that one behavior.

Split a test when it contains multiple independent acts, unrelated scenarios, or assertions whose failures would point to different product behaviors.

## Arrange, Act, Assert

Structure tests so the reader can identify:

1. **Arrange**: minimal preconditions and dependencies.
2. **Act**: the production action under test.
3. **Assert**: the observable result.

Keep the Act section small. If setup is large, use well-named helpers that describe domain state rather than hiding the scenario behind generic fixture machinery.

## Derive cases from the contract

Do not choose cases by walking implementation branches alone. Start with behavior classes such as:

- Normal/representative input.
- Minimum and maximum valid boundaries.
- Values immediately below or above boundaries when meaningful.
- Empty, missing, null, zero, or default input when permitted by the API.
- Invalid input and error behavior.
- State transitions and repeated operations.
- Idempotence, ordering, uniqueness, conservation, or other domain invariants.
- Previously failing regression scenarios.

Use equivalence classes to avoid redundant tests: one representative case is usually enough when all values are governed by the same rule.

## Choose values that expose defects

Use values that make mistakes observable:

- Prefer non-default values when testing storage, propagation, or transformation.
- Give different inputs distinct values so swapped or reused arguments are detectable.
- Avoid symmetric values when asymmetry is relevant.
- Avoid coincidental identities such as multiplying by 1, adding 0, or empty collections unless those identities are the behavior under test.
- Add explicit default-value cases separately when defaults are part of the contract.

A passing test is weak if broken code could return a language/runtime default and still satisfy the assertion.

## Parameterized tests

Use parameterized/table-driven tests when multiple inputs exercise the same behavior rule and share the same arrangement and assertion shape.

Do not combine semantically different behaviors into one data table merely to reduce lines of test code. Each parameterized case must have an identifiable name or failure output.

## Avoid logic that can hide test bugs

Keep expected results explicit when practical. Avoid loops, branches, duplicated production algorithms, parsers, or substantial calculations inside a unit test.

When expected values require non-trivial computation, prefer:

- a simple independent oracle,
- a trusted reference implementation,
- a property/invariant with independently checkable consequences, or
- a small explicit fixture with known semantics.

Do not compute the expected result using the same algorithm or helper under test.

## Regression tests

For a defect:

1. Capture the smallest scenario that reproduces the violated contract.
2. Ensure the test would fail for the defective behavior.
3. Assert the user/domain-visible consequence, not the exact implementation of the fix.
4. Generalize the fixture enough to protect the defect class without hard-coding a named artifact.
5. Preserve the test after the fix as regression coverage.

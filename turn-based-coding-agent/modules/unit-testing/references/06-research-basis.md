# Research Basis

This skill distills stable unit-testing guidance from the following sources. The operational modules intentionally avoid framework-specific syntax unless it illustrates a general rule.

## Microsoft Learn: Unit testing best practices

https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices

Key guidance used here:

- Good unit tests are fast, isolated, repeatable, self-checking, and timely.
- Avoid infrastructure dependencies in unit tests.
- Use descriptive names that communicate scenario and expected behavior.
- Arrange, Act, Assert improves readability.
- Avoid non-trivial logic inside tests.
- Treat coverage as useful information, not a synonym for quality.

## Microsoft Learn: Order unit tests

https://learn.microsoft.com/en-us/dotnet/core/testing/order-unit-tests

Key guidance used here:

- Unit-test ordering should normally not matter.
- Tests should not rely on state produced by previous tests.

## Google Testing Blog: Test Behavior, Not Implementation

https://testing.googleblog.com/2013/08/testing-on-toilet-test-behavior-not.html

Key guidance used here:

- Test public/user-visible behavior by default.
- Behavior-preserving refactors should not normally require assertion changes.
- Implementation-detail tests are justified only when the detail itself matters to the contract.

## Google Testing Blog: Keep Tests Focused

https://testing.googleblog.com/2018/06/testing-on-toilet-keep-tests-focused.html

Key guidance used here:

- One test should normally represent one scenario/behavior.
- Focused tests localize failures and make intent clearer.

## Google Testing Blog: Test Failures Should Be Actionable

https://testing.googleblog.com/2024/05/test-failures-should-be-actionable.html

Key guidance used here:

- A failing test's name and failure output should be enough to start diagnosis.
- Prefer precise assertions and narrow invariants over broad checks.

## Google Testing Blog: Writing Descriptive Test Names

https://testing.googleblog.com/2014/10/testing-on-toilet-writing-descriptive.html

Key guidance used here:

- Include the scenario and expected outcome in the test name.
- Test names should reveal missing behavior coverage and identify failures quickly.

## Google Testing Blog: Increase Test Fidelity By Avoiding Mocks

https://testing.googleblog.com/2024/02/increase-test-fidelity-by-avoiding-mocks.html

Key guidance used here:

- Prefer the highest-fidelity collaborator practical for a test.
- Excessive mocks can reduce bug-detection ability and couple tests to implementation details.

## Google Testing Blog: Know Your Test Doubles

https://testing.googleblog.com/2013/07/testing-on-toilet-know-your-test-doubles.html

Key guidance used here:

- Distinguish fakes, stubs, and mocks by purpose rather than calling every replacement a mock.

## Google Testing Blog: Choosing Values for Robust Tests

https://testing.googleblog.com/2026/06/choosing-values-for-robust-tests.html

Key guidance used here:

- Prefer non-default values where defaults could hide a broken implementation.
- Use distinct values for distinct inputs to expose swaps/reuse.
- Include boundaries, missing/empty cases, and important special cases.

## Google Testing Blog: Code Coverage Best Practices

https://testing.googleblog.com/2020/08/code-coverage-best-practices.html

Key guidance used here:

- Coverage is useful for identifying risk and gaps but is not proof of test quality.
- Do not add low-value tests simply to satisfy a coverage number.
- Mutation testing can help evaluate whether tests actually detect plausible defects.

## Google Testing Blog: Mutation Testing

https://testing.googleblog.com/2021/04/mutation-testing.html

Key guidance used here:

- Mutation testing evaluates test effectiveness by checking whether injected defects are detected.
- Counterfactual reasoning about plausible broken implementations is a useful lightweight analogue when mutation tooling is unavailable.

## Interpretation notes

Some testing schools disagree on how strictly a unit must isolate collaborators. This skill deliberately does **not** mandate that every collaborator be mocked. It defines the useful unit boundary by fast, deterministic, localizable behavior and prefers real in-process collaborators when they improve fidelity without sacrificing those properties.

Likewise, this skill does **not** mandate one assertion per test. The stronger rule is one coherent behavior per test with assertions narrow enough to keep failures actionable.

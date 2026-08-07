# Review, Regression, and Coverage

## Unit-test review order

Review a test in this order:

1. **Contract**: What behavior or invariant is this test supposed to protect?
2. **Scope**: Is this genuinely unit-scale, or is the risk integration/infrastructure behavior?
3. **Fixture**: Does the setup actually create the claimed scenario?
4. **Oracle**: Is the expected result independently justified?
5. **Signal**: Would a plausible defect make the test fail for the right reason?
6. **Isolation**: Can order, environment, time, randomness, or shared state change the result?
7. **Maintainability**: Would a behavior-preserving refactor unnecessarily break this test?
8. **Diagnostics**: Does failure output make the problem actionable?

## Counterfactual quality check

Ask what incorrect implementations would still pass.

Examples:

- returning a default value,
- ignoring one input,
- swapping two inputs,
- omitting a required state update,
- executing a side effect twice,
- accepting an invalid boundary,
- returning success without performing the operation.

If an obvious defect survives, strengthen the values or assertions rather than adding unrelated cases.

Mutation testing can automate this reasoning when the project supports it, but it is not required for every change.

## Code coverage

Use coverage to find unexercised risk, not as a definition of test quality.

High line coverage does not prove that assertions are meaningful or that important input classes are tested. Do not:

- copy/paste tests solely to raise a percentage,
- assert trivial facts after executing lines,
- weaken design to satisfy a coverage target,
- treat 100% coverage as proof of correctness.

Prioritize coverage for changed, critical, complex, failure-prone, and long-lived code. Investigate uncovered branches and conditions in terms of behavior.

## Regression-test proof

For a bug fix, prefer evidence that the regression test fails against the defective behavior and passes after the correction.

When strict turn separation prevents executing the test during the code-change turn, record the expected pre-fix failure reasoning and validate it in the designated test turn or against an available pre-fix artifact.

A regression test should protect the violated contract, not the specific line-level implementation of the fix.

## Flakiness

A flaky test is a defect in the test, production concurrency, environment, or infrastructure.

Do not normalize retries as the fix. Record:

- seeds,
- ordering,
- timing,
- parallelism,
- environment,
- shared resources,
- failure frequency.

Then remove or control the nondeterministic dependency.

## Common test smells

Investigate tests that have:

- multiple unrelated Acts,
- large shared/global fixtures,
- hidden test ordering,
- sleeps or timing races,
- network/database/filesystem dependence at unit scope,
- extensive mock setup,
- exact internal call-order verification,
- private-member testing,
- duplicated production algorithms in expected-value calculation,
- conditionals/loops that obscure cases,
- broad snapshots for narrow behavior,
- values equal to defaults everywhere,
- assertions that only check non-null/existence when semantics matter,
- ignored/skipped failures without a tracked reason.

## Invalid fixture versus product defect

Do not decide based on which fix is easier.

Separately establish:

1. documented expected behavior,
2. actual fixture state,
3. required preconditions for the scenario,
4. implementation result,
5. assertion semantics.

Correct the fixture only when it cannot structurally exercise the intended behavior. Otherwise preserve the test and fix production behavior.

## Review outcome

Classify findings as:

- valid test,
- missing scenario coverage,
- brittle implementation coupling,
- invalid fixture,
- incorrect expectation,
- wrong test level,
- isolation/flakiness defect,
- weak oracle/assertion,
- over-mocking,
- coverage gap without proven behavior gap.

For each actionable finding, state the smallest correction and how it will be verified.

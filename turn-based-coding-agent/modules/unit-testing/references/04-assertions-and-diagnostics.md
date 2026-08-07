# Assertions and Diagnostics

## Assert semantics, not representation

Assertions should target the smallest observable fact that proves the behavior.

Prefer:

- Exact domain values when exactness is contractual.
- Typed/status-aware matchers for errors and result types.
- Collection membership/order assertions that match the actual contract.
- Approximate numeric assertions with a justified tolerance when floating-point error is expected.
- Explicit state-transition checks.

Avoid broad equality against a large object when only one or two fields matter. Broad assertions create unrelated failures and couple tests to representation details.

## One behavior may need several assertions

Do not enforce a mechanical one-assert-per-test rule.

Several assertions are appropriate when they describe one coherent outcome, for example:

- operation succeeds,
- returned identifier is valid,
- resulting object contains the requested value,
- prohibited side effect did not occur.

Split the test when assertions protect independent behaviors or require multiple separate Acts.

## Make failure output actionable

A failed test should usually be diagnosable from its name and assertion message without adding logging and rerunning it.

Use the most specific assertion/matcher available. Prefer assertions that print expected and actual values, structured error details, collection differences, or relevant status information.

Avoid assertions such as `assertTrue(result.ok())` when the framework can assert the complete result/status and show the actual failure payload.

## Test names describe behavior

Follow the project's naming convention, but include at least:

- the scenario or precondition, and
- the expected outcome.

Examples of useful shapes:

```text
Method_Scenario_ExpectedBehavior
GivenCondition_WhenAction_ThenOutcome
ShouldOutcome_WhenScenario
```

Do not encode implementation steps in the name unless they are the contract.

## Exceptions and error behavior

Assert the strongest stable error contract available:

- error/result category or type,
- error code,
- required structured metadata,
- stable message fragment only when message text is part of the contract.

Avoid exact full-message assertions for incidental diagnostic wording.

## Floating point and tolerances

A tolerance is part of the test oracle. Derive it from numerical requirements, algorithmic error bounds, representation precision, or accepted domain accuracy.

Never increase a tolerance only because a regression currently fails.

## Snapshots and golden files

Use snapshots/goldens cautiously in unit tests. They are appropriate when serialized/rendered representation is itself the contract and changes can be reviewed semantically.

Do not use a broad snapshot to avoid writing meaningful assertions. Never regenerate a golden file solely to make the test pass; review and explain the semantic difference first.

## Failure messages and context

Add custom context when the native assertion cannot expose the relevant input or invariant. Keep it concise and deterministic.

For parameterized tests, ensure each case identifies its parameters or has a descriptive display name so one failing row is actionable.

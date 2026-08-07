# Test + Benchmark Turn

## Purpose

Validate the exact successfully built source commit, classify failures, and produce the proposed next Code + Build action plan. Do not edit implementation or validation logic.

## Entry checks

- Confirm the designated turn type is Test + Benchmark.
- Confirm the implementation commit built successfully.
- Identify the exact built evidence commit and latest handoff commit.
- Verify the evidence commit is reachable from the handoff commit and only allowed documentation changed between them.
- Obtain artifacts built from the exact evidence commit.
- Read the live handoff and verify the pending validation scope.
- When artifacts or workflow evidence come from GitHub Actions, read `references/10-github-connector-workflows.md`.
- When unit-test failures require fixture, expectation, assertion, isolation, or scope diagnosis, load the companion `unit-testing` skill for analysis only.

## Artifact integrity gate

Before executing a packaged binary:

1. Download the exact declared artifact through the connector.
2. Verify the outer digest when supplied.
3. Verify the recursive checksum manifest.
4. Verify source commit, clean source status, dependency/submodule revisions, required binaries/libraries, and fixture/input closure.
5. Extract into an arbitrary directory.
6. Do not configure, compile, relink, patch, or regenerate code.

If integrity fails, classify infrastructure status separately and do not claim product pass or fail.

## Allowed work

- Retrieve compiled artifacts and detailed workflow logs.
- Run focused, regression, integration, full-suite, and platform tests.
- Run correctness, quality, performance, memory, and determinism benchmarks.
- Collect logs, reports, traces, crash dumps, seeds, and outputs.
- Compare results with accepted baselines.
- Analyze unit-test design using the companion `unit-testing` skill without editing test code.
- Update TODO and validation-result documents.
- Propose the next Code + Build action plan.

## Forbidden work

- Modifying production behavior.
- Editing test or benchmark logic.
- Fixing build configuration.
- Weakening assertions or thresholds.
- Compiling a replacement source revision.
- Combining diagnosis with an implementation fix.

## Test order

Use increasing scope where practical:

1. Direct defect reproduction.
2. Focused subsystem tests.
3. Related regressions.
4. Integration tests.
5. Full suite.
6. Required platform validation.

Record exact commit, artifact, commands, environment, filters, counts, duration, exit type, and evidence locations.

## Unit-test diagnosis

For a failing unit test, use the companion `unit-testing` skill to check whether:

- the asserted behavior is supported by an authoritative contract,
- the fixture actually creates the claimed scenario,
- the test belongs at unit scope,
- expected values are independently justified,
- mocks or test doubles distort production semantics,
- ordering, time, randomness, environment, or shared state can change the result,
- the assertion is too broad, too weak, or coupled to implementation details.

This analysis may change the proposed next-turn plan, but all source/test edits remain deferred to the next Code + Build turn.

## Benchmark execution

Compare against last known good, previous phase, quality thresholds, runtime/memory budgets, and determinism requirements. Record inputs, repetition count, timing, memory, quality, variance, structural digests, and baseline differences.

Faster execution is not success when correctness or quality regresses.

## Remote evidence requirements

- Preserve every raw log and machine-readable result.
- Use the detailed workflow log artifact when diagnosing build or packaging failures.
- Record result and log artifact IDs, names, digests, source SHA, and retention when relevant.
- A green workflow summary does not prove artifact integrity or runtime correctness.
- Do not trigger a compile workflow from a Test + Benchmark turn to replace an invalid artifact.

## Failure classifications

Classify each failure as production implementation, structurally invalid fixture, incorrect expectation, infrastructure, performance regression, or nondeterminism. Preserve evidence and avoid over-claiming certainty.

## Exit requirements

- All requested validation results are recorded.
- Every failure is classified with evidence.
- Phase status is explicit: complete, incomplete, blocked, or regressed.
- A proposed next Code + Build plan exists.
- TODO records whether optional review is requested.
- The live handoff records the exact next turn, evidence commit/artifact, authoritative or pending plan, missing procedure, and lessons.
- Every agent entry-point document still links to the handoff.

If review is skipped, the proposed plan becomes authoritative. If requested, label it `proposed_pending_review`.

Use `templates/TEST_BENCHMARK_REPORT.md`.

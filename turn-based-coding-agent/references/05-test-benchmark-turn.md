# Test + Benchmark Turn

## Purpose

Validate the exact successfully built source commit, classify failures, and produce the proposed next Code + Build action plan. Do not edit implementation or validation logic.

## Entry checks

- Confirm the designated turn type is Test + Benchmark.
- Confirm the implementation commit built successfully.
- Identify the exact built evidence commit and the latest handoff commit.
- Verify the evidence commit is reachable from the handoff commit and that only agent documentation changed between them.
- Obtain artifacts built from the exact evidence commit.
- Read the live handoff first and verify it matches the commit and pending validation scope.
- Review acceptance criteria and this turn protocol.

## Allowed work

- Retrieve compiled artifacts.
- Run focused, regression, integration, full-suite, and platform tests.
- Run correctness, quality, performance, memory, and determinism benchmarks.
- Collect logs, reports, traces, crash dumps, seeds, and output artifacts.
- Compare results with accepted baselines.
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
6. Required platform-specific validation.

Record the exact commit, commands, environment, filters, counts, runtime, and evidence locations.

## Benchmark execution

Compare against applicable baselines and budgets:

- Last known good revision.
- Previous phase result.
- Correctness and output-quality thresholds.
- Runtime and memory budgets.
- Determinism requirements.

Record inputs, repetition count, timing, memory, quality metrics, variance, and baseline difference. Faster execution is not success when correctness or quality regresses.

## Failure classifications

### Production implementation failure

The implementation violates the intended contract. Preserve the test and plan a production-code correction.

### Structurally invalid test scenario

The fixture cannot create the condition the test claims to validate. Explain the mismatch and plan a stronger valid fixture without weakening the intended assertion.

### Incorrect test expectation

The fixture is valid, but the assertion conflicts with an authoritative contract. Cite the contract and plan the expectation correction.

### Infrastructure failure

The environment or artifact prevents meaningful validation. Separate infrastructure status from product correctness and do not claim pass or fail without evidence.

### Performance regression

Functional behavior passes but an accepted budget regresses. Quantify significance and plan optimization without weakening correctness.

### Nondeterministic failure

Results vary across repeated runs. Preserve seeds and artifacts; investigate ordering, shared state, concurrency, undefined behavior, or numerical instability next turn.

## Exit requirements

- All requested validation results are recorded.
- Every failure is classified with evidence.
- Phase status is explicit: complete, incomplete, blocked, or regressed.
- A proposed next Code + Build action plan exists.
- The TODO records whether optional independent review is requested.
- The live handoff is updated with the exact next turn, authoritative or pending plan, evidence references, missing procedure, and lessons from failures or invalid assumptions.
- It records the validated evidence commit separately from the documentation-only handoff commit.
- Every agent entry-point document still links to the handoff.

If review is skipped, this proposed plan becomes authoritative immediately.

If review is requested, label this plan `proposed_pending_review`; the Review turn may supersede it.

Use `templates/TEST_BENCHMARK_REPORT.md`.

# Test + Benchmark Plan

## Validation Identity

- Phase:
- Working branch:
- Evidence commit to validate:
- Build artifact(s):
- Artifact digest/checksum reference:
- Planned environment/platform:

## Validation Objective

- Behavior/invariant being validated:
- Regression or defect being reproduced, when applicable:
- Why this plan is sufficient to evaluate the active Code + Build change:

## Preconditions

- Required fixtures/inputs:
- Required seeds/configuration:
- Required dependencies/runtime:
- Artifact integrity checks:

## Ordered Execution Plan

### 1. Direct / Focused Validation

- Command/test/benchmark:
- Purpose:
- Expected result:
- Acceptance criterion:
- Evidence to preserve:

### 2. Related Regression Validation

- Command/test/benchmark:
- Purpose:
- Expected result:
- Acceptance criterion:
- Evidence to preserve:

### 3. Integration / Broader Validation

- Command/test/benchmark:
- Purpose:
- Expected result:
- Acceptance criterion:
- Evidence to preserve:

### 4. Full / Platform Validation

- Command/test/benchmark:
- Purpose:
- Expected result:
- Acceptance criterion:
- Evidence to preserve:

## Benchmark Plan

- Applicable: yes | no
- Baseline commit/result:
- Inputs/corpus:
- Repetitions/warmup:
- Correctness/quality criteria:
- Runtime budget:
- Memory budget:
- Variance tolerance:
- Determinism requirement:

## Unit-Test Design Check

When unit tests are included, reference `modules/unit-testing/MODULE.md` and record:

- Contract under test:
- Scenario/boundary represented:
- Why fixture values expose plausible broken behavior:
- Isolation/test-double rationale:
- Assertion semantics:

## Stop and Blocker Conditions

Stop execution and preserve evidence when:

- artifact/source identity does not match the plan,
- artifact integrity fails,
- required environment or dependency is unavailable,
- a plan-defined prerequisite fails,
- continuing would invalidate later evidence.

Other project-specific stop conditions:

-

## Plan-Defined Reruns

- Allowed repetitions/retries:
- Seeds/order permutations:
- Nondeterminism investigation rules:

## Completion Criteria

The TB plan is complete when:

- every planned item has a recorded result or explicit blocker,
- raw evidence is preserved,
- TB-REVIEW can evaluate every acceptance criterion without reconstructing intent from chat context.

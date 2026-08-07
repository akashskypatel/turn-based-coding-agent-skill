# Unit Test Plan

## Unit / behavior boundary

- Production surface:
- Public entry point:
- Contract/invariant source:
- Why this belongs at unit scope:

## Dependencies

| Dependency | Real / fake / stub / mock | Why |
|---|---|---|
| | | |

## Scenarios

| Scenario | Arrange | Act | Expected observable behavior | Why this case matters |
|---|---|---|---|---|
| Normal behavior | | | | |
| Boundary | | | | |
| Invalid/error | | | | |
| Regression, if applicable | | | | |

## Test values

- Non-default values used to expose ignored inputs:
- Distinct values used to expose swaps/reuse:
- Boundary/special values:
- Values intentionally omitted as redundant equivalence cases:

## Assertions

- Semantic assertions:
- Required side effects/interactions:
- Explicit non-effects:
- Floating-point tolerance and justification, if applicable:

## Isolation

- Clock/time control:
- Randomness/seed control:
- Shared/global state:
- Filesystem/database/network:
- Parallel/order independence:

## Counterfactual check

The tests should fail if production code:

- returns a default value:
- ignores an input:
- swaps/reuses inputs:
- skips the required state transition:
- returns success without performing the behavior:

## Validation

- Pre-fix failure evidence, if regression test:
- Focused test command:
- Related regression command:
- Integration coverage required separately:

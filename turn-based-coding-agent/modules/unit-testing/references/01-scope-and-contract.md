# Scope and Contract

## Start from behavior

Before choosing test cases, establish what the unit promises to callers or neighboring components.

Use the strongest available authority in this order when applicable:

1. Public API or protocol contract.
2. Product/design requirements and documented invariants.
3. Accepted behavior demonstrated by stable compatibility tests.
4. Existing implementation only as evidence, never as the sole definition of correctness.

Write the contract in observable terms: returned value, externally visible state change, emitted error, persisted command, or required interaction at a system boundary.

## Choose the unit boundary

A unit is the smallest useful behavior boundary for the test, not necessarily one method or one class.

A test is a good unit test when it can run quickly and deterministically while failures localize to a small production surface. A small group of inexpensive in-process objects may be tested together when separating them would require brittle mocks and would not improve diagnosis.

Move the check to integration scope when correctness depends on real behavior of infrastructure or multiple production components that cannot be represented faithfully at unit scope, such as a database engine, filesystem semantics, network protocol, renderer, OS API, external service, or serialization compatibility across components.

Do not call a test a unit test merely because a unit-test framework executes it.

## Test public behavior by default

Prefer testing through the same public or package-visible entry point production callers use.

Do not expose private methods only to test them. If important behavior is reachable only through complicated setup, first ask whether the production design has too many responsibilities or hidden dependencies.

Testing an implementation detail is justified only when that detail is itself an explicit requirement, such as a required boundary call, security property, cache-use guarantee, transaction rule, or performance-sensitive algorithmic invariant.

## Define success before implementation

For each scenario record:

- Given: relevant preconditions and inputs.
- When: one production action.
- Then: observable outcome or invariant.
- Why: the contract or defect this protects.

If the expected result cannot be derived independently of the current implementation, the test oracle is not yet trustworthy.

## Unit versus integration decision

Prefer a unit test when all are true:

- The behavior can be exercised without external infrastructure.
- Collaborators can be real, deterministic in-process objects or faithful test doubles.
- The result can be checked automatically.
- A failure localizes to a small code surface.

Prefer an integration test when the risk is specifically in the interaction between production components or with real infrastructure.

Do not replace necessary integration coverage with elaborate mocks that only prove the mocks were configured as expected.

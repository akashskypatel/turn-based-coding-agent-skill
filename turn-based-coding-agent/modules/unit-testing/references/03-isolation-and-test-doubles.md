# Isolation and Test Doubles

## Isolation goals

Unit tests should be fast, repeatable, order-independent, and safe to run in parallel unless the framework or target makes parallelism impossible.

Eliminate accidental dependence on:

- External network services.
- Production databases.
- Ambient filesystem contents.
- Wall-clock time and time zones.
- Uncontrolled randomness.
- Environment variables or machine-specific configuration.
- Process-wide mutable singletons.
- State left behind by another test.
- Execution order.

If one of these is the behavior being tested, the check may belong at integration scope instead of being simulated as a unit test.

## Make dependencies explicit

Prefer production designs where collaborators enter through constructors, parameters, interfaces, handles, or explicit context objects. Hidden dependency lookup makes both production reasoning and testing harder.

Do not introduce an abstraction solely to satisfy a mocking framework when a simpler deterministic collaborator can be used directly.

## Choose the highest-fidelity practical collaborator

Use this preference order as a default, not an absolute law:

1. **Real implementation** when it is local, fast, deterministic, and easy to construct.
2. **Fake** when the real dependency is slow, nondeterministic, unavailable, or infrastructure-bound but a lightweight behavioral implementation can preserve useful semantics.
3. **Stub** when the unit only needs controlled responses to reach a state or branch.
4. **Spy/mock** when the interaction itself is part of the observable contract and cannot be verified more directly.

The objective is not maximum isolation at any cost. The objective is a small, reliable test with enough production fidelity to provide confidence.

## Avoid mock-driven implementation coupling

Do not assert internal call sequences, exact call counts, or intermediate arguments unless those interactions are contractually meaningful.

Mock-heavy tests become brittle when a harmless refactor changes internal collaboration without changing behavior. Prefer asserting resulting state/output through the public API.

Warning signs of over-mocking:

- The mock setup is longer than the behavior under test.
- Understanding the test requires mentally simulating the production implementation.
- Several internal collaborators must be mocked for a simple public behavior.
- Harmless refactors repeatedly break tests.
- Assertions mostly verify calls instead of outcomes.

## Fakes require fidelity

A fake can create false confidence if its semantics drift from the real implementation.

For important fakes:

- Keep the interface shared with production.
- Reproduce contractually relevant success and failure behavior.
- Add conformance/contract tests that can run against both fake and real implementation where practical.
- Keep the fake at the lowest useful boundary so more real production code executes in tests.

## Control nondeterminism

Inject or otherwise control:

- clocks,
- random-number generators/seeds,
- ID generation,
- schedulers/executors when sequencing matters,
- locale/time-zone context,
- process/environment configuration.

Prefer deterministic advancement or explicit inputs over sleeping, polling, or retrying.

## Shared fixtures

Use shared setup only for immutable or mechanically repeated construction that does not hide the scenario.

Each test should start from a known state. Cleanup is a fallback, not a substitute for constructing isolated state.

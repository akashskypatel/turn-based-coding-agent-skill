# Unit Testing Module

Internal module of `turn-based-coding-agent` for framework-agnostic unit-test design, repair, diagnosis, and review.

It is bundled with the parent skill and must not be installed or invoked as a separate skill.

## Responsibilities

This module defines **how** unit tests should be designed and assessed:

- observable behavior and contract boundaries;
- focused scenario selection;
- boundary, error, invariant, state-transition, and regression coverage;
- deterministic isolation;
- real/fake/stub/mock collaborator choice;
- robust test values;
- narrow semantic assertions and actionable diagnostics;
- counterfactual, coverage, and optional mutation-testing review.

The parent skill defines **when** test code may change or execute.

## Layout

```text
modules/unit-testing/
├── MODULE.md
├── README.md
├── references/
│   ├── 01-scope-and-contract.md
│   ├── 02-case-design.md
│   ├── 03-isolation-and-test-doubles.md
│   ├── 04-assertions-and-diagnostics.md
│   ├── 05-review-regression-and-coverage.md
│   └── 06-research-basis.md
└── templates/
    ├── UNIT_TEST_PLAN.md
    └── UNIT_TEST_REVIEW.md
```

## Turn integration

- **Code + Build:** load the module before adding, repairing, or materially changing unit tests. Do not execute them.
- **Test + Benchmark:** use the module to diagnose unit-test fixture, expectation, assertion, scope, isolation, and nondeterminism issues. Do not edit test logic.
- **Optional Review:** use the module read-only to critique proposed test changes and amend the next Code + Build plan.

The parent `references/07-testing-integrity.md` remains authoritative against synthetic validation and fixture-specific production fixes.

## Research basis

See `references/06-research-basis.md` for the Microsoft Learn and Google Testing Blog guidance synthesized by this module.

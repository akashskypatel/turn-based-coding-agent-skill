# Unit Testing Skill

A framework-agnostic coding-agent skill for designing, reviewing, and repairing unit tests that are behavioral, focused, deterministic, maintainable, and diagnostically useful.

## Features

- Contract-first test design instead of implementation-driven assertions.
- Clear unit-versus-integration boundary guidance.
- Arrange/Act/Assert structure with one coherent behavior per test.
- Boundary, invalid-input, state-transition, invariant, and regression case design.
- Robust test-value selection that avoids accidental passes from default or symmetric values.
- Isolation guidance for clocks, randomness, global state, infrastructure, and test ordering.
- Fidelity-aware use of real collaborators, fakes, stubs, spies, and mocks.
- Narrow semantic assertions and actionable failure diagnostics.
- Counterfactual and optional mutation-testing checks for weak tests.
- Coverage treated as a gap/risk signal rather than proof of correctness.
- Structured templates for unit-test plans and reviews.
- Direct integration with the `turn-based-coding-agent` skill without weakening its turn boundaries.

## Layout

```text
unit-testing/
├── SKILL.md
├── README.md
├── VERSION
├── manifest.txt
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

## Installation

Clone the repository and copy the complete `unit-testing` directory into the skills directory recognized by your coding-agent host:

```bash
git clone https://github.com/akashskypatel/turn-based-coding-agent-skill.git
cp -a turn-based-coding-agent-skill/unit-testing /path/to/skills/
```

On PowerShell:

```powershell
git clone https://github.com/akashskypatel/turn-based-coding-agent-skill.git
Copy-Item -Recurse turn-based-coding-agent-skill\unit-testing C:\path\to\skills\
```

The installed entry point should be:

```text
/path/to/skills/unit-testing/SKILL.md
```

## Use with Turn-Based Coding Agent

Install both skills. `turn-based-coding-agent` delegates unit-test design and review to this skill when unit-test work is in scope:

- create or edit unit tests during **Code + Build** only;
- execute unit tests during **Test + Benchmark** only;
- critique test quality during the optional independent **Review** turn without editing code.

The unit-testing skill does not override those turn boundaries.

## Research basis

The guidance is based primarily on Microsoft Learn unit-testing best practices and Google Testing Blog guidance on behavior-focused testing, focused scenarios, actionable failures, test doubles, test-value selection, coverage, and mutation testing.

See `references/06-research-basis.md` for source links and interpretation notes.

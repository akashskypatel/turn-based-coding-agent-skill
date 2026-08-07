# Turn-Based Coding Agent Skill

A modular coding-agent skill for disciplined, recoverable software implementation with strict separation between implementation, runtime validation, and optional independent review.

```text
Code + Build -> Test + Benchmark -> [Optional Independent Review] -> Code + Build
```

The skill is intended for multi-turn feature development, remediation, refactoring, and production-hardening where correctness, exact evidence provenance, clean handoffs, and recoverable Git state matter more than making one fixture pass.

## Features

- Strict Code + Build, Test + Benchmark, and optional Review separation.
- Exact pushed-commit provenance for builds and runtime evidence.
- Recoverable phase branches, TODO tracking, and concise live handoffs.
- Independent review agents may revise the next Code + Build plan without modifying source.
- Testing-integrity rules distinguish production defects from invalid fixtures, incorrect expectations, infrastructure failures, regressions, and nondeterminism.
- Integrated research-backed unit-testing module for test design and review.
- Connector-first remote operation through `@GitHub` with bounded GitHub Actions execution when required.
- Progressive disclosure through focused references, modules, and reusable templates.

## Integrated Unit-Testing Module

Unit testing is bundled inside the skill at `turn-based-coding-agent/modules/unit-testing/` and is loaded only when unit-test design, repair, diagnosis, or review is in scope.

It provides:

- Contract-first, observable-behavior test design.
- Unit-versus-integration boundary guidance.
- Focused Arrange/Act/Assert scenarios.
- Boundary, invalid-input, invariant, state-transition, and regression case design.
- Robust values that expose ignored, swapped, or defaulted inputs.
- Isolation of time, randomness, global state, infrastructure, and test ordering.
- Fidelity-aware guidance for real collaborators, fakes, stubs, spies, and mocks.
- Narrow semantic assertions and actionable failure diagnostics.
- Counterfactual and optional mutation-testing review of test effectiveness.
- Coverage treated as a risk/gap signal rather than proof of correctness.

The module is subordinate to the turn cadence: unit-test source changes happen only during Code + Build; unit-test execution happens only during Test + Benchmark; optional Review may critique test design but may not edit it.

The research basis is documented in `turn-based-coding-agent/modules/unit-testing/references/06-research-basis.md`.

## Repository layout

```text
turn-based-coding-agent-skill/
├── README.md
├── LICENSE
└── turn-based-coding-agent/
    ├── SKILL.md
    ├── modules/
    │   └── unit-testing/
    │       ├── MODULE.md
    │       ├── references/
    │       └── templates/
    ├── references/
    ├── templates/
    └── ...
```

## Installation

Clone the repository:

```bash
git clone https://github.com/akashskypatel/turn-based-coding-agent-skill.git
```

### Bash

```bash
cd turn-based-coding-agent-skill/turn-based-coding-agent
./install.sh /path/to/skills
```

Use `--force` to replace an existing installation.

### PowerShell

```powershell
Set-Location turn-based-coding-agent-skill\turn-based-coding-agent
.\install.ps1 -Destination 'C:\path\to\skills'
```

Use `-Force` to replace an existing installation.

### Manual

Copy the complete `turn-based-coding-agent` directory into the skills directory recognized by the coding-agent host. The unit-testing module is installed automatically because it is part of that directory.

The resulting entry point is:

```text
/path/to/skills/turn-based-coding-agent/SKILL.md
```

## Use

Invoke `turn-based-coding-agent` for the implementation project. The entry skill routes to the integrated unit-testing module automatically when the active turn involves unit-test design, fixture/expectation diagnosis, or independent review of unit-test changes.

The module never overrides the active turn boundary or the skill's testing-integrity rules.

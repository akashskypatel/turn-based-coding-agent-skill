# Turn-Based Coding Agent Skills

A small collection of coding-agent skills for disciplined implementation and validation workflows.

This repository contains two complementary skills:

- **`turn-based-coding-agent`** — production implementation workflow with strict separation between code/build, runtime validation, and optional independent review.
- **`unit-testing`** — framework-agnostic guidance for designing, reviewing, and repairing focused, deterministic, behavior-oriented unit tests.

## Turn-Based Coding Agent

```text
Code + Build -> Test + Benchmark -> [Optional Independent Review] -> Code + Build
```

The workflow is intended for multi-turn feature development, remediation, refactoring, and production-hardening where correctness, exact evidence provenance, clean handoffs, and recoverable Git state matter.

Key features:

- Strict Code + Build, Test + Benchmark, and optional Review separation.
- Exact pushed-commit provenance for builds and runtime evidence.
- Recoverable phase branches, TODO tracking, and concise live handoffs.
- Independent review agents may revise the next Code + Build plan without modifying source.
- Testing-integrity rules distinguish production defects from invalid fixtures, incorrect expectations, infrastructure failures, regressions, and nondeterminism.
- Connector-first remote operation through `@GitHub` with bounded GitHub Actions execution when required.
- Progressive disclosure through focused references and reusable templates.

## Unit Testing

The companion `unit-testing` skill captures research-backed unit-test design rules without bloating the turn-based workflow.

Key features:

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

The guidance is based primarily on Microsoft Learn unit-testing best practices and Google Testing Blog material on behavior-focused tests, focused scenarios, actionable failures, test doubles, robust values, coverage, and mutation testing. See `unit-testing/references/06-research-basis.md`.

## Integration

When both skills are installed:

- `turn-based-coding-agent` determines **when** test code may be changed or executed.
- `unit-testing` determines **how** unit tests should be designed and reviewed.
- Unit-test source changes happen during **Code + Build** only.
- Unit-test execution happens during **Test + Benchmark** only.
- The optional independent **Review** turn may critique test design and revise the next action plan without editing test code.

The unit-testing skill never overrides the active turn boundary or the turn-based skill's testing-integrity rules.

## Repository layout

```text
turn-based-coding-agent-skill/
├── README.md
├── LICENSE
├── turn-based-coding-agent/
│   ├── SKILL.md
│   ├── references/
│   ├── templates/
│   └── ...
└── unit-testing/
    ├── SKILL.md
    ├── references/
    ├── templates/
    └── ...
```

## Installation

Clone the repository:

```bash
git clone https://github.com/akashskypatel/turn-based-coding-agent-skill.git
```

### Install Turn-Based Coding Agent

Bash:

```bash
cd turn-based-coding-agent-skill/turn-based-coding-agent
./install.sh /path/to/skills
```

PowerShell:

```powershell
Set-Location turn-based-coding-agent-skill\turn-based-coding-agent
.\install.ps1 -Destination 'C:\path\to\skills'
```

Or manually copy the complete `turn-based-coding-agent` directory into the host's skills directory.

### Install Unit Testing

Copy the complete `unit-testing` directory into the host's skills directory.

Bash example:

```bash
cp -a turn-based-coding-agent-skill/unit-testing /path/to/skills/
```

PowerShell example:

```powershell
Copy-Item -Recurse turn-based-coding-agent-skill\unit-testing C:\path\to\skills\
```

The resulting skill entry points should be:

```text
/path/to/skills/turn-based-coding-agent/SKILL.md
/path/to/skills/unit-testing/SKILL.md
```

## Use

For a multi-turn implementation project, invoke `turn-based-coding-agent` and provide the repository, authoritative project/design documents, build commands, test commands, benchmark commands, and branch policy when known.

Invoke `unit-testing` directly when the task is specifically to design, review, repair, or assess unit tests outside the turn-based workflow.

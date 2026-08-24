# Turn-Based Coding Agent Skill

A modular coding-agent skill for disciplined, recoverable software implementation with strict separation between implementation, runtime validation, and optional independent review.

```text
Code + Build -> Test + Benchmark -> [Optional Independent Review] -> Code + Build
```

For finer workflow control, Code + Build and Test + Benchmark can optionally expose resumable subturns:

```text
CB-DRAFT -> CB-APPLY -> CB-COMPILE -> CB-CLOSEOUT
    ^                         |
    |------ compile FAIL -----|

TB-EXEC -> TB-REVIEW -> TB-PLAN -> [Optional Independent Review]
```

Canonical turns remain valid; granular mode changes control and resumability, not safety or acceptance criteria.

## Features

- Strict Code + Build, Test + Benchmark, and optional Review separation.
- Optional granular CB/TB subturns for patch review, application, compile gates, closeout, execution, evidence review, and planning.
- Compile-fix loop that returns `CB-COMPILE` failures to `CB-DRAFT` rather than editing during the compile stage.
- Mandatory Test + Benchmark plan drafted before every Code + Build closeout.
- Exact pushed-commit provenance for builds and runtime evidence.
- Recoverable phase branches, TODO tracking, and concise live handoffs that record exact canonical turn/subturn state.
- Independent review agents may revise the next Code + Build plan without modifying source.
- Integrated engineering-guidelines module emphasizing surfaced assumptions, simplicity, surgical diffs, and verifiable goals.
- Testing-integrity rules that distinguish production defects from invalid fixtures, incorrect expectations, infrastructure failures, regressions, and nondeterminism.
- Integrated research-backed unit-testing module for test design and review.
- Connector-first remote operation through `@GitHub` with bounded GitHub Actions execution when required.
- Progressive disclosure through focused references, modules, and reusable templates.

## Granular Turn Control

### Code + Build

- **CB-DRAFT** — inspect evidence and draft the intended source changes as a plain patch against an exact base commit. Do not mutate source.
- **CB-APPLY** — apply the reviewed patch, verify the resulting diff, commit, and push ordinary source files. Do not compile or test.
- **CB-COMPILE** — compile the exact pushed commit without changing code. On failure, return to CB-DRAFT.
- **CB-CLOSEOUT** — write change documentation and the mandatory Test + Benchmark plan. No source/build/runtime changes.

### Test + Benchmark

- **TB-EXEC** — execute the authored test/benchmark plan and preserve raw evidence.
- **TB-REVIEW** — review evidence against acceptance criteria and classify findings without changing code or running new unplanned validation.
- **TB-PLAN** — produce corrective measures and the proposed next Code + Build plan; optionally request independent Review.

See `turn-based-coding-agent/references/11-granular-subturns.md`.

## Mandatory Test Planning

Every Code + Build turn must produce a concrete Test + Benchmark plan tied to the exact successfully compiled evidence commit/artifact. The plan specifies ordered validation commands, fixtures/inputs, acceptance criteria, benchmark baselines, evidence retention, and stop/rerun rules.

Template: `turn-based-coding-agent/templates/TEST_PLAN.md`.

## Integrated Engineering Guidelines

`turn-based-coding-agent/modules/engineering-guidelines/` incorporates and adapts guidance from:

- `multica-ai/andrej-karpathy-skills/skills/karpathy-guidelines/SKILL.md`
- `multica-ai/andrej-karpathy-skills/EXAMPLES.md`

The module makes four practices explicit throughout implementation and review:

- surface assumptions before coding;
- prefer the simplest sufficient implementation;
- keep changes surgical and style-consistent;
- define observable goals and verification before implementation.

The external examples are distilled into project-agnostic anti-pattern guidance rather than copied verbatim. Source attribution and the turn-workflow adaptation are documented in `modules/engineering-guidelines/references/03-source-attribution.md`.

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

## Repository layout

```text
turn-based-coding-agent-skill/
├── README.md
├── LICENSE
└── turn-based-coding-agent/
    ├── SKILL.md
    ├── modules/
    │   ├── engineering-guidelines/
    │   │   ├── MODULE.md
    │   │   └── references/
    │   └── unit-testing/
    │       ├── MODULE.md
    │       ├── references/
    │       └── templates/
    ├── references/
    │   └── 11-granular-subturns.md
    ├── templates/
    │   ├── TEST_PLAN.md
    │   └── SUBTURN_REPORT.md
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

Copy the complete `turn-based-coding-agent` directory into the skills directory recognized by the coding-agent host. All internal modules are installed automatically.

The resulting entry point is:

```text
/path/to/skills/turn-based-coding-agent/SKILL.md
```

## Use

Invoke `turn-based-coding-agent` for the implementation project. Configure `canonical`, `granular`, or `per_turn` execution in the project configuration. The entry skill routes automatically to the engineering-guidelines and unit-testing modules when required.

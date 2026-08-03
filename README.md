# Turn-Based Coding Agent

A modular coding-agent skill for production implementation work that keeps code changes, runtime validation, and independent review in separate, recoverable turns.

```text
Code + Build -> Test + Benchmark -> [Optional Independent Review] -> Code + Build
```

The skill is intended for multi-turn feature development, remediation, refactoring, and production-hardening projects where correctness, traceable evidence, clean handoffs, and reliable Git recovery matter more than making a single test fixture pass.

## Purpose

Long-running coding-agent sessions often lose rigor when implementation, compilation, testing, diagnosis, and planning happen in one continuous loop. This skill imposes a clear cadence:

1. **Code + Build** changes source and compiles the exact pushed commit, but never runs tests or benchmarks.
2. **Test + Benchmark** validates that built commit, records evidence, classifies failures, and proposes the next implementation plan without changing code.
3. **Independent Review** is optional. A fresh review agent may approve or revise the proposed next-turn plan without modifying implementation or validation logic.

When the Review turn is skipped, the Test + Benchmark plan remains authoritative.

## Features

- **Strict turn separation** prevents implementation and validation evidence from being mixed.
- **Optional independent review** adds a fresh planning checkpoint without blocking normal progress.
- **Generalized implementation rules** prohibit fixture-specific, benchmark-specific, or synthetic success paths.
- **Exact-commit provenance** ties builds, tests, benchmarks, and reports to pushed Git commits.
- **Recoverable phase branches** keep work divided into achievable implementation phases.
- **Live handoff documentation** lets a new coding agent resume the next turn without prior chat context.
- **Concise lessons learned** preserve important failed attempts, errors, and procedural mistakes without duplicating logs.
- **Testing-integrity rules** distinguish production defects, invalid test scenarios, incorrect expectations, infrastructure failures, regressions, and nondeterminism.
- **Progressive disclosure** keeps the entry skill small and loads only the reference modules needed for the active turn.
- **Reusable templates** provide project configuration, TODO tracking, handoff state, and turn reports.
- **Local or CI builds** are supported as long as validation uses artifacts from the exact recorded commit.

## Live handoff model

Each project using the skill maintains a concise, version-controlled handoff document based on `templates/HANDOFF.md`.

The handoff records only what a context-free successor agent needs to resume expertly:

- the next turn and active phase;
- the exact branch and relevant commit identities;
- explicit next steps or links to the authoritative plan containing them;
- procedural details not already covered by project documentation or this skill;
- key lessons from failed attempts, errors, and mistakes;
- recovery instructions and evidence locations.

The handoff must be linked from project agent entry points such as `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, or `.agents/README.md`. It references existing plans, reports, and logs instead of copying them.

## Package layout

```text
turn-based-coding-agent/
├── SKILL.md
├── README.md
├── VERSION
├── install.sh
├── install.ps1
├── manifest.txt
├── examples/
│   └── PROJECT_CONFIG.example.md
├── references/
│   ├── 01-project-configuration.md
│   ├── 02-initialization.md
│   ├── 03-repository-workflow.md
│   ├── 04-code-build-turn.md
│   ├── 05-test-benchmark-turn.md
│   ├── 06-optional-review-turn.md
│   ├── 07-testing-integrity.md
│   ├── 08-status-recovery-and-completion.md
│   └── 09-live-handoff.md
└── templates/
    ├── PROJECT_CONFIG.md
    ├── TODO.md
    ├── HANDOFF.md
    ├── CODE_BUILD_REPORT.md
    ├── TEST_BENCHMARK_REPORT.md
    └── REVIEW_REPORT.md
```

`SKILL.md` is the compact entry point and router. The detailed operating rules live in `references/`, while `templates/` contains project-local artifacts that the agent creates or adapts.

## Installation

### Requirements

- A coding-agent host that supports directory-based skills with a `SKILL.md` entry point and relative file references.
- Git, when installing from source.
- Bash or PowerShell only when using the included installer scripts; manual installation requires neither.

The installation destination is explicit because skill directories differ between coding-agent hosts and workspace configurations.

### Install from a Git clone with Bash

```bash
git clone https://github.com/<owner>/turn-based-coding-agent.git
cd turn-based-coding-agent
./install.sh /path/to/skills
```

Replace an existing installation:

```bash
./install.sh --force /path/to/skills
```

### Install from a Git clone with PowerShell

```powershell
git clone https://github.com/<owner>/turn-based-coding-agent.git
Set-Location turn-based-coding-agent
.\install.ps1 -Destination 'C:\path\to\skills'
```

Replace an existing installation:

```powershell
.\install.ps1 -Destination 'C:\path\to\skills' -Force
```

Replace `<owner>` with the repository owner before publishing this README.

### Install from a release archive

1. Download and extract `turn-based-coding-agent.zip` or `turn-based-coding-agent.tar.gz`.
2. Copy the complete `turn-based-coding-agent` directory into the skills directory used by your coding-agent host.
3. Keep the directory name and internal layout intact.

The resulting structure should include:

```text
/path/to/skills/turn-based-coding-agent/SKILL.md
```

### Manual installation from the repository

Copy this repository directory directly into the host's skills directory:

```bash
cp -a turn-based-coding-agent /path/to/skills/
```

On PowerShell:

```powershell
Copy-Item -Recurse -Force . 'C:\path\to\skills\turn-based-coding-agent'
```

## Getting started

1. Install the skill into the skills directory recognized by your coding-agent host.
2. Invoke or select `turn-based-coding-agent` for a multi-turn implementation project.
3. Provide the repository, base branch, build commands, test commands, benchmark commands, and authoritative project documents when known.
4. Let the initialization workflow create or normalize the project TODO and live handoff.
5. Begin with a **Code + Build** turn.

Project-specific configuration can be based on:

```text
templates/PROJECT_CONFIG.md
```

A completed example is available at:

```text
examples/PROJECT_CONFIG.example.md
```

## Turn summary

### Code + Build

The agent may edit production code, tests, benchmarks, build configuration, documentation, and tracking files. It compiles required targets and continues until the build succeeds or a genuine blocker is documented. It must not execute tests or benchmarks.

### Test + Benchmark

The agent validates artifacts from the exact built commit, records results, classifies failures, and prepares the next Code + Build plan. It must not change production, test, benchmark, or build logic.

### Optional Independent Review

A separate agent or fresh context reviews the evidence and proposed next-turn plan. It may approve, amend, reorder, narrow, expand, or replace that plan. It must not modify implementation or validation logic.

## Core integrity rules

- Never special-case a named fixture, input artifact, dataset, platform, or benchmark to manufacture success.
- Never weaken, bypass, disable, or silently skip meaningful validation.
- Correct structurally invalid test inputs when they do not exercise the behavior the test claims to validate.
- Build and validate exact pushed commits, and record their identities with the evidence.
- Keep the root TODO and live handoff current at the end of every turn.
- Merge phase branches only after their acceptance criteria are supported by build and validation evidence.

## Version

The current package version is recorded in [`VERSION`](turn-based-coding-agent/VERSION).

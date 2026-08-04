# Turn-Based Coding Agent

A modular coding-agent skill for production implementation work that keeps code changes, runtime validation, and independent review in separate, recoverable turns.

```text
Code + Build -> Test + Benchmark -> [Optional Independent Review] -> Code + Build
```

The skill is intended for multi-turn feature development, remediation, refactoring, and production-hardening projects where correctness, traceable evidence, clean handoffs, and reliable Git recovery matter more than making a single test fixture pass.

## Features

- Strict Code + Build, Test + Benchmark, and optional Review separation.
- Exact pushed-commit provenance for builds and runtime evidence.
- Recoverable phase branches, live handoffs, and concise lessons learned.
- Testing-integrity rules that distinguish product, fixture, expectation, infrastructure, performance, and nondeterminism failures.
- Connector-first remote repository operation through `@GitHub`.
- GitHub Actions as a bounded execution plane when direct repository execution is unavailable.
- Mandatory detailed workflow logging on success and failure with a separate unconditional log artifact.
- Atomic Git-data workflows for coherent multi-file remote commits.
- Idempotent large-patch application with already-applied detection and exact output-blob verification.
- Workflow-run, job-log, artifact, retry, trigger, and stale-trigger-PR procedures.
- Progressive disclosure through focused reference modules and reusable templates.

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
│   ├── 09-live-handoff.md
│   ├── 10-github-connector-workflows.md
│   └── github-connector-workflows/
│       ├── COMMON_TASKS.md
│       ├── PITFALLS.md
│       └── TOOL_MAP.md
├── scripts/
│   └── split_patch.py
└── templates/
    ├── PROJECT_CONFIG.md
    ├── TODO.md
    ├── HANDOFF.md
    ├── CODE_BUILD_REPORT.md
    ├── TEST_BENCHMARK_REPORT.md
    ├── REVIEW_REPORT.md
    └── github-actions/
        ├── logged-remote-task.yml
        ├── apply-unified-patch.yml
        └── PR_BODY.md
```

## Installation

### Bash

```bash
git clone https://github.com/akashskypatel/turn-based-coding-agent-skill.git
cd turn-based-coding-agent-skill/turn-based-coding-agent
./install.sh /path/to/skills
```

Replace an existing installation with `--force`.

### PowerShell

```powershell
git clone https://github.com/akashskypatel/turn-based-coding-agent-skill.git
Set-Location turn-based-coding-agent-skill\turn-based-coding-agent
.\install.ps1 -Destination 'C:\path\to\skills'
```

Use `-Force` to replace an existing installation.

### Manual

Copy the complete `turn-based-coding-agent` directory into the skill directory recognized by the coding-agent host. The resulting installation must contain:

```text
/path/to/skills/turn-based-coding-agent/SKILL.md
```

## Remote GitHub operation

When a target repository is accessible through `@GitHub` but not through a trusted local checkout:

1. Resolve repository, branch, commit, PR, and file authority with the connector.
2. Use direct connector actions for reads and repository mutations.
3. Use GitHub Actions only for bounded computation or operations the connector cannot perform directly.
4. Preserve the active turn boundary inside every workflow.
5. Upload detailed workflow logs under `if: always()` separately from valid result artifacts.
6. Use downloaded artifacts and exact source identities as validation authority.

See `turn-based-coding-agent/references/10-github-connector-workflows.md`.

## Integrity rules

- Never special-case a named fixture, input, platform, or benchmark to manufacture success.
- Never weaken or silently bypass meaningful validation.
- Correct structurally invalid fixtures when they cannot exercise their claimed contract.
- Build and validate exact pushed commits.
- Keep the root TODO and live handoff current.
- Do not merge a phase until acceptance criteria are supported by build and runtime evidence.

## Version

The package version is recorded in `turn-based-coding-agent/VERSION`.

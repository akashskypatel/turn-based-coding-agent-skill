# Turn-Based Coding Agent Skill

A progressive coding-agent skill for production implementation work with strict separation between:

```text
Code + Build -> Test + Benchmark -> [Optional Independent Review] -> Code + Build
```

The canonical cadence can optionally expose finer resumable subturns:

```text
CB-DRAFT -> CB-APPLY -> CB-COMPILE -> CB-CLOSEOUT
    ^                         |
    |------ compile FAIL -----|

TB-EXEC -> TB-REVIEW -> TB-PLAN
```

The package supports local repositories and remote repositories operated through the connected `@GitHub` app. When direct repository execution is unavailable, the connector is the control plane, GitHub Actions is a bounded execution plane, and Actions artifacts are the evidence plane.

## Turn execution modes

Configure one of:

- `canonical` — each CB/TB canonical turn executes as one turn.
- `granular` — expose each CB/TB subturn as a separate handoff boundary.
- `per_turn` — choose canonical or granular at the start of each canonical turn.

Granularity never relaxes turn restrictions. See `references/11-granular-subturns.md`.

Every Code + Build turn must finish with a Test + Benchmark plan for the exact successfully compiled evidence commit/artifact. Use `templates/TEST_PLAN.md`.

## Integrated engineering-guidelines module

`modules/engineering-guidelines/` distills the Karpathy-guidelines skill and examples into implementation rules compatible with this workflow:

- surface assumptions and materially different interpretations;
- prefer the simplest sufficient design;
- make surgical changes and match existing style;
- avoid speculative abstractions and drive-by cleanup;
- translate tasks into observable success criteria and verification.

The module adapts immediate test-first examples to strict turn separation: test/reproduction source can be authored and compiled during Code + Build, while runtime execution waits for Test + Benchmark.

## Integrated unit-testing module

Research-backed unit-test design and review guidance is bundled at `modules/unit-testing/`.

The module supplies the design standard for observable contracts, focused scenarios, boundaries, robust values, isolation, test doubles, actionable assertions, regression design, and coverage/effectiveness review.

The main skill remains authoritative for turn boundaries and testing integrity.

## Package layout

- `SKILL.md` — compact entry point and task router.
- `modules/engineering-guidelines/` — internal implementation/review discipline module.
- `modules/unit-testing/` — internal unit-test design/review module.
- `references/` — focused operating modules loaded by turn/subturn type.
- `references/11-granular-subturns.md` — optional CB/TB subturn model.
- `references/10-github-connector-workflows.md` — remote GitHub and Actions operating model.
- `references/github-connector-workflows/` — common recipes, pitfalls, and connector tool map.
- `templates/` — project configuration, TODO, handoff, turn reports, TB test plan, and subturn report.
- `templates/github-actions/` — logged remote-task, verified patch, and PR evidence templates.
- `scripts/split_patch.py` — deterministic unified-patch splitter.
- `examples/` — example project configuration.
- `manifest.txt` — package file list.

## Install manually

Extract or copy the complete `turn-based-coding-agent` directory into the skills directory used by your coding-agent host. Keep the directory name and internal layout intact. All modules are included automatically.

## Install with Bash

```bash
./install.sh /path/to/skills
```

Replace an existing installation:

```bash
./install.sh --force /path/to/skills
```

## Install with PowerShell

```powershell
.\install.ps1 -Destination 'C:\path\to\skills'
```

Replace an existing installation:

```powershell
.\install.ps1 -Destination 'C:\path\to\skills' -Force
```

## Use

Provide project-specific values using `templates/PROJECT_CONFIG.md`. On first use, the agent creates a concise project-local handoff from `templates/HANDOFF.md`, links it from all agent entry-point documents, and reads the initialization modules.

For a repository reachable only through `@GitHub`, configure the connector and workflow-policy fields, then load `references/10-github-connector-workflows.md`. Every remote workflow must retain detailed output on success and failure and upload a separate diagnostic log artifact under `if: always()`.

The independent Review turn is optional. When skipped, TB-PLAN/the Test + Benchmark plan becomes authoritative. When used, the Review report supersedes it when amendments are made.

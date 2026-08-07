# Turn-Based Coding Agent Skill

A progressive coding-agent skill for production implementation work with strict separation between:

```text
Code + Build -> Test + Benchmark -> [Optional Independent Review] -> Code + Build
```

The package supports both local repositories and remote repositories operated through the connected `@GitHub` app. When direct repository execution is unavailable, the connector is the control plane, GitHub Actions is a bounded execution plane, and Actions artifacts are the evidence plane.

## Companion unit-testing skill

This repository also contains the standalone `unit-testing` skill for contract-first unit-test design, focused case selection, dependency isolation, test-double choice, assertion quality, regression design, and test review.

When both are installed:

- this skill controls **when** tests may change or run;
- `unit-testing` controls **how** unit tests are designed and reviewed;
- unit-test edits remain limited to Code + Build;
- unit-test execution remains limited to Test + Benchmark;
- optional Review may critique test design without editing test code.

## Package layout

- `SKILL.md` - compact entry point and task router.
- `references/` - focused operating modules loaded by turn type.
- `references/10-github-connector-workflows.md` - remote GitHub and Actions operating model.
- `references/github-connector-workflows/` - common recipes, pitfalls, and connector tool map.
- `templates/` - project configuration, TODO, handoff, and turn reports.
- `templates/github-actions/` - logged remote-task, verified patch, and PR evidence templates.
- `scripts/split_patch.py` - deterministic unified-patch splitter.
- `examples/` - minimal example configuration.
- `manifest.txt` - package file list.

## Install manually

Extract or copy the complete `turn-based-coding-agent` directory into the skills directory used by your coding-agent host. Keep the directory name and internal layout intact.

Install the sibling `unit-testing` directory separately when unit-test design/review guidance is desired.

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

The independent Review turn is optional. When skipped, the Test + Benchmark plan is authoritative. When used, the Review report supersedes it when amendments are made.

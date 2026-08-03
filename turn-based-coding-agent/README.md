# Turn-Based Coding Agent Skill

A progressive, multi-file coding-agent skill for production implementation work with strict separation between:

```text
Code + Build -> Test + Benchmark -> [Optional Independent Review] -> Code + Build
```

## Package layout

- `SKILL.md` - small entry point and task router.
- `references/` - focused operating modules loaded by turn type.
- `templates/` - project configuration, TODO, live handoff, and turn reports.
- `examples/` - minimal example configuration.
- `manifest.txt` - package file list.

## Install manually

Extract or copy the complete `turn-based-coding-agent` directory into the skills directory used by your coding-agent host. Keep the directory name and internal layout intact.

## Install with Bash

```bash
./install.sh /path/to/skills
```

To replace an existing installation:

```bash
./install.sh --force /path/to/skills
```

## Install with PowerShell

```powershell
.\install.ps1 -Destination 'C:\path\to\skills'
```

To replace an existing installation:

```powershell
.\install.ps1 -Destination 'C:\path\to\skills' -Force
```

The destination is intentionally explicit because different coding-agent hosts use different skill directories.

## Use

Provide project-specific values using `templates/PROJECT_CONFIG.md`. On first use, the agent creates a concise project-local handoff from `templates/HANDOFF.md`, links it from all agent entry-point documents, and reads the initialization modules. On subsequent turns, it loads only the module for the designated turn plus shared integrity, recovery, and handoff modules.

The independent Review turn is optional. When skipped, the Test + Benchmark plan is authoritative. When used, the Review report supersedes it when amendments are made.

# Turn-Based Coding Agent Skill

A modular coding-agent skill for disciplined, recoverable software implementation with strict separation between implementation, runtime validation, and optional independent review.

```text
Code + Build -> Test + Benchmark -> [Optional Independent Review] -> Code + Build
```

Optional granular control:

```text
CB-DRAFT -> CB-APPLY -> CB-COMPILE -> CB-CLOSEOUT
    ^                         |
    |------ compile FAIL -----|

TB-EXEC -> TB-REVIEW -> TB-PLAN -> [Optional Review]
```

## Key features

- Strict Code + Build, Test + Benchmark, and optional independent Review boundaries.
- Optional resumable CB/TB subturns for finer workflow control.
- Mandatory Test + Benchmark plan produced by every Code + Build turn.
- Exact pushed-commit provenance for builds and runtime evidence.
- Recoverable phase branches, TODO tracking, and concise live handoffs.
- Integrated unit-testing module for behavior-oriented test design/review.
- Integrated engineering-guidelines module for assumptions, simplicity, surgical diffs, and verifiable goals.
- Connector-first remote operation through `@GitHub` with bounded Actions execution.
- **Strict on-demand context loading** so agents do not preload the whole skill/reference tree.

## Demand-driven context model

`SKILL.md` is intentionally a small dispatcher. Normal resume should follow:

```text
SKILL.md
  -> project HANDOFF.md
  -> exactly one references/turns/<STATE>.md
  -> only triggered capability MODULE.md files
  -> only specifically routed deep references/templates/evidence
```

The handoff precomputes a `Context Load Plan` with `load_next`, conditional modules, and explicit `do_not_preload` guidance.

Context tiers:

```text
Tier 0  SKILL.md dispatcher
Tier 1  current canonical turn/subturn file
Tier 2  conditional capability modules
Tier 3  deep references/templates/research
```

Rules intentionally forbid reading sibling turn files, whole module reference directories, research/provenance, templates, or historical reports "for completeness."

## Integrated modules

### Unit testing

`turn-based-coding-agent/modules/unit-testing/`

Loaded only when unit-test design, repair, diagnosis, or review is materially in scope. It is normally **not** loaded for `CB-COMPILE` or `TB-EXEC`.

### Engineering guidelines

`turn-based-coding-agent/modules/engineering-guidelines/`

Loaded for implementation design/corrective planning and independent review, not routine apply/compile/runtime execution.

### GitHub connector

`turn-based-coding-agent/modules/github-connector/MODULE.md`

Loaded only for `github_connector`/`hybrid` access or GitHub Actions/artifact operations, then routes to the minimum detailed connector reference needed.

## Repository layout

```text
turn-based-coding-agent-skill/
├── README.md
├── LICENSE
└── turn-based-coding-agent/
    ├── SKILL.md
    ├── modules/
    │   ├── engineering-guidelines/
    │   ├── github-connector/
    │   └── unit-testing/
    ├── references/
    │   ├── core/
    │   ├── turns/
    │   └── ...
    ├── templates/
    └── ...
```

Legacy `references/04-*`, `05-*`, `06-*`, and `11-*` paths remain as tiny compatibility routers so existing handoffs can redirect to the focused turn files without loading old monolithic procedures.

## Installation

```bash
git clone https://github.com/akashskypatel/turn-based-coding-agent-skill.git
cd turn-based-coding-agent-skill/turn-based-coding-agent
./install.sh /path/to/skills
```

Use `--force` to replace an existing installation.

PowerShell:

```powershell
Set-Location turn-based-coding-agent-skill\turn-based-coding-agent
.\install.ps1 -Destination 'C:\path\to\skills'
```

Use `-Force` to replace an existing installation.

Manual installation: copy the complete `turn-based-coding-agent` directory into the coding-agent host's skills directory. The only installable skill entry point is `turn-based-coding-agent/SKILL.md`; internal modules are bundled automatically.

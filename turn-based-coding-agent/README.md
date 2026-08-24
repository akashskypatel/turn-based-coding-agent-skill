# Turn-Based Coding Agent Skill

A progressive coding-agent skill for separated implementation, runtime validation, and optional independent review, with optional granular subturn control and strict on-demand context loading.

## Runtime routing

Normal resume is intentionally narrow:

```text
SKILL.md
-> project live handoff
-> one references/turns/<STATE>.md
-> only triggered modules/<capability>/MODULE.md
-> only explicitly routed deep references/templates/evidence
```

Do not preload sibling turns or whole reference directories.

## Canonical and granular workflow

```text
Code + Build -> Test + Benchmark -> [Optional Review] -> Code + Build

CB-DRAFT -> CB-APPLY -> CB-COMPILE -> CB-CLOSEOUT
    ^                         |
    |------ compile FAIL -----|

TB-EXEC -> TB-REVIEW -> TB-PLAN -> [Optional Review]
```

Every Code + Build path must finish with an executable Test + Benchmark plan for the exact successfully compiled evidence commit/artifact.

## Package layout

- `SKILL.md` — Tier-0 dispatcher and load policy.
- `references/turns/` — one focused file per canonical turn/subturn.
- `references/core/` — small shared boundary/evidence/recovery rules loaded only when declared.
- `modules/engineering-guidelines/` — conditional implementation/planning guidance.
- `modules/unit-testing/` — conditional unit-test design/review guidance.
- `modules/github-connector/` — conditional remote GitHub routing.
- `references/github-connector-workflows/PATCH_APPLICATION.md` — 19 KB connector write ceiling and deterministic compressed patch transport.
- `references/github-connector-workflows/WORKFLOW_POLICY.md` — generalized durable Actions policy.
- `references/github-connector-workflows/TEMP_WORKFLOW_LIFECYCLE.md` — exact temporary caller/marker procedure.
- `templates/` — load only when producing the corresponding artifact.
- `references/04-*`, `05-*`, `06-*`, `10-*`, `11-*` — compatibility redirect/router paths only.

Research, attribution, examples, and provenance references are cold storage and are not part of normal execution context.

## GitHub connector safety

For connector-based writes:

- keep every individual content-bearing write at or below **19 KB UTF-8**;
- use direct connector writes when all individual writes fit;
- otherwise use deterministic gzip+Base64 patch payloads;
- split the exact Base64 stream into ordered <=19 KB fragments only when necessary;
- verify encoded and decoded patch SHA-256 values;
- require `git apply --check`, `git diff --check`, and exact intended changed-path verification before commit.

`scripts/split_patch.py` prepares the payload. `templates/github-actions/apply-unified-patch.yml` is the verified application baseline.

## Handoff contract

Project handoffs based on `templates/HANDOFF.md` contain a `Context Load Plan`:

```yaml
load_next:
  - references/turns/<exact-current-state>.md
conditional_modules:
  - trigger: <specific condition>
    path: modules/<capability>/MODULE.md
deep_references:
  - <only if already known necessary>
templates_when_producing:
  - <only when artifact is produced>
do_not_preload:
  - sibling turn/subturn files
  - module reference directories
  - research/provenance/examples
  - uncited historical reports
```

This lets a context-free successor resume without reconstructing state by reading the entire skill or repository history.

## Installation

Manual: copy this complete `turn-based-coding-agent` directory into the host skills directory.

Bash:

```bash
./install.sh /path/to/skills
```

PowerShell:

```powershell
.\install.ps1 -Destination 'C:\path\to\skills'
```

Use `--force` / `-Force` to replace an existing installation.

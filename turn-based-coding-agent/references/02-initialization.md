# One-Time Initialization

Complete this process before entering the turn cadence or when repository state must be reconstructed.

## 1. Read authoritative material

Review:

- Current TODO and milestone state.
- Implementation and remediation plans.
- Architecture records and public contracts.
- Project notes and white papers.
- Previous failure diagnostics.
- Current test and benchmark results.
- CI, build, test, and benchmark definitions.
- Relevant production and validation code.
- `modules/engineering-guidelines/MODULE.md` for implementation discipline.

Do not begin implementation from the high-level task description alone.

## 2. Inspect repository state

Determine:

- Base-branch head.
- Existing active working branches.
- Unmerged or abandoned work.
- Staged, unstaged, and untracked changes.
- Existing patch artifacts explicitly identified as authoritative.
- Current build state.
- Known test failures and benchmark regressions.
- Whether prior work stopped in a recoverable canonical turn or granular subturn.

## 3. Resolve execution policy

Resolve from project configuration or user instruction:

- `canonical` — each Code + Build or Test + Benchmark turn executes as one turn.
- `granular` — expose CB-DRAFT/CB-APPLY/CB-COMPILE/CB-CLOSEOUT and TB-EXEC/TB-REVIEW/TB-PLAN as resumable subturns.
- `per_turn` — choose canonical or granular at the start of each canonical turn and record the choice.

When granular mode is possible, read `references/11-granular-subturns.md` and resolve how temporary CB-DRAFT patches may be stored between agents.

## 4. Clone efficiently

Use a shallow single-branch clone unless history is required:

```bash
git clone --depth 1 --branch <base_branch> --single-branch <repository>
```

Initialize required submodules with shallow history:

```bash
git submodule update --init --recursive --depth 1
```

Fetch additional history only when a concrete investigation requires it.

## 5. Create or normalize the root TODO and live handoff

The root TODO must record:

- Objective and current phase.
- Base and active working branches.
- Current source commit.
- Execution mode.
- Last completed and next canonical turn.
- Last completed and next granular subturn when applicable.
- Active patch/build/test-plan/artifact references.
- Completed, active, blocked, and deferred tasks.
- Known validation failures and regressions.
- Commands or workflows needed next.
- Recovery instructions.

Use `templates/TODO.md`.

Create or normalize the configured handoff file using `templates/HANDOFF.md`. It must let a new coding agent with no chat context identify the exact next canonical turn/subturn, authoritative plan, required patch/build/test-plan evidence, unresolved risks, and resume procedure. Keep it concise by linking to existing documents instead of copying them.

Add a visible link to the handoff from every configured or detected agent entry-point document. Do not duplicate the handoff contents in those entry points.

Read `references/09-live-handoff.md` for the complete contract.

## 6. Produce the initial assessment

Report:

- Implemented behavior.
- Missing or incomplete behavior.
- Known correctness and architecture risks.
- Build, test, and benchmark status.
- Documentation contradictions that affect implementation.
- Material assumptions that remain unresolved.
- Simplest credible phase decomposition.
- The first Code + Build task list.
- Whether the first Code + Build turn will be canonical or granular.

## 7. Create the first phase branch

Use:

```text
<work_branch_prefix>/<phase-name>
```

A phase must be coherent, independently buildable, independently testable, and associated with explicit success criteria.

Begin with Code + Build. If granular mode is active, begin with CB-DRAFT.

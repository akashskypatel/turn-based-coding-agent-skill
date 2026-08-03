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
- Whether prior work stopped in a recoverable state.

## 3. Clone efficiently

Use a shallow single-branch clone unless history is required:

```bash
git clone --depth 1 --branch <base_branch> --single-branch <repository>
```

Initialize required submodules with shallow history:

```bash
git submodule update --init --recursive --depth 1
```

Fetch additional history only when a concrete investigation requires it.

## 4. Create or normalize the root TODO and live handoff

The root TODO must record:

- Objective and current phase.
- Base and active working branches.
- Current source commit.
- Last completed turn and next turn.
- Completed, active, blocked, and deferred tasks.
- Known validation failures and regressions.
- Commands or workflows needed next.
- Recovery instructions.

Use `templates/TODO.md`.

Create or normalize the configured handoff file using `templates/HANDOFF.md`. It must let a new coding agent with no chat context identify the exact next turn, authoritative plan, required evidence, unresolved risks, and resume procedure. Keep it concise by linking to existing documents instead of copying them.

Add a visible link to the handoff from every configured or detected agent entry-point document. Do not duplicate the handoff contents in those entry points.

Read `references/09-live-handoff.md` for the complete contract.

## 5. Produce the initial assessment

Report:

- Implemented behavior.
- Missing or incomplete behavior.
- Known correctness and architecture risks.
- Build, test, and benchmark status.
- Documentation contradictions that affect implementation.
- Recommended achievable phase boundaries.
- The first Code + Build task list.

## 6. Create the first phase branch

Use:

```text
<work_branch_prefix>/<phase-name>
```

A phase must be coherent, independently buildable, independently testable, and associated with explicit success criteria.

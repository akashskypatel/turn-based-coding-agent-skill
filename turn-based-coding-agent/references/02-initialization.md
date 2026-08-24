# One-Time Initialization

**Context class:** `conditional-turn`

Load only for first use, project reset, or recovery when no trustworthy current handoff exists.

Do not eagerly read all repository documentation. Initialization uses staged discovery.

## 1. Establish state from cheap sources

Read first:

- repository root/agent entry instructions;
- existing live handoff, if any;
- root TODO/current milestone pointer;
- project configuration or obvious build/CI entry points.

Inventory other potentially authoritative documents by path/title before opening them.

## 2. Resolve only material unknowns

Open additional design plans, architecture/contracts, failure reports, test results, benchmark results, notes, or CI files only when needed to resolve:

- current phase/objective;
- authoritative next action;
- repository/branch state;
- build/test/benchmark commands;
- correctness/acceptance criteria;
- a contradiction or known failure relevant to the active phase.

Do not read historical notes, old result directories, unrelated architecture, or all workflows for completeness.

## 3. Inspect repository state

Determine base head, active work branch, unmerged work, dirty/untracked changes, authoritative pending patch artifacts, current build evidence, and known relevant validation failures.

Use a shallow clone/submodule fetch unless concrete investigation needs history.

## 4. Normalize project state

Create/update:

- `templates/PROJECT_CONFIG.md` equivalent;
- root TODO;
- live handoff;
- links to the handoff from agent entry points.

The handoff must include a `Context Load Plan` with exactly one primary `load_next` turn/subturn file plus only triggered capability modules.

## 5. Initial assessment

Report implemented/missing behavior, relevant risks, current build/validation status, material documentation conflicts, phase boundary, and the first Code + Build plan.

Use `modules/engineering-guidelines/MODULE.md` only when designing that first implementation plan.

## 6. Start

Create the phase work branch and set the next state:

- canonical mode: `references/turns/CB.md`
- granular mode: `references/turns/CB-DRAFT.md`

Write that exact path into the handoff `load_next` field. Do not preload later turn files.

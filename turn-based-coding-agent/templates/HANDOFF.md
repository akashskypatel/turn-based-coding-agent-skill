# Live Agent Handoff

> First-read runtime state for a coding agent with no prior chat context. Keep concise; link authoritative details instead of duplicating them.

## Resume State

- Repository:
- Base branch:
- Active working branch:
- Active phase:
- Execution mode: canonical | granular | per_turn
- Canonical turn: Code + Build | Test + Benchmark | Optional Review
- Next state/subturn: canonical | CB-DRAFT | CB-APPLY | CB-COMPILE | CB-CLOSEOUT | TB-EXEC | TB-REVIEW | TB-PLAN | REVIEW
- Current source commit:
- Evidence commit:
- Planning commit, when applicable:
- Handoff commit, when later than evidence:
- Last updated:

## Context Load Plan

```yaml
load_next:
  - references/turns/<exact-current-state>.md
conditional_modules:
  # Add only triggers that are actually relevant to the next state.
  # - trigger: unit-test design is in scope
  #   path: modules/unit-testing/MODULE.md
  # - trigger: GitHub connector or Actions work is required
  #   path: modules/github-connector/MODULE.md
deep_references:
  # Only already-known required references; never whole directories.
templates_when_producing:
  # Only artifacts the next state must create.
do_not_preload:
  - sibling turn/subturn files
  - module reference directories
  - research/provenance/examples
  - uncited historical reports
```

## Authoritative Next Steps

- Authoritative plan: `<path or durable reference>#<section>`
- Plan status: authoritative | proposed_pending_review
- If the reference does not contain explicit executable next steps, list them here:
  1.

## Start Here

1. Read this handoff.
2. Load only the `load_next` file above.
3. Load conditional modules only when their trigger is true.
4. Retrieve/verify:
5. Execute/modify:
6. Success evidence:

## Current Blockers or Decisions

-

## Missing Procedure

Only procedure needed for the next state that is not already defined by the loaded turn/module or linked authoritative plan.

-

## Lessons Not to Repeat

Only concise reusable lessons from failed attempts, errors, invalid assumptions, misleading diagnostics, or process mistakes.

-

## Evidence and Detailed History

- Latest turn/subturn report:
- Build evidence:
- Test/benchmark evidence:
- Review report, when used:
- Historical diagnostics needed by the next state:

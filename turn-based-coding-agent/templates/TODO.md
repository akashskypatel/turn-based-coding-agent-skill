# Project Implementation TODO

## Objective

Describe the production behavior in invariant-based terms.

## Current State

- Base branch:
- Active working branch:
- Active phase:
- Execution mode: canonical | granular | per_turn
- Current canonical turn:
- Current subturn/state:
- Current source commit:
- Validated/evidence source commit:
- Planning commit:
- Latest handoff commit:
- Last completed state:
- Next state:
- Next primary context file (`load_next`):
- Optional review: skipped | requested | completed
- Last updated:

## Authoritative Sources

Store references, not copied content.

- Project configuration:
- Live handoff:
- Milestone tracker:
- Implementation plan:
- Architecture/contracts:
- Failure diagnostics:
- Test results:
- Benchmark results:

## Completed

- [ ]

## Active Phase

- [ ]

## Blocked

- [ ]

## Deferred / Out of Scope

- [ ]

## Known Failures

### Failure

- Classification:
- Reproduction/evidence:
- Expected behavior:
- Actual behavior:
- Violated invariant or fixture issue:
- Likely root cause:
- Planned correction:

## Benchmark Status

- Baseline commit/result:
- Current commit/result:
- Regression or improvement:
- Remaining risks:

## Proposed Next Code + Build Plan

Status: draft | proposed_pending_review | authoritative | superseded

1. Task
   - Required change:
   - Scope boundary:
   - Build verification:
   - Future validation:

## Independent Review

- Requested:
- Decision:
- Review report:
- Superseded plan:
- Authoritative replacement plan:

## Recovery

1. Read live handoff.
2. Verify branch/commit state.
3. Load only the handoff `load_next` turn/subturn file.
4. Load conditional modules only when their trigger is true.
5. Retrieve cited evidence/plan only as required by that state.
6. Do not preload sibling turns, module reference directories, templates, or historical reports.

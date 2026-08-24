# Project Configuration

## Repository

- Repository:
- Repository access mode: local | github_connector | hybrid
- GitHub connector name: `@GitHub`
- Base branch:
- Working branch prefix:
- Root TODO file:
- Live handoff file:
- Agent entry-point documents:

## Workflow Control

- Execution mode: canonical | granular | per_turn
- Current canonical turn:
- Current subturn/state:
- Review policy: never | optional | required-when-criteria-match

## Context Loading

- Policy: strict_on_demand
- Handoff must provide exact `load_next`: required
- Preload sibling turn files: no
- Preload module reference directories: no
- Preload templates: no
- Research/provenance/examples during normal execution: no
- Historical reports: only when cited by handoff/current turn
- Project-specific additional always-load files, if truly unavoidable:

## Objective and Scope

- Objective:
- In scope:
- Out of scope:
- Supported platforms/configurations:

## Authoritative Sources

Record paths first. Do not preload their contents.

- Design documents:
- Milestone tracker:
- Remediation/implementation plan:
- Project notes:
- Architecture/contracts:
- Failure diagnostics:
- Existing results:

## Commands and Workflows

### Build
- Core targets:
- Test targets:
- Benchmark targets:
- Remote workflows:
- Compile-only execution boundary:

### Test
- Reproduction:
- Focused:
- Regression:
- Integration:
- Full suite:
- Platform-specific:
- Artifact-only execution boundary:

### Benchmark
- Correctness/quality:
- Performance:
- Memory:
- Determinism:

## Acceptance Criteria

- Correctness invariants:
- Failure behavior:
- Quality thresholds:
- Performance budgets:
- Phase merge criteria:

## GitHub Workflow Policy

- Workflow files may be changed through: connector | authenticated external client
- Workflow self-modification permitted: no
- Detailed success/failure activity logging: required
- Dedicated log artifact under `if: always()`: required
- Result artifacts separated from logs: required
- Artifact naming/retention:
- Trigger/concurrency policy:
- Least-privilege permissions:
- Secret-tracing restrictions:
- Temporary trigger/workflow cleanup policy:

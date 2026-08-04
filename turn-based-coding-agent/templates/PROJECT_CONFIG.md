# Project Configuration

## Repository

- Repository:
- Repository access mode: local | github_connector | hybrid
- GitHub connector name: `@GitHub`
- Base branch:
- Working branch prefix:
- Root TODO file:
- Live handoff file (under agent documentation):
- Agent entry-point documents:

## Objective and Scope

- Objective:
- In scope:
- Out of scope:
- Supported platforms/configurations:

## Authoritative Sources

- Design documents:
- Milestone tracker:
- Remediation plan:
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

## Review Policy

- Policy: optional
- Review required when:
- Review may be skipped when:

## Acceptance Criteria

- Correctness invariants:
- Failure behavior:
- Quality thresholds:
- Performance budgets:
- Phase merge criteria:

## GitHub Workflow Policy

- Workflow files may be changed through: connector | authenticated external client
- Workflow self-modification permitted: no
- Required persistent log location: outside worktree
- Detailed success/failure activity logging: required
- Dedicated log artifact under `if: always()`: required
- `if-no-files-found: error` for logs: required
- Result artifacts separated from logs: required
- Log artifact retention:
- Result artifact retention:
- Artifact naming convention:
- Required run/source/ref metadata:
- Required tool/build/test output:
- Secret-tracing restrictions:
- Trigger policy: workflow_dispatch | exact marker path | other
- Concurrency policy:
- Least-privilege permissions:
- Failure diagnosis source: detailed log artifact
- Temporary trigger/workflow cleanup policy:

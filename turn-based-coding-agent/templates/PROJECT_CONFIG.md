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
- Regression/root-cause tracker, when required:

## Commands

### Build
- Core targets:
- Test targets:
- Benchmark targets:
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

## GitHub Connector Write Policy

- Individual content-write safety ceiling: 19000 UTF-8 bytes
- Direct write allowed only when every individual write is <= ceiling: yes
- Patch payload encoding: gzip+base64
- Patch payload fragment maximum: 19000 bytes
- Encoded-stream SHA-256 verification: required
- Original patch SHA-256 verification: required
- `git apply --check`: required
- `git diff --check` before patch commit: required
- Exact intended changed-path verification: required
- Expected output blob verification, when practical: required
- Checksum mismatch behavior: fail closed

## GitHub Workflow Policy

### Allowed uses

- Long/resource-heavy compile/build:
- Large verified patch application beyond connector direct-write ceiling:
- Source/repository snapshot generation:
- Repository-wide workflow-run inventory when connector discovery is insufficient:
- Workflow YAML schema validation:
- Other connector-unavailable bounded computation:

### Durable reusable workflows

- Reusable compile/build workflow:
- Run-ID observer workflow:
- Recent-runs inventory workflow:
- Workflow-schema validator workflow:

### Temporary state locations

- Temporary workflow callers:
- Trigger markers:
- Workflow observations:
- Patch/payload files:

### Workflow contract

- Workflow files may be changed through: connector | authenticated external client
- Workflow self-modification permitted: no
- Validate workflow YAML before publication/trigger: required
- Detailed success/failure activity logging: required
- Dedicated diagnostic log artifact under `if: always()`: required
- Result artifacts separated from logs: required
- Logs/evidence outside worktree: required
- Trigger/concurrency policy:
- Reusable caller permission union: required
- Least-privilege permissions:
- Secret-tracing restrictions:
- Fine-grained token/PAT allowed for intentional follow-up workflow-triggering pushes:
- Commit-run lookup authoritative for push events: no unless connector behavior is explicitly verified
- Preferred run-ID observation channel:
- Branch-file observation fallback:

### Compile/cache policy

- Reusable compile workflow mandatory when configured: yes
- Temporary callers may override reusable cache lineage/versioning: no
- Compiler cache type:
- Stable compatibility-key owner: reusable compile workflow
- Cache compatibility facts:
- Per-run/source-SHA cache-key suffixes permitted: no
- Cache size cap:

### Test workflow policy

- Required full-suite acceptance run may be repository-timeout-limited solely for elapsed time: no
- Focused diagnostic timeout policy:
- Zero-selected filter classification: orchestration failure

### Cleanup/retention

- Temporary workflow cleanup order: workflow caller -> marker -> payload/observation
- Artifact naming/retention:
- Cleanup policy:
- Final PR summary/comment must occur after repository mutations, when required:

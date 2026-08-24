# Example Project Configuration

## Repository

- Repository: `owner/example-project`
- Repository access mode: `github_connector`
- GitHub connector name: `@GitHub`
- Base branch: `main`
- Working branch prefix: `agent/example-project`
- Root TODO file: `TODO.md`
- Live handoff file: `.agents/HANDOFF.md`
- Agent entry-point documents: `AGENTS.md`, `.agents/README.md`

## Objective and Scope

- Objective: Make the parser recover from malformed records without losing subsequent valid records.
- In scope: parser state, diagnostics, focused fixtures, performance regression coverage.
- Out of scope: public syntax changes and serializer behavior.
- Supported platforms/configurations: Linux and Windows release builds.

## Authoritative Sources

- Design documents: `docs/design/*.md`
- Milestone tracker: `docs/MILESTONE_3.md`
- Remediation plan: `docs/parser-remediation.md`
- Architecture/contracts: `docs/file-format.md`
- Failure diagnostics: `results/failed-recovery.md`
- Existing results: `results/latest/`
- Regression tracker: `.agents/REGRESSIONS.md`

## Turn Execution Policy

- Execution mode: `per_turn`
- Default Code + Build mode: `granular`
- Default Test + Benchmark mode: `granular`
- Temporary CB-DRAFT patch storage: agent artifact
- Temporary patch persistence permitted: yes
- Temporary patch cleanup: remove after CB-APPLY verifies committed source
- Mandatory Test + Benchmark plan: `.agents/parser/TB_PLAN.md`

## Context Loading

- Policy: `strict_on_demand`
- Example successor state: `CB-COMPILE`
- `load_next`: `references/turns/CB-COMPILE.md`
- Conditional modules: `modules/github-connector/MODULE.md` only because compile is remote
- Do not preload engineering/unit-testing modules during compile unless a separate trigger requires them.

## Commands and Workflows

- Build: reusable compile workflow for approved parser/test targets
- Test: packaged `parser_tests` filters followed by the full suite
- Benchmark: packaged recovery corpus benchmark, four independent runs

## GitHub Connector Write Policy

- Individual content-write safety ceiling: `19000` UTF-8 bytes
- Direct connector writes: only when each individual content write is <=19000 bytes
- Patch payload encoding: deterministic `gzip+base64`
- Patch fragment maximum: `19000` bytes
- Patch helper: `turn-based-coding-agent/scripts/split_patch.py`
- Encoded-stream SHA-256: required
- Original patch SHA-256: required
- `git apply --check`: required
- `git diff --check`: required
- Exact intended changed-path verification: required
- Expected final blob verification: required when practical
- Checksum mismatch: fail closed

## GitHub Workflow Policy

### Allowed workflow uses

- Long/resource-heavy build: allowed
- Large patch application beyond direct-write ceiling: allowed
- Snapshot generation: allowed
- Repository-wide run inventory when connector lookup is insufficient: allowed
- Workflow YAML validation: allowed
- Small connector-native file edits through Actions: disallowed

### Durable reusable workflows

- Reusable compile: `.github/workflows/agent-compile-reusable.yml`
- Run observer: `.github/workflows/agent-run-observer-reusable.yml`
- Recent runs inventory: `.github/workflows/agent-recent-workflow-runs-reusable.yml`
- Schema validator: `.github/workflows/agent-workflow-schema-validator-reusable.yml`

Temporary callers must use declared reusable inputs and may not invent cache compatibility/versioning.

### Temporary workflow lifecycle

- Caller directory: `.github/workflows/`
- Marker directory: `.agents/connector-triggers/`
- Observation directory: `.agents/workflow-observation/`
- Payload directory: `.agents/turn-payloads/`
- Trigger sequence: install/verify caller commit -> separate marker commit
- Preferred run-ID channel: PR conversation comment
- Repository-wide run inventory: use when observer is missing; do not infer push-run absence from commit lookup
- Cleanup: delete caller first, then marker, then payload/observation state

### Workflow contract

- Detailed logging: required before checkout and on success/failure
- Dedicated log artifact: separate, `if: always()`, missing logs fail evidence gate
- Workflow self-modification: forbidden
- YAML schema validation before publication: required
- Reusable caller permissions: union of all nested workflow/job requirements
- Narrow exact marker trigger: required for temporary push callers
- Default-token recursive push behavior: do not rely on it for follow-up workflows

### Compile/cache

- All compile work uses reusable compile workflow: yes
- Cache owner: reusable compile workflow
- Cache: compiler-object cache, fixed compatibility key from stable toolchain/config facts
- Run ID/source SHA/timestamp/turn suffixes in cache key: forbidden
- Source SHA remains build evidence authority

### Test execution

- Required full-suite acceptance run: uninterrupted to organic result
- Repository timeout solely to cap full-suite elapsed time: forbidden
- Focused diagnostic timeouts: allowed when justified; timeout is orchestration failure
- Zero-selected test filter: orchestration failure

## Review Policy

- Policy: optional
- Review required when: recovery contract or test fixtures change.
- Review may be skipped when: localized implementation defect has direct reproduction and regression evidence.

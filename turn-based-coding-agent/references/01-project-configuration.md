# Project Configuration

Resolve project-specific values before beginning work. Do not silently invent material requirements.

## Required values

- `repository`: repository URL or owner/name.
- `base_branch`: branch that receives completed phases.
- `work_branch_prefix`: prefix for per-phase branches.
- `todo_file`: authoritative root-level progress tracker.
- `handoff_file`: concise live document under project agent documentation; default `.agents/HANDOFF.md` when no convention exists.
- `agent_entry_points`: agent-facing entry documents that link to the handoff.
- `milestone_tracker`, `project_notes`, `remediation_plan`, `results_directory`, `failure_diagnostics`: paths to project authority/evidence; record paths first and load on demand.
- `build_commands`, `test_commands`, `benchmark_commands`: exact commands or workflows.
- `repository_access_mode`: `local`, `github_connector`, or `hybrid`.
- `review_policy`: `never`, `optional`, or criteria requiring independent review.
- `turn_execution_mode`: `canonical`, `granular`, or `per_turn`.
- `cb_execution_mode`, `tb_execution_mode`: defaults when `per_turn` is used.
- `draft_patch_policy`: temporary CB-DRAFT patch storage/persistence/cleanup.
- `test_plan_policy`: authoritative TB plan path/pattern, required contents, evidence retention, stop/rerun rules.

## GitHub connector/workflow configuration

When GitHub connector/Actions are used, also resolve:

- `connector_write_limit_bytes`: default `19000`; applies to every individual content-bearing connector write.
- `patch_payload_encoding`: default `gzip+base64`.
- `patch_payload_fragment_bytes`: default `19000` maximum.
- `workflow_allowed_uses`: project allowlist; may be stricter than skill defaults.
- `durable_compile_workflow`: reusable compile/build implementation, when provided.
- `durable_run_observer_workflow`: reusable run-ID observer, when provided.
- `durable_recent_runs_workflow`: repository-wide run inventory, when provided.
- `durable_schema_validator_workflow`: workflow YAML validator, when provided.
- `temporary_workflow_directory`, `trigger_marker_directory`, `workflow_observation_directory`, `patch_payload_directory`.
- `workflow_permissions_policy`: least privilege plus reusable caller permission-union rules.
- `workflow_cache_policy`: reusable workflow ownership of cache compatibility/versioning.
- `full_suite_timeout_policy`: required acceptance suite runs organically unless project policy explicitly says otherwise.
- `workflow_cleanup_policy` and `artifact_retention_policy`.
- `regression_tracker`: optional durable regression/root-cause tracker required before TB closeout when configured.

Use `templates/PROJECT_CONFIG.md` as the project-local configuration record and `templates/HANDOFF.md` for live resume state.

When `repository_access_mode` is `github_connector` or `hybrid`, load `modules/github-connector/MODULE.md` and only the focused reference it routes to. Do not preload the GitHub reference directory.

## Execution-mode semantics

- `canonical`: Code + Build and Test + Benchmark each execute as one turn while satisfying granular responsibilities internally.
- `granular`: Code + Build exposes CB-DRAFT, CB-APPLY, CB-COMPILE, CB-CLOSEOUT; Test + Benchmark exposes TB-EXEC, TB-REVIEW, TB-PLAN.
- `per_turn`: choose canonical or granular at each canonical turn start and record it in TODO/handoff.

Granularity changes resumability and permission boundaries, not acceptance standards.

## Resolution order

Resolve missing values from:

1. User explicit instructions.
2. Repository-root/agent policy documentation.
3. Existing TODO, handoff, and milestone records.
4. Architecture/design/contracts.
5. CI/build definitions.
6. Historical evidence cited by current state.

Ask a clarifying question only when a material requirement remains unresolved and proceeding risks implementing the wrong contract.

## GitHub workflow policy minimum

Unless repository policy is stricter, every created or modified workflow must:

- follow `references/github-connector-workflows/WORKFLOW_POLICY.md`;
- initialize persistent logging before checkout/fallible work;
- retain detailed success/failure output and separate unconditional diagnostic logs;
- use narrow triggers/concurrency, least privilege, exact source/hash checks, and external workflow-file mutation only;
- validate workflow YAML before publication/trigger;
- compute reusable caller permissions from the complete called workflow graph;
- preserve the active turn/subturn boundary;
- use workflow-first cleanup for temporary callers/markers;
- avoid repository-imposed cutoff of a required full acceptance suite merely to cap elapsed runtime.

Any connector content write must be <=19 KB UTF-8 unless project policy lowers that limit. Larger source changes use the verified compressed patch strategy in `PATCH_APPLICATION.md`.

## Scope statement

Record production behavior, explicit out-of-scope items, required platforms/configurations, correctness invariants, failure behavior, performance/quality budgets, and phase acceptance criteria.

## Engineering discipline

Load `modules/engineering-guidelines/MODULE.md` before implementation planning. Project configuration must not silently authorize speculative complexity or broad refactoring.

## Generalization check

The objective must describe domain behavior, not one failing fixture. Rewrite fixture-specific goals into invariant-based goals before implementation.

# Project Configuration

Resolve project-specific values before beginning work. Do not silently invent material requirements.

## Required values

- `repository`: repository URL or owner/name.
- `base_branch`: branch that receives completed phases.
- `work_branch_prefix`: prefix for per-phase branches.
- `todo_file`: authoritative root-level progress tracker.
- `handoff_file`: concise live document under the project's agent-documentation directory; default to `.agents/HANDOFF.md` when no convention exists.
- `agent_entry_points`: agent-facing entry documents that must link to the handoff, such as `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, or repository-specific equivalents.
- `milestone_tracker`: current milestone or implementation-state document.
- `project_notes`: implementation notes, design records, white papers, and architecture documents.
- `remediation_plan`: current implementation or remediation plan.
- `results_directory`: existing test and benchmark evidence.
- `failure_diagnostics`: prior failure analyses.
- `build_commands`: commands or workflows for all affected build targets.
- `test_commands`: focused, integration, and full-suite commands.
- `benchmark_commands`: correctness and performance benchmark commands.
- `remote_workflows`: workflow names, trigger paths, permissions, inputs, and artifact names when applicable.
- `repository_access_mode`: `local`, `github_connector`, or `hybrid`.
- `github_workflow_policy`: repository-specific requirements for logging, artifacts, permissions, triggers, execution boundaries, and cleanup.
- `review_policy`: `never`, `optional`, or criteria describing when an independent review should be used.

Use `templates/PROJECT_CONFIG.md` as the project-local configuration record. Use `templates/HANDOFF.md` for the live handoff.

When `repository_access_mode` is `github_connector` or `hybrid`, load `references/10-github-connector-workflows.md` before any remote mutation or workflow execution.

## Resolution order

Resolve missing values from:

1. The user's explicit instructions.
2. Repository-root documentation.
3. Existing TODO and milestone records.
4. Architecture and design documents.
5. CI and build definitions.
6. Historical test and benchmark artifacts.

Ask a clarifying question only when a material requirement remains unresolved and proceeding risks implementing the wrong contract.

## GitHub workflow policy minimum

Unless repository policy is stricter, every created or modified workflow must:

- initialize persistent logging before checkout or other fallible work;
- retain detailed activity and command output on success and failure;
- upload a dedicated log artifact under `if: always()` and `if-no-files-found: error`;
- keep diagnostic logs separate from valid result/build artifacts;
- avoid exposing tokens, secrets, credentials, or authenticated URLs;
- preserve the active turn boundary;
- avoid modifying `.github/workflows/**` from inside a workflow.

Record artifact naming, retention, and failure-debugging requirements explicitly.

## Scope statement

Record:

- The production behavior being implemented.
- What is explicitly out of scope.
- Required platforms and configurations.
- Correctness invariants.
- Failure behavior.
- Performance or quality budgets.
- Phase-level acceptance criteria.

## Generalization check

The configured objective must describe domain behavior, not one failing fixture. Rewrite fixture-specific goals into invariant-based goals before implementation.

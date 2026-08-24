# GitHub Connector and Actions Workflow — Compatibility Router

**Context class:** `compatibility-router`

This path is retained for existing handoffs and documents. New work should load `modules/github-connector/MODULE.md` and then only the focused reference required by the active operation.

Route as follows:

- Connector tool/action selection: `references/github-connector-workflows/TOOL_MAP.md`
- Common direct read/write recipes: `references/github-connector-workflows/COMMON_TASKS.md`
- Any connector content write or patch transport/application: `references/github-connector-workflows/PATCH_APPLICATION.md`
- GitHub Actions policy, reusable workflows, permissions, observability, cache, execution boundaries, and hygiene: `references/github-connector-workflows/WORKFLOW_POLICY.md`
- Temporary caller + marker workflow execution: `references/github-connector-workflows/TEMP_WORKFLOW_LIFECYCLE.md`
- Known races/failure modes: `references/github-connector-workflows/PITFALLS.md`

Do not load all references automatically.

Core invariants:

- connector = control plane;
- Actions = bounded execution plane;
- artifacts/logs = evidence plane;
- each individual connector content write must be `<=19 KB` UTF-8;
- workflow use must remain inside the active turn/subturn boundary;
- workflow-created/modified YAML must be validated before publication/trigger;
- temporary workflow cleanup is workflow-first;
- source/evidence authority is exact commit/hash based.

Return to the active turn/subturn file after the required GitHub operation.

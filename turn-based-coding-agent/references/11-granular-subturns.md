# Granular Workflow Compatibility Router

**Context class:** `compatibility`

Granular behavior now lives in focused turn files. Do not load this file during normal execution.

```text
CB-DRAFT -> CB-APPLY -> CB-COMPILE -> CB-CLOSEOUT
    ^                         |
    |------ compile FAIL -----|

TB-EXEC -> TB-REVIEW -> TB-PLAN -> [Optional Review]
```

Use the live handoff's exact `load_next` target under `references/turns/`. If recovering an older handoff, select the matching state from `SKILL.md` and load only that one turn file.

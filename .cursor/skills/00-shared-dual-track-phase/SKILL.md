---
name: 00-shared-dual-track-phase
description: >-
  Unit Converter Dual-Track TDD phase workflow. Use when starting or finishing
  a phase (spec, red, green, refactoring), checking branch constraints, or
  branch transition announcements.
---

# Dual-Track Phase Workflow

## Branch map

```
spec → red → green → refactoring
```

| Step | Branch | Complete when |
|------|--------|---------------|
| 01 | `spec` | Mom Test + scenarios in Report/01 |
| 02 | `red` | Acceptance tests fail correctly |
| 03 | `green` | Acceptance tests Green |
| 05 | `refactoring` | OCP/SRP cleanup, tests Green |

## Before any work

1. `git branch --show-current`
2. Match `.cursor/rules/00-shared-dual-track-tdd-branches.mdc`
3. If mismatch, stop and tell user correct branch

## Phase transitions (user creates branches)

| Finished | Tell user |
|----------|-----------|
| `spec` + Mom Test | `git checkout red` or `git checkout -b red` |
| `red` | `git checkout -b green` |
| `green` | `git checkout -b refactoring` |

## Reference

- `.cursor/00-index.md`
- `Report/01-spec-requirements-analysis-report.md`

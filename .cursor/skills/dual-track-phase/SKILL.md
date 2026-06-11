---
name: dual-track-phase
description: >-
  Unit Converter Dual-Track TDD phase workflow. Use when starting or finishing
  a phase (spec, red, green, refactoring), checking branch constraints, or
  when the user says phase-red, phase-green, or branch transition.
---

# Dual-Track Phase Workflow

## Branch map

```
spec → red → green → refactoring
(step 04 extras excluded)
```

| Step | Branch | Dual-Track | Complete when |
|------|--------|------------|---------------|
| 01 | `spec` | Analyze | Scenarios + rules in Report/01 |
| 02 | `red` | Outer Red | Acceptance tests fail correctly |
| 03 | `green` | Inner RGR | Acceptance tests Green |
| 05 | `refactoring` | Refactor | OCP/SRP cleanup, tests Green |

## Before any work

1. Run `git branch --show-current`
2. Match branch to allowed work (see `.cursor/rules/dual-track-tdd-branches.mdc`)
3. If mismatch, stop and tell user which branch they need

## Phase transitions (user creates branches)

| Finished | Tell user |
|----------|-----------|
| `spec` complete | `git checkout -b red` |
| `red` complete (all AT Red) | `git checkout -b green` |
| `green` complete (all AT Green) | `git checkout -b refactoring` |
| `refactoring` complete | optional merge to `main` only if user asks |

Do **not** run branch creation unless user explicitly requests it.

## Per-phase checklist

### `red`

- [ ] Acceptance tests for AT-1, AT-1b, AT-2 … AT-5
- [ ] `pytest` run shows expected failures
- [ ] No production implementation
- [ ] Export step 02 artifacts

### `green`

- [ ] Unit tests via RGR for parsing, conversion, rounding, validation
- [ ] Acceptance tests Green
- [ ] Export step 03 artifacts

### `refactoring`

- [ ] Classes/modules split (Parser, Registry, Converter, Formatter)
- [ ] All tests Green after each refactor
- [ ] Export step 05 artifacts

## Reference

- Scenarios: `Report/01-spec-requirements-analysis-report.md`
- Domain rules: `.cursor/rules/unit-converter-domain.mdc`

# 00 — Shared — Workflow Harness

Dual-Track TDD #1 (Outside-In): acceptance tests first, then unit RGR.

```
spec (01 Analyze + Mom Test)
  → red (02 outer Red)
  → green (03 inner RGR → Green)
  → refactoring (05 OCP/SRP)
```

## Gates

| Step | Branch | Gate |
|------|--------|------|
| 01 | `spec` | Mom Test + scenarios confirmed before red |
| 02 | `red` | Tests only; no prod implementation |
| 03 | `green` | RGR until acceptance Green |
| 05 | `refactoring` | Refactor only; tests stay Green |

## Artifacts per step

- `Report/{NN}-{slug}-report.md`
- `Prompting/{NN}-{slug}-transcript.md`
- Optional: update `.cursor/` step files

See `.cursor/skills/00-shared-export-phase-artifacts/SKILL.md`.

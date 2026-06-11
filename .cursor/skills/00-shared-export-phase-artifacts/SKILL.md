---
name: 00-shared-export-phase-artifacts
description: >-
  Export Unit Converter phase Report and Prompting transcript with consistent
  numbering. Use when a phase completes or user runs 00-export-artifacts.
---

# Export Phase Artifacts

## Numbering

| Step | Branch | slug |
|------|--------|------|
| 01 | `spec` | `spec-requirements-analysis` |
| 02 | `red` | `acceptance-red` |
| 03 | `green` | `basic-green` |
| 05 | `refactoring` | `refactoring` |

Skip step **04**.

## Attribution

- **Prompting/**: Turn User = 사람, Turn Assistant = AI (no suffix on every line)
- **Report/**: use Speaker and Authority columns per `00-shared-report-prompting-format.mdc`

1. Create `Report/{NN}-{slug}-report.md` (see `00-shared-report-prompting-format.mdc`)
2. Export `Prompting/{NN}-{slug}-transcript.md` from agent-transcripts JSONL
3. Update `Report/00-index.md` and `Prompting/00-index.md`

## After export

Tell user next branch if phase complete.

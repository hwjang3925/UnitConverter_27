# .cursor Index — Unit Converter Dual-Track TDD

Numbering: `{NN}-{phase-slug}-*` (aligned with `Report/` and `Prompting/`)

| NN | Branch | phase-slug |
|----|--------|------------|
| 00 | shared | `shared` |
| 01 | `spec` | `spec` |
| 02 | `red` | `red` |
| 03 | `green` | `green` |
| ~~04~~ | — | excluded |
| 05 | `refactoring` | `refactoring` |

## Directory map

| Folder | Purpose |
|--------|---------|
| `models/` | Phase model / prompting notes |
| `agents/` | Subagent definitions (`.cursor/agents/`) |
| `harness/` | Phase gates, workflow orchestration notes |
| `rules/` | Always-on or glob rules (`.mdc`) |
| `skills/` | Workflow skills (`SKILL.md`) |
| `commands/` | Slash commands (`.md`) |

## Files by step

### 00 shared

| Type | File |
|------|------|
| model | `models/00-shared-model-notes.md` |
| agent | `agents/00-shared-phase-coordinator.md` |
| harness | `harness/00-shared-workflow.md` |
| rule | `rules/00-shared-unit-converter-workflow.mdc` |
| rule | `rules/00-shared-dual-track-tdd-branches.mdc` |
| rule | `rules/00-shared-unit-converter-domain.mdc` |
| rule | `rules/00-shared-report-prompting-format.mdc` |
| skill | `skills/00-shared-dual-track-phase/SKILL.md` |
| skill | `skills/00-shared-export-phase-artifacts/SKILL.md` |
| skill | `skills/00-shared-acceptance-test-authoring/SKILL.md` |
| command | `commands/00-export-artifacts.md` |

### 01 spec

| Type | File |
|------|------|
| model | `models/01-spec-model-notes.md` |
| agent | `agents/01-spec-requirements-analyst.md` |
| harness | `harness/01-spec-gate.md` |
| rule | `rules/01-spec-mom-test.mdc` |
| skill | `skills/01-spec-mom-test/SKILL.md` |
| command | `commands/01-spec-mom-test.md` |

### 02 red (when active)

| command | `commands/02-phase-red.md` |

### 03 green (when active)

| command | `commands/03-phase-green.md` |

### 05 refactoring (when active)

| command | `commands/05-phase-refactoring.md` |

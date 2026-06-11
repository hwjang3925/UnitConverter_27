# Report Index

Unit Converter 실습 — Dual-Track TDD 단계별 보고서 목록

## Numbering 규칙

| 항목 | 형식 | 예시 |
|------|------|------|
| Report | `Report/{NN}-{phase-slug}-report.md` | `01-spec-requirements-analysis-report.md` |
| Transcript | `Prompting/{NN}-{phase-slug}-transcript.md` | `01-spec-requirements-analysis-transcript.md` |

- `{NN}`: 2자리 순번 (01, 02, 03, 05 — **04 제외**)
- `{phase-slug}`: kebab-case 단계명
- Report / Transcript **동일 번호·slug** 사용

## 단계 매핑

| No | Phase | Branch | Report | Transcript |
|----|-------|--------|--------|------------|
| 01 | Spec / Requirements Analysis | `spec` | ✅ Complete | ✅ |
| 02 | Acceptance Test Red (Outer Loop) | `red` | (예정) | (예정) |
| 03 | Basic Implementation Green (Inner RGR) | `green` | (예정) | (예정) |
| ~~04~~ | Extra Requirements | — | **제외** | **제외** |
| 05 | Refactoring | `refactoring` | (예정) | (예정) |

## Cursor 설정

- Rules: `.cursor/rules/`
- Skills: `.cursor/skills/`
- Commands: `.cursor/commands/` (`/phase-red`, `/phase-green`, `/phase-refactoring`, `/export-artifacts`)

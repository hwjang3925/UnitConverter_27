# Report Index

Unit Converter 실습 — Dual-Track TDD 단계별 보고서 목록

## Numbering 규칙

| 항목 | 형식 | 예시 |
|------|------|------|
| Report | `Report/{NN}-{phase-slug}-report.md` | `01-spec-requirements-analysis-report.md` |
| Transcript | `Prompting/{NN}-{phase-slug}-transcript.md` | `01-spec-requirements-analysis-transcript.md` |

- `{NN}`: 2자리 순번 (01, 02, 03, 05 — **04 제외**)
- Report / Transcript **동일 번호·slug** 사용

## Attribution (Speaker / Authority)

| 산출물 | 규칙 |
|--------|------|
| **Prompting/** | Turn User = 사람, Turn Assistant = AI |
| **Report/** | Speaker / Authority 열 (`.cursor/rules/00-shared-report-prompting-format.mdc`) |

## Product documentation

| File | Role |
|------|------|
| **`doc/PRD.md`** | Product Requirements Document (기능·수용 기준·범위) |
| `doc/README.md` | doc 폴더 안내 |
| **`Report/green-test-results.html`** | Green 단계 pytest 결과 (브라우저) |
| **`doc/terminal-self-test.md`** | 터미널 self-test 가이드 + 검증 로그 |
| **`doc/golden-master.md`** | Golden Master 가이드 (10 cases × API/CLI) |
| **`doc/diagrams/`** | As-Is / To-Be 아키텍처 다이어그램 |

## 단계 매핑

| No | Phase | Branch | Report | Transcript |
|----|-------|--------|--------|------------|
| 01 | Spec / Requirements Analysis | `spec` | ✅ Complete | ✅ |
| 02 | Acceptance Test Red (Outer Loop) | `red` | ✅ Complete | ✅ |
| 03 | Basic Implementation Green (Inner RGR) | `green` | ✅ Complete (§9 rename) | ✅ |
| ~~04~~ | Extra Requirements | — | **제외** | **제외** |
| 05 | Refactoring | `refactoring` | (예정) | (예정) |

## Cursor commands

See `.cursor/00-index.md` — `/02-phase-red`, `/03-phase-green`, `/00-export-artifacts`

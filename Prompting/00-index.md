# Prompting Index

Unit Converter 실습 — AI 대화 Transcript Export 목록

## Numbering 규칙

Report 폴더와 **동일 번호·slug**를 사용합니다.

```
Prompting/{NN}-{phase-slug}-transcript.md
```

## Export 목록

| No | File | Phase | Branch |
|----|------|-------|--------|
| 01 | [01-spec-requirements-analysis-transcript.md](./01-spec-requirements-analysis-transcript.md) | Spec / Requirements Analysis | `spec` |
| 02 | [02-acceptance-red-transcript.md](./02-acceptance-red-transcript.md) | Acceptance Test Red | `red` |
| 03 | (예정) | Basic Implementation Green | `green` |
| ~~04~~ | — | **제외** | — |
| 05 | (예정) | Refactoring | `refactoring` |

## Export 시점

각 단계 **완료 시** `/export-artifacts` 또는 export-phase-artifacts skill 사용.

## Cursor 설정

See `.cursor/00-index.md`.

| Command | Step |
|---------|------|
| `/01-spec-mom-test` | 01 spec |
| `/02-phase-red` | 02 red |
| `/03-phase-green` | 03 green |
| `/05-phase-refactoring` | 05 refactoring |
| `/00-export-artifacts` | any |

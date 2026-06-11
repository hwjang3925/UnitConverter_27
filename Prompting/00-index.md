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
| 02 | (예정) | Acceptance Test Red | `red` |
| 03 | (예정) | Basic Implementation Green | `green` |
| ~~04~~ | — | **제외** | — |
| 05 | (예정) | Refactoring | `refactoring` |

## Export 시점

각 단계 **완료 시** `/export-artifacts` 또는 export-phase-artifacts skill 사용.

## Cursor 설정

- Rules: `.cursor/rules/`
- Skills: `.cursor/skills/`
- Commands: `.cursor/commands/`

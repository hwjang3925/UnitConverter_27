# 01 — Spec / Requirements Analysis — Report

| Item | Value |
|------|-------|
| Step | 01 |
| Phase | Spec / Requirements Analysis (Analyze) |
| Branch | `spec` |
| Method | Dual-Track TDD #1 (Outside-In) |
| Date | 2026-06-11 |
| Status | **Complete** |

---

## 1. 목적

README 요구사항과 starter 코드(`UnitConverter.py`) 간 갭을 분석하고, Dual-Track TDD 1번 방식(인수 테스트 먼저 → 내부 RGR)으로 진행하기 위한 **인수 시나리오·단위 테스트·설계 방향**을 정리한다.

---

## 2. 현재 프로젝트 상태

### 2.1 파일 구성

| 파일 | 역할 |
|------|------|
| `README.md` | 과제 설명, 요구사항, 6시간 실습 일정 |
| `UnitConverter.py` | 단일 파일 기본 구현 (~37줄) |
| `unit-converter.jpg` | 설명용 이미지 |

- 테스트, 설정 파일(JSON/YAML), `venv` **없음**
- Git 브랜치: `spec`

### 2.2 Starter 코드 동작

- 입력 형식: `unit:value` (예: `meter:2.5`)
- 지원 단위: meter, feet, yard
- meter 기준 변환 후 3단위 출력
- 부분적 입력 검증: 형식 오류, 숫자 오류, 알 수 없는 단위

### 2.3 README 대비 갭 분석

| 항목 | 현재 | 필요 |
|------|------|------|
| 3단위 변환 | 부분 구현 | 출력 포맷·반올림 규칙 정립 |
| OCP | 미적용 | 새 단위 추가 시 기존 코드 변경 최소화 |
| SRP | 미적용 | Parser / Converter / Formatter 분리 |
| 입력 검증 | 부분 | **음수** 검증 추가 |
| 테스트 | 없음 | 인수 + 단위 테스트 |
| 설정 외부화 | 없음 | JSON/YAML (4단계) |
| 동적 단위 등록 | 없음 | 런타임 등록 (4단계) |
| 출력 포맷 선택 | 없음 | JSON / CSV / 표 (4단계) |

---

## 3. 비즈니스 규칙

| 규칙 | 값 |
|------|-----|
| 1 meter | 3.28084 feet |
| 1 meter | 1.09361 yard |
| feet ↔ yard | meter 기준 간접 계산 |
| 입력 예시 | `meter:2.5` → `2.5 meter = 8.2 feet`, `2.5 meter = 2.7 yard` |
| **출력 반올림** | **소수 1자리 반올림** (확정) |
| **0 허용** | `meter:0` 등 **0은 유효 입력** (확정) |

### 확정 사항 (2026-06-11)

- [x] 출력: 변환 결과 **소수 1자리 반올림** (`round(x, 1)` 또는 동등 규칙)
- [x] **0 허용**, **음수만 거부** (`meter:-1` → 오류)
- [x] 오류 메시지: starter 코드 문구 유지

| 조건 | 오류 메시지 |
|------|-------------|
| 콜론 없음 | `Invalid format. Use unit:value (ex: meter:2.5)` |
| 숫자 아님 | `Invalid number: {value_str}` |
| 음수 | `Invalid number: {value_str}` *(starter 패턴 동일)* |
| 없는 단위 | `Unknown unit: {unit}` |

### 출력 예시 (반올림 적용)

| 입력 | 기대 출력 (일부) |
|------|------------------|
| `meter:2.5` | `2.5 meter = 8.2 feet`, `2.5 meter = 2.7 yard` |
| `meter:0` | `0 meter = 0.0 feet`, `0 meter = 0.0 yard` |

---

## 4. Dual-Track TDD 진행 계획

### 4.1 방법론 요약

| 개념 | 설명 |
|------|------|
| **Dual-Track TDD** | 외부(인수) + 내부(단위) 이중 테스트 루프 |
| **외부 루프** | 사용자 시나리오 인수 테스트 — Red → Green |
| **내부 루프** | RGR (Red → Green → Refactor) 단위 테스트 |
| **ARRR (실습)** | Analyze → Red → Green → Refactor |

### 4.2 브랜치 로드맵

| No | Branch | Dual-Track 역할 | 완료 기준 |
|----|--------|-----------------|-----------|
| 01 | `spec` ✅ | Analyze | 본 보고서 + 시나리오 확정 |
| 02 | `red` | 외부 Red | 실패하는 인수 테스트만 존재 |
| 03 | `green` | 내부 RGR | AT-1~AT-5, AT-1b Green |
| ~~04~~ | — | **제외** | README 추가 요구사항 미진행 |
| 05 | `refactoring` | Refactor | OCP/SRP 정리, 테스트 Green |

---

## 5. 인수 테스트 시나리오 (외부 루프)

| ID | 시나리오 | Given | When | Then |
|----|----------|-------|------|------|
| AT-1 | 정상 변환 | meter/feet/yard | `meter:2.5` | 3단위 변환 결과 출력 (소수 1자리) |
| AT-1b | 0 허용 | 유효 단위 | `meter:0` | 3단위 0 변환 출력 |
| AT-2 | 형식 오류 | 잘못된 형식 | `meter2.5` | `Invalid format. Use unit:value (ex: meter:2.5)` |
| AT-3 | 숫자 오류 | 비숫자 값 | `meter:abc` | `Invalid number: abc` |
| AT-4 | 음수 | 음수 값 | `meter:-1` | `Invalid number: -1` |
| AT-5 | 없는 단위 | 미등록 단위 | `mile:1` | `Unknown unit: mile` |

---

## 6. 단위 테스트 후보 (내부 루프)

| ID | 테스트 | 검증 내용 |
|----|--------|-----------|
| UT-1 | `test_meter_to_feet` | 2.5 m → 8.2 feet |
| UT-2 | `test_meter_to_yard` | 2.5 m → 2.7 yard |
| UT-3 | `test_feet_to_meter` | 역변환 정확도 |
| UT-4 | `test_yard_to_meter` | 역변환 정확도 |
| UT-5 | `test_parse_input_valid` | `unit:value` 파싱 |
| UT-6 | `test_parse_input_invalid_format` | 콜론 없음 |
| UT-7 | `test_parse_input_invalid_number` | abc 등 |
| UT-8 | `test_parse_input_negative` | 음수 거부 (`-1` → 오류) |
| UT-9 | `test_parse_input_zero_allowed` | `0` 허용 |
| UT-10 | `test_unknown_unit_raises` | mile 등 미등록 단위 |
| UT-11 | `test_round_one_decimal` | 소수 1자리 반올림 |

---

## 7. 설계 방향 (OCP / SRP)

```
config.json/yaml  →  UnitRegistry (단위·비율 로드/등록)
                         ↓
InputParser (검증)  →  Converter (meter 기준 변환)
                         ↓
                    OutputFormatter (text / JSON / CSV)
```

| 클래스 | 책임 (SRP) |
|--------|------------|
| `InputParser` | 입력 파싱·검증 |
| `UnitRegistry` | 단위·변환 비율 관리 (OCP: 등록으로 확장) |
| `Converter` | meter 기준 변환 로직 |
| `OutputFormatter` | 출력 형식 (text → JSON/CSV 확장) |

---

## 8. spec 단계 체크리스트

```
✅ AT-1 ~ AT-5 (+ AT-1b) 시나리오 표 작성   → §5
✅ 내부 단위 테스트 목록 정리               → §6 (UT-1 ~ UT-11)
✅ 클래스 역할 분리 메모                    → §7
✅ 반올림: 소수 1자리 / 0 허용 / 오류 메시지 → §3
```

---

## 9. 다음 단계

**01 spec 완료** → `red` 브랜치 생성 후 02단계 진행

다음 작업:
1. 실패하는 인수 테스트만 작성 (구현 코드 없음)
2. `Report/02-acceptance-red-report.md` 생성
3. `Prompting/02-acceptance-red-transcript.md` Export

---

## 10. AI 활용 요약 (본 단계)

| 활동 | AI 활용 |
|------|---------|
| README·코드 갭 분석 | 프로젝트 탐색, 갭 표 작성 |
| Dual-Track TDD / ARRR 설명 | 방법론 정리, 과제 적용 예시 |
| 브랜치 전략 | 단계별 브랜치·완료 기준 제안 |
| 보고서·Transcript | Report/Prompting 폴더 구조 및 01번 산출물 생성 |

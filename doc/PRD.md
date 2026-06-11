# Product Requirements Document — Unit Converter

| Item | Value |
|------|-------|
| Product | Unit Converter (Python CLI) |
| Version | 1.0 |
| Status | **Approved** (spec phase 확정, green 구현 완료) |
| Date | 2026-06-11 |
| Authority | README + spec 분석 + Mom Test → **사람 확정** |
| Related | `Report/01-spec-requirements-analysis-report.md`, `README.md` |

---

## 1. 개요 (Overview)

### 1.1 문제 정의

사용자가 길이 값을 **한 단위로 입력**하면, **meter / feet / yard** 세 단위로 변환된 결과를 **한 번에** 확인할 수 있어야 한다.  
입력 형식은 단순(`unit:value`)하고, 잘못된 입력은 **명확한 오류 메시지**로 거부한다.

### 1.2 제품 목표

| 목표 | 설명 |
|------|------|
| **정확한 변환** | meter 기준 비율로 feet·yard 계산 |
| **일관된 출력** | 변환된 feet/yard는 **소수 1자리** 표시 |
| **안전한 입력** | 형식·숫자·단위·음수 검증 |
| **테스트 가능** | 인수 테스트 + 단위 테스트로 검증 |
| **확장 가능 설계** | OCP/SRP (refactoring 단계) |

### 1.3 실행 방식

```bash
python UnitConverter.py
```

프롬프트에 `meter:2.5` 형식으로 입력 → 변환 결과 3줄 또는 오류 1줄 출력.

---

## 2. 범위 (Scope)

### 2.1 In Scope (v1 — 본 실습)

| 영역 | 내용 |
|------|------|
| 단위 | `meter`, `feet`, `yard` |
| 입력 | `unit:value` (콜론 1개로 분리) |
| 출력 | 텍스트 3줄 (입력 단위 + meter + feet + yard) |
| 검증 | 형식, 숫자, 음수, 미등록 단위 |
| 품질 | OCP, SRP, Dual-Track TDD |
| 테스트 | AT-1 ~ AT-5, AT-1b + 단위 테스트 |

### 2.2 Out of Scope (README step-04 — 제외)

| 항목 | 설명 |
|------|------|
| 설정 외부화 | JSON/YAML에서 비율 로드 |
| 동적 단위 등록 | 런타임 `1 cubit = 0.4572 meter` 등록 |
| 출력 포맷 선택 | JSON / CSV / 표 형태 |

---

## 3. 사용자·사용 시나리오

### 3.1 대상 사용자

- 길이 단위를 빠르게 비교해야 하는 **일반 사용자** (CLI)
- 과제/실습 맥락: Python CLI + TDD 학습

### 3.2 핵심 시나리오

| ID | As a user | I want to | So that |
|----|-----------|-----------|---------|
| US-1 | 사용자 | `meter:2.5` 입력 | 세 단위 변환 결과를 즉시 확인 |
| US-2 | 사용자 | 잘못된 입력(`meter2.5`) | 무엇이 틀렸는지 메시지로 알 수 있음 |
| US-3 | 사용자 | `meter:0` 입력 | 0도 유효한 길이로 변환됨 |
| US-4 | 사용자 | `meter:-1` 입력 | 음수는 거부되고 이유를 알 수 있음 |

---

## 4. 기능 요구사항 (Functional Requirements)

### FR-1 입력 파싱

- 형식: `{unit}:{value}` — **첫 번째 콜론** 기준 split
- `unit`: 문자열 (공백 trim 없음 — starter 동작 유지)
- `value`: Python `float()` 파싱

### FR-2 단위 변환

| 규칙 | 값 |
|------|-----|
| 1 meter | 3.28084 feet |
| 1 meter | 1.09361 yard |
| feet ↔ yard | **meter 기준** 간접 계산 |

지원 단위: `meter`, `feet`, `yard` 만.

### FR-3 출력

입력 `meter:2.5` 예시:

```text
2.5 meter = 2.5 meter
2.5 meter = 8.2 feet
2.5 meter = 2.7 yard
```

| 규칙 | 상세 |
|------|------|
| 줄 수 | 3줄 (입력 단위→meter, 입력→feet, 입력→yard) |
| meter 줄 | 입력 value 그대로 표시 (반올림 없음) |
| feet/yard 줄 | `round(x, 1)` 후 **`:.1f`** 표시 |
| 0 입력 | `0 meter = 0.0 feet`, `0 meter = 0.0 yard` |

### FR-4 입력 검증

| 조건 | 동작 | 오류 메시지 (정확히 일치) |
|------|------|---------------------------|
| 콜론 없음 | 거부 | `Invalid format. Use unit:value (ex: meter:2.5)` |
| 숫자 아님 | 거부 | `Invalid number: {value_str}` |
| 음수 (`value < 0`) | 거부 | `Invalid number: {value_str}` |
| 미등록 단위 | 거부 | `Unknown unit: {unit}` |
| **0** | **허용** | 정상 변환 |

오류 시 **한 줄**만 출력하고 변환 결과는 출력하지 않는다.

---

## 5. 비기능 요구사항 (Non-Functional Requirements)

### NFR-1 설계 (품질)

| 원칙 | 요구 |
|------|------|
| **OCP** | 새 단위 추가 시 기존 코드 변경 최소 (refactoring에서 `UnitRegistry` 등) |
| **SRP** | Parser / Converter / Formatter 책임 분리 (refactoring 단계) |

### NFR-2 테스트

| 유형 | 목적 |
|------|------|
| Acceptance (CLI) | 사용자 관점 AT-1 ~ AT-5, AT-1b |
| Unit | 파싱·검증·반올림·변환 수학 |

방법론: **Dual-Track TDD #1 (Outside-In)** — 인수 테스트 먼저, 내부 RGR.

### NFR-3 코드 구조 (green 이후)

| 파일 | 역할 |
|------|------|
| `UnitConverter.py` | CLI 진입점 (`input` / `print`) |
| `conversion.py` | 파싱·검증·변환·반올림 로직 |

---

## 6. 수용 기준 (Acceptance Criteria)

| ID | Given | When | Then |
|----|-------|------|------|
| **AT-1** | 유효 단위 | `meter:2.5` | 3단위 출력, feet/yard **소수 1자리** |
| **AT-1b** | 유효 단위 | `meter:0` | 3단위 0 변환 (`0.0 feet`, `0.0 yard`) |
| **AT-2** | — | `meter2.5` | `Invalid format. Use unit:value (ex: meter:2.5)` |
| **AT-3** | — | `meter:abc` | `Invalid number: abc` |
| **AT-4** | — | `meter:-1` | `Invalid number: -1` |
| **AT-5** | — | `mile:1` | `Unknown unit: mile` |

**완료 기준:** `python -m pytest tests/` — acceptance 7 + unit 4 + golden 20 = **31 passed** (Golden Master: `doc/golden-master.md`).

---

## 7. Mom Test — 요구 검증 (배경)

과제 README는 주어졌으나, **요구가 실제 문제를 푸는지** Mom Test로 검증했다.

| ID | 질문 요약 | Speaker | 결과 |
|----|-----------|---------|------|
| Q4 | 아주 큰 길이 변환 시 결과가 직관적이지 않았는가? | 사람 | **배경 동기** — 다중 단위 변환 필요성 뒷받침; **상한/과학적 표기 요구 없음** |
| Q5 | `0.02`처럼 작은 값 변환이 헷갈렸는가? | 사람 | **양수 소수 허용**; 1자리 반올림 유지; 극소값은 **알려진 UX 한계** |

| 검증 | 판정 | Authority | spec 영향 |
|------|------|-----------|-----------|
| V6 | README에 큰 수/표기 요구 없음 | AI 제안 → 사람 확정 | AT 변경 없음 |
| V7 | `0.02` 등 양수 소수 유효 | AI 제안 → 사람 확정 | AT-1 범위 내 |
| V8 | 극소값 + 1자리 반올림 혼란 가능 | 주의 기록 | 필수 AT 추가 없음 |

---

## 8. 아키텍처 방향 (Target — refactoring)

```
InputParser (검증)
      ↓
UnitRegistry (단위·비율 — OCP)
      ↓
Converter (meter 기준 변환)
      ↓
OutputFormatter (텍스트 출력)
```

| 컴포넌트 | SRP |
|----------|-----|
| `InputParser` | 파싱·검증 |
| `UnitRegistry` | 단위·변환 비율 |
| `Converter` | meter 기준 변환 |
| `OutputFormatter` | stdout 형식 |

현재 green: 위 역할이 **`conversion.py`** 에 함수로 통합. refactoring에서 클래스/모듈 분리.

---

## 9. 구현 상태

| Phase | Branch | Status | 비고 |
|-------|--------|--------|------|
| Spec / Analyze | `spec` | ✅ | 본 PRD + Report/01 |
| Acceptance Red | `red` | ✅ | 2 failed (의도) → green |
| Basic Green | `green` | ✅ | 11 passed |
| Refactoring | `refactoring` | ⏸ | **✅ Complete** |

---

## 10. 용어

| 용어 | 정의 |
|------|------|
| AT | Acceptance Test 시나리오 (AT-1 …) |
| UT | Unit Test (UT-1 … UT-11) |
| RGR | Red → Green → Refactor |
| meter base | 모든 변환의 중간 기준 단위 |

---

## 11. 참고 문서

| 문서 | 용도 |
|------|------|
| `README.md` | 과제 원문·실습 일정 |
| `Report/01-spec-requirements-analysis-report.md` | 갭 분석·시나리오·설계 메모 |
| `Report/02-acceptance-red-report.md` | Red 단계 결과 |
| `Report/03-basic-green-report.md` | Green 구현·rename |
| `conversion.py` | 현재 도메인 로직 |
| `doc/diagrams/` | As-Is / To-Be 아키텍처 다이어그램 |
| `tests/` | acceptance + unit |

---

## 12. 변경 이력

| Version | Date | 변경 | Authority |
|---------|------|------|-----------|
| 1.0 | 2026-06-11 | 초안 — Report/01·README·Mom Test·green 확정 반영 | AI 작성 → 사람 요청 |

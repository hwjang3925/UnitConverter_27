# 02 — Acceptance Test Red — Report

| Item | Value |
|------|-------|
| Step | 02 |
| Phase | Acceptance Test Red (Outer Loop) |
| Branch | `red` |
| Method | Dual-Track TDD #1 (Outside-In) |
| Date | 2026-06-11 |
| Status | **Complete** |

---

## 1. 목적

spec 단계에서 정의한 인수 시나리오(AT-1 ~ AT-5, AT-1b)에 대한 **실패하는(또는 미충족) acceptance 테스트**를 작성한다. **프로덕션 코드는 수정하지 않는다.**

---

## 2. 작업 내용

### 2.1 추가 파일

| 파일 | 역할 |
|------|------|
| `tests/conftest.py` | CLI subprocess 헬퍼 `run_converter()` |
| `tests/acceptance/test_cli_conversion.py` | AT-1, AT-1b |
| `tests/acceptance/test_cli_validation.py` | AT-2 ~ AT-5 |
| `pytest.ini` | pytest 설정 |
| `requirements-dev.txt` | `pytest>=8.0` |

### 2.2 시나리오 ↔ 테스트 매핑

| ID | 테스트 | 입력 |
|----|--------|------|
| AT-1 | `test_at1_meter_input_shows_rounded_feet_and_yard` | `meter:2.5` |
| AT-1b | `test_at1b_zero_input_shows_zero_conversions` | `meter:0` |
| AT-2 | `test_at2_missing_colon_shows_format_error` | `meter2.5` |
| AT-3 | `test_at3_non_numeric_value_shows_number_error` | `meter:abc` |
| AT-4 | `test_at4_negative_value_shows_number_error` | `meter:-1` |
| AT-5 | `test_at5_unknown_unit_shows_unit_error` | `mile:1` |

---

## 3. pytest 실행 결과 (Red 확인)

```text
python -m pytest tests/acceptance/ -v
```

| 결과 | 테스트 | 실패/통과 이유 |
|------|--------|----------------|
| **FAIL** | AT-1 (반올림) | stdout에 `8.2 feet`, `2.7 yard` 없음 (현재 `8.2021`, `2.734025`) |
| **FAIL** | AT-4 (음수) | `Invalid number: -1` 없음 (현재 변환 수행) |
| PASS | AT-1b | starter가 0.0 feet/yard 출력 |
| PASS | AT-2, AT-3, AT-5 | starter가 이미 검증 구현 |
| PASS | AT-1 meter line | `2.5 meter = 2.5 meter` 존재 |

**요약: 2 failed, 5 passed** — Green 단계에서 해결할 항목: **소수 1자리 반올림**, **음수 거부**

---

## 4. Red 단계 준수

- [x] `UnitConverter.py` **미수정**
- [x] acceptance 테스트만 추가
- [x] 의도된 Red 실패 2건 확인 (AT-1, AT-4)
- [x] README step-04 extras 미구현

---

## 5. Green 단계에서 할 일 (미리보기)

내부 RGR로 아래를 구현:

1. 변환 결과 **소수 1자리 반올림** (UT-11)
2. **음수 입력 거부** (UT-8)
3. 필요 시 단위 테스트로 파싱·변환 분리

---

## 6. 다음 단계

**02 red 완료** → `green` 브랜치 생성

```powershell
git checkout -b green
```

Green 단계: `/phase-green` 또는 「03 시작」

---

## 7. AI 활용 요약

| 활동 | 내용 |
|------|------|
| 테스트 설계 | spec Report §5 시나리오 → pytest CLI 테스트 |
| Red 검증 | pytest 실행으로 실패 원인 기록 |
| 산출물 | 02 Report + Transcript Export |

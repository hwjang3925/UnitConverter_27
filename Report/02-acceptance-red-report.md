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

spec §5 인수 시나리오(AT-1 … AT-5, AT-1b)에 대한 **acceptance 테스트만** 작성하고, **의도된 Red**를 확인한다. `UnitConverter.py`는 수정하지 않는다.

---

## 2. 작업 내용

| Speaker | Content |
|---------|---------|
| AI | pytest acceptance 테스트·scaffolding 설계 |
| AI | `tests/`, `pytest.ini`, `requirements-dev.txt` 추가 |
| 사람 | red 브랜치에서 단계 재진행·커밋 |

### 2.1 추가 파일

| 파일 | AT |
|------|-----|
| `tests/conftest.py` | CLI helper |
| `tests/acceptance/test_cli_conversion.py` | AT-1, AT-1b |
| `tests/acceptance/test_cli_validation.py` | AT-2 … AT-5 |
| `pytest.ini` | 설정 |
| `requirements-dev.txt` | pytest |

---

## 3. pytest 결과 (Red 확인)

```text
python -m pytest tests/acceptance/ -v
→ 2 failed, 5 passed
```

| Result | Test | AT | 실패/통과 이유 | Speaker |
|--------|------|-----|----------------|---------|
| **FAIL** | `test_at1_meter_input_shows_rounded_feet_and_yard` | AT-1 | `8.2 feet`, `2.7 yard` 없음 (raw float) | AI (테스트) |
| **FAIL** | `test_at4_negative_value_shows_number_error` | AT-4 | `Invalid number: -1` 없음 (변환 수행) | AI (테스트) |
| PASS | `test_at1_meter_input_shows_meter_line` | AT-1 | meter 줄 존재 | AI |
| PASS | `test_at1b_zero_input_shows_zero_conversions` | AT-1b | `0.0 feet/yard` | AI |
| PASS | AT-2, AT-3, AT-5 | AT-2~5 | starter가 이미 충족 | AI |

**Green에서 해결:** 소수 1자리 반올림 (AT-1), 음수 거부 (AT-4).

---

## 4. Red 단계 준수

| Check | Status | Authority |
|-------|--------|-----------|
| `UnitConverter.py` 미수정 | ✅ | AI 확인 |
| acceptance 테스트만 추가 | ✅ | AI |
| 의도된 Red 2건 | ✅ AT-1, AT-4 | AI |
| step-04 extras 미구현 | ✅ | AI 제안 → 사람 확정 |

---

## 5. Decisions — Authority

| Decision | Value | Authority |
|----------|-------|-----------|
| Red 완료 기준 | 2 failed (AT-1, AT-4), 5 passed | AI 제안 → 사람 확정 |
| 다음 브랜치 | `green` | AI |

---

## 6. 다음 단계

```powershell
git add tests/ pytest.ini requirements-dev.txt Report/ Prompting/
git commit -m "test: add acceptance tests — Red phase (AT-1, AT-4 failing)"
git checkout -b green
```

Green: `/03-phase-green` — 내부 RGR로 AT-1·AT-4 Green.

---

## 7. 참고

- 시나리오·Mom Test: `Report/01-spec-requirements-analysis-report.md` §5, §11
- 대화: `Prompting/02-acceptance-red-transcript.md`

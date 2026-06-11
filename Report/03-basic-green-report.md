# 03 — Basic Implementation Green — Report

| Item | Value |
|------|-------|
| Step | 03 |
| Phase | Basic Implementation Green (Inner RGR) |
| Branch | `green` |
| Method | Dual-Track TDD #1 (Outside-In) |
| Date | 2026-06-11 |
| Status | **Complete** |

---

## 1. 목적

red 단계에서 실패한 **AT-1(반올림)**, **AT-4(음수)** 를 내부 RGR로 해결하고, **acceptance 7건 + unit 4건 Green** 달성.

---

## 2. RGR 요약

| Speaker | Content |
|---------|---------|
| AI | `conversion.py` 모듈 추출, `UnitConverter.py`는 CLI 진입점 |
| AI | UT-8 음수 → `parse_input` Green |
| AI | UT-11 반올림 → `convert_to_all_units` Green |
| AI | acceptance 7건 Green 확인 |

### 2.1 변경·추가 파일

| 파일 | 역할 |
|------|------|
| `conversion.py` | 파싱·검증·변환·반올림 로직 |
| `UnitConverter.py` | `input()` + `run()` 호출 |
| `tests/unit/test_validation.py` | UT-8, UT-9 |
| `tests/unit/test_rounding.py` | UT-11 |

---

## 3. 구현 내용

| 요구 | 구현 |
|------|------|
| AT-4 음수 | `value < 0` → `Invalid number: {value_str}` |
| AT-1 반올림 | feet/yard `round(..., 1)` + `:.1f` 출력 |
| AT-1b | `0.0 feet`, `0.0 yard` |
| 오류 문구 | starter와 동일 유지 |

---

## 4. pytest 결과

```text
python -m pytest tests/ -v
→ 11 passed (7 acceptance + 4 unit)
```

| Suite | Count | Status |
|-------|-------|--------|
| acceptance | 7 | Green |
| unit | 4 | Green |

---

## 5. Green 단계 준수

| Check | Status | Authority |
|-------|--------|-----------|
| acceptance 테스트 미완화 | ✅ | AI |
| step-04 extras 미구현 | ✅ | AI 제안 → 사람 확정 |
| OCP/SRP 대규모 분리 | ⏸ refactoring 단계로 연기 | AI |

---

## 6. Decisions — Authority

| Decision | Value | Authority |
|----------|-------|-----------|
| 로직 모듈 `conversion.py` | green에서 최소 추출; post-green 2안 rename (`unit_converter.py` → `conversion.py`) | AI 제안 → 사람 확정 |
| 다음 브랜치 | `refactoring` | AI |

---

## 7. 다음 단계

```powershell
git add conversion.py UnitConverter.py tests/
git commit -m "feat: rounding and negative validation — Green phase"
git commit -m "refactor: rename unit_converter.py to conversion.py (2안)"
git checkout -b refactoring
```

`/05-phase-refactoring` — InputParser, Converter 등 OCP/SRP 분리.

---

## 9. Post-green — 모듈 rename (2안)

| Item | Value |
|------|-------|
| Date | 2026-06-11 |
| Branch | `green` |
| Authority | AI 제안 → 사람 확정 |

### 9.1 배경

`UnitConverter.py`(CLI)와 `unit_converter.py`(로직) 이름이 유사해 역할 구분이 어렵다.

### 9.2 채택안 (2안 — 최소 rename)

| 파일 | 역할 | 변경 |
|------|------|------|
| `UnitConverter.py` | README 진입점, `input()` / `print()` | **유지** |
| `conversion.py` | 파싱·검증·변환·반올림 | `unit_converter.py`에서 rename |

### 9.3 영향 범위

| 대상 | 변경 |
|------|------|
| `UnitConverter.py` | `from conversion import run` |
| `tests/unit/test_validation.py` | `from conversion import parse_input` |
| `tests/unit/test_rounding.py` | `from conversion import convert_to_all_units` |
| `tests/conftest.py` | 변경 없음 (`UnitConverter.py` subprocess 유지) |

### 9.4 pytest

```text
python -m pytest tests/ -q
→ 11 passed
```

### 9.5 refactoring 예고

refactoring 단계에서 `conversion.py`를 `InputParser`, `UnitRegistry`, `Converter`, `OutputFormatter` 등으로 분리 예정 (1안 패키지 구조는 그때 검토).

---

## 8. 참고

- Transcript: `Prompting/03-basic-green-transcript.md`
- red Report: `Report/02-acceptance-red-report.md`

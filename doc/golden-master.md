# Golden Master — Unit Converter

| Item | Value |
|------|-------|
| Baseline | Green phase (`conversion.run` / CLI output) |
| Location | `tests/golden/masters/*.txt` |
| Tests | `tests/golden/test_golden_master.py` |
| Count | 10 cases × 2 (API + CLI) = **20 tests** |

---

## Purpose

Refactoring 시 **출력 전체**가 Green 기준과 동일한지 검증한다.  
Acceptance 테스트(AT)는 부분 문자열 검사; Golden Master는 **줄 단위 완전 일치**.

---

## Cases

| ID | Input | Master file |
|----|-------|-------------|
| AT-1 | `meter:2.5` | `meter_2_5.txt` |
| AT-1b | `meter:0` | `meter_0.txt` |
| AT-2 | `meter2.5` | `meter2_5_error.txt` |
| AT-3 | `meter:abc` | `meter_abc_error.txt` |
| AT-4 | `meter:-1` | `meter_neg1_error.txt` |
| AT-5 | `mile:1` | `mile_1_error.txt` |
| EXT-feet | `feet:10` | `feet_10.txt` |
| EXT-yard | `yard:5` | `yard_5.txt` |
| EXT-0.02 | `meter:0.02` | `meter_0_02.txt` |
| EXT-meter1 | `meter:1` | `meter_1.txt` |

---

## Run

```powershell
python -m pytest tests/golden/ -v
python -m pytest tests/ -q
# → 31 passed (11 + 20 golden)
```

---

## Updating masters (intentional behavior change only)

1. PRD / AT 먼저 수정  
2. Green 동작 확인 후 master 파일 수동 갱신  
3. `pytest tests/golden/` 재실행  

**Refactoring 중:** master 변경 없이 구조만 수정 → 31 tests Green 유지.

---

## CLI prompt handling

CLI stdout includes `Insert value for converting (ex: meter:2.5): ` prefix.  
`tests/conftest.normalize_cli_stdout()` strips it before comparison.

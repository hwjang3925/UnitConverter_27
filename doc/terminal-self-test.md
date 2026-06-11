# Terminal Self-Test Guide — Unit Converter

| Item | Value |
|------|-------|
| Phase | Green |
| Platform | Windows · Python 3.14.5 · pytest 9.0.3 |
| Verified | 2026-06-11 (Agent 실행 확인) |
| Project root | `c:\dev\UnitConverter_27` |

---

## 1. 준비 (최초 1회)

```powershell
cd c:\dev\UnitConverter_27

python -m venv venv
.\venv\Scripts\activate

pip install -r requirements-dev.txt
```

---

## 2. pytest — 자동 self test

### 2.1 전체 (31 tests — acceptance + unit + golden)

**명령:**

```powershell
python -m pytest tests/ -v
```

**결과 (Golden Master 포함):**

```text
31 passed
```

| Suite | Count |
|-------|-------|
| acceptance | 7 |
| unit | 4 |
| golden (API + CLI) | 20 |
| **합계** | **31** |

### 2.2 Green only (11 tests)

**명령:**

```powershell
python -m pytest tests/acceptance/ tests/unit/ -v
```

**결과 (검증됨):**

```text
collected 11 items
… 11 passed in 0.94s
```

### 2.3 Golden Master only

```powershell
python -m pytest tests/golden/ -v
# → 20 passed
```

See [`golden-master.md`](./golden-master.md).

### 2.4 요약만

**명령:**

```powershell
python -m pytest tests/ -q
```

**결과 (검증됨):**

```text
11 passed in 1.18s
```

### 2.3 인수 테스트만 (7 tests)

**명령:**

```powershell
python -m pytest tests/acceptance/ -v
```

**결과 (검증됨):**

```text
7 passed in 0.92s
```

### 2.4 단위 테스트만 (4 tests)

**명령:**

```powershell
python -m pytest tests/unit/ -v
```

**결과 (검증됨):**

```text
4 passed in 0.05s
```

### 2.5 특정 테스트 (예: AT-4)

```powershell
python -m pytest tests/acceptance/test_cli_validation.py::TestNegativeValue::test_at4_negative_value_shows_number_error -v
```

---

## 3. 수동 CLI smoke test

`UnitConverter.py`를 파이프로 입력해 동작 확인.

### 3.1 정상 변환

**명령:**

```powershell
"meter:2.5" | python UnitConverter.py
```

**출력 (검증됨):**

```text
Insert value for converting (ex: meter:2.5): 2.5 meter = 2.5 meter
2.5 meter = 8.2 feet
2.5 meter = 2.7 yard
```

### 3.2 음수 거부 (AT-4)

**명령:**

```powershell
"meter:-1" | python UnitConverter.py
```

**출력 (검증됨):**

```text
Insert value for converting (ex: meter:2.5): Invalid number: -1
```

### 3.3 형식 오류 (AT-2)

**명령:**

```powershell
"meter2.5" | python UnitConverter.py
```

**출력 (검증됨):**

```text
Insert value for converting (ex: meter:2.5): Invalid format. Use unit:value (ex: meter:2.5)
```

---

## 4. HTML 결과 보기

pytest 후 브라우저에서 Green 요약:

```powershell
Start-Process ".\Report\green-test-results.html"
```

---

## 5. 트러블슈팅

| 증상 | 해결 |
|------|------|
| `pytest` 명령 없음 | `python -m pytest tests/ -v` |
| `ModuleNotFoundError: conversion` | 프로젝트 **루트**에서 실행 |
| 테스트 0개 | `pip install -r requirements-dev.txt` |

---

## 6. 관련 문서

| 문서 | 용도 |
|------|------|
| [PRD.md](./PRD.md) | 수용 기준 AT-1 … AT-5 |
| [../Report/green-test-results.html](../Report/green-test-results.html) | 브라우저용 테스트 요약 |
| [../Report/03-basic-green-report.md](../Report/03-basic-green-report.md) | Green 단계 Report |

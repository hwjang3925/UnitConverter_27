# 05 — Refactoring — Report

| Item | Value |
|------|-------|
| Step | 05 |
| Phase | Refactoring (OCP / SRP) |
| Branch | `refactoring` |
| Method | Dual-Track TDD #1 (Outside-In) |
| Date | 2026-06-11 |
| Status | **Complete** |

---

## 1. 목적

Green `conversion.py` 함수 묶음을 **SRP 클래스**로 분리하고 **UnitRegistry**로 **OCP** 확장점을 두되, **Golden Master·AT·unit 테스트 31건 Green** 유지.

---

## 2. Before / After

| | Green | Refactoring |
|--|-------|-------------|
| 구조 | `conversion.py` (단일 모듈, 함수) | `conversion/` 패키지 (4 클래스 + facade) |
| SRP | 다중 책임 한 파일 | Parser / Registry / Converter / Formatter |
| OCP | `if unit == …` | `UnitRegistry.register()` |

**다이어그램:** `doc/diagrams/as-is-class-diagram.md` → `doc/diagrams/to-be-class-diagram.md`

---

## 3. 클래스 책임 (SRP)

| Class | File | Responsibility |
|-------|------|----------------|
| `InputParser` | `input_parser.py` | `unit:value` 파싱·검증 |
| `UnitRegistry` | `unit_registry.py` | 단위 등록·meter 기준 변환 계수 |
| `Converter` | `converter.py` | `ConversionResult` 수치 변환 |
| `OutputFormatter` | `output_formatter.py` | 반올림·stdout 3줄 형식 |
| Facade | `__init__.py` | `run`, `parse_input`, `convert_to_all_units` (테스트 호환) |

---

## 4. OCP — 단위 확장

```python
registry = default_registry()
registry.register("inch", to_meter_divisor=39.37, from_meter_factor=39.37)
```

Converter / OutputFormatter / InputParser(known check)는 **기존 코드 수정 없이** Registry만 확장 가능 (step-04 동적 등록·파일 로드는 범위 외).

---

## 5. 호환성

| Consumer | 변경 |
|----------|------|
| `UnitConverter.py` | 없음 (`from conversion import run`) |
| `tests/unit/` | 없음 (`parse_input`, `convert_to_all_units`) |
| `tests/golden/` | master **변경 없음** — 31 Green |
| Golden Master | yard float: `value / METER_TO_YARD` 나눗셈 유지 (Green 동일 비트 패턴) |

---

## 6. pytest 결과

```text
python -m pytest tests/ -q
→ 31 passed (7 acceptance + 4 unit + 20 golden)
```

| Suite | Count | Status |
|-------|-------|--------|
| acceptance | 7 | Green |
| unit | 4 | Green |
| golden | 20 | Green |

---

## 7. 체크리스트

| Check | Status | Authority |
|-------|--------|-----------|
| InputParser / UnitRegistry / Converter / OutputFormatter 분리 | ✅ | AI |
| OCP Registry.register | ✅ | AI |
| step-04 extras 미구현 | ✅ | AI 제안 → 사람 확정 |
| Golden Master 미변경 | ✅ | AI |
| Report/05 + Transcript | ✅ | AI |

---

## 8. 파일 변경

| Action | Path |
|--------|------|
| 삭제 | `conversion.py` |
| 추가 | `conversion/__init__.py`, `input_parser.py`, `unit_registry.py`, `converter.py`, `output_formatter.py` |

---

## 9. 참고

- Transcript: `Prompting/05-refactoring-transcript.md`
- Green Report: `Report/03-basic-green-report.md`
- Golden Master: `doc/golden-master.md`

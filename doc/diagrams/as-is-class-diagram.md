# As-Is Architecture — Green Phase (Current Code)

| Item | Value |
|------|-------|
| Phase | Green (pre-refactoring) |
| Branch baseline | `green` / `refactoring` start |
| Date | 2026-06-11 |
| Code | `conversion.py`, `UnitConverter.py` |

현재 코드에는 **Python `class`가 없음**. 아래 다이어그램은 **논리적 책임**을 UML 클래스 형태로 표현한다.

---

## 1. Module overview

```mermaid
classDiagram
    direction TB

    class UnitConverter {
        +main()
        -input() stdin
        -print() stdout
    }

    class conversion_module {
        <<module / 함수 묶음>>
        +run(input_str) list~str~
        +parse_input(input_str) tuple
        +to_meters(value, unit) float
        +convert_to_all_units(value, unit) dict
        ---
        METER_TO_FEET : float
        METER_TO_YARD : float
        KNOWN_UNITS : set
    }

    class tests_acceptance {
        <<pytest>>
        +run_converter(stdin)
        subprocess → UnitConverter.py
    }

    class tests_unit {
        <<pytest>>
        import parse_input
        import convert_to_all_units
    }

    UnitConverter --> conversion_module : run()
    tests_acceptance --> UnitConverter : CLI subprocess
    tests_unit --> conversion_module : direct import
```

**해석:** `conversion.py` **한 모듈**이 파싱·단위·변환·출력·흐름을 모두 담당한다. CLI(`UnitConverter.py`)만 I/O로 분리되어 있다.

---

## 2. SRP problem — overlapping responsibilities in `conversion.py`

```mermaid
classDiagram
    direction LR

    class conversion_py {
        <<single module>>
    }

    class InputParsing {
        parse_input()
        format / number / negative / unit check
    }

    class UnitCatalog {
        KNOWN_UNITS
        METER_TO_FEET
        METER_TO_YARD
    }

    class Conversion {
        to_meters()
        meter → feet / yard math
    }

    class Formatting {
        round(x, 1)
        f-string lines
        display[] strings
    }

    class Orchestration {
        run()
    }

    conversion_py *-- InputParsing : same file
    conversion_py *-- UnitCatalog : same file
    conversion_py *-- Conversion : same file
    conversion_py *-- Formatting : same file
    conversion_py *-- Orchestration : same file

    note for conversion_py "SRP violation:\nmultiple reasons to change\n(input rules, units, math, output, flow)"
```

| 겹친 책임 | 코드 | 바뀌면 수정하는 이유 |
|-----------|------|----------------------|
| 입력 검증 | `parse_input()` | 오류 메시지, 음수 규칙 |
| 단위·비율 | `KNOWN_UNITS`, `METER_TO_*` | 새 단위 추가 |
| 변환 | `to_meters()`, `convert_to_all_units()` | 비율·알고리즘 |
| 출력 | `display`, `:.1f` | JSON/CSV, 자릿수 |
| 흐름 | `run()` | 파이프라인 변경 |

---

## 3. OCP problem — adding `inch` (extension vs modification)

```mermaid
flowchart TD
    A["새 단위 inch 추가 요구"] --> B["KNOWN_UNITS 수정"]
    A --> C["parse_input unit 검사"]
    A --> D["to_meters() elif 분기 추가"]
    A --> E["convert_to_all_units() 출력 구조"]
    A --> F["display 3줄 고정 로직"]

    B --> G["여러 함수·상수 동시 수정"]
    C --> G
    D --> G
    E --> G
    F --> G

    G --> H["OCP violation:\n확장인데 기존 코드를\n반복적으로 수정"]
```

**해당 코드 (`to_meters`):**

```python
if unit == "meter":
    return value
if unit == "feet":
    return value / METER_TO_FEET
if unit == "yard":
    return value / METER_TO_YARD
```

단위가 늘 때마다 **분기·상수·출력**을 함께 고칠 가능성이 크다.

---

## 4. Test coupling

```mermaid
classDiagram
    class conversion_module {
        parse_input()
        convert_to_all_units()
        run()
    }

    class test_validation {
        tests parse_input only
    }

    class test_rounding {
        tests convert_to_all_units only
    }

    class test_acceptance {
        tests full CLI only
    }

    test_validation --> conversion_module
    test_rounding --> conversion_module
    test_acceptance --> UnitConverter

    note for conversion_module "convert_to_all_units bundles\nconversion + rounding + formatting"
```

- Unit 테스트: **함수 일부**만 검증
- Acceptance: **CLI 전체**만 검증
- Registry / Formatter **단독 테스트 불가**

---

## 5. Summary — what works vs what to refactor

| 관점 | 현재 (Green) | 평가 |
|------|--------------|------|
| **기능** | AT-1~5, 11 tests Green | ✅ OK |
| **CLI SRP** | `UnitConverter.py` = I/O only | ✅ OK |
| **Domain SRP** | `conversion.py` = 다중 책임 | ⚠️ Refactor 대상 |
| **OCP** | `if/elif` + 하드코딩 상수 | ⚠️ Refactor 대상 |

**Next:** [to-be-class-diagram.md](./to-be-class-diagram.md)

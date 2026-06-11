# To-Be Architecture — Refactoring Target

| Item | Value |
|------|-------|
| Phase | Refactoring (05) |
| Goals | SRP, OCP (README 품질 요구) |
| Constraints | 11 tests Green, step-04 제외 |
| Related | `doc/PRD.md` §8, `.cursor/commands/phase-refactoring.md` |

---

## 1. Target class diagram

```mermaid
classDiagram
    direction TB

    class UnitConverter {
        +main()
    }

    class ConversionFacade {
        +run(input_str) list~str~
        parse_input() backward compat
        convert_to_all_units() backward compat
    }

    class InputParser {
        +parse(input_str) ParseResult
    }

    class UnitRegistry {
        +is_known(unit) bool
        +to_meters(value, unit) float
        +from_meters(meters, unit) float
        +units() list
        +register(name, meters_per_unit) void
    }

    class Converter {
        +convert(value, unit) ConversionResult
    }

    class OutputFormatter {
        +format_lines(value, unit, result) list~str~
    }

    UnitConverter --> ConversionFacade : run()
    ConversionFacade --> InputParser
    ConversionFacade --> Converter
    ConversionFacade --> OutputFormatter
    Converter --> UnitRegistry
    InputParser --> UnitRegistry : unit validation

    note for UnitRegistry "OCP:\ninch 추가 시 Registry만 확장\nConverter/Formatter 수정 최소"
    note for InputParser "SRP:\nparse + validate only"
    note for OutputFormatter "SRP:\ntext lines + 1 decimal only"
```

---

## 2. Request flow (sequence)

```mermaid
sequenceDiagram
    participant CLI as UnitConverter
    participant Run as ConversionFacade
    participant P as InputParser
    participant R as UnitRegistry
    participant C as Converter
    participant F as OutputFormatter

    CLI->>Run: run("meter:2.5")
    Run->>P: parse("meter:2.5")
    P->>R: is_known("meter")?
    R-->>P: true
    P-->>Run: unit, value, no error
    Run->>C: convert(2.5, "meter")
    C->>R: to_meters / from_meters
    R-->>C: meter, feet, yard values
    C-->>Run: ConversionResult
    Run->>F: format_lines(...)
    F-->>Run: 3 display lines
    Run-->>CLI: list[str]
```

**Error path:** `InputParser`가 오류 문자열 반환 → `run()`은 `[error]` 한 줄만 반환 (PRD §4).

---

## 3. OCP — adding `inch` (target behavior)

```mermaid
flowchart LR
    A["inch 추가"] --> B["UnitRegistry.register('inch', 0.0254)"]
    B --> C["InputParser: is_known → OK"]
    B --> D["Converter: generic math unchanged"]
    B --> E["OutputFormatter: loop known units\n(or fixed 3-unit policy)"]

    style B fill:#1a3a2a
    style D fill:#1a3a2a
```

**Scope note:** step-04(동적 런타임 등록, JSON/YAML)는 **제외**. To-Be Registry는 **코드/생성자에서 등록**으로 OCP를 **설명**한다.

---

## 4. SRP mapping — Green → To-Be

| Green (`conversion.py`) | To-Be class |
|-------------------------|-------------|
| `parse_input()` | `InputParser` |
| `KNOWN_UNITS`, `METER_TO_*` | `UnitRegistry` |
| `to_meters()`, 변환 계산 | `Converter` + `UnitRegistry` |
| `display`, `round`, `:.1f` | `OutputFormatter` |
| `run()` | `ConversionFacade` (or module-level facade) |

**Backward compatibility:** unit tests import `parse_input`, `convert_to_all_units` from `conversion` — facade가 위임 유지.

---

## 5. Out of scope (step-04)

| Not in refactoring | Reason |
|--------------------|--------|
| `config.json` / YAML load | README 추가 요구 — 제외 |
| User runtime `cubit` registration | 동적 등록 — 제외 |
| JSON / CSV output | 출력 포맷 선택 — 제외 |

Report/01 §7 다이어그램의 `config.json → UnitRegistry`는 **미래 확장** 그림이다.

---

## 6. Done criteria

- [ ] Classes/modules split per diagram
- [ ] `python -m pytest tests/` → **11 passed**
- [ ] `Report/05-refactoring-report.md` with Before/After reference to [as-is](./as-is-class-diagram.md)

**Before:** [as-is-class-diagram.md](./as-is-class-diagram.md)

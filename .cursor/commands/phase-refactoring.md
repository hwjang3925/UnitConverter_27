# Phase Refactoring — Structure improvement, tests stay Green

Current branch must be **`refactoring`**.

## Do

1. Confirm branch: `git branch --show-current` → `refactoring`
2. Refactor toward OCP/SRP: `InputParser`, `UnitRegistry`, `Converter`, `OutputFormatter`
3. Run `pytest` after **each** refactor step; all tests must stay Green
4. Remove duplication; keep behavior identical to spec
5. On phase complete: run export-artifacts workflow for step **05**

## Do not

- Change behavior without tests
- Delete or skip tests
- Add out-of-scope features (step 04 extras)

## Done when

- Clean module/class layout
- Full test suite Green
- `Report/05-refactoring-report.md` and transcript exported

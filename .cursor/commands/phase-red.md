# Phase Red — Acceptance tests only (Dual-Track outer loop)

Current branch must be **`red`**.

## Do

1. Confirm branch: `git branch --show-current` → `red`
2. Read scenarios in `Report/01-spec-requirements-analysis-report.md` §5 (AT-1 … AT-5, AT-1b)
3. Add pytest acceptance tests only (CLI/subprocess or thin public API)
4. Run tests; confirm they **fail for the intended reason** (outer Red)
5. On phase complete: run export-artifacts workflow for step **02**

## Do not

- Write production code to make tests pass
- Relax assertions to match starter `UnitConverter.py` gaps
- Implement README step-04 extras

## Done when

- All acceptance tests exist and fail correctly
- Tell user to create branch **`green`**

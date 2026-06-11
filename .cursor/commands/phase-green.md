# Phase Green — Inner RGR until acceptance tests pass

Current branch must be **`green`**.

## Do

1. Confirm branch: `git branch --show-current` → `green`
2. Pick one failing unit test (Red) → minimal code (Green) → Refactor
3. Repeat until acceptance tests AT-1 … AT-5, AT-1b are **Green**
4. Follow domain rules: 1 decimal rounding, zero allowed, error message strings
5. On phase complete: run export-artifacts workflow for step **03**

## Do not

- Change acceptance tests to hide bugs (unless spec was wrong)
- Add config files, dynamic registration, JSON/CSV output
- Merge to `main` without user request

## Done when

- `pytest` acceptance + unit tests pass
- Tell user to create branch **`refactoring`**

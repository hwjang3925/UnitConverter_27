---
name: acceptance-test-authoring
description: >-
  Write failing acceptance tests for Unit Converter on the red branch.
  Use on branch red, phase-red command, or when authoring AT-1 through AT-5 tests.
---

# Acceptance Test Authoring (red branch)

## Preconditions

- Branch: **`red`**
- Read `Report/01-spec-requirements-analysis-report.md` §3 and §5
- Framework: **pytest**

## Scenarios to implement

| ID | Input | Assert |
|----|-------|--------|
| AT-1 | `meter:2.5` | stdout contains `8.2 feet`, `2.7 yard` (1 decimal) |
| AT-1b | `meter:0` | stdout contains `0.0 feet`, `0.0 yard` |
| AT-2 | `meter2.5` | `Invalid format. Use unit:value (ex: meter:2.5)` |
| AT-3 | `meter:abc` | `Invalid number: abc` |
| AT-4 | `meter:-1` | `Invalid number: -1` |
| AT-5 | `mile:1` | `Unknown unit: mile` |

## Suggested layout

```
tests/
  acceptance/
    test_cli_conversion.py
    test_cli_validation.py
```

## CLI test pattern

```python
import subprocess
import sys

def run_converter(stdin: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "UnitConverter.py"],
        input=stdin,
        text=True,
        capture_output=True,
        cwd=project_root,
    )
```

Use `pytest.mark.parametrize` for multiple inputs.

## Red phase rules

1. Write tests **before** fixing `UnitConverter.py`
2. Run `pytest tests/acceptance/` — expect failures
3. Verify failure reason matches missing behavior (not typos in tests)
4. Do **not** add implementation in `red` branch

## After all tests fail correctly

Notify user: create **`green`** branch and begin inner RGR.

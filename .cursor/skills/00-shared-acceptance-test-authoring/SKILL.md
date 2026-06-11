---
name: 00-shared-acceptance-test-authoring
description: >-
  Write failing acceptance tests on red branch. Use with 02-phase-red for
  AT-1 through AT-5 scenarios.
---

# Acceptance Test Authoring (02 red)

Primary branch: **`red`**. Read spec Report §3 and §5 first.

## Scenarios

| ID | Input | Assert |
|----|-------|--------|
| AT-1 | `meter:2.5` | `8.2 feet`, `2.7 yard` |
| AT-1b | `meter:0` | `0.0 feet`, `0.0 yard` |
| AT-2 | `meter2.5` | format error |
| AT-3 | `meter:abc` | `Invalid number: abc` |
| AT-4 | `meter:-1` | `Invalid number: -1` |
| AT-5 | `mile:1` | `Unknown unit: mile` |

## Red rules

1. Tests before fixing `UnitConverter.py`
2. `pytest tests/acceptance/` — expect intended failures
3. No production implementation on `red`

## Layout

```
tests/acceptance/test_cli_conversion.py
tests/acceptance/test_cli_validation.py
tests/conftest.py
```

When done, tell user to create **`green`** branch.

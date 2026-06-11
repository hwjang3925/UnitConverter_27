# 01 — Spec — Gate

Branch must be **`spec`**.

## Entry criteria

- README and starter code reviewed (`Report/01` gap analysis exists).

## Required before leaving spec

- [x] Mom Test Q&A with **Speaker / Authority** columns (§11)
- [ ] Rounding: 1 decimal on converted feet/yard output
- [ ] Zero allowed; negative rejected
- [ ] Error messages match starter strings
- [ ] AT-1 … AT-5, AT-1b scenarios documented

## Exit criteria

- Mom Test section committed on `spec`
- User told: `git checkout red` (or `git checkout -b red` if first time)

## Blocked actions on spec

- Committing `tests/` as spec deliverable (belongs on `red`)
- Implementing rounding/negative fixes in `UnitConverter.py` (belongs on `green`)

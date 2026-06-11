---
name: 01-spec-mom-test
description: >-
  Run Mom Test requirements validation on spec branch. Use with 01-spec-mom-test
  command, Mom Test questions, or before moving from spec to red.
---

# 01 Spec — Mom Test Skill

Branch: **`spec`**. User owns PASS/FAIL decisions.

## Step 1 — Problem questions (user answers)

| ID | Question |
|----|----------|
| Q1 | What pain does the user have when converting length units without this tool? |
| Q2 | What problem does README output (`8.2 feet`, `2.7 yard`) solve vs raw floats? |
| Q3 | What breaks today in starter code (rounding, negative, etc.)? |

## Step 2 — Requirement validation (PASS/FAIL)

| ID | Validation question | Maps to |
|----|---------------------|---------|
| V1 | Without 1-decimal rounding, output mismatches README? | AT-1 |
| V2 | Blocking `meter:0` blocks valid use? | AT-1b |
| V3 | Converting `meter:-1` hides input error? | AT-4 |
| V4 | Changing error strings breaks assignment consistency? | AT-2 … AT-5 |
| V5 | Basic + quality reqs doable without step-04 extras? | scope |

## Step 3 — Record

Add **§ Mom Test** to `Report/01-spec-requirements-analysis-report.md` or create `Report/01-spec-mom-test-report.md` with:

- Questions, answers, PASS/FAIL
- Link each PASS to AT-ID
- Confirmed rules: round 1 decimal, zero OK, negative reject, error strings

## Step 4 — Gate check

Use `.cursor/harness/01-spec-gate.md` checklist.

When complete:

1. Export/update step 01 artifacts if needed
2. Tell user: commit on `spec`, then `git checkout red`

## Forbidden

- Writing `tests/` or modifying `UnitConverter.py` for green behavior

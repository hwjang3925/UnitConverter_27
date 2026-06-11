# 01 — Spec — Mom Test

Branch must be **`spec`**.

## Do

1. Confirm branch: `git branch --show-current` → `spec`
2. Run Mom Test skill: `.cursor/skills/01-spec-mom-test/SKILL.md`
3. User answers Q1–Q3; user marks V1–V5 PASS/FAIL
4. Record results in Report (§ Mom Test or `Report/01-spec-mom-test-report.md`)
5. Verify `.cursor/harness/01-spec-gate.md` checklist
6. On complete: `00-export-artifacts` for step 01 if transcript/report updated

## Do not

- Write acceptance tests (`tests/`) — step 02 `red`
- Fix `UnitConverter.py` — step 03 `green`

## Done when

- Mom Test documented with PASS/FAIL
- User commits on `spec`
- Tell user: `git checkout red` (or `-b red` if new)

Use agent: **01-spec-requirements-analyst**

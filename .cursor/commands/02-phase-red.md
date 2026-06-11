# 02 — Red — Acceptance tests only

Branch must be **`red`**.

1. Confirm branch → `red`
2. Read `Report/01-spec-requirements-analysis-report.md` §5
3. Add pytest acceptance tests only (skill `00-shared-acceptance-test-authoring`)
4. Run pytest; confirm **intended** failures (AT-1, AT-4 typically)
5. Export step 02 via `00-export-artifacts`

Do **not** modify `UnitConverter.py` to pass tests.

Done → tell user: `git checkout -b green`

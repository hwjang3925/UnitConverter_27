---
name: 00-shared-phase-coordinator
description: >-
  Unit Converter Dual-Track TDD phase coordinator. Use when checking branch,
  phase transitions, or which .cursor artifact applies. Verifies spec→red→green→refactoring flow.
---

You coordinate the Unit Converter lab workflow.

1. Run `git branch --show-current` and match work to branch rules in `.cursor/rules/00-shared-dual-track-tdd-branches.mdc`.
2. Never merge to `main` unless the user explicitly requests it.
3. Tell the user when to create the next branch; do not create branches yourself unless asked.
4. On phase completion, remind user to export Report/Prompting (skill `00-shared-export-phase-artifacts`).
5. Step 04 (README extras) is excluded from scope.

Reference: `.cursor/00-index.md`, `.cursor/harness/00-shared-workflow.md`.

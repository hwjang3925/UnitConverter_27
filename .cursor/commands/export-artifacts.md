# Export phase Report and Transcript

Export artifacts for the **current completed phase**.

## Steps

1. Identify step number and slug from branch:

   | Branch | Step | slug |
   |--------|------|------|
   | `spec` | 01 | `spec-requirements-analysis` |
   | `red` | 02 | `acceptance-red` |
   | `green` | 03 | `basic-green` |
   | `refactoring` | 05 | `refactoring` |

2. Create or update:
   - `Report/{NN}-{slug}-report.md`
   - `Prompting/{NN}-{slug}-transcript.md`

3. Update `Report/00-index.md` and `Prompting/00-index.md`

4. Export transcript from Cursor agent-transcripts (JSONL → markdown, Turn User/Assistant)

Use the **export-phase-artifacts** skill for full checklist and templates.

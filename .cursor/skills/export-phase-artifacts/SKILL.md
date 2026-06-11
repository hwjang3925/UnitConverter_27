---
name: export-phase-artifacts
description: >-
  Export Unit Converter phase Report and Prompting transcript with consistent
  numbering. Use when a phase completes, user runs export-artifacts, or asks
  for Report/Prompting files.
---

# Export Phase Artifacts

## Numbering

| Step | Branch | phase-slug | Report | Transcript |
|------|--------|------------|--------|------------|
| 01 | `spec` | `spec-requirements-analysis` | `01-spec-requirements-analysis-report.md` | `01-spec-requirements-analysis-transcript.md` |
| 02 | `red` | `acceptance-red` | `02-acceptance-red-report.md` | `02-acceptance-red-transcript.md` |
| 03 | `green` | `basic-green` | `03-basic-green-report.md` | `03-basic-green-transcript.md` |
| 05 | `refactoring` | `refactoring` | `05-refactoring-report.md` | `05-refactoring-transcript.md` |

Skip step **04** (no files).

## Report workflow

1. Create `Report/{NN}-{slug}-report.md` using template in `.cursor/rules/report-prompting-format.mdc`
2. Sections: purpose, branch, work done, test results, checklist, next step, AI usage summary
3. Set `Status: Complete` when phase is done
4. Update `Report/00-index.md` row for that step

## Transcript workflow

1. Locate JSONL under Cursor agent-transcripts for this project
2. Export to `Prompting/{NN}-{slug}-transcript.md`
3. Format: header table + `## Turn N — User` / `## Turn N — Assistant`
4. Strip `<user_query>` tags and `[REDACTED]` tool noise where possible
5. Update `Prompting/00-index.md`

## Python export snippet (optional)

```python
import json, re
from pathlib import Path

def export_transcript(jsonl_path: Path, out_path: Path, header: str):
    lines = []
    turn = 0
    for raw in jsonl_path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        obj = json.loads(raw)
        if obj.get("type") == "turn_ended":
            continue
        role = obj.get("role")
        texts = []
        for block in obj.get("message", {}).get("content", []):
            if block.get("type") == "text":
                t = re.sub(r"</?user_query>", "", block.get("text", ""))
                t = t.replace("[REDACTED]", "").strip()
                if t:
                    texts.append(t)
        if not texts:
            continue
        body = "\n\n".join(texts)
        if role == "user":
            turn += 1
            lines.append(f"## Turn {turn} — User\n\n{body}\n")
        elif role == "assistant":
            lines.append(f"## Turn {turn} — Assistant\n\n{body}\n")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(header + "\n---\n\n".join(lines), encoding="utf-8")
```

## After export

Tell user which files were created and the next branch if the phase is complete.

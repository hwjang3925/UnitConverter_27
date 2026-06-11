import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLI_PROMPT = "Insert value for converting (ex: meter:2.5): "


def run_converter(stdin: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "UnitConverter.py")],
        input=stdin,
        text=True,
        capture_output=True,
        cwd=PROJECT_ROOT,
    )


def normalize_cli_stdout(stdout: str) -> list[str]:
    """Strip CLI prompt; return output lines for Golden Master comparison."""
    text = stdout.replace("\r\n", "\n")
    if text.startswith(CLI_PROMPT):
        text = text[len(CLI_PROMPT) :]
    return text.strip().split("\n")

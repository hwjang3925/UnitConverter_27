import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_converter(stdin: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "UnitConverter.py")],
        input=stdin,
        text=True,
        capture_output=True,
        cwd=PROJECT_ROOT,
    )

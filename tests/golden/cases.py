"""Golden Master case registry — Green phase baseline (conversion.run output)."""

from pathlib import Path

MASTERS_DIR = Path(__file__).parent / "masters"

# AT coverage (required) + extended cases (feet/yard input, Mom Test Q5)
GOLDEN_CASES = [
    {"id": "AT-1", "input": "meter:2.5", "master": "meter_2_5.txt"},
    {"id": "AT-1b", "input": "meter:0", "master": "meter_0.txt"},
    {"id": "AT-2", "input": "meter2.5", "master": "meter2_5_error.txt"},
    {"id": "AT-3", "input": "meter:abc", "master": "meter_abc_error.txt"},
    {"id": "AT-4", "input": "meter:-1", "master": "meter_neg1_error.txt"},
    {"id": "AT-5", "input": "mile:1", "master": "mile_1_error.txt"},
    {"id": "EXT-feet", "input": "feet:10", "master": "feet_10.txt"},
    {"id": "EXT-yard", "input": "yard:5", "master": "yard_5.txt"},
    {"id": "EXT-0.02", "input": "meter:0.02", "master": "meter_0_02.txt"},
    {"id": "EXT-meter1", "input": "meter:1", "master": "meter_1.txt"},
]

CLI_PROMPT = "Insert value for converting (ex: meter:2.5): "


def load_master(filename: str) -> list[str]:
    path = MASTERS_DIR / filename
    return path.read_text(encoding="utf-8").strip().splitlines()

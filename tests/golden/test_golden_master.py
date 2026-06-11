"""Golden Master tests — full output snapshot vs Green baseline.

API: conversion.run() lines match masters/.
CLI: UnitConverter.py stdout (prompt stripped) matches same masters.
"""

import pytest

from conversion import run
from tests.conftest import normalize_cli_stdout, run_converter
from tests.golden.cases import GOLDEN_CASES, load_master


@pytest.mark.parametrize("case", GOLDEN_CASES, ids=[c["id"] for c in GOLDEN_CASES])
def test_golden_api_matches_master(case):
    expected = load_master(case["master"])
    assert run(case["input"]) == expected


@pytest.mark.parametrize("case", GOLDEN_CASES, ids=[f"cli-{c['id']}" for c in GOLDEN_CASES])
def test_golden_cli_matches_master(case):
    expected = load_master(case["master"])
    result = run_converter(case["input"] + "\n")
    assert result.returncode == 0
    assert normalize_cli_stdout(result.stdout) == expected

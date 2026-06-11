"""Acceptance tests: AT-1, AT-1b — conversion output."""

from tests.conftest import run_converter


class TestConversionOutput:
    """AT-1: meter:2.5 → rounded 1-decimal output for all units."""

    def test_at1_meter_input_shows_rounded_feet_and_yard(self):
        result = run_converter("meter:2.5\n")

        assert result.returncode == 0
        assert "8.2 feet" in result.stdout
        assert "2.7 yard" in result.stdout

    def test_at1_meter_input_shows_meter_line(self):
        result = run_converter("meter:2.5\n")

        assert "2.5 meter = 2.5 meter" in result.stdout


class TestZeroAllowed:
    """AT-1b: meter:0 is valid and shows zero conversions with 1 decimal."""

    def test_at1b_zero_input_shows_zero_conversions(self):
        result = run_converter("meter:0\n")

        assert result.returncode == 0
        assert "0.0 feet" in result.stdout
        assert "0.0 yard" in result.stdout

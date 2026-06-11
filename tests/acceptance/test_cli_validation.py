"""Acceptance tests: AT-2 … AT-5 — input validation."""

from tests.conftest import run_converter

class TestInvalidFormat:
    """AT-2: missing colon."""

    def test_at2_missing_colon_shows_format_error(self):
        result = run_converter("meter2.5\n")

        assert "Invalid format. Use unit:value (ex: meter:2.5)" in result.stdout


class TestInvalidNumber:
    """AT-3: non-numeric value."""

    def test_at3_non_numeric_value_shows_number_error(self):
        result = run_converter("meter:abc\n")

        assert "Invalid number: abc" in result.stdout


class TestNegativeValue:
    """AT-4: negative values rejected."""

    def test_at4_negative_value_shows_number_error(self):
        result = run_converter("meter:-1\n")

        assert "Invalid number: -1" in result.stdout


class TestUnknownUnit:
    """AT-5: unregistered unit."""

    def test_at5_unknown_unit_shows_unit_error(self):
        result = run_converter("mile:1\n")

        assert "Unknown unit: mile" in result.stdout

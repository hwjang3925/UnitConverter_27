"""Unit tests: UT-11 — one decimal place on converted output."""

from conversion import convert_to_all_units


def test_meter_to_feet_and_yard_rounded():
    result = convert_to_all_units(2.5, "meter")
    assert "8.2 feet" in result["display"][1]
    assert "2.7 yard" in result["display"][2]


def test_zero_conversions_show_one_decimal():
    result = convert_to_all_units(0, "meter")
    assert "0.0 feet" in result["display"][1]
    assert "0.0 yard" in result["display"][2]

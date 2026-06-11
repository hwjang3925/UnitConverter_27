"""Unit tests: UT-8 — negative input rejected."""

from conversion import parse_input


def test_parse_input_negative_rejected():
    unit, value, error = parse_input("meter:-1")
    assert unit is None
    assert value is None
    assert error == "Invalid number: -1"


def test_parse_input_zero_allowed():
    unit, value, error = parse_input("meter:0")
    assert error is None
    assert unit == "meter"
    assert value == 0.0

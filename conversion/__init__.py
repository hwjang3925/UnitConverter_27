"""Unit conversion facade — backward-compatible API for tests and CLI."""

from conversion.converter import ConversionResult, Converter
from conversion.input_parser import InputParser
from conversion.output_formatter import OutputFormatter
from conversion.unit_registry import (
    METER_TO_FEET,
    METER_TO_YARD,
    UnitRegistry,
    default_registry,
)

_registry = default_registry()
_parser = InputParser(_registry)
_converter = Converter(_registry)
_formatter = OutputFormatter()

KNOWN_UNITS = _registry.known_units()


def parse_input(input_str: str) -> tuple[str | None, float | None, str | None]:
    return _parser.parse(input_str)


def to_meters(value: float, unit: str) -> float:
    return _registry.to_meters(value, unit)


def convert_to_all_units(value: float, unit: str) -> dict:
    result = _converter.convert(value, unit)
    return _formatter.format_result(result)


def run(input_str: str) -> list[str]:
    unit, value, error = _parser.parse(input_str)
    if error:
        return [error]
    result = _converter.convert(value, unit)
    return _formatter.format_lines(result)


__all__ = [
    "ConversionResult",
    "Converter",
    "InputParser",
    "KNOWN_UNITS",
    "METER_TO_FEET",
    "METER_TO_YARD",
    "OutputFormatter",
    "UnitRegistry",
    "convert_to_all_units",
    "default_registry",
    "parse_input",
    "run",
    "to_meters",
]

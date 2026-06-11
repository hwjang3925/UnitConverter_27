"""Meter-base conversion math."""

from dataclasses import dataclass

from conversion.unit_registry import UnitRegistry


@dataclass(frozen=True)
class ConversionResult:
    value: float
    unit: str
    meter: float
    feet: float
    yard: float


class Converter:
    def __init__(self, registry: UnitRegistry) -> None:
        self._registry = registry

    def convert(self, value: float, unit: str) -> ConversionResult:
        meter_value = self._registry.to_meters(value, unit)
        return ConversionResult(
            value=value,
            unit=unit,
            meter=meter_value,
            feet=self._registry.from_meters(meter_value, "feet"),
            yard=self._registry.from_meters(meter_value, "yard"),
        )

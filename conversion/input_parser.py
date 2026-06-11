"""Parse and validate unit:value input."""

from conversion.unit_registry import UnitRegistry


class InputParser:
    def __init__(self, registry: UnitRegistry) -> None:
        self._registry = registry

    def parse(self, input_str: str) -> tuple[str | None, float | None, str | None]:
        """Return (unit, value, error_message). error_message set on validation failure."""
        if ":" not in input_str:
            return None, None, "Invalid format. Use unit:value (ex: meter:2.5)"

        unit, value_str = input_str.split(":", 1)

        try:
            value = float(value_str)
        except ValueError:
            return None, None, f"Invalid number: {value_str}"

        if value < 0:
            return None, None, f"Invalid number: {value_str}"

        if not self._registry.is_known(unit):
            return None, None, f"Unknown unit: {unit}"

        return unit, value, None

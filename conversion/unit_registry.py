"""Unit ratios and registration — OCP extension point."""

METER_TO_FEET = 3.28084
METER_TO_YARD = 1.09361


class UnitRegistry:
    """Stores per-unit divisors/factors for meter-base conversion.

    to_meters:   value / to_meter_divisor
    from_meters: meters * from_meter_factor

    Uses division for to_meters to match Green-phase float behavior (Golden Master).
    """

    def __init__(self) -> None:
        self._to_meter_divisor: dict[str, float] = {}
        self._from_meter_factor: dict[str, float] = {}

    def register(
        self,
        name: str,
        *,
        to_meter_divisor: float,
        from_meter_factor: float,
    ) -> None:
        self._to_meter_divisor[name] = to_meter_divisor
        self._from_meter_factor[name] = from_meter_factor

    def is_known(self, unit: str) -> bool:
        return unit in self._to_meter_divisor

    def known_units(self) -> frozenset[str]:
        return frozenset(self._to_meter_divisor)

    def to_meters(self, value: float, unit: str) -> float:
        if unit not in self._to_meter_divisor:
            raise ValueError(f"Unknown unit: {unit}")
        return value / self._to_meter_divisor[unit]

    def from_meters(self, meters: float, unit: str) -> float:
        if unit not in self._from_meter_factor:
            raise ValueError(f"Unknown unit: {unit}")
        return meters * self._from_meter_factor[unit]


def default_registry() -> UnitRegistry:
    registry = UnitRegistry()
    registry.register("meter", to_meter_divisor=1.0, from_meter_factor=1.0)
    registry.register(
        "feet", to_meter_divisor=METER_TO_FEET, from_meter_factor=METER_TO_FEET
    )
    registry.register(
        "yard", to_meter_divisor=METER_TO_YARD, from_meter_factor=METER_TO_YARD
    )
    return registry

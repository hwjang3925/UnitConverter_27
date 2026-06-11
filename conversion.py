METER_TO_FEET = 3.28084
METER_TO_YARD = 1.09361

KNOWN_UNITS = {"meter", "feet", "yard"}


def parse_input(input_str: str) -> tuple[str | None, float | None, str | None]:
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

    if unit not in KNOWN_UNITS:
        return None, None, f"Unknown unit: {unit}"

    return unit, value, None


def to_meters(value: float, unit: str) -> float:
    if unit == "meter":
        return value
    if unit == "feet":
        return value / METER_TO_FEET
    if unit == "yard":
        return value / METER_TO_YARD
    raise ValueError(f"Unknown unit: {unit}")


def convert_to_all_units(value: float, unit: str) -> dict:
    meter_value = to_meters(value, unit)
    in_feet = round(meter_value * METER_TO_FEET, 1)
    in_yards = round(meter_value * METER_TO_YARD, 1)

    display = [
        f"{value} {unit} = {meter_value} meter",
        f"{value} {unit} = {in_feet:.1f} feet",
        f"{value} {unit} = {in_yards:.1f} yard",
    ]
    return {
        "meter": meter_value,
        "feet": in_feet,
        "yard": in_yards,
        "display": display,
    }


def run(input_str: str) -> list[str]:
    unit, value, error = parse_input(input_str)
    if error:
        return [error]
    return convert_to_all_units(value, unit)["display"]

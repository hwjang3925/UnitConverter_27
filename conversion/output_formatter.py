"""Format conversion results for stdout."""

from conversion.converter import ConversionResult


class OutputFormatter:
    def format_result(self, result: ConversionResult) -> dict:
        in_feet = round(result.feet, 1)
        in_yards = round(result.yard, 1)

        display = [
            f"{result.value} {result.unit} = {result.meter} meter",
            f"{result.value} {result.unit} = {in_feet:.1f} feet",
            f"{result.value} {result.unit} = {in_yards:.1f} yard",
        ]
        return {
            "meter": result.meter,
            "feet": in_feet,
            "yard": in_yards,
            "display": display,
        }

    def format_lines(self, result: ConversionResult) -> list[str]:
        return self.format_result(result)["display"]

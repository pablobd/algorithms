from typing import List


class Item:
    def __init__(self, value: float, weight: int) -> None:
        self.value: float
        self.weight: int
        self.fractional_value: float = value / weight

    def __gt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.fractional_value > other.fractional_value

    def __ge__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.fractional_value >= other.fractional_value

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.fractional_value < other.fractional_value

    def __le__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.fractional_value <= other.fractional_value

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.fractional_value == other.fractional_value

    def _is_valid_operand(self, other):
        return hasattr(other, "fractional_value")


def sort_items(items: List[Item]) -> List[Item]:
    return sorted(items, reverse=True)

from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    value: float
    weight: int

    @property
    def fractional_value(self):
        return self.value / self.weight

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

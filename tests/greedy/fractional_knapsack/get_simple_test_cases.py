from typing import List, Sequence, Tuple

from solutions.greedy.fractional_knapsack import Item


def get_simple_cases() -> Sequence[Tuple[int, int, List[Item], float]]:
    cases = []
    items = [
        Item(value=60, weight=20),
        Item(value=100, weight=50),
        Item(value=120, weight=30),
    ]
    cases.append((3, 50, items, 180.0))

    items = [Item(value=500, weight=30)]
    cases.append((1, 10, items, 166.6667))

    items = [
        Item(value=60, weight=10),
        Item(value=100, weight=20),
        Item(value=120, weight=30),
    ]
    cases.append((3, 50, items, 240.0))

    items = [Item(value=60, weight=10), Item(value=100, weight=20)]
    cases.append((2, 50, items, 160.0))

    return cases

from typing import List, Tuple

import pytest

from solutions.greedy import fractional_knapsack
from solutions.greedy.fractional_knapsack import Item
from tests.greedy.fractional_knapsack.get_simple_test_cases import get_simple_test_cases


@pytest.mark.parametrize("input_fractional_knapsack", get_simple_test_cases())
def test_brute_force_solution_simple_cases(
    input_fractional_knapsack: Tuple[int, int, List[Item], float]
):
    total_items, capacity, items, solution = input_fractional_knapsack
    output = fractional_knapsack.brute_force_solution((total_items, capacity, items))
    assert abs(output - solution) <= 1e-3

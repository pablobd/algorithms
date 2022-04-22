import copy
import random
from typing import List, Tuple

import pytest

from solutions.greedy import fractional_knapsack
from solutions.greedy.fractional_knapsack import Item
from tests.greedy.fractional_knapsack.get_simple_cases import get_simple_cases
from tests.greedy.fractional_knapsack.stress_tests_params import StressTestsParams
from tests.performance_measures import PerformanceMeasures
from tests.read_config import get_names, read_config

""" Performance tests show that the efficient solution is a 1000 times faster when
there are at least 3 items with weights between 10 and 20.
"""


#
# simple cases tests
#


@pytest.mark.parametrize("input_fractional_knapsack", get_simple_cases())
def test_efficient_solution_simple_cases(
    input_fractional_knapsack: Tuple[int, int, List[Item], float]
):
    total_items, capacity, items, solution = input_fractional_knapsack
    output = fractional_knapsack.efficient_solution((total_items, capacity, items))
    assert abs(output - solution) <= 1e-3


#
# get test parameters
#


names = ["fractional_knapsack", "stress_tests"]
small_tests_params = read_config(StressTestsParams, get_names(names, "small_tests"))
big_tests_params = read_config(StressTestsParams, get_names(names, "big_tests"))
performance_params = read_config(StressTestsParams, get_names(names, "performance"))

#
# parametrize test inputs
#


def sample_input_fractional_knapsack(
    params: StressTestsParams,
) -> List[Tuple[int, int, List[Item]]]:
    random.seed(params.seed)
    test_cases = []
    for _ in range(params.test_iterations):
        total_items = random.randint(params.min_num_items, params.max_num_items)
        capacity = random.randint(params.min_capacity, params.max_capacity)
        items = []
        for _ in range(total_items):
            weight = random.randint(params.min_weight, params.max_weight)
            value = random.randint(params.min_value, params.max_value)
            items.append(Item(weight, value))
        test_cases.append((total_items, capacity, items))
    return test_cases


#
# stress tests
#


@pytest.mark.parametrize(
    "input_fractional_knapsack", sample_input_fractional_knapsack(small_tests_params)
)
def test_stress_tests_efficient_solution_small_stress(input_fractional_knapsack):
    input_fractional_knapsack_copy = copy.deepcopy(input_fractional_knapsack)
    brute_force = fractional_knapsack.brute_force_solution(
        input_fractional_knapsack_copy
    )
    efficient = fractional_knapsack.efficient_solution(input_fractional_knapsack)
    assert abs(brute_force - efficient) <= 1e-3


@pytest.mark.parametrize(
    "input_fractional_knapsack",
    sample_input_fractional_knapsack(big_tests_params),
)
def test_stress_tests_efficient_solution_big_stress(input_fractional_knapsack):
    input_fractional_knapsack_copy = copy.deepcopy(input_fractional_knapsack)
    efficient = fractional_knapsack.efficient_solution(input_fractional_knapsack)
    brute_force = fractional_knapsack.brute_force_solution(
        input_fractional_knapsack_copy
    )
    assert abs(brute_force - efficient) <= 1e-3


#
# performance tests
#


@pytest.mark.parametrize(
    "input_fractional_knapsack", sample_input_fractional_knapsack(performance_params)
)
def test_performance(input_fractional_knapsack) -> None:
    config_names = ["fractional_knapsack", "performance_tests"]
    performance_measures = read_config(PerformanceMeasures, config_names)
    input_fractional_knapsack_copy = copy.deepcopy(input_fractional_knapsack)
    brute_force_time = performance_measures.measure_performance(
        fractional_knapsack.brute_force_solution,
        input_fractional_knapsack_copy,
    )
    efficient_time = performance_measures.measure_performance(
        fractional_knapsack.efficient_solution,
        input_fractional_knapsack,
    )
    times_faster = performance_measures.times_faster_efficient_to_brute_force

    assert times_faster * efficient_time < brute_force_time

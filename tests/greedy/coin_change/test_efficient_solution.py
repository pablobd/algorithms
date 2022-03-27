import random
from typing import List

import pytest

from solutions.greedy import coin_change
from tests.greedy.coin_change.stress_tests_params import StressTestsParams
from tests.performance_measures import PerformanceMeasures
from tests.read_config import get_names, read_config

""" Performance tests show that the efficient solution is a 100000 times faster for
two numbers between 45 and 50.
"""

#
# simple cases tests
#


def test_efficient_solution_simple_cases():
    assert coin_change.efficient_solution(0) == 0
    assert coin_change.efficient_solution(1) == 1
    assert coin_change.efficient_solution(2) == 2
    assert coin_change.efficient_solution(3) == 3
    assert coin_change.efficient_solution(4) == 4
    assert coin_change.efficient_solution(5) == 1
    assert coin_change.efficient_solution(6) == 2
    assert coin_change.efficient_solution(7) == 3
    assert coin_change.efficient_solution(10) == 1
    assert coin_change.efficient_solution(11) == 2
    assert coin_change.efficient_solution(12) == 3
    assert coin_change.efficient_solution(15) == 2
    assert coin_change.efficient_solution(25) == 3


#
# get test parameters
#


names = ["coin_change", "stress_tests"]
small_tests_params = read_config(StressTestsParams, get_names(names, "small_tests"))
big_tests_params = read_config(StressTestsParams, get_names(names, "big_tests"))
performance_params = read_config(StressTestsParams, get_names(names, "performance"))

#
# parametrize test inputs
#


def sample_input_coin_change(params: StressTestsParams) -> List[int]:
    random.seed(params.seed)
    test_cases = []
    min_number = params.min_number
    max_number = params.max_number
    for _ in range(params.test_iterations):
        coin_change = random.randint(min_number, max_number)
        test_cases.append(coin_change)
    return test_cases


#
# stress tests
#


@pytest.mark.parametrize(
    "input_coin_change", sample_input_coin_change(small_tests_params)
)
def test_stress_tests_efficient_solution_small_stress(input_coin_change):
    brute_force = coin_change.brute_force_solution(input_coin_change)
    efficient = coin_change.efficient_solution(input_coin_change)
    assert brute_force == efficient


@pytest.mark.parametrize(
    "input_coin_change", sample_input_coin_change(big_tests_params)
)
def test_stress_tests_efficient_solution_big_stress(input_coin_change):
    efficient = coin_change.efficient_solution(input_coin_change)
    brute_force = coin_change.brute_force_solution(input_coin_change)
    assert brute_force == efficient


#
# performance tests
#


@pytest.mark.parametrize(
    "input_coin_change", sample_input_coin_change(performance_params)
)
def test_performance(input_coin_change) -> None:
    config_names = ["coin_change", "performance_tests"]
    performance_measures = read_config(PerformanceMeasures, config_names)
    efficient_time = performance_measures.measure_performance(
        coin_change.efficient_solution,
        input_coin_change,
    )
    brute_force_time = performance_measures.measure_performance(
        coin_change.brute_force_solution,
        input_coin_change,
    )
    times_faster = performance_measures.times_faster_efficient_to_brute_force
    assert times_faster * efficient_time < brute_force_time

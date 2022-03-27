import random
from typing import List, Tuple

import pytest

from solutions.mathematical import partial_sum_fibonacci_last_digit
from tests.mathematical.partial_sum_fibonacci_last_digit import StressTestsParams
from tests.performance_measures import PerformanceMeasures
from tests.read_config import get_names, read_config

""" Performance tests show that the efficient solution is a 1000 times faster for
two numbers between 40000 and 40020.
"""


def test_efficient_solution():
    assert 0 == partial_sum_fibonacci_last_digit.efficient_solution((0, 0))
    assert 1 == partial_sum_fibonacci_last_digit.efficient_solution((0, 1))
    assert 2 == partial_sum_fibonacci_last_digit.efficient_solution((1, 2))
    assert 4 == partial_sum_fibonacci_last_digit.efficient_solution((0, 3))
    assert 3 == partial_sum_fibonacci_last_digit.efficient_solution((2, 3))
    assert 7 == partial_sum_fibonacci_last_digit.efficient_solution((0, 4))
    assert 5 == partial_sum_fibonacci_last_digit.efficient_solution((3, 4))
    assert 2 == partial_sum_fibonacci_last_digit.efficient_solution((0, 5))
    assert 8 == partial_sum_fibonacci_last_digit.efficient_solution((4, 5))
    assert 0 == partial_sum_fibonacci_last_digit.efficient_solution((0, 6))
    assert 6 == partial_sum_fibonacci_last_digit.efficient_solution((4, 6))
    assert 3 == partial_sum_fibonacci_last_digit.efficient_solution((0, 7))
    assert 6 == partial_sum_fibonacci_last_digit.efficient_solution((5, 7))
    assert 4 == partial_sum_fibonacci_last_digit.efficient_solution((0, 8))
    assert 0 == partial_sum_fibonacci_last_digit.efficient_solution((4, 8))
    assert 8 == partial_sum_fibonacci_last_digit.efficient_solution((0, 9))
    assert 6 == partial_sum_fibonacci_last_digit.efficient_solution((6, 9))
    assert 5 == partial_sum_fibonacci_last_digit.efficient_solution((10, 10))
    assert 5 == partial_sum_fibonacci_last_digit.efficient_solution((0, 100))
    assert 2 == partial_sum_fibonacci_last_digit.efficient_solution((10, 200))


#
# get test parameters
#


names = ["partial_sum_fibonacci_last_digit", "stress_tests"]
small_tests_params = read_config(StressTestsParams, get_names(names, "small_tests"))
big_tests_params = read_config(StressTestsParams, get_names(names, "big_tests"))
performance_params = read_config(StressTestsParams, get_names(names, "performance"))

#
# parametrize test inputs
#


def sample_input_fibonacci(params: StressTestsParams) -> List[Tuple[int, int]]:
    random.seed(params.seed)
    test_cases = []
    high_min_fibonacci = params.high_min_fibonacci_number
    high_max_fibonacci = params.high_max_fibonacci_number
    low_min_fibonacci = params.low_min_fibonacci_number
    low_max_fibonacci = params.low_max_fibonacci_number
    for _ in range(params.test_iterations):
        high_fibonacci_number = random.randint(high_min_fibonacci, high_max_fibonacci)
        low_fibonacci_number = random.randint(low_min_fibonacci, low_max_fibonacci)
        test_cases.append((low_fibonacci_number, high_fibonacci_number))
    return test_cases


#
# stress tests
#


@pytest.mark.parametrize("input_fibonacci", sample_input_fibonacci(small_tests_params))
def test_stress_tests_efficient_solution_small_stress(input_fibonacci):
    brute_force = partial_sum_fibonacci_last_digit.brute_force_solution(input_fibonacci)
    efficient = partial_sum_fibonacci_last_digit.efficient_solution(input_fibonacci)
    assert brute_force == efficient


@pytest.mark.parametrize("input_fibonacci", sample_input_fibonacci(big_tests_params))
def test_stress_tests_efficient_solution_big_stress(input_fibonacci):
    efficient = partial_sum_fibonacci_last_digit.efficient_solution(input_fibonacci)
    brute_force = partial_sum_fibonacci_last_digit.brute_force_solution(input_fibonacci)
    assert brute_force == efficient


#
# performance tests
#


@pytest.mark.parametrize("input_fibonacci", sample_input_fibonacci(performance_params))
def test_performance(input_fibonacci) -> None:
    config_names = ["partial_sum_fibonacci_last_digit", "performance_tests"]
    performance_measures = read_config(PerformanceMeasures, config_names)

    efficient_time = performance_measures.measure_performance(
        partial_sum_fibonacci_last_digit.efficient_solution,
        input_fibonacci,
    )
    brute_force_time = performance_measures.measure_performance(
        partial_sum_fibonacci_last_digit.brute_force_solution,
        input_fibonacci,
    )

    # The efficient solution takes 10000 times less for fibonacci number 30
    times_faster = performance_measures.times_faster_efficient_to_brute_force
    assert times_faster * efficient_time < brute_force_time

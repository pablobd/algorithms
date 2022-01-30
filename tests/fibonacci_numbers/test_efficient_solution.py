import random
from typing import List

import pytest

from solutions import fibonacci_numbers
from tests.fibonacci_numbers import StressTestsParams
from tests.measure_performance import PerformanceMeasures
from tests.read_config import get_names, read_config

""" Performance tests show that the efficient solution takes 10000 times less time for
fibonacci number 30.
"""


#
# simple cases tests
#


def test_efficient_solution_simple_cases():
    assert 0 == fibonacci_numbers.efficient_solution(0)
    assert 1 == fibonacci_numbers.efficient_solution(1)
    assert 1 == fibonacci_numbers.efficient_solution(2)
    assert 2 == fibonacci_numbers.efficient_solution(3)
    assert 3 == fibonacci_numbers.efficient_solution(4)
    assert 5 == fibonacci_numbers.efficient_solution(5)
    assert 8 == fibonacci_numbers.efficient_solution(6)
    assert 13 == fibonacci_numbers.efficient_solution(7)


#
# get test parameters
#


names = ["fibonacci_numbers", "stress_tests"]
small_tests_params = read_config(StressTestsParams, get_names(names, "small_tests"))
big_tests_params = read_config(StressTestsParams, get_names(names, "big_tests"))
performance_params = read_config(StressTestsParams, get_names(names, "performance"))


#
# parametrize test inputs
#


def sample_input_fibonacci(params: StressTestsParams) -> List[int]:
    random.seed(params.seed)
    test_cases = []
    min_fibonacci = params.min_fibonacci_number
    max_fibonacci = params.max_fibonacci_number
    for _ in range(params.test_iterations):
        fibonacci_number = random.randint(min_fibonacci, max_fibonacci)
        test_cases.append(fibonacci_number)
    return test_cases


#
# stress tests
#


@pytest.mark.parametrize("input_fibonacci", sample_input_fibonacci(small_tests_params))
def test_stress_tests_efficient_solution_small_stress(input_fibonacci):
    brute_force = fibonacci_numbers.brute_force_solution(input_fibonacci)
    efficient = fibonacci_numbers.efficient_solution(input_fibonacci)
    assert brute_force == efficient


@pytest.mark.parametrize("input_fibonacci", sample_input_fibonacci(big_tests_params))
def test_stress_tests_efficient_solution_big_stress(input_fibonacci):
    brute_force = fibonacci_numbers.brute_force_solution(input_fibonacci)
    efficient = fibonacci_numbers.efficient_solution(input_fibonacci)
    assert brute_force == efficient


#
# performance tests
#


@pytest.mark.parametrize("input_fibonacci", sample_input_fibonacci(performance_params))
def test_performance(input_fibonacci) -> None:
    config_names = ["fibonacci_numbers", "performance_tests"]
    performance_measures = read_config(PerformanceMeasures, config_names)
    brute_force_time = performance_measures.measure_performance(
        fibonacci_numbers.brute_force_solution,
        input_fibonacci,
    )

    efficient_time = performance_measures.measure_performance(
        fibonacci_numbers.efficient_solution,
        input_fibonacci,
    )

    # The efficient solution takes 10000 times less for fibonacci number 30
    times_faster = performance_measures.times_faster_efficient_to_brute_force
    assert times_faster * efficient_time < brute_force_time

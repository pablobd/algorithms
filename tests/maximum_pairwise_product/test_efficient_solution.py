import random
import timeit
from dataclasses import dataclass
from typing import Callable, List

import pytest

from solutions import maximum_pairwise_product

""" Performance tests show that the efficient solution takes 100 times less time for
input sequences of length 1000.
"""

#
# prepare tests
#


@dataclass
class PerformanceMeasuresParams:
    __test__ = False  # Will not be discovered as a test

    repeat_performance_tests_per_input: int = 5
    number_performance_tests_per_input: int = 10
    times_faster_efficient_to_brute_force: float = 1e2


@dataclass
class TestParams:
    __test__ = False  # Will not be discovered as a test

    max_sequence_len: int
    max_number_in_sequence: int
    test_iterations: int
    min_sequence_len: int = 2
    min_number_in_sequence: int = 1
    seed: int = 123


small_tests_params = TestParams(5, 10, 100)
large_tests_params = TestParams(100, 1000, 1000)
performance_tests_params = TestParams(1000, 100, 5, 999, 10)
performance_measures_params = PerformanceMeasuresParams()


def generate_input_data(params: TestParams) -> List[List[int]]:
    random.seed(params.seed)
    test_cases = []
    for _ in range(params.test_iterations):
        len = random.randrange(params.min_sequence_len, params.max_sequence_len)
        population = range(params.min_number_in_sequence, params.max_number_in_sequence)
        test_cases.append(random.choices(population, k=len))
    return test_cases


#
# stress tests
#


@pytest.mark.parametrize("input_data", generate_input_data(small_tests_params))
def test_stress_tests_small_numbers(input_data) -> None:
    brute_force = maximum_pairwise_product.brute_force_solution(input_data)
    efficient = maximum_pairwise_product.efficient_solution(input_data)
    assert brute_force == efficient


@pytest.mark.parametrize("input_data", generate_input_data(large_tests_params))
def test_stress_tests_large_numbers(input_data) -> None:
    brute_force = maximum_pairwise_product.brute_force_solution(input_data)
    efficient = maximum_pairwise_product.efficient_solution(input_data)
    assert brute_force == efficient


#
# performance tests
#


@pytest.mark.parametrize("input_data", generate_input_data(performance_tests_params))
def test_performance(input_data) -> None:

    brute_force_time = _measure_performance(
        maximum_pairwise_product.brute_force_solution,
        input_data,
        performance_measures_params,
    )

    efficient_time = _measure_performance(
        maximum_pairwise_product.efficient_solution,
        input_data,
        performance_measures_params,
    )

    # The efficient solution takes 100 times less for sequences of length 1000
    times_faster = performance_measures_params.times_faster_efficient_to_brute_force
    assert times_faster * efficient_time < brute_force_time


def _measure_performance(
    func: Callable[[List[int]], int],
    input_data: List[int],
    performance_measures_params: PerformanceMeasuresParams,
) -> float:
    repeat_param = performance_measures_params.repeat_performance_tests_per_input
    number_param = performance_measures_params.number_performance_tests_per_input
    t = timeit.Timer(lambda: func(input_data))
    time_list = t.repeat(repeat_param, number_param)
    # higher values in the result vector are typically not caused by variability in Python's speed,
    # but by other processes interfering with your timing accuracy
    time = min(time_list)
    return time

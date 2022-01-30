import random
from typing import List

import pytest

from solutions import maximum_pairwise_product
from tests.maximum_pairwise_product import StressTestsParams
from tests.performance_measures import PerformanceMeasures
from tests.read_config import get_names, read_config

""" Performance tests show that the efficient solution is a 100 times faster for
input sequences of length 1000.
"""

#
# get test parameters
#


names = ["maximum_pairwise_product", "stress_tests"]
small_tests_params = read_config(StressTestsParams, get_names(names, "small_tests"))
big_tests_params = read_config(StressTestsParams, get_names(names, "big_tests"))
performance_params = read_config(StressTestsParams, get_names(names, "performance"))


#
# parametrize test inputs
#


def sample_input_sequence(params: StressTestsParams) -> List[List[int]]:
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


@pytest.mark.parametrize("input_sequence", sample_input_sequence(small_tests_params))
def test_stress_tests_small_numbers(input_sequence) -> None:
    brute_force = maximum_pairwise_product.brute_force_solution(input_sequence)
    efficient = maximum_pairwise_product.efficient_solution(input_sequence)
    assert brute_force == efficient


@pytest.mark.parametrize("input_sequence", sample_input_sequence(big_tests_params))
def test_stress_tests_large_numbers(input_sequence) -> None:
    brute_force = maximum_pairwise_product.brute_force_solution(input_sequence)
    efficient = maximum_pairwise_product.efficient_solution(input_sequence)
    assert brute_force == efficient


#
# performance tests
#


@pytest.mark.parametrize("input_sequence", sample_input_sequence(performance_params))
def test_performance(input_sequence) -> None:
    config_names = ["maximum_pairwise_product", "performance_tests"]
    performance_measures = read_config(PerformanceMeasures, config_names)
    brute_force_time = performance_measures.measure_performance(
        maximum_pairwise_product.brute_force_solution,
        input_sequence,
    )

    efficient_time = performance_measures.measure_performance(
        maximum_pairwise_product.efficient_solution,
        input_sequence,
    )

    # The efficient solution takes 100 times less for sequences of length 1000
    times_faster = performance_measures.times_faster_efficient_to_brute_force
    assert times_faster * efficient_time < brute_force_time

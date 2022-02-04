import random
from typing import List, Tuple

import pytest

from solutions import least_common_multiple
from tests.least_common_multiple.stress_tests_params import StressTestsParams
from tests.performance_measures import PerformanceMeasures
from tests.read_config import get_names, read_config

""" Performance tests show that the efficient solution is a 100 times faster for
two numbers between 2000 and 2100.
"""

#
# simple cases tests
#


def test_efficient_solution_simple_cases():
    assert least_common_multiple.efficient_solution((5, 7)) == 5 * 7
    assert least_common_multiple.efficient_solution((5 * 2, 2 * 7)) == 5 * 2 * 7
    assert least_common_multiple.efficient_solution((1, 1)) == 1
    assert least_common_multiple.efficient_solution((4, 2)) == 4


#
# get test parameters
#


names = ["least_common_multiple", "stress_tests"]
small_tests_params = read_config(StressTestsParams, get_names(names, "small_tests"))
big_tests_params = read_config(StressTestsParams, get_names(names, "big_tests"))
performance_params = read_config(StressTestsParams, get_names(names, "performance"))


#
# parametrize test inputs
#


def sample_input_lcm(params: StressTestsParams) -> List[Tuple[int, int]]:
    random.seed(params.seed)
    test_cases = []
    biggest_number = params.biggest_number
    smallest_number = params.smallest_number
    for _ in range(params.test_iterations):
        numbers = random.choices(list(range(smallest_number, biggest_number)), k=2)
        test_cases.append((numbers[0], numbers[1]))
    return test_cases


#
# stress tests
#


@pytest.mark.parametrize("input_gcd", sample_input_lcm(small_tests_params))
def test_stress_tests_efficient_solution_small_stress(input_gcd):
    brute_force = least_common_multiple.brute_force_solution(input_gcd)
    efficient = least_common_multiple.efficient_solution(input_gcd)
    assert brute_force == efficient


@pytest.mark.parametrize("input_gcd", sample_input_lcm(big_tests_params))
def test_stress_tests_efficient_solution_big_stress(input_gcd):
    brute_force = least_common_multiple.brute_force_solution(input_gcd)
    efficient = least_common_multiple.efficient_solution(input_gcd)
    assert brute_force == efficient


#
# performance tests
#


@pytest.mark.parametrize("input_gcd", sample_input_lcm(performance_params))
def test_performance(input_gcd) -> None:
    config_names = ["least_common_multiple", "performance_tests"]
    performance_measures = read_config(PerformanceMeasures, config_names)

    brute_force_time = performance_measures.measure_performance(
        least_common_multiple.brute_force_solution,
        input_gcd,
    )
    efficient_time = performance_measures.measure_performance(
        least_common_multiple.efficient_solution,
        input_gcd,
    )
    # The efficient solution takes 100 times less for sequences of length 1000
    times_faster = performance_measures.times_faster_efficient_to_brute_force
    assert times_faster * efficient_time < brute_force_time

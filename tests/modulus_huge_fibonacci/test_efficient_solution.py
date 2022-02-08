import random
from typing import List, Tuple

import pytest

from solutions import modulus_huge_fibonacci
from solutions.modulus_huge_fibonacci.efficient_solution import _get_pisano_period
from tests.modulus_huge_fibonacci.stress_tests_params import StressTestsParams
from tests.performance_measures import PerformanceMeasures
from tests.read_config import get_names, read_config

""" Performance tests show that the efficient solution is a 1000 times faster for
two numbers between 400000 and 400020.
"""

#
# Pisano Period simple cases tests
#


def test_get_pisano_period_simple_cases():
    assert 1 == _get_pisano_period(1)
    assert 3 == _get_pisano_period(2)
    assert 8 == _get_pisano_period(3)
    assert 6 == _get_pisano_period(4)
    assert 20 == _get_pisano_period(5)
    assert 24 == _get_pisano_period(6)
    assert 16 == _get_pisano_period(7)
    assert 12 == _get_pisano_period(8)
    assert 24 == _get_pisano_period(9)
    assert 60 == _get_pisano_period(10)
    assert 10 == _get_pisano_period(11)
    assert 24 == _get_pisano_period(12)


#
# simple cases tests
#


@pytest.mark.parametrize("mod", [1, 2, 3, 4, 5, 6])
def test_efficient_solution_simple_cases(mod: int):
    assert 0 % mod == modulus_huge_fibonacci.efficient_solution((0, mod))
    assert 1 % mod == modulus_huge_fibonacci.efficient_solution((1, mod))
    assert 1 % mod == modulus_huge_fibonacci.efficient_solution((2, mod))
    assert 2 % mod == modulus_huge_fibonacci.efficient_solution((3, mod))
    assert 3 % mod == modulus_huge_fibonacci.efficient_solution((4, mod))
    assert 5 % mod == modulus_huge_fibonacci.efficient_solution((5, mod))
    assert 8 % mod == modulus_huge_fibonacci.efficient_solution((6, mod))
    assert 13 % mod == modulus_huge_fibonacci.efficient_solution((7, mod))


#
# get test parameters
#


names = ["modulus_huge_fibonacci", "stress_tests"]
small_tests_params = read_config(StressTestsParams, get_names(names, "small_tests"))
big_tests_params = read_config(StressTestsParams, get_names(names, "big_tests"))
performance_params = read_config(StressTestsParams, get_names(names, "performance"))

#
# parametrize test inputs
#


def sample_input_fibonacci(params: StressTestsParams) -> List[Tuple[int, int]]:
    random.seed(params.seed)
    test_cases = []
    min_fibonacci = params.min_fibonacci_number
    max_fibonacci = params.max_fibonacci_number
    min_modulus = params.min_modulus
    max_modulus = params.max_modulus
    for _ in range(params.test_iterations):
        fibonacci_number = random.randint(min_fibonacci, max_fibonacci)
        modulus = random.randint(min_modulus, max_modulus)
        test_cases.append((fibonacci_number, modulus))
    return test_cases


#
# stress tests
#


@pytest.mark.parametrize("input_fibonacci", sample_input_fibonacci(small_tests_params))
def test_stress_tests_efficient_solution_small_stress(input_fibonacci):
    brute_force = modulus_huge_fibonacci.brute_force_solution(input_fibonacci)
    efficient = modulus_huge_fibonacci.efficient_solution(input_fibonacci)
    assert brute_force == efficient


@pytest.mark.parametrize("input_fibonacci", sample_input_fibonacci(big_tests_params))
def test_stress_tests_efficient_solution_big_stress(input_fibonacci):
    brute_force = modulus_huge_fibonacci.brute_force_solution(input_fibonacci)
    efficient = modulus_huge_fibonacci.efficient_solution(input_fibonacci)
    assert brute_force == efficient


#
# performance tests
#


@pytest.mark.parametrize("input_fibonacci", sample_input_fibonacci(performance_params))
def test_performance(input_fibonacci) -> None:
    config_names = ["modulus_huge_fibonacci", "performance_tests"]
    performance_measures = read_config(PerformanceMeasures, config_names)

    brute_force_time = performance_measures.measure_performance(
        modulus_huge_fibonacci.brute_force_solution,
        input_fibonacci,
    )
    efficient_time = performance_measures.measure_performance(
        modulus_huge_fibonacci.efficient_solution,
        input_fibonacci,
    )

    times_faster = performance_measures.times_faster_efficient_to_brute_force
    assert times_faster * efficient_time < brute_force_time

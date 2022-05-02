import random
from typing import List, Tuple

import pytest

from solutions.greedy import minimum_refueling_stops
from tests.greedy.minimum_refueling_stops.stress_tests_params import StressTestsParams
from tests.performance_measures import PerformanceMeasures
from tests.read_config import get_names, read_config


def test_efficient_solution_simple_cases() -> None:
    assert 2 == minimum_refueling_stops.efficient_solution(
        (950, 400, [200, 375, 550, 750])
    )

    assert -1 == minimum_refueling_stops.efficient_solution((10, 3, [1, 2, 5, 9]))
    assert 0 == minimum_refueling_stops.efficient_solution((200, 250, [100, 150]))


#
# get test parameters
#


names = ["minimum_refueling_stops", "stress_tests"]
small_tests_params = read_config(StressTestsParams, get_names(names, "small_tests"))
big_tests_params = read_config(StressTestsParams, get_names(names, "big_tests"))
performance_params = read_config(StressTestsParams, get_names(names, "performance"))

#
# parametrize test inputs
#


def _cumsum(x: List[int]) -> List[int]:
    res = []
    elements_sum = 0
    for element in x:
        elements_sum += element
        res.append(elements_sum)
    return res


def sample_input_minimum_refueling_stops(
    params: StressTestsParams,
) -> List[Tuple[int, int, List[int]]]:
    random.seed(params.seed)
    test_cases = []
    for _ in range(params.test_iterations):
        number_stops = random.randint(params.min_fuel_stops, params.max_fuel_stops)
        min_distance = params.min_distance_between_stops
        max_distance = params.max_distance_between_stops
        stops = _cumsum(
            [random.randint(min_distance, max_distance) for _ in range(number_stops)]
        )
        distance_to_destination = (
            random.randint(
                params.min_distance_to_destination_from_last_stop,
                params.max_distance_to_destination_from_last_stop,
            )
            + stops[-1]
        )
        tank_capacity = random.randint(
            params.min_tank_capacity, params.max_tank_capacity
        )
        test_cases.append((distance_to_destination, tank_capacity, stops))
    return test_cases


#
# stress tests
#


@pytest.mark.parametrize(
    "input_minimum_refueling_stops",
    sample_input_minimum_refueling_stops(small_tests_params),
)
def test_stress_tests_efficient_solution_small_stress(
    input_minimum_refueling_stops: Tuple[float, float, List[float]]
) -> None:
    brute_force = minimum_refueling_stops.brute_force_solution(
        input_minimum_refueling_stops
    )
    efficient = minimum_refueling_stops.efficient_solution(
        input_minimum_refueling_stops
    )
    assert brute_force == efficient


@pytest.mark.parametrize(
    "input_minimum_refueling_stops",
    sample_input_minimum_refueling_stops(big_tests_params),
)
def test_stress_tests_efficient_solution_big_stress(
    input_minimum_refueling_stops: Tuple[float, float, List[float]]
) -> None:
    brute_force = minimum_refueling_stops.brute_force_solution(
        input_minimum_refueling_stops
    )
    efficient = minimum_refueling_stops.efficient_solution(
        input_minimum_refueling_stops
    )
    assert brute_force == efficient


#
# performance tests
#


@pytest.mark.parametrize(
    "input_minimum_refueling_stops",
    sample_input_minimum_refueling_stops(performance_params),
)
def test_performance(input_minimum_refueling_stops: Tuple[int, int, List[int]]) -> None:
    config_names = ["minimum_refueling_stops", "performance_tests"]
    performance_measures = read_config(PerformanceMeasures, config_names)
    brute_force_time = performance_measures.measure_performance(
        minimum_refueling_stops.brute_force_solution,
        input_minimum_refueling_stops,
    )
    efficient_time = performance_measures.measure_performance(
        minimum_refueling_stops.efficient_solution,
        input_minimum_refueling_stops,
    )

    times_faster = performance_measures.times_faster_efficient_to_brute_force
    assert times_faster * efficient_time < brute_force_time

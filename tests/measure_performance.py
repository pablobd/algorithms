import timeit
from dataclasses import dataclass
from typing import Any, Callable

from tests.read_config import Config


@dataclass
class PerformanceMeasures(Config):

    repeat_performance_tests_per_input: int = 5
    number_performance_tests_per_input: int = 10
    times_faster_efficient_to_brute_force: float = 1e2

    def measure_performance(self, func: Callable[[Any], Any], input_data: Any) -> float:
        repeat_param = self.repeat_performance_tests_per_input
        number_param = self.number_performance_tests_per_input
        t = timeit.Timer(lambda: func(input_data))
        time_list = t.repeat(repeat_param, number_param)
        # higher values in the result vector are typically not caused by variability in Python's speed,
        # but by other processes interfering with your timing accuracy
        time = min(time_list)
        return time

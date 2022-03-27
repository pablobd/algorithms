from dataclasses import dataclass

from tests.read_config import Config


@dataclass
class StressTestsParams(Config):
    high_max_fibonacci_number: int
    high_min_fibonacci_number: int
    low_max_fibonacci_number: int
    low_min_fibonacci_number: int
    test_iterations: int
    seed: int = 123

from dataclasses import dataclass

from tests.read_config import Config


@dataclass
class StressTestsParams(Config):
    biggest_number: int
    smallest_number: int
    test_iterations: int
    seed: int = 321

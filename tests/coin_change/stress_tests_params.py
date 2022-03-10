from dataclasses import dataclass

from tests.read_config import Config


@dataclass
class StressTestsParams(Config):
    max_number: int
    min_number: int
    test_iterations: int
    seed: int = 123

from dataclasses import dataclass

from tests.read_config import Config


@dataclass
class StressTestsParams(Config):
    max_fibonacci_number: int
    min_fibonacci_number: int
    min_modulo: int
    max_modulo: int
    test_iterations: int
    seed: int = 123

from dataclasses import dataclass

from tests.read_config import Config


@dataclass
class StressTestsParams(Config):
    max_fibonacci_number: int
    min_fibonacci_number: int
    min_modulus: int
    max_modulus: int
    test_iterations: int
    seed: int = 123

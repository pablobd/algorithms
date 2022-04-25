from dataclasses import dataclass

from tests.read_config import Config


@dataclass
class StressTestsParams(Config):
    min_num_items: int
    max_num_items: int
    max_value: int
    min_value: int
    max_weight: int
    min_weight: int
    max_capacity: int
    min_capacity: int
    test_iterations: int
    seed: int = 123

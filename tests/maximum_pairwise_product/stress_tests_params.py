from dataclasses import dataclass

from tests.read_config import Config


@dataclass
class StressTestsParams(Config):
    max_sequence_len: int
    max_number_in_sequence: int
    test_iterations: int
    min_sequence_len: int = 2
    min_number_in_sequence: int = 1
    seed: int = 123

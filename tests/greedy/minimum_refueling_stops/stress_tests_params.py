from dataclasses import dataclass

from tests.read_config import Config


@dataclass
class StressTestsParams(Config):
    max_fuel_stops: int
    min_fuel_stops: int
    max_distance_between_stops: int
    min_distance_between_stops: int
    max_tank_capacity: int
    min_tank_capacity: int
    max_distance_to_destination_from_last_stop: int
    min_distance_to_destination_from_last_stop: int
    test_iterations: int
    seed: int = 123

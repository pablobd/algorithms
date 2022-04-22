from typing import List, Tuple


def brute_force_solution(
    input_min_refueling_stops: Tuple[float, float, List[float]]
) -> int:
    """Solve the problem using brute force.

    Parameters
    ----------
    input_min_refueling_stops : Tuple[float, float, List[int]]
        The input data, a tuple of the form (distance, tank_capacity, stations).

    Returns
    -------
    int
        The minimum number of refueling stops.
    """
    destination_distance, tank_capacity, gas_stations = input_min_refueling_stops
    stops = [0.0] + gas_stations + [destination_distance]
    refuel = 0
    i = 0
    while i + 2 < len(stops):
        for j, next_gas_station in enumerate(stops[(i + 1) :]):
            if tank_capacity < next_gas_station - stops[i]:
                if j == 0:
                    return -1
                refuel += 1
                break
        i += j
    return refuel

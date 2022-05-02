from typing import List, Tuple


def efficient_solution(
    input_min_refueling_stops: Tuple[float, float, List[float]]
) -> int:
    """Solve the problem using a greedy solution. The greedy solution is consists on
    refueling at the last possible station that the tank deposit capacity allows, then
    removing the previous stations and start again. This is O(1) in time and O(n) in
    space.

    Parameters
    ----------
    input_min_refueling_stops : Tuple[float, float, List[float]]
        The input data, a tuple of the form (distance, tank_capacity, stations).

    Returns
    -------
    int
        The minimum number of refueling stops.
    """
    destination_distance, tank_capacity, gas_stations = input_min_refueling_stops
    stops = [0.0] + gas_stations + [destination_distance]
    refueling, i = 0, 0
    while i < len(stops) - 1:
        i += 1
        if tank_capacity < stops[i] - stops[0]:
            if i == 1:
                return -1
            refueling += 1
            stops = stops[i - 1 :]
            i = 0
    return refueling

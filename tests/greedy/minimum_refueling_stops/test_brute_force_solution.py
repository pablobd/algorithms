from solutions.greedy import minimum_refueling_stops


def test_brute_force_solution():
    assert 2 == minimum_refueling_stops.brute_force_solution(
        (950, 400, [200, 375, 550, 750])
    )
    assert -1 == minimum_refueling_stops.brute_force_solution((10, 3, [1, 2, 5, 9]))
    assert 0 == minimum_refueling_stops.brute_force_solution((200, 250, [100, 150]))

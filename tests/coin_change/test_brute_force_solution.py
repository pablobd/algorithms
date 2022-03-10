from solutions.coin_change import brute_force_solution


def test_brute_force_solution_simple_cases():
    assert brute_force_solution(0) == 0
    assert brute_force_solution(1) == 1
    assert brute_force_solution(2) == 2
    assert brute_force_solution(3) == 3
    assert brute_force_solution(4) == 4
    assert brute_force_solution(5) == 1
    assert brute_force_solution(6) == 2
    assert brute_force_solution(7) == 3
    assert brute_force_solution(10) == 1
    assert brute_force_solution(11) == 2
    assert brute_force_solution(12) == 3
    assert brute_force_solution(15) == 2
    assert brute_force_solution(25) == 3

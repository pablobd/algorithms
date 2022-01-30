from solutions import fibonacci_numbers


def test_brute_force_manual():
    assert 0 == fibonacci_numbers.brute_force_solution(0)
    assert 1 == fibonacci_numbers.brute_force_solution(1)
    assert 1 == fibonacci_numbers.brute_force_solution(2)
    assert 2 == fibonacci_numbers.brute_force_solution(3)
    assert 3 == fibonacci_numbers.brute_force_solution(4)
    assert 5 == fibonacci_numbers.brute_force_solution(5)
    assert 8 == fibonacci_numbers.brute_force_solution(6)
    assert 13 == fibonacci_numbers.brute_force_solution(7)

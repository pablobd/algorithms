from solutions import sum_fibonacci_last_digit


def test_brute_force_solution_simple_cases():
    assert 0 == sum_fibonacci_last_digit.brute_force_solution(0)
    assert 1 == sum_fibonacci_last_digit.brute_force_solution(1)
    assert 2 == sum_fibonacci_last_digit.brute_force_solution(2)
    assert 4 == sum_fibonacci_last_digit.brute_force_solution(3)
    assert 7 == sum_fibonacci_last_digit.brute_force_solution(4)
    assert 2 == sum_fibonacci_last_digit.brute_force_solution(5)
    assert 0 == sum_fibonacci_last_digit.brute_force_solution(6)
    assert 3 == sum_fibonacci_last_digit.brute_force_solution(7)
    assert 4 == sum_fibonacci_last_digit.brute_force_solution(8)
    assert 8 == sum_fibonacci_last_digit.brute_force_solution(9)
    assert 5 == sum_fibonacci_last_digit.brute_force_solution(100)

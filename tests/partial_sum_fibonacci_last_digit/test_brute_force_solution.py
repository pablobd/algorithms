from solutions import partial_sum_fibonacci_last_digit


def test_brute_force_solution():
    assert 0 == partial_sum_fibonacci_last_digit.brute_force_solution((0, 0))
    assert 1 == partial_sum_fibonacci_last_digit.brute_force_solution((0, 1))
    assert 2 == partial_sum_fibonacci_last_digit.brute_force_solution((1, 2))
    assert 4 == partial_sum_fibonacci_last_digit.brute_force_solution((0, 3))
    assert 3 == partial_sum_fibonacci_last_digit.brute_force_solution((2, 3))
    assert 7 == partial_sum_fibonacci_last_digit.brute_force_solution((0, 4))
    assert 5 == partial_sum_fibonacci_last_digit.brute_force_solution((3, 4))
    assert 2 == partial_sum_fibonacci_last_digit.brute_force_solution((0, 5))
    assert 8 == partial_sum_fibonacci_last_digit.brute_force_solution((4, 5))
    assert 0 == partial_sum_fibonacci_last_digit.brute_force_solution((0, 6))
    assert 6 == partial_sum_fibonacci_last_digit.brute_force_solution((4, 6))
    assert 3 == partial_sum_fibonacci_last_digit.brute_force_solution((0, 7))
    assert 6 == partial_sum_fibonacci_last_digit.brute_force_solution((5, 7))
    assert 4 == partial_sum_fibonacci_last_digit.brute_force_solution((0, 8))
    assert 0 == partial_sum_fibonacci_last_digit.brute_force_solution((4, 8))
    assert 8 == partial_sum_fibonacci_last_digit.brute_force_solution((0, 9))
    assert 6 == partial_sum_fibonacci_last_digit.brute_force_solution((6, 9))
    assert 5 == partial_sum_fibonacci_last_digit.brute_force_solution((10, 10))
    assert 5 == partial_sum_fibonacci_last_digit.brute_force_solution((0, 100))
    assert 2 == partial_sum_fibonacci_last_digit.brute_force_solution((10, 200))

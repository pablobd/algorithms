from solutions import greatest_common_divisor


def test_brute_force_solution():
    assert greatest_common_divisor.efficient_solution((1, 1)) == 1
    assert greatest_common_divisor.efficient_solution((1, 2)) == 1
    assert greatest_common_divisor.efficient_solution((2, 2)) == 2
    assert greatest_common_divisor.efficient_solution((3, 2)) == 1
    assert greatest_common_divisor.efficient_solution((3, 6)) == 3
    assert greatest_common_divisor.efficient_solution((6, 3)) == 3
    assert greatest_common_divisor.efficient_solution((6, 9)) == 3
    assert greatest_common_divisor.efficient_solution((3 * 5 * 7, 8 * 5)) == 5

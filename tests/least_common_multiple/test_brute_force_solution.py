from solutions import least_common_multiple


def test_brute_force_solution_simple_cases():
    assert least_common_multiple.brute_force_solution((5, 7)) == 5 * 7
    assert least_common_multiple.brute_force_solution((5 * 2, 2 * 7)) == 5 * 2 * 7
    assert least_common_multiple.brute_force_solution((1, 1)) == 1
    assert least_common_multiple.brute_force_solution((4, 2)) == 4

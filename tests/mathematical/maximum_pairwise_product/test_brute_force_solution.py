from solutions.mathematical import maximum_pairwise_product


def test_short_case() -> None:
    x = [2, 3, 1, 4]
    res = maximum_pairwise_product.brute_force_solution(x)
    assert res == 12


def test_long_case() -> None:
    x = [2, 10, 3, 1, 5, 4, 40, 2, 1, 5, 4, 6]
    res = maximum_pairwise_product.brute_force_solution(x)
    assert res == 400


def test_edge_case_two_numbers() -> None:
    x = [1, 2]
    res = maximum_pairwise_product.brute_force_solution(x)
    assert res == 2


def test_edge_case_two_equal_numbers() -> None:
    x = [2, 2]
    res = maximum_pairwise_product.brute_force_solution(x)
    assert res == 4

from solutions import maximum_pairwise_product


def test_trivial_example():
    x = [2, 3, 1, 4]
    res = maximum_pairwise_product.brute_force_solution(x)
    assert res == 12

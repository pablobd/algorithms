import pytest

from solutions.mathematical import modulo_huge_fibonacci


@pytest.mark.parametrize("mod", [1, 2, 3, 4, 5, 6])
def test_brute_force_solution_simple_cases(mod):
    assert 0 % mod == modulo_huge_fibonacci.brute_force_solution((0, mod))
    assert 1 % mod == modulo_huge_fibonacci.brute_force_solution((1, mod))
    assert 1 % mod == modulo_huge_fibonacci.brute_force_solution((2, mod))
    assert 2 % mod == modulo_huge_fibonacci.brute_force_solution((3, mod))
    assert 3 % mod == modulo_huge_fibonacci.brute_force_solution((4, mod))
    assert 5 % mod == modulo_huge_fibonacci.brute_force_solution((5, mod))
    assert 8 % mod == modulo_huge_fibonacci.brute_force_solution((6, mod))
    assert 13 % mod == modulo_huge_fibonacci.brute_force_solution((7, mod))

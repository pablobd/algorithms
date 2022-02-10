from typing import Tuple

from solutions import modulus_huge_fibonacci


def brute_force_solution(numbers: Tuple[int, int]) -> int:
    k, n = numbers
    partial_sum = 0
    for i in range(k, n + 1):
        partial_sum += modulus_huge_fibonacci.efficient_solution((i, 10))
    return partial_sum % 10

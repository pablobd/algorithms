from typing import Tuple

from solutions import modulus_huge_fibonacci


def efficient_solution(numbers: Tuple[int, int]) -> int:
    k, n = numbers
    if n <= 2:
        sum_n = n
    else:
        sum_n = modulus_huge_fibonacci.efficient_solution((n + 2, 10)) - 1
    if k <= 2:
        sum_k = max([k - 1, 0])
    else:
        sum_k = modulus_huge_fibonacci.efficient_solution((k + 1, 10)) - 1
    return (sum_n - sum_k) % 10

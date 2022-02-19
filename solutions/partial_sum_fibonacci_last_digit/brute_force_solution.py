from typing import Tuple

from solutions import modulo_huge_fibonacci


def brute_force_solution(numbers: Tuple[int, int]) -> int:
    """Compute the last digit of sum of all Fibonacci numbers between two Fibonacci
    numbers with brute force.

    This solution has a time and space complexity of O(n-k) and O(1) respectively.

    Parameters
    ----------
    numbers : Tuple[int, int]
        A tuple of integers, the first smaller than the second.

    Returns
    -------
    int
        The solution.
    """
    k, n = numbers
    partial_sum = 0
    for i in range(k, n + 1):
        partial_sum += modulo_huge_fibonacci.efficient_solution((i, 10))
    return partial_sum % 10

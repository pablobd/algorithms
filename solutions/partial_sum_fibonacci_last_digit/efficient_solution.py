from typing import Tuple

from solutions import modulo_huge_fibonacci


def efficient_solution(numbers: Tuple[int, int]) -> int:
    """Compute the last digit of sum of all Fibonacci numbers between two Fibonacci
    numbers with an efficient solution.

    Since we take modulo 10 to get the last digit and we make use of the solution of the
    modulo of a Fibonacci number efficient solution, based on the Pisano period, which
    has a complexity O(m) where m is the modulo, we conclude this solution has a
    constant time complexity O(1). It also has a O(1) space complexity.

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
    if n <= 2:
        sum_n = n
    else:
        sum_n = modulo_huge_fibonacci.efficient_solution((n + 2, 10)) - 1
    if k <= 2:
        sum_k = max([k - 1, 0])
    else:
        sum_k = modulo_huge_fibonacci.efficient_solution((k + 1, 10)) - 1
    return (sum_n - sum_k) % 10

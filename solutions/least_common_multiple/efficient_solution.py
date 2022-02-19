from typing import Tuple

from solutions import greatest_common_divisor


def efficient_solution(numbers: Tuple[int, int]) -> int:
    """Compute the least common multiple of two numbers in a efficient way.

    This solution makes use of the greatest common divisor solution and the time and
    space complexities are the same, O(log(n)) and O(1) respectively.

    Parameters
    ----------
    numbers : Tuple[int, int]
        A tuple of two integers.

    Returns
    -------
    int
        The least common multiple of the two numbers.
    """
    gcd = greatest_common_divisor.efficient_solution(numbers)
    n, k = numbers
    return n * k // gcd

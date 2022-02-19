from typing import Tuple


def brute_force_solution(numbers: Tuple[int, int]) -> int:
    """Compute the least common multiple of two numbers with a brute force solution.

    The time complexity is O(max(n, k) - min(n, k)) and the space complexity is O(1).

    Parameters
    ----------
    numbers : Tuple[int, int]
        The two integer numbers.

    Returns
    -------
    int
        The Least Common Multiple of two numbers.

    Raises
    ------
    ValueError
        Raised if both numbers are negative or zero.
    ValueError
        Raised if one of the numbers is negative or zero.
    """
    n, k = numbers

    if n <= 0 and k <= 0:
        raise ValueError("Both numbers are negative or zero")

    for i in range(max([n, k]), n * k + 1):
        if i % n == 0 and i % k == 0:
            return i

    raise ValueError("One of the numbers is negative or zero")

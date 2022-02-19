from typing import Tuple


def brute_force_solution(numbers: Tuple[int, int]) -> int:
    """Compute the modulo of a Fibonacci number with brute force.

    The time and space complexities are O(n) and O(1).

    Parameters
    ----------
    numbers : Tuple[int, int]
        A tuple of integers, the first the Fibonacci number and the second the modulo.

    Returns
    -------
    int
        The modulo of the Fibonacci number.
    """
    n, m = numbers
    if n <= 1:
        return n % m

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

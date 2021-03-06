from typing import Tuple


def brute_force_solution(numbers: Tuple[int, int]) -> int:
    """Compute the greatest common divisor by applying a brute force solution.

    The time and space complexities are O(n) and O(1) respectively.

    Parameters
    ----------
    numbers : Tuple[int, int]
        A tuple of integers, with the first element greater or equal to the second.

    Returns
    -------
    int
        The result of the brute force solution to the greatest common divisor.
    """
    n, k = numbers
    greatest_common_divisor = 1
    for i in range(1, min([n, k]) + 1):
        if n % i == 0 and k % i == 0:
            greatest_common_divisor = i
    return greatest_common_divisor

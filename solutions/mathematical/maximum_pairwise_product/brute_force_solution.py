"""A brute force solution to the maximum pairwise product challenge."""

from typing import List


def brute_force_solution(numbers: List[int]) -> int:
    """Compute the maximum pairwise product of a sequence of integers with a brute force
    solution.

    The time and space complexities are O(n^2) and O(1).

    Parameters
    ----------
    numbers : List[int]
        List of positive integers

    Returns
    -------
    int
        The product that is maximum among all pairs
    """
    max_pairwise_product: int = 0

    for i, n in enumerate(numbers):
        for k in numbers[i + 1 :]:
            product = n * k
            if max_pairwise_product < product:
                max_pairwise_product = product

    return max_pairwise_product

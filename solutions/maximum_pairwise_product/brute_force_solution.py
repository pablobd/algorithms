"""A brute force solution to the maximum pairwise product challenge."""

from typing import List


def brute_force_solution(numbers: List[int]) -> int:
    """Brute force solution to maximum pairwise product problem.

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
        residual_numbers = numbers[:i] + numbers[i + 1 :]
        for k in residual_numbers:
            product = n * k
            if max_pairwise_product < product:
                max_pairwise_product = product

    return max_pairwise_product

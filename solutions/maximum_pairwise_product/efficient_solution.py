from typing import List


def efficient_solution(x: List[int]) -> int:
    """Compute the maximum pairwise product of a sequence of integers with an efficient
    solution.

    The time and space complexities are O(n) and O(1).

    Parameters
    ----------
    numbers : List[int]
        List of positive integers

    Returns
    -------
    int
        The product that is maximum among all pairs
    """
    first_max = 0
    index_first_max = 0
    for i, n in enumerate(x):
        if first_max < n:
            first_max = n
            index_first_max = i

    second_max = 0
    for i, n in enumerate(x):
        if index_first_max != i and second_max < n:
            second_max = n

    return first_max * second_max

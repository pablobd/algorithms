from typing import List


def efficient_solution(x: List[int]) -> int:
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

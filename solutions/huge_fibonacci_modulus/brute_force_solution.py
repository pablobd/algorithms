from typing import Tuple


def brute_force_solution(numbers: Tuple[int, int]) -> int:
    n, m = numbers
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

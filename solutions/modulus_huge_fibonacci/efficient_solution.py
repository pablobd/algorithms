from typing import Tuple


def efficient_solution(numbers: Tuple[int, int]) -> int:
    n, m = numbers
    if n <= 1:
        return n % m

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % m, (previous + current) % m

    return current

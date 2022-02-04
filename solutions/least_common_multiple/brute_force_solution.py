from typing import Tuple


def brute_force_solution(numbers: Tuple[int, int]) -> int:
    n, k = numbers
    for i in range(max([n, k]), n * k + 1):
        if i % n == 0 and i % k == 0:
            return i
    raise ValueError(f"{n} and {k} are not positive integers")

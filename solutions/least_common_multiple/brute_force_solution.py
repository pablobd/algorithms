from typing import Tuple


def brute_force_solution(numbers: Tuple[int, int]) -> int:
    n, k = numbers

    if (n < 0 and k < 0) or (n == 0 and k == 0):
        raise ValueError("Both numbers are negative or zero")

    for i in range(max([n, k]), n * k + 1):
        if i % n == 0 and i % k == 0:
            return i

    raise ValueError("One of the numbers is negative or zero")

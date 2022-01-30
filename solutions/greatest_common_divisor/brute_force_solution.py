from typing import Tuple


def brute_force_solution(numbers: Tuple[int, int]) -> int:
    n, k = numbers
    greatest_common_divisor = 1
    for i in range(1, min([n, k]) + 1):
        if n % i == 0 and k % i == 0:
            greatest_common_divisor = i
    return greatest_common_divisor

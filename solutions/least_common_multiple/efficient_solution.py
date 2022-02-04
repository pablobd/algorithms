from typing import Tuple

from solutions import greatest_common_divisor


def efficient_solution(numbers: Tuple[int, int]) -> int:
    gcd = greatest_common_divisor.efficient_solution(numbers)
    n, k = numbers
    return n * k // gcd

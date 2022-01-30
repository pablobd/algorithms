from typing import Tuple


def efficient_solution(numbers: Tuple[int, int]) -> int:
    n, k = numbers
    if n < k:
        a = k
        b = n
    else:
        a = n
        b = k
    while True:
        modulo = a % b
        if modulo == 0:
            return b
        else:
            a = b
            b = modulo

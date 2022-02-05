from typing import Tuple


def _get_pisano_period(mod: int) -> int:
    if mod == 1:
        return 1
    previous, current = 0, 1
    i = 0
    while True:
        i += 1
        previous, current = current, (previous + current) % mod

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            break

    return i


def efficient_solution(numbers: Tuple[int, int]) -> int:
    n, m = numbers
    mod = _get_pisano_period(m)

    n_mod = n % mod
    if n_mod <= 1:
        return n_mod % m

    previous = 0
    current = 1
    for _ in range(n_mod - 1):
        # Modulo addition is associative
        previous, current = current % m, (previous + current) % m

    return current

from typing import Tuple


def _get_pisano_period(m: int) -> int:
    """Compute the Pisano period for a modulo, m.

    To compute the Pisano period, we observe that all sequences need to start with the
    pattern 0, 1 (the first two Fibonacci numbers, 0 and 1, modulo any number are 0 and
    1). There fore we compute the Fibonacci numbers and take the modulo until finding
    the 0 and 1 pattern.

    The time complexity of the period-finding is O(m). The loop takes at most m steps to
    find the period. The space complexity is O(1).

    Parameters
    ----------
    m : int
        The modulo, for which we compute the pisano period.

    Returns
    -------
    int
        The pisano period.
    """
    if m == 1:
        return 1
    previous, current = 0, 1
    i = 0
    while True:
        i += 1
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            break

    return i


def efficient_solution(numbers: Tuple[int, int]) -> int:
    """Compute the modulo of a Fibonacci number in a efficient way.

    This solution has a time complexity O(m) and a space complexity O(1).

    Parameters
    ----------
    m : int
        The modulo, for which we compute the pisano period.

    Returns
    -------
    int
        The pisano period.
    """
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

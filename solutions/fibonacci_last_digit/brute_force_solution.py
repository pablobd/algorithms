def brute_force_solution(n: int) -> int:
    """Compute the last digit of a large fibonacci number n computed with a brute force
    algorithm.

    The time and space complexities of the solution are T(n) = O(n log(n)^2) for very
    big numbers and S(n) = F(n). Since, very big numbers do not fit in the CPU
    bus of the machine (2e64 for 64 bit machines), it turns out the sum can't be
    computed in parallel and stops being O(1) and becomes O(log(n)). See reference:
    https://iq.opengenus.org/time-complexity-of-addition/

    Parameters
    ----------
    n : int
        The fibonacci number to compute the last digit of.

    Returns
    -------
    int
        The last digit of the fibonacci number.
    """
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

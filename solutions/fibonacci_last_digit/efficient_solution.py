def efficient_solution(n: int) -> int:
    """Compute the last digit of a large fibonacci number in a efficient way.

    The solution comes out from the modulo property w.r.t. to the sum,
    (n1  + n2) % m = (n1 % m + n2 % m) % m.

    The time and space complexities are O(n) and O(1).

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
        previous, current = current, (previous + current) % 10

    return current

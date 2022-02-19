def efficient_solution(n: int) -> int:
    """Compute the n fibonacci number computed in a more efficient way.

    The solution is T(n) = O(n) time complexity and S(n) = O(1)

    Parameters
    ----------
    n : int
        The fibonacci number to compute.

    Returns
    -------
    int
        The fibonacci number computed efficiently.
    """
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

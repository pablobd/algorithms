def brute_force_solution(n: int) -> int:
    """Compute using brute force the fibonacci number n, where n starts at 0, so,
    F(0),... , F(8),... = 0, 1, 1, 2, 3, 5, 8, 13, 21,...

    Note the solution is T(n) = O(2^n)  in time and S(n) = O(2^n) in space. Why?
    Because there is a call to the function two times,
            T(n) = T(n-1) + T(n-2) + 3 > F(n),

    which grows exponentially fast, ~ O(2^n), a similar thing can be said of S(n).

    Parameters
    ----------
    n : int
        The fibonacci number to compute.

    Returns
    -------
    int
        The fibonacci number computed by brute force.
    """
    if n <= 1:  # by the definition, F(0) = 0 and F(1) = 1
        return n
    else:  # then F(n) = F(n-1) + F(n-2)
        return brute_force_solution(n - 1) + brute_force_solution(n - 2)

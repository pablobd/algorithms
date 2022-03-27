from solutions.mathematical import modulo_huge_fibonacci


def efficient_solution(n: int) -> int:
    """Compute the last digit of the sum of Fibonacci squares in an efficient way.

    The solution is inspired by the sequence of geometric representation of Fibonacci
    numbers in squares that resembles a spiral. We also make use of the
    modulo_huge_fibonacci efficient solution.

    Because the solution of the modulo of huge a fibonacci number is O(m), where m is
    the modulo, and this problem the modulo is constant, the time complexity is O(1).
    Similarly, the space complexity is constant, so O(1).

    Parameters
    ----------
    n : int
        The fibonacci number for which to compute the squared sum modulo 10.

    Returns
    -------
    int
        The squared sum modulo 10.
    """
    if n <= 1:
        return n
    n_mod = modulo_huge_fibonacci.efficient_solution((n, 10))
    n_mod_ = modulo_huge_fibonacci.efficient_solution((n - 1, 10))
    return n_mod * (n_mod + n_mod_) % 10

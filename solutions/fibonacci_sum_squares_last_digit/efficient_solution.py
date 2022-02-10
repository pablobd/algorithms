from solutions import modulus_huge_fibonacci


def efficient_solution(n: int) -> int:
    """Compute it in an efficient way. The solution is inspired by the sequence of
    geometric representation of fibonacci numbers in squares.

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
    n_mod = modulus_huge_fibonacci.efficient_solution((n, 10))
    n_mod_ = modulus_huge_fibonacci.efficient_solution((n - 1, 10))
    return n_mod * (n_mod + n_mod_) % 10

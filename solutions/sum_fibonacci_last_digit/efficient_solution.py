from solutions import modulus_huge_fibonacci


def efficient_solution(n: int) -> int:
    """Compute the solution of sum of Fibonacci numbers from 1 to n in an efficient way.

    The solution comes from the recursive formula, F(n+1) = F(n) + F(n-1),
        F(n-1) = F(n+1) - F(n)
        F(n-2) = F(n)   - F(n-1)
        F(n-3) = F(n-1) - F(n-2)
        .
        .
        .
        F(2)   = F(4)   - F(3)
        F(1)   = F(3)   - F(2)
    So, The sum F(1) + ... + F(n) = F(n+2) - 1

    Parameters
    ----------
    n : int
        The Fibonacci number to compute the sum.

    Returns
    -------
    int
        The sum of Fibonacci numbers.
    """
    if n <= 2:
        return n
    sum_n = modulus_huge_fibonacci.efficient_solution((n + 2, 10)) - 1
    return sum_n % 10

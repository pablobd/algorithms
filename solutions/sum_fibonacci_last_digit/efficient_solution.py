from solutions import modulo_huge_fibonacci


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

    Also since the last digit means taking the modulo 10, and taking the modulo of a
    Fibonacci number has a time complexity of O(m), where m is the modulo; we conclude
    the time complexity is contant, i.e. O(1). The space complexity is also constant.

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
    sum_n = modulo_huge_fibonacci.efficient_solution((n + 2, 10)) - 1
    return sum_n % 10

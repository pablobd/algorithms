from solutions import modulo_huge_fibonacci


def brute_force_solution(n: int) -> int:
    """Compute the last digit of the sum of all Fibonacci numbers until Fibonacci number
    n with a brute force solution.

    This solution has a time and space complexities O(n) and O(1).

    Parameters
    ----------
    n : int
        The Fibonacci number.

    Returns
    -------
    int
        The last digit of the sum of all Fibonacci numbers until Fibonacci number n.
    """
    sum_of_fibonacci_numbers = 0
    for i in range(n + 1):
        sum_of_fibonacci_numbers += modulo_huge_fibonacci.efficient_solution((i, 10))
    return sum_of_fibonacci_numbers % 10

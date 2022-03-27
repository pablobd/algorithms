from typing import Tuple


def efficient_solution(numbers: Tuple[int, int]) -> int:
    """Compute the greatest common divisor with an efficient algorithm.

    We follow the lemma that says,

    Lemma. Let a' be the remainder of a divided by b, then gcd(a, b) = gcd(b, a')
    Proof. Since a = a' + bq, for some q, then a % b = a' % b + bq % b = a' % b.

    Using the Lemma, we achieve a time complexity O(log(n)). See proof below:
    https://www.geeksforgeeks.org/time-complexity-of-euclidean-algorithm/

    Space complexity is O(1).

    Parameters
    ----------
    numbers : Tuple[int, int]
        Tuple of two intergers, the firs greater than the second.

    Returns
    -------
    int
        The gcd of the two numbers.
    """
    n, k = numbers
    if n < k:
        a = k
        b = n
    else:
        a = n
        b = k
    while True:
        modulo = a % b
        if modulo == 0:
            return b
        else:
            a = b
            b = modulo

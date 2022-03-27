def brute_force_solution(n: int) -> int:
    """Compute the last digit of the sum of fibonacci squares, i.e. S = F(0)^2 + F(1)^2
    + F(2)^2 + F(3)^2 + F(4)^2 + F(5)^2...

    The time and space complexities are O(n log(n)^2) and S(n) = O(n) respectively.

    Multiplication is a O(log(n)^2) operation, see:
    https://en.wikipedia.org/wiki/Multiplication_algorithm#Usage_in_computers

    Because of challenge fibonacci last digit, we know that summation of two very
    big numbers take O(log(n)), therefore
        T(n) = O(n log(n)^3)

    Space complexity is constant, hence O(1).

    Parameters
    ----------
    n : int
        The las fibonacci number of the summation of squares.

    Returns
    -------
    int
        The last digit of the sum of fibonacci squares.
    """
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

from solutions.greedy.coin_change.constants import COIN_CHANGE


def brute_force_solution(n: int) -> int:
    """Compute, with brute force, the minimal number of coins needed to change an amount
    n, given coins of 10, 5 and 1.

    This solution iterates over the three coins trying all possible combinations, for
    which the coin value is lower than the total, therefore the solution is O(2^n) in
    time complexity.

    Parameters
    ----------
    n : int
        The total amount to be changed.

    Returns
    -------
    int
        The number of coins needed to change the amount, n.
    """
    if n == 0:
        return n  # base case

    res = float("inf")
    for coin in COIN_CHANGE:
        if coin <= n:
            res = min([res, brute_force_solution(n - coin) + 1])

    return int(res)

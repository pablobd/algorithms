from solutions.greedy.coin_change.constants import COIN_CHANGE


def efficient_solution(n: int) -> int:
    """Compute, with a greedy algorithm, the minimal number of coins needed to change an
    amount n, given coins of 10, 5 and 1.

    The biggest coin smaller than n, must be part of the solution. To see that we apply
    reduction ad absurdum. Assume the coins are sorted, so k_1 < ... < k_{n+1}. Then,
    let N be the amount and assume k_{n+1} < N < k_n < k_{m}, for all m < n. Now, if k_n
    is not change for N, then we can group some coins so that their sum equals k_n.
    This is change with a smaller number of coins.

    Parameters
    ----------
    n : int
        The total amount to be changed.

    Returns
    -------
    int
        The number of coins needed to change the amount, n.
    """
    sorted_coins = sorted(COIN_CHANGE, reverse=True)
    number_of_coins: int = 0
    while n > 0:
        for coin in sorted_coins:
            if coin <= n:
                number_of_coins += 1
                n = n - coin
                break
    return number_of_coins

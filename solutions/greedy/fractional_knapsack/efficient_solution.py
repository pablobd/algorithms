from typing import List, Tuple

from solutions.greedy.fractional_knapsack.item import Item, sort_items


def efficient_solution(input_fractional_napsack: Tuple[int, int, List[Item]]) -> float:
    """
    Efficient solution for the fractional knapsack problem. We use a greedy algorithm
    to solve this problem. We start with the most valuable item and add it to the bag.
    The remaining problem is a reduced version of the original problem. Hence, we
    repeat.

    This solution is O(n * log(n)) in time complexity and O(1) in space complexity.

    Parameters
    ----------
    total_items : int
        Total number of items.
    capacity : int
        Capacity of the bag.
    items : List[Item]
        The list of item with its value and weight.

    Returns
    -------
    int
        The maximal value of fractions of items that fit into the knapsack.
    """
    _, capacity, items = input_fractional_napsack
    knapsack_value = 0.0
    capacity_left = capacity
    sorted_items = sort_items(items)
    for item in sorted_items:
        if item.weight <= capacity_left:
            knapsack_value += item.value
            capacity_left -= item.weight
        else:
            knapsack_value += item.fractional_value * capacity_left
            capacity_left = 0

        if capacity_left == 0:
            return knapsack_value

    return knapsack_value

from typing import List, Tuple

from solutions.greedy.fractional_knapsack.item import Item


def brute_force_solution(
    input_fractional_knapsack: Tuple[int, int, List[Item]]
) -> float:
    """
    Brute force solution for the fractional knapsack problem.

    This solution is O(2^n) in time complexity.

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
    total_items, capacity, items = input_fractional_knapsack
    # base case
    if total_items == 0 or capacity == 0 or (total_items == 1 and items[0].weight == 0):
        return 0

    # if weight of the nth item is 0 remove item from the list and change
    # total_items to total_items - 1
    if items[total_items - 1].weight == 0:
        items = items[:-1]
        total_items = total_items - 1

    # remove a fraction of the nth item from the list
    item = items[total_items - 1]
    remaining_item = _remove_fraction_from_item(item)
    items[total_items - 1] = remaining_item

    # return the maximum of two cases:
    # 1) nth item included
    # 2) not included
    return max(
        item.fractional_value
        + brute_force_solution((total_items, capacity - 1, items)),
        brute_force_solution((total_items, capacity, items)),
    )


def _remove_fraction_from_item(item: Item) -> Item:
    new_weight = item.weight - 1
    item_part_left = Item(value=item.fractional_value * new_weight, weight=new_weight)
    return item_part_left

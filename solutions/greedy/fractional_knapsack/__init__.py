"""Problem statement: a thief finds much more loot than his bag can fit. Help him to
find the most valuable combination of items assuming that any fraction of a loot item
can be put into his bag."""

from solutions.greedy.fractional_knapsack.brute_force_solution import (
    brute_force_solution,
)
from solutions.greedy.fractional_knapsack.efficient_solution import efficient_solution
from solutions.greedy.fractional_knapsack.item import Item

__all__ = ["brute_force_solution", "efficient_solution", "Item"]

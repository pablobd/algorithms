"""Solutions based on greedy strategy.

The greedy strategy consist in,
    1. split problem in two elements,
    2. prove that one element is part of the solution,
    3. prove that the other element is a subproblem,
    4. continue at 1 until you can't split it further."""

from solutions.greedy import coin_change

__all__ = ["coin_change"]

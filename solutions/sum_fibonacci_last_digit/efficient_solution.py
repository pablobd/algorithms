from solutions import modulus_huge_fibonacci


def efficient_solution(n: int) -> int:
    if n <= 2:
        return n
    sum_n = modulus_huge_fibonacci.efficient_solution((n + 2, 10)) - 1
    return sum_n % 10

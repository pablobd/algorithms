from solutions import modulus_huge_fibonacci


def brute_force_solution(n: int) -> int:
    sum_of_fibonacci_numbers = 0
    for i in range(n + 1):
        sum_of_fibonacci_numbers += modulus_huge_fibonacci.efficient_solution((i, 10))
    return sum_of_fibonacci_numbers % 10

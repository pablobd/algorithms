from solutions import fibonacci_last_digit


def efficient_solution(n: int) -> int:
    if n <= 2:
        return n
    sum_n = fibonacci_last_digit.efficient_solution(n + 2) - 1
    return sum_n % 10

def brute_force_solution(n: int, k: int) -> int:
    greatest_common_divisor = 1
    for i in range(min([n, k])):
        if n % i == 0 and k % i == 0:
            greatest_common_divisor = i
    return greatest_common_divisor

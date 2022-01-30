def brute_force_solution(n: int) -> int:
    if n <= 1:
        return n
    else:
        return brute_force_solution(n - 1) + brute_force_solution(n - 2)

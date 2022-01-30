def efficient_solution(n: int) -> int:
    if n == 0:
        return 0

    numbers = []
    for k in range(0, n + 1):
        if k <= 1:
            numbers.append(k)
        else:
            numbers.append(numbers[k - 1] + numbers[k - 2])

    return numbers[-1]

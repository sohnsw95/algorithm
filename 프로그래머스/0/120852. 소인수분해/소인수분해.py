def solution(n):
    a = []
    for i in range(2, n + 1):
        while n % i == 0:
            a.append(i)
            n = n // i
    result = list(set(a))
    result.sort()
    return result
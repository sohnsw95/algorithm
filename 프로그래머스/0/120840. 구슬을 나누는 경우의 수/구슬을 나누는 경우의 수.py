def factorial(n):
    fac = 1

    while n > 1:
        fac *= n
        n -= 1
    return fac


def solution(balls, share):
    ans = factorial(balls) // (factorial(balls - share) * factorial(share))
    return ans


print(solution(3,2))
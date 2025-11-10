def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    answer = 0
    for m in range(0,a):
        answer += month[m]
    result = day[(answer + b - 1) % 7]
    return result
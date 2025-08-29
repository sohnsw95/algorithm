from collections import deque

def solution(numbers, direction):
    answer = []
    dq = deque()

    for i in range(len(numbers)):
        dq.append(numbers[i])

    if direction == "left":
        a = dq.popleft()
        dq.append(a)

    if direction == "right":
        b = dq.pop()
        dq.appendleft(b)
    
    
    return list(dq)
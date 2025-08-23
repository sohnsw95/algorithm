def solution(num, k):
    answer = list(map(int, str(num)))

    if k in answer:
        for i in range(len(answer)):
            if k == answer[i]:
                return i+1
    else:
        return -1
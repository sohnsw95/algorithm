def solution(array):
    num = 0
    idx = 0
    answer = []
    for i in range(len(array)):
        if array[i] > num:
            num = array[i]
            idx = i
    answer.append(num)
    answer.append(idx)


    return answer
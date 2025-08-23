def solution(array):
    answer = [0, 0]
    big_array = answer[0]
    
    for i in range(len(array)):
        if array[i] > big_array:
            big_array = array[i]
            answer[0] = big_array
            answer[1] = i
    return answer
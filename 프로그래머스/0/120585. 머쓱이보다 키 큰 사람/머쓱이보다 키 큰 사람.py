def solution(array, height):
    n = len(array)
    
    answer = 0
    i = 0
    
    while i < n:
        if array[i] > height:
            answer += 1
        i += 1
            
    
    return answer
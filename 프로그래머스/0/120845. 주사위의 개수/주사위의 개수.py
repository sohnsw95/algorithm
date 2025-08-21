def solution(box, n):
    
    answer = 1
    
    for i in box:     
        b = i // n
        answer *= b
    
    
    return answer
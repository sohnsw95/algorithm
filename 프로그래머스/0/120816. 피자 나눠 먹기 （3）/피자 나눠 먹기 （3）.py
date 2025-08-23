def solution(slice, n):
    a = n % slice 
    b = n // slice
    answer = 0
    if a:
        answer = b + 1
    else:
        answer = b
    
        
    return answer
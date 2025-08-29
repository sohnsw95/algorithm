def solution(order):
    
    result = 0
    for i in str(order):
        if i == '3' or i == '6' or i == '9':
            result += 1
        
    return result
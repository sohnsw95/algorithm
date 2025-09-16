def solution(array):
    s = str(array)
    cnt = 0
    
    for i in s:
        if i == '7':
            cnt += 1
    
    return cnt
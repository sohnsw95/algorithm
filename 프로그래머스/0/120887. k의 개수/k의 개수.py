def solution(i, j, k):
        
    cnt = 0
    
    for x in range(i,j+1):
        for digit in str(x):
            if digit == str(k):
                cnt += 1
                
    return cnt
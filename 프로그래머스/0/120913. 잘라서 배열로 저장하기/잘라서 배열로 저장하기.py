def solution(my_str, n):
    K = len(my_str)
    M = K//n
    answer = []
    Nam = K % n 
    for i in range(0, K, n):
        answer.append(my_str[i:i+n])
    
    return answer

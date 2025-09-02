def solution(num_list, n):
    a = len(num_list)
    b = a//n
    answer = [[] for _ in range(b)]
    
    for i in range(b):
        
        for j in range(n):
            answer[i].append(num_list[i*n+j])
    
    
    return answer
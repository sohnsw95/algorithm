def solution(n_str):
    
    cnt = 0
    
    for i in n_str:
         
        if i != '0':
            break
        else:
            cnt += 1
    
    return n_str[cnt:]
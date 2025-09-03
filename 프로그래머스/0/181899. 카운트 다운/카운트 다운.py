def solution(start_num, end_num):
    
    # s_len = len(start_num)
    # e_len = len(end_num)
    # x = s_len - e_len
    answer = []
    
    for i in range(start_num, end_num-1, -1):
        answer.append(i)

    
    return answer
def solution(rsp):
    
    ga = 2
    ba = 0
    bo = 5
    answer = []
    
    for i in rsp:
        if i == '2':
            answer.append('0')
        elif i == '0':
            answer.append('5')
        elif i == '5':
            answer.append('2')
    
    return ''.join(answer)
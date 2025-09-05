def solution(s):
    '''
    1. 빈 딕셔너리 생성
    2. 문자열 카운트하여 딕셔너리에 value를 하나씩 쌓는다.
    3. value가 1인 key들만 출력한다.
    enumerate -> 인덱스넘버, value 뽑는다      
    
    1. sort정렬시킨, 새로운 리스트 생성
    2. 완전탐색으로 문자 카운트해라
    '''
    sort_s = sorted(s)
    answer = []
    for i in sort_s:
        if sort_s.count(i) == 1:
            answer.append(i)
    return "".join(answer)
            
        
        
        
        
    
    answer = ''
    return answer
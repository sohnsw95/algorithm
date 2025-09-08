def solution(emergency):
    
    new = sorted(emergency, reverse=True) # 내림차순 정렬
    my_dict = {}
    result = []
    rank = 1 # 순위 카운터
    while new:
        val = new.pop(0) # 가장 앞 원소 꺼내기
        my_dict[val] = rank
        rank += 1

    for i in emergency:
        result.append(my_dict[i])

    return result
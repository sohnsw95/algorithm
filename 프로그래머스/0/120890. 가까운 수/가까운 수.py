def solution(array, n):
    result = []
    my_dict = {}

    # 각 인덱스에 대해 n과의 차이를 기록
    for i in range(len(array)):
        a = array[i] - n
        my_dict[i] = a

    # 차이의 절댓값만 뽑아서 result에 저장
    for key, val in my_dict.items():
        result.append(abs(val))

    # 최소 차이값 찾기
    min_result = min(result)

    # 최소 차이를 가진 값들을 후보로 모음
    candidates = []
    for key, val in my_dict.items():
        if abs(val) == min_result:
            candidates.append(array[key])

    # 후보 중 가장 작은 값 반환
    return min(candidates)

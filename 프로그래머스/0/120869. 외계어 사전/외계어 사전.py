def solution(spell, dic):
    # spell을 정렬해서 기준 문자열을 만듭니다.
    target = "".join(sorted(spell))

    for word in dic:
        # word도 정렬해서 target과 '완전히 똑같은지' 비교합니다.
        if "".join(sorted(word)) == target:
            return 1

    return 2
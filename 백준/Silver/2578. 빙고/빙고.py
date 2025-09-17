bingo = []
speak = []
# 빙고는 2차원 배열로, speak는 1차원으로 평탄화하여 입력 받음.
for _ in range(5):
    bingo.append(list(map(int, input().split())))
for _ in range(5):
    speak.extend(list(map(int, input().split())))
# visted의 개념으로 사회자가 부른 숫자 값을 bingo에서 0으로 바꿔줘서 cnt진행

called = 0 # 사회자가 숫자를 부른 횟수
for num in speak:
    called += 1

    # found flag변수 선언(찾으면 바로 2중 루프 break)
    found = False
    # num을 빙고판에서 찾으면, bingo 0으로 표시
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0
                found = True
                break

        if found:
            break

    # 빙고가 몇개인지 계산 (항상 0부터 새로)
    bingo_cnt = 0

    # row 행 체크하기
    for row in bingo:
        if row.count(0) == 5:
            bingo_cnt += 1
    # 열 column 체크 (zip으로 전치)
    for col in zip(*bingo):
        if col.count(0) == 5:
            bingo_cnt += 1

    # 대각선 2개 체크 (우상향, 좌하향)
    daegak1 = [bingo[i][i] for i in range(5)]
    if daegak1.count(0) == 5:
            bingo_cnt += 1

    daegak2 = [bingo[i][5-1-i] for i in range(5)]
    if daegak2.count(0) == 5:
            bingo_cnt += 1

    if bingo_cnt >= 3:
        print(called)
        break
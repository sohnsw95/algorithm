T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 카운트는 아래의 for문이 돌고나면 초기화해주는거임
            cnt = 0

            for x in range(i, i+M):
                for y in range(j, j+M):
                    # 1. 범위를 잘못지정해줘서 못풀었음
                    cnt += graph[x][y]

                    '''
                    # cnt에 값을 넣어줄 때 M = 2일때는 밑에가 맞지만, 다른 경우에는 아님
                    cnt = graph[x][y]+graph[x+1][y]+graph[x][y+1]+graph[x+1][y+1]
                    내가 막힌 부분 : 특정 배열 구간의 합을 구하는 방법
                    M일때 만큼의 배열 합을 구해야함
                    # '''
                    ans = max(ans, cnt)
    print(f"#{tc} {ans}")

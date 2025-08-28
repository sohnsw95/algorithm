T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input())) for _ in range(N)]

    center = N // 2
    total = 0
    '''
    00100 # i=0 j=2
    01110 # i=1 j=1,2,3
    11111 # i=2 j=0,1,2,3,4
    01110 # i=3 j=1,2,3
    00100 # i=4 j=2
    '''

    # 위 아래가 xy 대칭임 절반까지만 구한다, # i는 0,1,2까지
    for i in range(center+1):
        '''
        j는 (2), (1,2,3), (0,1,2,3,4)
        i 가 0,1,2로 간다
        range(center-i, center+i+1)
        2,2
        1,4
        0,4
        '''
        # i=0 -> j=2 , i=1 -> j=1,2,3, i=2 -> j=0,1,2,3,4

        for j in range(center-i, center+i+1):
            total += grid[i][j] + grid[N-i-1][j]
    result = total - sum(grid[center])

    print(f"#{tc} {result}")
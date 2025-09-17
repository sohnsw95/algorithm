# 색종이의 장 수
N = int(input())
# 색종이를 놓을 공간 선언
grid = [[0] * 101 for _ in range(101)]

# (x,y)시작점, 너비와 높이 입력
for paper_num in range(1, N+1):
    x, y, w, h = list(map(int, input().split()))

    for i in range(x, x+w):

        for j in range(y, y+h):

            grid[j][i] = paper_num

for paper_num in range(1, N + 1):
    cnt = 0

    for y in range(101):
        for x in range(101):

            if grid[y][x] == paper_num:
                cnt += 1
    print(cnt)
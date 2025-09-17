# 색종이의 장 수
N = int(input())
# 색종이를 놓을 공간 선언
grid = [[0] * 1001 for _ in range(1001)]

# 실제 범위 체크
max_x = 0
max_y = 0


# (x,y)시작점, 너비와 높이 입력
for paper_num in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            grid[j][i] = paper_num
    max_x = max(max_x, x+w)
    max_y = max(max_y, y+h)


cnt = [0] * (N+1)

for y in range(max_y):
    for x in range(max_x):
        if grid[y][x] != 0:
            cnt[grid[y][x]] += 1

for paper_num in range(1, N + 1):
    print(cnt[paper_num])
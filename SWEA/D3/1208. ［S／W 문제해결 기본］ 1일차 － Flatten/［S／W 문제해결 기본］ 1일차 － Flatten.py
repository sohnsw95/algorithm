T = 10
for tc in range(1, T + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):
        boxes.sort()    # 가장 낮은~높은 순으로 정렬
        boxes[0] += 1             # 가장 낮은 곳에 1 쌓기
        boxes[-1] -= 1            # 가장 높은 곳에서 1 빼기

    boxes.sort() # 마지막에 한 번 더 정렬해서 차이 계산
    ans = boxes[-1] - boxes[0]
    print(f"#{tc} {ans}")

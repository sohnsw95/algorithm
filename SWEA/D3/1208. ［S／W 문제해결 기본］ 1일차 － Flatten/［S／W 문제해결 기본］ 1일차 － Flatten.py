T = 10
for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump): #dump 횟수만큼 진행한다.

        max_idx = boxes.index(max(boxes))
        min_idx = boxes.index(min(boxes))

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    ans = max(boxes) - min(boxes)
    print(f"#{tc} {ans}")
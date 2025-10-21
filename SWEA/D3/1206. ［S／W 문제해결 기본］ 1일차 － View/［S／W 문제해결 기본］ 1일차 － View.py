for tc in range(1, 11):
    N = int(input())
    Buildings = list(map(int, input().split()))

    len_B = len(Buildings)
    ans = 0
    for i in range(2, len_B-2):

        neighbor_max = max(Buildings[i-1], Buildings[i-2], Buildings[i+1], Buildings[i+2])

        if Buildings[i] > neighbor_max:
            ans += Buildings[i] - neighbor_max


    print(f"#{tc} {ans}")
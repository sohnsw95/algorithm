T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card_name = list(map(str, input().split()))
    # card_name의 길이
    a = len(card_name)
    arr = []
    # 짝수 일 때
    if a % 2 == 0:
        for i in range(a):

            # 반으로 나눠, 가장 앞과 반으로 나눴을때 앞을 append한다. 
            if i < a//2:
                arr.append(card_name[i])
                arr.append(card_name[i+a//2])
    # 홀수 일 때
    else:
        for i in range(a):

            # 반으로 나눠, 가장 앞과 반으로 나눴을때 앞을 append한다.
            if i < a//2:
                arr.append(card_name[i])
                arr.append(card_name[i + a//2 + 1])
            # 홀수 일때는, 중간값이 존재하므로 위 작업 이후에 중간값 추가
            if i == a//2:
                arr.append(card_name[a // 2])
    ans = ' '.join(arr)
    print(f"#{tc} {ans}")

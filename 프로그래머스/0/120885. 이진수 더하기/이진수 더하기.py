def solution(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)
    ans = a + b

    if ans == 0:               # 합이 0이면 바로 "0"
        return "0"

    bits = []
    while ans:
        ans, r = divmod(ans, 2)  # ans//=2, r=ans%2 를 한 번에
        bits.append(str(r))

    return ''.join(reversed(bits))  # 혹은 ''.join(bits[::-1])

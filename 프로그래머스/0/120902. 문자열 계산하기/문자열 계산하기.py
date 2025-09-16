def solution(my_string):
    tokens = my_string.split()   # ["3","+","4"]
    result = int(tokens[0])

    for i in range(1, len(tokens), 2):  # 연산자는 홀수 위치
        op = tokens[i]
        num = int(tokens[i+1])

        if op == '+':
            result += num
        elif op == '-':
            result -= num
    return result
'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''

# 종료조건이 없이 입력 받는 경우에는 try, except로 처리
# EOFError(End Of File) -> 더 이상 읽을 입력이 없다는 뜻 
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break
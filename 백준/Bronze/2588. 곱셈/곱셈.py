'''
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
      4 7 2        (1)
    × 3 8 5        (2)
    ---------
      2 3 6 0      (3)
    3 7 7 6        (4)
  1 4 1 6          (5)
    ---------
  1 8 1 7 2 0      (6)
(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
'''
def solve(num1, num2):

    num2 = list(reversed(num2)) # [3,8,5] -> [5,8,3]


    # 1) 세자리 수 이기때문에, 0~2로 직접 할당하여 구현
    # 2) 반복문 사용 구현 -> 채택
    result = []
    for digit in num2:
        result.append(num1 * digit)

    result.append(num1 * int("".join(map(str, reversed(num2)))))

    return result



num1 = int(input()) # 472
num2 = list(map(int, input())) # 385
for r in solve(num1,num2):
    print(r)


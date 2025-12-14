'''
문제
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
'''
N = int(input())
arr_N = list(map(int, input().split()))

result = []
# 최대 최소를 비교하기 위해 첫 번째 값을 기준으로 초기화
min_num = arr_N[0]
max_num = arr_N[0]
# 최소값, 최대값 구하기 방법 1
# min, max 함수 이용
# result.append(min(arr_N))
# result.append(max(arr_N))

# 최소값, 최대값 구하기 방법 2
# 반복문을 통해 가장 작은 값, 큰 값 비교하여 넣기
for i in arr_N:

    if i > max_num:
        max_num = i

    if i < min_num:
        min_num = i

result.append(min_num)
result.append(max_num)
print(*result)
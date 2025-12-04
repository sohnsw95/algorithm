'''
꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!
'''

a, b, c = map(int, input().split())
result = sum((a, b, c)) #sum 은 iterable list, tuple 중 하나를 넣어야 한다.
# sum 사용 말고 a+b+c 도 직관적으로 가능하다.
print(result)


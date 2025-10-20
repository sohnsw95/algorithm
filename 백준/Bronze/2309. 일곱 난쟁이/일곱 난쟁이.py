dwarf = []
for i in range(9):
    dwarf.append(int(input()))

# dwarf = [20, 7, 23, 19, 10, 15, 25, 8, 13]
dwarf.sort()

#전체 난쟁이 키의 합
sum_dwarf = sum(dwarf)
# dwarf = [7, 8, 10, 13, 15, 19, 20, 23, 25]


# i,j를 뽑는데 같은 값이 나오면 안된다. 즉, 다른 조합으로 뽑아야한다.
# i,j는 제외할 두명의 난쟁이를 가리키는 인덱스
for i in range(9):
    for j in range(i+1, 9):
        # 전체 난쟁이 키의 합 - i,j 난쟁이 키 == 100 일 때 조건 만족
        if sum_dwarf -(dwarf[i]+dwarf[j]) == 100:

            # 전체 난챙이에서 i, j가 아닌 경우 출력
            for x in range(9):
                # 뽑았는데, i도 아니고 j도 아닌 경우
                if x != i and x != j:
                    print(dwarf[x])
            exit()
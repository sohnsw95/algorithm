def solution(hp):
    general = 5
    soldier = 3
    worker = 1
    a=b=c=0
    a, b = divmod(hp, general)
    hp = b
    b, c = divmod(hp, soldier)
    hp = c
    c = hp // worker
         
    answer = a+b+c
    
    return answer
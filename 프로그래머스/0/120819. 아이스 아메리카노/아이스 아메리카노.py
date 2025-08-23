def solution(money):
    answer = []
    americano = 5500
    
    coffee = money // americano
    change = money % americano
    
    answer = [coffee, change]
    
    return answer
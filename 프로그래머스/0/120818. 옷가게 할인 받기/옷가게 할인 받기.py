def solution(price):
    
    if price < 100000:
        return price
    elif 300000 > price >= 100000:
        return int(price * 0.95)
    elif 500000 > price >= 300000:
        return int(price * 0.9)
    elif 500000 <= price:
        return int(price * 0.8)
    
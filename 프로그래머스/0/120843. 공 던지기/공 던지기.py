def solution(numbers, k):
    
    for i in range(k):
        answer = numbers[2*i % len(numbers)]
    return answer
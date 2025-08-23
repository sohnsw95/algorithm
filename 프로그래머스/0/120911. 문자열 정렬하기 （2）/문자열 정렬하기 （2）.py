def solution(my_string):
    
    answer = my_string.lower()
    a = "".join(sorted(answer))
    return a
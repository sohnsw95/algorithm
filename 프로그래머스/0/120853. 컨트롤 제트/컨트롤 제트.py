def solution(s):
    new_s = s.split()
    result = []
    
    for i in new_s:
        if i == "Z":
            if result:
                result.pop()
        
        else:
            result.append(int(i))
        
    return sum(result)
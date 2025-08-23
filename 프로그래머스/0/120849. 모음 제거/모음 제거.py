def solution(my_string):
    mouem = 'aeiou'
    result = []
    
    for i in my_string:
        
        if i in mouem:
            continue
            
        else:            
            result.append(i)      
            
    
    return "".join(result)
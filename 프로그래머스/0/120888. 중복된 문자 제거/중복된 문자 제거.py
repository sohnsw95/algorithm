def solution(my_string):
    stack = []
    
    for i in my_string:
        if i not in stack:
            stack.append(i)
    return "".join(stack)    

    

              
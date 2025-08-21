def solution(cipher, code):
    
    answer = list(cipher)
    answer = answer[code-1::code]
    
    return "".join(answer)
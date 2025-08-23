def solution(my_string, num1, num2):
    
    answer = []
    new_answer = []
    for i in my_string:
        answer.append(i)
    for i in range(len(answer)):

        if i == num1:
            new_answer.append(answer[num2])
        elif i == num2:
            new_answer.append(answer[num1])
        else:
            new_answer.append(answer[i])

    return "".join(new_answer)
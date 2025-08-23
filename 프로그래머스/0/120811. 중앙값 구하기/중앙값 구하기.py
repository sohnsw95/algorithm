def solution(array):
    
    array.sort()
    
#     while len(array) > 1:
        
#         maxa = max(array)
#         mina = min(array)
        
#         array.remove(maxa)
#         array.remove(mina)
    
    return array[len(array)//2]
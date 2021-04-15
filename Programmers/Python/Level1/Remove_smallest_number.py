def solution(arr):
    temp = []
    
    if len(arr) == 1: return [-1]
    temp = sorted(arr)
    arr.remove(temp[0])
    
    return arr
    
#def solution(arr):
#    if len(arr) == 1: return [-1]
#    arr.remove(min(arr))            # min()함수 사용 : min함수는 list중 가장 작은 수를 반환
#    return arr
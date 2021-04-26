def solution(x):
    answer = False
    a = str(x)
    result = 0
    
    for i in range(len(a)):
        result += int(a[i])
    
    if x % result == 0:
        answer = True
        
    return answer
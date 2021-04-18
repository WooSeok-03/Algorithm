import math

def solution(n):
    answer = 0
    
    n **= (1/2)
    a = math.trunc(n)
    
    if n - a > 0: return -1
    n += 1
    n **= 2
    
    return n
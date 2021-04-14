import math

def solution(s):
    answer = ''
    l = len(s)
    
    mid_idx = math.floor(l/2)
    
    if l % 2 == 0:
        answer = s[mid_idx-1 : mid_idx+1]
    else:
        answer = s[mid_idx]
    
    return answer
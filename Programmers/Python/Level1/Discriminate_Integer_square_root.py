import math

def solution(n):
    answer = 0
    
    n **= (1/2)         # **는 제곱하는 연산이다. ( n ** (1/2)를 하면 제곱근을 구할 수 있다.
    a = math.trunc(n)   # math.trunc()함수는 소수점을 버리는 함수이다.
    
    if n - a > 0: return -1
    n += 1
    n **= 2
    
    return n
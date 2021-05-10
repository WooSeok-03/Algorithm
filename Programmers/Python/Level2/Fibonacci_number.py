def fibo(n):
    n1, n2 = 0, 1
    for i in range(n):
        n1, n2 = n2, n1 + n2
    return n1

def solution(n):
    answer = fibo(n)
    answer %= 1234567
    
    return answer
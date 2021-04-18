def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

def solution(n, m):
    answer = []
    
    answer.append(gcd(n,m))
    answer.append(n * m / gcd(n,m))
    
    return answer
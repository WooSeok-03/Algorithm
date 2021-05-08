def is_prime(n):    # 에라토스테네스의 체 (소수 구하는 함수)
    arr = [False,False] + [True]*(n-1)
    primes=[]
    for i in range(2, n+1):
        if arr[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                arr[j] = False
    return primes

def solution(n):
    primes = is_prime(n)
    answer = len(primes)
    
    return answer
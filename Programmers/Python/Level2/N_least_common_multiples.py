def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def solution(arr):
    while len(arr) > 1:
        lcm = (arr[0] * arr[1]) / gcd(arr[0], arr[1])
        del arr[0:2]
        arr.insert(0, int(lcm))
    
    return arr[0]
    

# from fractions import gcd
# gcd를 구현할 필요없이 fractions 헤더파일에 gcd 함수를 사용해도 된다.
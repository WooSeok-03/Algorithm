import string
tmp = string.digits + string.ascii_lowercase

def convert(num, base) :        # 10진수 -> n(base)진수로 변환하는 함수
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n):
    n = convert(n, 3)
    reverse_n = list(reversed(list(n)))
    answer = "".join(reverse_n)
    
    return int(answer, 3)
def solution(n):
    l = list(str(n))        # string형 list로 변환
    l.sort(reverse=True)    # sort(reverse=True)로 내림차순 정렬
    return int(''.join(l))  # ''.join으로 l을 문자열로 변환후, int형으로 변환하여 return

def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for i, j in zip(A, B):
        answer += i * j

    return answer

# zip() : 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
# ex) 
# >>> list(zip([1, 2, 3], [4, 5, 6]))
# [(1, 4), (2, 5), (3, 6)]
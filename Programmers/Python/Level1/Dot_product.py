def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        answer += a[i] * b[i]
    
    return answer
    

#def solution(a, b):
#    answer = 0
#    for x, y in zip(a,b):  # zip() : 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
#        answer += x*y
#    return answer

# zip() 예시
# >>> list(zip([1, 2, 3], [4, 5, 6]))
# [(1, 4), (2, 5), (3, 6)]

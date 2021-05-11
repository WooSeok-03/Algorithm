def solution(n):
    answer = 0
    
    for i in range(1, n+1, 2):
        if n % i == 0:
            answer += 1
    return answer

# 주어진 자연수를 연속된 자연수의 합으로 표현하는 방법의 수는 주어진 수의 홀수 약수의 개수와 같다라는 정수론 정리가 있다.
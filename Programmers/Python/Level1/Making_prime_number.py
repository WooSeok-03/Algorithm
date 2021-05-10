import itertools

def is_prime(n):    # 소수인지 검사하는 함수
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

    
def solution(nums):
    answer = 0
    result = []
    
    combi = list(itertools.combinations(nums, 3))   # 조합을 이용하여 3개씩 묶음 ( 중복 허용 X )
    for num1, num2, num3 in combi:                  # 조합의 각 요소를 num1, num2, num3에 담는다.
        result.append(num1 + num2 + num3)
    
    for i in result:
        if is_prime(i):
            answer += 1
    return answer

# combinations을 사용하기 위해서는 itertools를 import해주어야 한다.
# combinations는 순서는 중요하지 않고, 중복은 허용안될때 주로 사용한다.
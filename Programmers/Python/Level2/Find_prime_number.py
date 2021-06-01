from itertools import permutations
import math

def is_prime(num):  # 소수 확인 함수
    if num < 2: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False        
    return True

def solution(numbers):
    answer = 0
    num = ""
    permu = []
    num_list = []
    
    for length in range(2, len(numbers)+1):
        permu += list(permutations(list(numbers), length))
    
    for i in range(len(permu)):
        for j in range(len(permu[i])):
            num += permu[i][j]    
        num_list.append(num)
        num = ""
    
    for i in numbers:
        if i not in num:
            num_list.append(i)

    num_list = list(map(int, num_list))
    num_list = list(set(num_list))
    
    for i in num_list:
        if is_prime(i):
            answer += 1
    
    return answer
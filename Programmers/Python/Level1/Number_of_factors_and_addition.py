def solution(left, right):
    answer = 0
    count = 0
    for divisor in range(left, right+1):
        for i in range(1, divisor+1):
            if divisor % i == 0:
                count += 1
        if count % 2 == 0:
            answer += divisor
        else:
            answer -= divisor
        count = 0
        
    return answer
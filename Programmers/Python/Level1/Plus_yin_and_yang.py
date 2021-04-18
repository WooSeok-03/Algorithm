def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] *= -1
        #answer += absolutes[i]     <- 이 코드로 합을 구해도 된다.
            
    for i in absolutes:
        answer += i
    
    return answer
    
    
# list 사용
#def solution(absolutes, signs):
#    answer = []
#    
#    for i in range(len(absolutes)):
#        if signs[i]:
#            answer.append(absolutes[i])
#        else:
#            answer.append(absolutes[i] * (-1))
#    
#    return sum(answer)
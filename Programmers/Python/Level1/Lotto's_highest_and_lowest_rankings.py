def solution(lottos, win_nums):
    answer = []
    count = 0
    
    # 최고 순위
    for number in lottos:
        if number in win_nums:
            count += 1
        elif number == 0:
            count += 1
            
    answer.append(count)
    count = 0
    
     # 최저 순위
    for number in lottos:
        if number in win_nums:
            count += 1
            
    answer.append(count)
    
    
    for i in range(2):
        if answer[i] == 6:
            answer[i] = 1
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 2:
            answer[i] = 5
        else:
            answer[i] = 6
    
    return answer
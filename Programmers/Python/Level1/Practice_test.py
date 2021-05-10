def solution(answers):
    answer = []
    score = [0 for i in range(3)]
    first_way = 1
    second_way = 1
    
    for i in range(len(answers)):
        # 1번 수포자
        if first_way == answers[i]:
            score[0] += 1
            
        first_way += 1
        if first_way > 5: 
            first_way = 1
        
        
        # 2번 수포자
        if i % 2 == 0:
            if answers[i] == 2:
                score[1] += 1
        else:
            if answers[i] == second_way:
                score[1] += 1
                
            second_way += 1
            if second_way == 2:
                second_way += 1
            if second_way > 5: 
                second_way = 1
        
        
        # 3번 수포자
        if i % 10 == 0 or i % 10 == 1:
            if answers[i] == 3:
                score[2] += 1
        elif i % 10 == 2 or i % 10 == 3:
            if answers[i] == 1:
                score[2] += 1
        elif i % 10 == 4 or i % 10 == 5:
            if answers[i] == 2:
                score[2] += 1
        elif i % 10 == 6 or i % 10 == 7:
            if answers[i] == 4:
                score[2] += 1
        elif i % 10 == 8 or i % 10 == 9:
            if answers[i] == 5:
                score[2] += 1
    
    
    top_rank = max(score)
    for i in range(len(score)):
        if top_rank == score[i]:
            answer.append(i + 1)
            
    return answer
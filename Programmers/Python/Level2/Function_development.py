def solution(progresses, speeds):
    answer = []
    count = 1
    
    day = 0
    day_list = []
    
    for i in range(len(progresses)):
        while(True):
            progresses[i] += speeds[i]
            day += 1
            if progresses[i] >= 100:
                day_list.append(day)
                day = 0
                break
    
    temp1 = day_list.pop(0)
    temp2 = day_list.pop(0)
    
    while True:
        if temp1 >= temp2:
            count += 1
        else:
            answer.append(count)
            temp1 = temp2
            count = 1
            
        if len(day_list) != 0:
            temp2 = day_list.pop(0)
        else:
            answer.append(count)
            break

    return answer
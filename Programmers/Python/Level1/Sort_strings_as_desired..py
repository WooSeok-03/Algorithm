def solution(strings, n):
    answer = []
    temp = []
    
    for i in strings:
        temp.append(i[n])
        
    strings.sort()
    temp.sort()
    
    for i in range(len(temp)):
        for j in range(len(strings)):
            if temp[i] == strings[j][n]:
                if strings[j] not in answer:
                    answer.append(strings[j])
    
    return answer
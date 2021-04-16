def solution(array, commands):
    answer = []
    arr = []
    
    for i in range(len(commands)):
        for j in range(3):
            a = commands[i][0] - 1
            b = commands[i][1]
            c = commands[i][2] - 1
            arr.append(array[a:b].sort())
        answer.append(sorted(array[a:b])[c])
    
    return answer
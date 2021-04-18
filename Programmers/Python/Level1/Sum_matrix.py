# answer변수 초기화 O
def solution(arr1, arr2):
    answer = arr1
    
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]      
    return answer
    

# answer변수 초기화 X
#def solution(arr1, arr2):
#    
#    for i in range(len(arr1)):
#        for j in range(len(arr1[i])):
#            arr1[i][j] += arr2[i][j]
#            
#    return arr1
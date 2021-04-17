def solution(n):
    answer = []
    a = []
    
    a = str(n)  # n을 string(a)으로 변환
    a = ''.join(reversed(a))    # string(a)을 list로 변환 & reversed함수로 string 뒤집기
    
    for i in a: # list(a)에 있는 요소를 반복
        answer.append(int(i))   # int형으로 변환해주고 answer에 삽입
        
    return answer
    
    #return list(map(int, reversed(str(n))))    # map함수를 사용하여 뒤집은 str(n)을 int로 바꾸어주고, list로 형변환 시킴.
    

# list() 함수 : 변수를 list로 변환
# map() 함수 : map은 리스트의 요소를 지정된 함수 처리해주는 함수
# reversed() 함수 : string을 뒤집어 주는 함수
# str() 함수 : 변수를 string형으로 바꾸어 주는 함수
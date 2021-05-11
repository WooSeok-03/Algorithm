def solution(n, arr1, arr2):
    answer = []
    temp1 = []
    temp2 = []
    
    for i in arr1:
        temp1.append(format(i, 'b').zfill(n))
    for i in arr2:
        temp2.append(format(i, 'b').zfill(n))
    
    for x, y in zip(arr1, arr2):
        answer.append(format(x | y, 'b').zfill(n))
    
    for i in range(len(answer)):
        answer[i] = answer[i].replace('0', ' ')
        answer[i] = answer[i].replace('1', '#')
         
    return answer
    
# format(변수, 'b')는 int형 변수를 2진수로 변환해준다.
# zfill(n)은 2진수의 자릿수를 n만큼 만들어주겠다는 뜻이다. |예) n == 6인 경우, 110 -> 000110 
# replace()는 첫번째 파라미터(문자)를 두번째 파라미터(문자)로 변경해주는 함수이다. ( string만 가능하다 )
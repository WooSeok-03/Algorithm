def solution(s):
    answer = True
    l = len(s)
    p = 0
    y = 0
    
    for i in range(l):
        if s[i] == 'p' or s[i] == 'P':
            p += 1
        if s[i] == 'y' or s[i] == 'Y':
            y += 1
            
    if y != p:
        return False
            
    return True
    

def solution(s):
    answer = True
    
    # lower() 함수는 문자열 전체를 소문자로 변환
    # count() 함수는 문자열의 개수를 반환
    # ( count() 함수의 매개변수(문자)를 넣어주면 문자의 개수를 반환 )
    
    return s.lower().count('p') == s.lower().count('y')
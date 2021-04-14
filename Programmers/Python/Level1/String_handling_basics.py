def solution(s):
    answer = True
    l = len(s)
    
    for i in range(l):
        if s[i].isalpha():              #알파벳인지 확인하는 함수 isalpha()를 사용 ( 알파벳만 있는 경우 return True )
        #if s[i].isdigit() == False:    #숫자인지 확인하는 함수 isdigit()을 사용 ( 숫자만 있는 경우 return True )
            return False
    if not(l == 4 or l == 6):
        return False
    
    return answer
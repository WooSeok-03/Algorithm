def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):   # startswith는 문자열이 특정문자로 시작하는지 여부를 알려준다 (bool)
            return False
    
    #for i, j in zip(phone_book, phone_book[1:]):
    #    if j.startswith(i):
    #        return False
    
    return True
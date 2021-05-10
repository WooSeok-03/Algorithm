def solution(n):
    answer = ''
    temp = []
    
    while n > 0:
        if n % 3 == 1:
            temp.append('1')
        elif n % 3 == 2:
            temp.append('2')
        elif n % 3 == 0:
            temp.append('4')  
        n = (n - 1) /3
        n = int(n)
    
    temp.reverse()
    answer = "".join(temp)
    
    return answer
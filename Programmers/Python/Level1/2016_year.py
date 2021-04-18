import calendar

def solution(a, b):
    answer = ''
    
    a = calendar.weekday(2016, a, b)
    if a == 0:
        answer = 'MON'
    elif a == 1:
        answer = 'TUE'
    elif a == 2:
        answer = 'WED'
    elif a == 3:
        answer = 'THU'
    elif a == 4:
        answer = 'FRI'
    elif a == 5:
        answer = 'SAT'
    elif a == 6:
        answer = 'SUN'
    
    return answer
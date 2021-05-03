upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
lower = "abcdefghijklmnopqrstuvwxyz"

def solution(s, n):
    answer = ''

    for i in s:
        if i == " ":
            answer += " "
        elif i.isupper():
            idx = upper.find(i) + n
            if idx > 25: idx -= 26
            answer += upper[idx]
        else:
            idx = lower.find(i) + n
            if idx > 25: idx -= 26
            answer += lower[idx]
        
    return answer
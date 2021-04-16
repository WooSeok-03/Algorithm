def solution(phone_number):
    answer = ""
    for i in range(len(phone_number)-4): answer += "*" 
    for i in range(-4, 0): answer += phone_number[i]
    return answer
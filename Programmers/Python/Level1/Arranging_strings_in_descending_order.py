def solution(s):
    answer = []
    for i in range(len(s)):
        answer.append(s[i])
        
    answer.sort(reverse=True)
    a = ''.join(answer)
    return a

    
#def solution(s):
#    return ''.join(sorted(s, reverse=True))

# ''.join()을 사용하면 list의 요소들을 띄워쓰기 없이 string으로 변환해준다.
# sorted()함수에서 reverse=True를 해주면 내림차순으로 정렬된다.
# sorted()함수의 매개변수에 list가 아닌 string을 넣어도 된다. ( 단, 반환은 list로 된다. )
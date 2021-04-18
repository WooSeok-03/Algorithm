def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 %s에 있다" % i


#def solution(seoul):
#    return "김서방은 {}에 있다".format(seoul.index("Kim"))

# seoul.index()를 사용하여 "Kim"이 인덱스 몇번에 있는지 알아낸다.

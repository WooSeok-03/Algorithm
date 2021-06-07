def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key=lambda x: x*3, reverse=True)   # lambda x : x*3 은 자리수를 맞추어 주기 위해서
    # String은 비교할때 첫번째 문자로 비교한다.
    return str(int(''.join(num)))
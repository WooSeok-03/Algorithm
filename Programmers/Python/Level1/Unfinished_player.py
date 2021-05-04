def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    completion.append("")   # IndexError: list index out of range 방지
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]

        
#import collections

#def solution(participant, completion):
#    answer = collections.Counter(participant) - collections.Counter(completion)
#    return list(answer.keys())[0]

# participant와 completion를 collections.Counter에 넣는다.
# ( collections.Counter는 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체이다. )
# ( collections.Counter는 딕셔너리 형태로 반환된다. )

# collections.Counter(participant) - collections.Counter(completion)를 통해 같은 값은 모두 없애준다.
# 딕셔너리 형태로 반환되었기 때문에, answer.keys()를 list로 변경한 뒤, 0번째 인덱스를 return해준다.
# ( str(answer.key())를 하게 될 경우 "dict_keys(['ABC'])" 형태로 반환되기 때문에 list를 거쳐준다. )
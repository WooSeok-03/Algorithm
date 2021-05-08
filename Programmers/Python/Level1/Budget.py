def solution(d, budget):
    answer = 0
    department_budget = 0
    d.sort()
    for i in d:
        department_budget += i
        if budget < department_budget:
            break
        answer += 1
    return answer
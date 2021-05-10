def solution(N, stages):
    answer = []
    stage_player = []
    reach = []
    fail = []
    count = 0
    no_count_player = 0
    
    for i in range(1, N+1): # stage에 도착한 유저의 수 (stage_player)
        for j in stages:
            if i == j:
                count += 1
        stage_player.append(count)
        count = 0
    
    for i in stages:    # N에 해당하지 않는 stage에 도착한 유저의 수 (no_count_player)
        if i > N:
            no_count_player += 1
    
    for i in range(len(stage_player)):  # stage에 도달한(도착&클리어한) 유저의 수 (reach)
        reach.append(sum(stage_player[i:]) + no_count_player)
    # 0번째 인덱스 : stage 1에 도달한 유저의 수
    # 1번째 인덱스 : stage 2에 도달한 유저의 수 ...
         
    for i in range(len(reach)): # 해당 stage의 실패율 구하기 (fail)
        if stage_player[i] != 0 and reach[i] != 0:
            fail.append(stage_player[i]/reach[i])
        else:
            fail.append(0)
    
    sort_fail = sorted(fail, reverse=True)
    
    for i in range(N):  # 실패율이 높은 순서대로 answer에 추가
        for j in range(len(fail)):
            if sort_fail[i] == fail[j]:
                if j+1 not in answer:
                    answer.append(j+1)
            
    return answer
import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) != 1:
        sum_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, sum_scoville)
        answer += 1
        
    for i in scoville:
        if i < K:
            return -1
        
    return answer
    
    
# heapq를 import하여 heap(Queue)을 사용하였습니다.
# heapq.heapify(list)는 list를 heap으로 만들어 줍니다. ( 이 때 힙에는 오름차순으로 정렬된다. )
# heapq.heappush(heap, 추가할 값)은 heap에 두번째 파라미터의 값을 push합니다.
# heapq.heappop(heap)는 heap의 가장 첫 번째 값을 꺼냅니다. ( 이 때 반환도 함께 됩니다. )
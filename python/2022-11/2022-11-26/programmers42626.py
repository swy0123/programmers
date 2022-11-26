# Lv.2 더 맵게 : 힙

import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    for i in range(len(scoville)-1):
        if scoville[0] >= k:
            break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer += 1
    
    if scoville[0] < k:
        answer = -1
        

    return answer

print(solution([1, 2], 7))
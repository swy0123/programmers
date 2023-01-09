# Lv.3 디스크 컨트롤러 : 힙

# jobs	                    return
# [[0, 3], [1, 9], [2, 6]]	9

import heapq

def solution(jobs):
    answer = 0
    cur, i, start = 0, 0, -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= cur:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            tmp = heapq.heappop(heap)
            start = cur
            cur += tmp[0]
            answer += (cur - tmp[1])
            i += 1
        else:
            cur += 1
        
    return answer//len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))
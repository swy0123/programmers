import heapq

def solution(n, arr):
    arr.sort()
    heap = []
    answer = 1
    heapq.heappush(heap, arr[0][1])
    for i in range(1, n):
        if heap[0] >= arr[i][0]:
            heapq.heappush(heap, arr[i][1])
        else:
            answer += 1
            heap = []
            heapq.heappush(heap, arr[i][1])
    return answer

n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

print(solution(n, arr))
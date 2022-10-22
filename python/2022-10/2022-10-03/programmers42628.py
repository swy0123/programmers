# 이중우선순위큐
# 명령어	수신 탑(높이)
# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	    큐에서 최댓값을 삭제합니다.
# D -1	    큐에서 최솟값을 삭제합니다.

# operations	                                                                return
# ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	                [0,0]
# ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	[333, -45]

def solution(operations):
    priorityQueue = []
    answer = []
    for i in operations:
        if i[0] == 'I':
            priorityQueue.append(int(i[2:]))
            priorityQueue.sort()
        else:
            if not priorityQueue:
                continue
            if i[2] == '-':
                priorityQueue.pop(0)
            else:
                priorityQueue.pop()
    
    if not priorityQueue:
        answer = [0, 0]
    else:
        answer = [priorityQueue[-1], priorityQueue[0]]

    return answer


# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))


# 소감
# heapq를 사용하여 푸는데 실패하여 조악한 풀이로 해결함
# 프로그래머스에서 제한시간에 대해 관대한 편인지 통과하긴 했지만 추후 다시 풀어볼 것
# 두 heap을 동기화하는 법이나 이중우선순위큐 알고리즘을 이해할 필요가 있음
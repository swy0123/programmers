# Lv.2 다리를 지나는 트럭

# 큐를 사용하여 풀이

# bridge_length	weight	truck_weights	                return
# 2	            10	    [7,4,5,6]	                    8
# 100	        100	    [10]	                        101
# 100	        100	    [10,10,10,10,10,10,10,10,10,10]	110

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [deque([]), 0]
    truck = deque(truck_weights)

    while True:
        if bridge[0] and bridge[0][-1][1] == answer:
            bridge[1] -= bridge[0][-1][0]
            bridge[0].pop()
        if truck and len(bridge[0]) < bridge_length and bridge[1] + truck[0] <= weight:
            cur = truck.popleft()
            bridge[1] += cur
            bridge[0].appendleft((cur, bridge_length + answer))
        if len(bridge[0]) == 0 and len(truck) == 0:
            break
        answer += 1

    return answer+1

print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]	))
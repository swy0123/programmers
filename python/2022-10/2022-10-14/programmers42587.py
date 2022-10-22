# 프린터

# 소감
# 먼저 뽑아야되는 우선순위를 정하고 출력되는 우선순위를 변경하여 문제를 해결했다.
# 효과적인 문제 해결을 위해 배열의 뒤에서 pop을 할 수 있도록 구성했다.

# priorities	        location	return
# [2, 1, 3, 2]	        2	        1
# [1, 1, 9, 1, 1, 1]	0	        5

def solution(priorities, location):
    answer = 0
    seq = priorities[:]
    seq.sort()

    idx = 0
    while seq:
        max = seq[-1]
        
        # print(idx, max)
        if priorities[idx] == max:
            priorities[idx] = 0
            seq.pop()
            answer += 1
            if idx == location:
                break
        idx += 1
        if idx == len(priorities):
            idx = 0

    return answer


# print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
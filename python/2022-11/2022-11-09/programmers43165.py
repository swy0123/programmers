# 타겟 넘버

# dfs를 이용하여 풀이

# numbers	        target	return
# [1, 1, 1, 1, 1]	3	    5
# [4, 1, 2, 1]	4	2

def solution(numbers, target):
    answer = []
    stack = []
    ret = 0
    stack.append((numbers[0], 0))
    stack.append((-numbers[0], 0))
    while stack:
        cur = stack.pop()
        # print('cur', cur)
        if cur[1]+1 < len(numbers):
            stack.append((cur[0]+numbers[cur[1]+1], cur[1]+1))
            stack.append((cur[0]-numbers[cur[1]+1], cur[1]+1))
        else:
            answer.append(cur[0])
    # print(stack)
    for i in answer:
        if i == target:
            ret += 1

    return ret


print(solution([4, 1, 2, 1], 4))
# 네트워크

# dfs를 이용하여 해결함

# n	computers	                        return
# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

def solution(n, computers):
    answer = 0
    
    link = [False for i in range(n)]

    for i in range(len(computers)):
        stack = []
        if link[i] == False:
            stack.append(computers[i])
            link[i] = True
            answer += 1
        else:
            continue

        while len(stack) > 0:
            cur = stack.pop()
            for j in range(i, len(cur)):
                if cur[j] == 1 and link[j] is False:
                    stack.append(computers[j])
                    link[j] = True

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# Lv.2 주식가격

# 스택을 활용하여 풀이

# prices	        return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

def solution(prices):
    answer = [0 for i in range(len(prices))]
    stack = []

    for i, price in enumerate(prices):
        if not stack:
            stack.append((price, i))
        elif stack[-1][0] <= price:
            stack.append((price, i))
        else:
            while stack:
                if stack[-1][0] > price:
                    cur = stack.pop()
                    answer[cur[1]] = i - cur[1]
                else:
                    break
            stack.append((price, i))
    i = len(prices)-1
    while stack:
        cur = stack.pop()
        answer[cur[1]] = i - cur[1]
    return answer

print(solution([1, 2, 3, 2, 3]))

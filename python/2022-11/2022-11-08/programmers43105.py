# 정수 삼각형
# DP를 이용하여 품

# triangle	                                                result
# [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30

def solution(triangle):

    for i in range(1, len(triangle)):
        for j in range(i+1):
            left = 0
            if j > 0: left = triangle[i-1][j-1]
            right = 0
            if j < len(triangle[i])-1: right = triangle[i-1][j]
            triangle[i][j] += left if left > right else right

    answer = sorted(triangle[len(triangle)-1][:])

    return answer[-1]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

# [7]
# [3, 8]
# [8, 1, 0]
# [2, 7, 4, 4]
# [4, 5, 2, 6, 5]
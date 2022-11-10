 # 폰켓몬

# 해시문제로 분류되지만 set을 이용해 중복을 제거하여 풀이

# nums	        result
# [3,1,2,3]	    2
# [3,3,3,2,2,4]	3
# [3,3,3,2,2,2]	2

def solution(nums):
    answer = 0
    n = len(nums)
    s = set(nums)
    if len(s) > n//2: answer = n//2
    else: answer = len(s)
    return answer

print(solution([3,3,3,2,2,2]))
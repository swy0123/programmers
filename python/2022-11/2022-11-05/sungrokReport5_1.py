# 자리 값의 합 
# DP

def solution(n, s, cache):
    if s==0:
        return 0
    if s==1:
        return 1
    
    if (n, s) in cache:
        return cache[(n, s)]
    count = 0
    for i in range(n):
        count += solution(n-i, s-1, cache)
    
    cache[(n, s)] = count 
    print(cache)
    return count


# l, s = int(input().split())
l, s = 4, 9
dic = {}

print(solution(l, s, dic))


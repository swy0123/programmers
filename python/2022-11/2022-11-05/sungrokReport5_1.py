# 자리 값의 합 
# DP

def solution(n, s, cache=dict()):
    if n==0:
        return 0
    elif n == 1:
        return 1
    if s<0:
        return 0

    if (n, s) in cache:
        return cache[(n, s)]
    count = 0
    for i in range(s):
        count += solution(n-1, s-i, cache)
    if s > 9:
        count -= n*(s-9)-1
    cache[(n, s)] = count 
    print(cache)
    return count

l, s = 3, 27
dic = {}

print(solution(l, s, dic))
# print(solution(4, 2, dic))
# print(solution(5, 3, dic))
# print(solution(20, 1, dic))

# def solution(n, s, cache):
#     if n==0:
#         return 0
#     if n == 1 and s > 9:
#         return 0
#     elif n == 1:
#         return 1

    
#     if (n, s) in cache:
#         return cache[(n, s)]
#     count = 0
#     for i in range(n):
#         count += solution(n-1, s-i, cache)
    
#     cache[(n, s)] = count 
#     print(cache)
#     return count


    # if (n, s) in cache:
    #     return cache[(n, s)]
    # count = 0
    # for i in range(n):
    #     count += solution(n-i, s-1, cache)
    
    # cache[(n, s)] = count 
    # print(cache)
    # return count

# l, s = int(input().split())
# l, s = 2, 15
# dic = {}

# print(solution(l, s, dic))


# print(solution1(l, s))
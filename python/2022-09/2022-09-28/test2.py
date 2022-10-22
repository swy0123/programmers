import sys

answer = 0
# arr = list(map(int, input().split()))
arr = [9, 1, 3, 2, 7, 0, -2, 4, 5]
length = len(arr)
print(length)


for i in range(length):
    cur = arr[:i+1]
    cur.sort()
    print(cur, cur[i//3])
    answer += cur[i//3]

print(answer)
print(arr)

# 9 1 3 2 7 0 -2 4 5
# [-2, 0, 1, 2, 3, 4, 5, 7, 9]

# 0~8

# -2
# -2
# -2
# 0
# 0
# 0

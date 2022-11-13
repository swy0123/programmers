import sys
import itertools

T = int(sys.stdin.readline())

for i in range(1, T+1):
    print(i)
    arr = []
    for j in range(1, i+1):
        arr.append(j)
    com = list(itertools.combinations(arr, i))
    for j in com:
        print(j, len(j))
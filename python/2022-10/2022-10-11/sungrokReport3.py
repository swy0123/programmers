# 2차원 정렬된 배열에서 탐색(분할정복)
# 이차원 N^2 리스트에서 서로 다른 정수들이 행과 열마다 오름차순으로 정렬되어 있을 때,
# 주어진 수 k가 있으면 해당 X,Y값을 반환하고 없으면 (-1, -1)을 반환하라.

import sys

def Rotating_List(A, a, b, c, d):
    x1 = (a+c) // 2     # 점 p1의 x좌표
    y1 = (a+c) // 2 + 1 # 점 p2의 x좌표
    x2 = (b+d) // 2     # 점 p1의 y좌표
    y2 = (b+d) // 2 + 1 # 점 p2의 y좌표
    while A[x1][x2] <= A[y1][y2]:
        if a+1 == c and b+1 == d:   # n == 2일 때, 결과 반환
            if A[a][b] == k:
                return (a, b)
            elif A[c][b] ==k:
                return (c, b)
            elif A[a][d] ==k:
                return (a, d)
            elif A[c][d] ==k:
                return (c, d)
            else:
                return(-1,-1)
        if k == A[x1][x2]:
            return (x1,x2)
        elif k == A[y1][y2]:
            return (y1,y2)
        elif k < A[x1][x2]: # 1, 2, 3 사분면
            return max(Rotating_List(A, a, b, x1, x2), Rotating_List(A, a, y2, x1, d), Rotating_List(A, y1, b, c, x2))
        elif k > A[y1][y2]: # 1, 3, 4  사분면
            return max(Rotating_List(A, a, y2, x1, d), Rotating_List(A, y1, b, c, x2), Rotating_List(A, y1, y2, c, d))
        elif A[x1][x2] < k < A[y1][y2]: # 1, 3 사분면
            return max(Rotating_List(A, a, y2, x1, d), Rotating_List(A, y1, b, c, x2))

n, k = map(int, sys.stdin.readline().split())
A=[]
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))
print(Rotating_List(A, 0, 0, n-1, n-1))


# 4 16
# 2 5 10 19
# 3 8 16 19
# 7 20 20 32
# 13 25 37 44

# 8 23
# 1 2 3 4 5 6 7 8
# 9 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31 32
# 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48
# 49 50 51 52 53 54 55 56
# 57 58 59 60 61 62 63 64

# 4 -20
# -24 -9 -8 18
# -21 -7 3 19
# -20 -4 7 22
# -10 -2 15 25
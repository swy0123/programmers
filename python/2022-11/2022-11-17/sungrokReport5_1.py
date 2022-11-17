# 자리 값의 합 
# DP

def solution(l, s):
    arr = [[0]*(s+1) for _ in range(l+1)]
    if s<10:
        for i in range(1, s+1):
            arr[1][i] = 1
        for i in range(1, l+1):
            arr[i][1] = 1
        for i in range(2, l+1):
            for j in range(2, s+1):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
    else:
        for i in range(1, l+1):
            arr[i][1] = 1
        for i in range(1, 10):
            arr[1][i] = 1
        for i in range(2, l+1):
            for j in range(2, 10):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
            for k in range(10, s+1):
                for a in range(0, 10):
                    arr[i][k] += arr[i-1][k-a]
        
    
    return arr[l][s]


l, s = map(int, input().split())

print(solution(l, s))

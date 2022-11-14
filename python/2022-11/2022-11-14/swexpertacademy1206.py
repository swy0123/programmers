# D3. 1206 View
import sys

for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    answer = 0
    for i in range(n):
        if i == 0:
            if arr[0] > arr[1] and arr[0] > arr[2]:
                answer += arr[0] - max(arr[1], arr[2])
        elif i == 1:
            if arr[1] == max(arr[0:4]):
                answer += arr[1] - max(arr[0], arr[2], arr[3])
        elif i < n-2:
            if arr[i] == max(arr[i-2:i+3]):
                answer += arr[i] - max(arr[i-2:i]+arr[i+1:i+3])
        elif i == n-2:
            if arr[i] == max(arr[i-2:]):
                answer += arr[i] - max(arr[i-2], arr[i-1], arr[-1])
        elif i == n-1:
            if arr[i] > arr[i-1] and arr[i] > arr[i-2]:
                answer += arr[i] - max(arr[i-1], arr[i-2])
    print('#' + str(test_case), answer)
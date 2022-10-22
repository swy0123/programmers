# 멀리 뛰기
# n	| result
# 4	| 5
# 3	| 3

def solution(n):
    arr = [1, 2]

    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2])

    return arr[n-1] % 1234567

print(solution(4))

# 소감
# DP를 이용하여 간단히 풀 수 있었지만 지난번에 학습했던 파이썬의 멀티플 할당을 이용하면 더욱 간단히 할 수 있다는 점을 잊고 있었다.
# 파이썬의 장점을 살리기 위해서 이런 사용법도 익힐 필요가 있는 것 같다.

# def solution(num):
#     a, b = 1, 2

#     for i in range(2,num):
#         a, b = b, a+b

#     return b


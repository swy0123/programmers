# N개의 최소공배수

# arr	      | result
# [2,6,8,14]  | 168
# [1,2,3]	  | 6

# def solution(arr):
#     answer = 1
#     arr.sort(reverse = True)

#     while True:
#         cur = arr.pop()
#         answer *= cur
#         if not arr:
#             break

#         length = len(arr)
#         for i in range(length):
#             if arr[i] % cur == 0:
#                 arr[i] = arr[i] // cur

#     return answer

# print(solution([9,21]))

# 유클리드 호제법 사용

def solution(arr):
    answer = 0
    arr.sort()
    answer = arr.pop()
    # print(arr, max)

    while arr:
        a = answer
        b = arr.pop()
        answer = a*b
        while a%b != 0:
            mod = a%b
            a = b
            b = mod
        # print(a, b)
        answer //= b

    return answer

print(solution([9, 30]))

print(solution([2,6,8,14]))

print(solution([1,2,3]))

# 소감
# 유클리드 호제법이 기억에 나지 않아 생각보다 많은 시간이 걸린 것 같다.
# 최소공배수를 구하는 부분을 함수로 만들어 보면 더 좋을 것 같다는 생각이 든다.
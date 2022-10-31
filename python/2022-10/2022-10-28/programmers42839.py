# 소수 찾기
# 소감
# 처음에 소수 찾기를 보자마자 에라토스테네스의 체를 이용하여 풀 생각을 하였다. 그리고 set을 이용해 문제를 풀어 보려고 했지만 중복되는 숫자가 있어 불가능했다.
# 결과적으로 숫자의 범위도 크지 않았고 일부의 숫자만 소수인지 판별하면 되기 때문에 함수를 이용해 순열을 구하고 소수인지 판별해 해결했다.
# 순열과 조합을 구하는 문제는 항상 귀찮을 뿐만 아니라 수행시간도 무척 많이 들었는데 함수를 이용하면 쉽고 빠르게 해결할 수 있어 좋은 것 같다.

from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    # print(numbers)
    per = []

    for i in range(1, len(numbers)+1):
        per += list(permutations(numbers, i))
    num = set([int(''.join(t)) for t in per])
    # print(num)

    for i in num:
        max = int(i)

        if max < 2:
            continue
        else:
            check = True
            for j in range(2, int(max**0.5)+1):
                if max%j == 0:
                    check = False
                    break
            if check:
                answer += 1

    return answer


print(solution("17"))
print(solution("011"))
print(solution("1231"))





# def solution(numbers):
#     answer = 0
#     numbers = list(map(int, numbers.strip()))

#     s = set(numbers)

#     max = int(''.join(str(i) for i in sorted(numbers, reverse=True)))
#     # print(max)
#     arr = [True for i in range(max+1)]
#     arr[0] = False
#     arr[1] = False
#     for i in range(2, max+1):
#         if arr[i] == True:
#             for j in range(i*2, max, i):
#                 arr[j] = False
#             cur = set(map(int, str(i)))
#             # print(cur)
#             if s > cur:
#                 print(i)
#                 answer += 1

#     return answer

# print(solution("17"))
# print(solution("011"))
# print(solution("1231"))
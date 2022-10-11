# 문제 설명
# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

# 예를들어

# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 와 같이 이어집니다.

# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

# 제한 사항 n은 2 이상 100,000 이하인 자연수입니다.


def solution(n):
    answer = 0

    fib = [0 for _ in range(100001)]
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n+1):
        fib[i] = fib[i-2] + fib[i-1]
    
    answer = fib[n] % 1234567

    return answer

print(solution(5))

# 풀이 후 개선 점
# 1. 처음에 100001짜리 리스트를 만드는 것보다 append를 이용하는 것이 메모리 절약
# 2. 훨씬 간단한 코드 있음 - 파이썬의 특징을 이용
# def fibonacci(num):
#     a,b = 0,1
#     for i in range(num):
#         a,b = b,a+b
#     return a

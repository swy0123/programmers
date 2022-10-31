# 백준 1918 후위 표기식

# 소감
# 알고리즘 복습 차원에서 stack을 이용한 기본적인 문제를 해결해보았다. 파이썬은 문자열 처리가 간단하단 것을 다시금 느낄 수 있었다.


import sys

def solution(string):
    stack = []
    answer = []

    for i in string:
        # print(answer, '   ', stack)
        if i in ('*', '/', '+', '-', '(', ')'):
            if i == ')' and stack:
                while stack:
                    j = stack.pop()
                    if j == '(': break
                    answer.append(j)
            elif (i == '+' or i == '-') and len(stack)>0:
                if stack[-1] != '(':
                    while stack:
                        if stack[-1] == '(': break
                        answer.append(stack.pop())
                    stack.append(i)
                else: stack.append(i)
            elif (i == '/' or i == '*') and len(stack)>0:
                if stack[-1] != '(':
                    if stack[-1] == '/' or stack[-1] == '*':
                        answer.append(stack.pop())
                stack.append(i)
            else: stack.append(i)
        else:
            answer.append(i)
    while stack:
        answer.append(stack.pop())
    
    return str(''.join(answer))

input = sys.stdin.readline().strip()

print(solution(input))
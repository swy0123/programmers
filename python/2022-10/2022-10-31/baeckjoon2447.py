# 백준 2447 별찍기 - 10
# 파이썬의 문자열 연산 방법을 복습할 수 있었다.
# 배열을 출력 할 때 *arr, sep='\n'을 이용하면 더 간단하게 배열을 출력할 수 있다.

def star(s, n):
    tmp = []

    if n == 3:
        return s
    
    for i in s:
        tmp.append(i*3)
    for i in s:
        tmp.append(i+' '*len(i)+i)
    for i in s:
        tmp.append(i*3)
    return star(tmp, n//3)

start = ['***', '* *', '***']

input = int(input())

print(*star(start, input), sep='\n')

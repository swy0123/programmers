# 14692. 통나무 자르기 D3

t = int(input())

for test_case in range(1, t+1):
    tc = int(input())
    answer = '#' + str(test_case)
    if tc % 2 == 0: answer += ' Alice'
    else: answer += ' Bob'
    print(answer)
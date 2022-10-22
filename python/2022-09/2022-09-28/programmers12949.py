# 행렬의 곱셈

# 1 4     3 3
# 3 2     3 3
# 4 1

def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(answer)):
        for j in range(len(arr1[i])):
            for k in range(len(arr1[i])):
                answer[i][j] += arr1[i][k]*arr2[k][j]

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))



# (0,0*0,0 0,1*1,0) (0,0*0,1 0,1*1,1)
# (1,0*0,0 1,1*1,0) (1,0*0,1 1,1*1,1)
# (2,0*0,0 2,1*1,0) (2,0*0,1 2,1*1,1)

# 소감
# 행렬의 곱셈법을 알면 쉽게 풀 수 있는 문제 같다.
# 물론 핼렬의 곱셈법을 알아야 한다.


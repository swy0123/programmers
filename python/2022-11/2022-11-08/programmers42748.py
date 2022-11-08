# K번째수

# 정렬 문제

# array	                commands	                        return
# [1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]

def solution(array, commands):
    answer = []
    for i in commands:
        resert = sorted(array[i[0]-1:i[1]])
        answer.append(resert[i[-1]-1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
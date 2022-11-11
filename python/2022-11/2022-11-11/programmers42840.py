# Lv.1 모의고사

# 완전탐색

# answers	    return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

def solution(answers):
    fst = [1, 2, 3, 4, 5] * (len(answers)//5+1)
    sec = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8+1)
    thd = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10+1)
    score = [[0,1], [0,2], [0,3]]
    
    for i in range(len(answers)):
        if answers[i] == fst[i]: score[0][0] += 1
        if answers[i] == sec[i]: score[1][0] += 1
        if answers[i] == thd[i]: score[2][0] += 1
    score.sort(key=lambda x: (x[0], -x[1]) ,reverse=True)
    answer = [score[0][1]]
    for i in score[1:]:
        if i[0] == score[0][0]:
            answer.append(i[1])

    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]))
# 성격 유형 검사하기
# 딕셔너리를 이용하면 매우 쉽게 풀리는 문제인 것 같다.
# mbti검사를 떠올리며 푸니 상당히 흥미로운 문제였다.

# survey	                        choices	        result
# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
# ["TR", "RT", "TR"]	            [7, 1, 3]   	"RCJA"

# R T
# C F
# J M
# A N

def solution(survey, choices):
    answer = ''
    dic = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    
    for i in range(len(survey)):
        if survey[i][0] > survey[i][1]:
            survey[i] = survey[i][1]+survey[i][0]
            choices[i] = 8-choices[i]
        dic[survey[i]] = dic[survey[i]] + choices[i] - 4

    for i in dic:
        if dic[i] > 0:
            answer += i[1]
        else:
            answer += i[0]
    
    return answer


print(solution(["TR", "RT", "TR"], [7, 1, 3]))
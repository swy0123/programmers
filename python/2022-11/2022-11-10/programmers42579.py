# Lv.3 베스트앨범

# 딕셔너리의 원소 정렬, 튜플 활용
# 다른 풀이를 봤을 때 enumerate를 활용하여 더욱 간결하게 해결한 것을 확인했다. 이후 이를 활용해 문제를 풀이해봐야겠다.

# genres	                                        plays	                    return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]


def solution(genres, plays):
    answer = []
    dic = {}
    dicSum = {}

    for i in range(len(plays)):
        if genres[i] in dic:
            dic[genres[i]].append((plays[i], i))
            dicSum[genres[i]] += plays[i]
        else:
            dic[genres[i]] = []
            dic[genres[i]].append((plays[i], i))
            dicSum[genres[i]] = plays[i]
    # print(dic)

    sortedDicSum = sorted(dicSum.items(), key=lambda x: x[1], reverse=True)
    # print(sortedDicSum)

    for i in sortedDicSum:
        sortedDic = sorted(dic[i[0]], key=lambda x: (x[0], -x[1]), reverse=True)
        if len(sortedDic) > 1:
            answer.append((sortedDic[0][1]))
            answer.append((sortedDic[1][1]))
        else:
            answer.append((sortedDic[0][1]))

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop", 'test'], [500, 600, 500, 700, 2500, 10]))
print(solution(["classic", "pop"], [500, 100]))
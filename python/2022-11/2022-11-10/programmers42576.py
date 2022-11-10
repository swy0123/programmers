# 완주하지 못한 선수

# 딕셔너리(해시)를 이용하여 풀이

# participant	                                        completion	                                    return
# ["leo", "kiki", "eden"]	                            ["eden", "kiki"]	                            "leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	    ["josipa", "filipa", "marina", "nikola"]	    "vinko"
# ["mislav", "stanko", "mislav", "ana"]	                ["stanko", "ana", "mislav"]	                    "mislav"


def solution(participant, completion):
    answer = ''
    dic = {}
    for i in completion:
        if i in dic: dic[i] = dic[i]+1
        else: dic[i] = 1
    for i in participant:
        if i in dic:
            dic[i] = dic[i]-1
            if dic[i] >= 0:
                continue
        answer = i

    return answer


print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
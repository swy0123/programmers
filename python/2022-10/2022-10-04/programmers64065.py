# 튜플

#               s	                result
# "{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
# "{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
# "{{20,111},{111}}"	            [111, 20]
# "{{123}}"	                        [123]
# "{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]

def solution(s):
    answer = []
    arr = s[2:-2].split('},{')
    s=[]
    for i in arr:
        s.append(list(map(int, (i.split(',')))))
    s.sort(key=lambda i:len(i))

    for i in s:
        answer.extend(list((set(i))-set(answer)))
    # print(answer)

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

# 소감
# 문제를 이해하는데 시간이 오래 걸렸다. 차근차근 읽는 습관이 필요할 것 같다.
# 중복이 없는 튜플의 표현이라는 설명을 이해하지 못해 상당히 돌아가야 했다.
# sort(key=lambda x: x)와  extend의 사용이 코드를 상당히 간략하게 만들어준 것 같다.
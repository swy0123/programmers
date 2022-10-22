# 위장

from typing import Counter


def solution(clothes):
    answer = 1
    dic = {}

    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    
    for i in dic:
        answer *= (dic[i]+1)

    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["a", "headgear"], ["b", "headgear"], ["c", "eyewear"], ["d", "eyewear"], ["e", "face"], ["f", "face"]]))

# 소감
# 모두 안 입은 경우를 빼서 구하면 매우 쉽게 풀 수 있는 문제였다.
# 파이썬 딕셔너리를 이용하여 풀었는데 다 풀고서 다른 사람들의 풀이를 보니 람다식과  Counter를 이용해서 더 간결하게 푼게 눈에 들어왔다.
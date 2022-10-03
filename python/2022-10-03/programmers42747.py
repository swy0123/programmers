# H-Index

# citations	        return
# [3, 0, 6, 1, 5]	3

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    length = len(citations)
    max = length
    for i in citations:
        if i < max:
            break
        if i <= length:
            max = i
            break

    for i in range(max, 0, -1):
        if citations[i-1] >= i:
            # print(i, citations[i-1])
            answer = i
            break

    return answer

print(solution([6, 5, 5, 5, 3, 2, 1, 0]))
print(solution([4, 4, 4]))
print(solution([3, 0, 6, 1, 5]))
print(solution([10, 10, 10, 10, 10]))
print(solution([12, 11, 10, 9, 8, 1]))
print(solution([0,1,2,3,3,3,3,3,3,4,10,20,30,40]))


# 소감
# 문제를 이해하는데 상당히 애를 먹었다.
# 결국 다른 설명을 보고 새로운 테스트 케이스를 실험해본 뒤에야 풀 수 있었다.
# 다 푼 뒤에 다른 풀이를 살펴보니 enumerate를 이용한 풀이가 눈에 띄었는데 이 함수에 대해 학습을 해봐야겠다.
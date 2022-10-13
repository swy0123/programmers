# 기능개발 42586

# 소감
# 쉬운 방법으로 풀었지만 더 좋은 방법이 있다고 생각한다.
# 두번의 반복문으로 O(N^2)의 시간복잡도를 갖고 있지만 리스트를 뒤집어서 pop을 O(1)만으로 수행한다면 좀 더 시간을 줄일 수 있을 것 같다.

# progresses	            speeds	            return
# [93, 30, 55]	            [1, 30, 5]	        [2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]  [1, 3, 2]

import math

def solution(progresses, speeds):
    answer = []

    for i in range(len(progresses)):
        if progresses[i] >= 100:
            answer[-1] += 1
        else:
            answer.append(1)
            tmp = math.ceil((100 - progresses[i]) / speeds[i])
            for j in range(i, len(progresses)):
                progresses[j] += speeds[j] * tmp
            
    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# 가장 큰 수

# 소감
# 처음에는 정렬 방식을 잘못 정해 상당히 돌아갔지만 다른 사람의 테스트케이스를 
# 참고해 풀 수 있었다.

# numbers	        return
# [6, 10, 2]	    "6210"
# [3, 30, 34, 5, 9]	"9534330"

def solution(numbers):
    answer = ''
    arr = list(map(str, numbers))  
    arr.sort(key=lambda x: int((str(x)*4)[:4]), reverse=True)
    # print(arr)
    answer = str(int(''.join(arr)))
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
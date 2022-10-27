# 큰 수 만들기

# 소감
# 그리디 알고리즘에 대해 복습의 시간을 가졌다.

# number	    k	return
# "1924"	    2	"94"
# "1231234"	    3	"3234"
# "4177252841"	4	"775841"

def solution(number, k):
    number = list(number)
    result = [number.pop(0)]
    for i in number:
        if result[-1] < i:
            while result and result[-1] < i and k > 0:
                result.pop()
                k -= 1
            result.append(i)
        elif k == 0 or result[-1] >= i:
            result.append(i)
            
    if k > 0:
        result = result[:-k]
        
    answer = ''.join(result)

    return answer


print(solution("1924", 2))
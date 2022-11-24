# Lv.1 같은 숫자는 싫어

# arr	            answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	    [4,3]

def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            continue
        else:
            answer.append(arr[i])
    
    return answer
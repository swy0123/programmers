def solution(n):
    arr = []
    
    for i in range(1, n+1):
        if n % i == 0:
            arr.append(i)
    
    print(arr)
    
    answer = 0
    return answer

solution(16)
def solution(s):
    answer = ''
    arr = list(map(int, s.split(' ')))
    max = arr[0]
    min = arr[0]

    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    
    answer = str(min) + ' ' + str(max)
    print(answer)
    return answer

solution("1 2 3 4")
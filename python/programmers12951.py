def solution(s):
    answer = ''
    arr = list(s.split(' '))
    
    for i in arr:
        st = i[:1].upper()+i[1:].lower()
        answer += (st + ' ')

    return answer[:-1]

print(solution("3people unFollowed me"))
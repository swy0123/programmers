def solution(s):
    print("start")
    answer = [0,0]
    s1 = s

    while s1 != '1':
        print(s1)
        answer[0] += 1
        s2 = ''
        for i in s1:
            if i == '0':
                answer[1] += 1
            if i == '1':
                s2 += i
        s1 = str(bin(len(s2)))[2:]

    print("end")
    return answer

print(solution("110010101001"))
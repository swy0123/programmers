# [DP] 왼쪽맞춤

def solution(w, string):
    answer = 0

    word = string.split(' ')

    arr = ['' for i in range(len(word))]
    idx = 0

    for i in word:
        if len(arr[idx]) == 0:
            arr[idx] += i
        elif len(i) + len(arr[idx]) + 1 <= w:
            arr[idx] = arr[idx] + ' ' + i
        else:
            answer += (w - len(arr[idx]))**3
            idx += 1
            if len(arr[idx]) == 0:
                arr[idx] += i
            elif len(i) + len(arr[idx]) + 1 <= w:
                arr[idx] = arr[idx] + ' ' + i
    answer += (w - len(arr[idx]))**3
    print(arr)


    return answer

w = 12
string = 'ape eats apple cider a lot.'
print(solution(w, string))

w = 8
string = 'ape eats apple cider a lot.'
print(solution(w, string))

w = 5
string = 'ab c de'
print(solution(w, string))

w = 38
string = 'The word \'algorithm\' has its roots in Latinizing the name of Persian mathematician Muhammad idn Muse al-Khwarizmi in the first sreps to algorithmus.'
print(solution(w, string))


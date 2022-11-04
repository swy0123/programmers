# 전화번호 목록

# 문자열을 정렬하면 같은 문자열 순서대로 나열되므로 단순히 앞과 뒤의 문자열을 비교해 해결했다.

# phone_book	r                   eturn
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	            true
# ["12","123","1235","567","88"]	false

def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break

    return answer

print(solution(["12457", "119", "19111", "21", "97674223", "1195524421"]))

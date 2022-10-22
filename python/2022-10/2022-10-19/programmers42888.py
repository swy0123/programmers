# 오픈채팅방

# 소감
# uid를 딕셔너리로 저장하여 매우 쉽게 풀 수 있는 문제였다.

# record	
# ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
# result
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

def solution(record):
    answer = []
    stack = []
    dic = {}
    message1 = "님이 들어왔습니다."
    message2 = "님이 나갔습니다."

    for i in record:
        text = list(i.split(" "))
        if text[0] == "Enter":
            stack.append((text[1], 1))
            dic[text[1]] = text[2]
        elif text[0] == "Leave":
            stack.append((text[1], 0))
        elif text[0] == "Change":
            dic[text[1]] = text[2]


    for i in stack:
        if i[1] == 1:
            answer.append(dic[i[0]]+message1)
        else:
            answer.append(dic[i[0]]+message2)

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
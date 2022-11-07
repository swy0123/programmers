# 올바른 괄호

# s	        answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false

def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False

    return True



print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()))"))
print(solution("(()("))
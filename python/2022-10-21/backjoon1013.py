# 백준 1013 Contact

# 그동안 파이썬의 정규표현식에 대해 잘 몰랐는데 백준의 질문 검색을 통해 정규표현식을 학습하고 풀이해보았다.
# 새로운 기술을 습득한 것 같아 기쁘다. 

import sys
import re

N = int(input())
arr = []
for i in range(N):
    cur = sys.stdin.readline().strip()
    p = re.compile('(100+1+|01)+')
    if p.fullmatch(cur): 
        arr.append("YES")
    else: 
        arr.append("NO")
 
for i in arr:
    print(str(i))


# for string in arr:
#     idx = 0
#     flag = 0
#     while idx < len(string):
#         if string[idx] == '0':
#             if idx+1 < len(string) and string[idx+1] == '1':
#                 idx += 2
#             else:
#                 flag = 1
#                 break
#         elif string[idx] == '1':
#             if idx+2 < len(string)-1 and string[idx+1] == string[idx+2] == '0':
#                 tmpIdx = idx+3
#                 while tmpIdx < len(string)-1:
#                     if string[tmpIdx] == '0':
#                         tmpIdx += 1
#                     else:
#                         break
#                 idx = tmpIdx
#                 if string[idx] == '1':
#                     tmpIdx = idx
#                     while tmpIdx < len(string):
#                         if string[tmpIdx] == '1':
#                             tmpIdx += 1
#                         else:
#                             break
#                     idx = tmpIdx
#                 else:
#                     break
#             else:
#                 flag = 1
#                 break
#         else:
#             flag = 1
#             break
#         if flag == 1:
#             break
#     if flag == 1:
#         print('NO')
#     else:
#         print('YES')

# 1
# 10010111

# for i in range(1, 100):
#     answer = ''
#     for j in range(2):
#         if j == 0:
#             answer += '01'
#         else:
#             for k in range(1, i):
#                 for l in range(1, i):
#                     answer += "10" + "0"*k + "1"*l
#     print(answer)        
#     if answer in dic:
#         dic[answer] = 1
#         print(answer)
    
# for i in dic:
#     if dic[i] == 1:
#         print("YES")
#     else:
#         print("NO")

# print(dic)
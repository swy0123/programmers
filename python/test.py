# # 10814
# import sys

# n = int(sys.stdin.readline())
# curO = ''
# cnt = 0
# arr = []

# for i in range(n):
#     a, b = map(str, sys.stdin.readline().split())

#     # if a == curO:
#     #     cnt += 1
#     # else:
#     #     cnt = 0
#     #     curO = a
    
#     arr.append((int(a), b))
# arr.sort(key = lambda x: x[0])

# for i in arr:
#     print(str(i[0]) + ' ' + i[1])

# #1251
# import sys

# text = list(sys.stdin.readline().strip())
# ret = []
# temp = []

# for i in range(1, len(text)-1):
#     for j in range(i+1, len(text)):
#         a = text[:i]
#         b = text[i:j]
#         c = text[j:]
#         a.reverse()
#         b.reverse()
#         c.reverse()
#         temp.append(''.join(a+b+c))

# for i in temp:
#     ret.append(i)

# ret.sort()

# print(ret[0])



# import sys

# text = list(sys.stdin.readline().strip())
# print(text)

# cur = []
# ret = []

# minA = 'z'
# minN = 0
# curN = 0
# cut = 2

# for cnt in range(3):
#     if cnt == 2:
#         # print(cnt)
#         # print(text[minN:])
#         for i in text[minN:]:
#             cur.append(i)
#         cur.reverse()

#         for i in cur:
#             ret.append(i)
#         break
#     # print(cnt)
#     # print(text[minN:len(text)])
#     for i in range(minN,len(text)-cut):
#         if text[i] < minA:
#             minA = text[i]
#             curN = i

#     for i in range(minN,curN+1):
#         cur.append(text[i])
#     cut -= 1
#     minN = curN+1
#     minA = 'z'
#     cur.reverse()

#     for i in cur:
#         ret.append(i)
#     cur.clear()

# for i in ret:
#     print(i, end='')

# ret = ''
# temp = []
# min = 'z'
# cur = 0
# for i in text[cur:-3]:
#     if i < min:
#         min = i
#         cur = i.index(min)

# for i in text[0:cur]:
#     temp.append(i)
# temp.reverse()
# ret=''.join(temp)
# temp.clear()

# min = 'z'
# cur2 = 0
# for i in text[cur+1:-2]:
#     if i < min:
#         min = i
#         cur2 = i.index(min)

# for i in text[cur+1:cur2]:
#     temp.append(i)
# temp.reverse()
# ret=''.join(temp)
# temp.clear()

# min = 'z'
# cur1 = 0
# for i in text[cur2+1:]:
#     if i < min:
#         min = i
#         cur1 = i.index(min)

# for i in text[cur2+1:cur1]:
#     temp.append(i)
# temp.reverse()
# ret=''.join(temp)
# temp.clear()

# print(ret)







# for i in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     num = 1
#     a = a % 10
#     if a==0:
#         print(10)
#         continue
#     elif a in [1, 5, 6]:
#         print(a)
#         continue
#     elif a in [2, 3, 7, 8]:
#         b = b%4
#         if b == 0: b =4
#     elif a in [4, 9]:
#         b = b%2
#         if b == 0: b =2
#     for j in range(b):
#         num *= a
#     print(num%10)

def quick_select(A,k):
	p = A[0]
	S = L = M = []
	M.append(p)
	for x in A:
		if x < p : 
			S.append(x)
		elif x == p:
			M.append(x)
		else:
			L.append(x)
	if len(S)>= k:
        print(S)
        return quick_select(S,k)
	elif len(S)+ len(M) < k :
        print(L)
        return quick_select(L,k-len(S)-len(M))
    else:
        print(p)
        return p
	 
A = list(map(int, input().split()))
print(A)
answer = 0
quick_select(A,0)
# for i in range(len(A)):
# 		m = A[:i+1]
# 		a = quick_select(m,i//3)
# 		# print(m[i//3])
# 		answer += a

print(answer)
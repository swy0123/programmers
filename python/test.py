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


def merge_sort_3(A,first,last):
    if last - first < 2: return
    middle1 = first + (last-first)//3
    middle2 = first + 2*(last-first)//3 +1
    merge_sort_3(A, first, middle1)
    merge_sort_3(A, middle1+1, middle2)
    merge_sort_3(A, middle2+1, last)
    B = []
    i = first
    j = middle1+1
    k = middle2+1
    while i <= middle1 and j <= middle2 and k<= last:
        if A[i] <= A[j] and A[i]<= A[k]:
            B.append(A[i])
            i += 1
        elif A[j] <= A[k] and A[j]< A[i]:
            B.append(A[j])
            j += 1
        elif A[k] < A[i] and A[k]< A[j]:
            B.append(A[k])
            k += 1

    if i > middle1:
        while j <= middle2 and k<= last:
            if A[j] <= A[k]:
                B.append(A[j])
                j += 1
            else:
                B.append(A[k])
                k += 1
        for j in range(j, middle2+1): 
            B.append(A[j])
        for k in range(k, last+1): 
            B.append(A[k])

    elif j > middle2:
        while i <= middle1 and k<= last:
            if A[i] <= A[k]:
                B.append(A[i])
                i += 1
            else:
                B.append(A[k])
                k += 1
        for i in range(i, middle1+1): 
            B.append(A[i])
        for k in range(k, last+1): 
            B.append(A[k])

    elif k >last:
        while i <= middle1 and j<= middle2:
            if A[i] <= A[j]:
                B.append(A[i])
                i += 1
            else:
                B.append(A[j])
                j += 1
        for i in range(i, middle1+1): 
            B.append(A[i])
        for j in range(j, middle2+1): 
            B.append(A[j])

    for k in range(first, last+1):
        A[k] = B[k-first]


A = [9,8,7,6,5,4,3,2,1,11,12,15,17,14,13,16,19,20,10,0]
print(merge_sort_3(A, 0, 19))
print(A)
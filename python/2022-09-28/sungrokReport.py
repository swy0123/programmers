# def quick_select(A,k):
#     p = A[0]
#     S,L,M = [],[],[]
#     M.append(p)
#     for x in A[1:]:
#         if x < p : 
#             S.append(x)
#         elif x == p:
#             M.append(x)
#         else:
#             L.append(x)
#     if len(S) >= k:
#         return quick_select(S,k)
#     elif len(S)+ len(M) < k :
#         return quick_select(L, k-len(S)-len(M))
#     else:
#         return p


# import heapq

# def heap_selection(arr, n):
#     heap = arr
#     heapq.heapify(heap)
#     for i in range(n):
#         heapq.heappop(heap)
    
#     return heap[0]

# # A = list(map(int,input().split()))
# A = [9, 1, 3, 2, 7, 0, -2, 4, 5]
# # 19

# # A = [7, 6, 5, 4, 3, 2, 1]
# # 33

# # A = [11, 12, -20, 14, -10, -8, -7, -6, -4, -2]
# # -38

# answer = 0

# for i in range(len(A)):
#     m = A[:i+1]
#     print(m, i//3)
#     a = heap_selection(m,i//3)
#     print(a)
#     answer += a

# print(answer)


import heapq
import sys

# A = list(map(int,sys.stdin.readline().split())) #리스트를 입력받는다
A = [9, 1, 3, 2, 7, 0, -2, 4, 5]
# 19
answer = 0
m=[]
cnt =0
tmp = [-A[0]]
for i in range(len(A)):
    heapq.heappush(m,A[i])
    if i//3 == cnt:
        if m[0] < -tmp[0]:
            heapq.heappush(m,heapq.heappop(tmp))
            heapq.heappush(tmp,-(heapq.heappop(m)))
    else:
        cnt+=1
        if m[0] < -tmp[0]:
            heapq.heappush(tmp,-(heapq.heappop(m)))
        else:
            heapq.heappush(tmp,-(heapq.heappop(m)))
    print("M", m)
    print("tmp",tmp)
    print("cnt", cnt)
    answer += -(tmp[0])
    print(answer)
print(answer)
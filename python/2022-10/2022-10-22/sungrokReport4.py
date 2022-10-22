import random, timeit
##
## 여기에 세 가지 정렬함수를 위한 코드를...
##
import random

def quick_sort(A, first, last):
	global Qc # 비교
	global Qs # 교환횟수
	if first >= last: return
	left, right = first+1, last
	pivot = A[first]
	while left <= right:
		while left <= last and A[left] < pivot:
			left += 1
			Qc+=1
		while right > first and A[right] >= pivot:
			right -= 1
			Qc+=1
		if left <= right: # swap A[left] and A[right]
			A[left], A[right] = A[right], A[left]
			Qs +=1 #교환
			left += 1
			right -= 1
	# place pivot at the right place
	A[first], A[right] = A[right], A[first]
	Qs +=1 #교환
	quick_sort(A, first, right-1)
	quick_sort(A, right+1, last)

def insertion_sort_1(A):
	global Qc1 # 비교
	global Qs1 # 교환횟수
	for i in range(1,len(A)):
		j = i-1
		while j >=0 and A[j]>A[j+1]:
			Qc1 +=1
			A[j],A[j+1] = A[j+1],A[j]
			Qs1 +=1
			j = j-1
def quick_sort_1(A,first, last):
	global Qc1 # 비교
	global Qs1 # 교환횟수
	if last - first <= 10: 
		insertion_sort_1(A)
		# A.sort()
	left, right = first+1, last
	pivot = A[first]
	while left <= right:
		while left <= last and A[left] < pivot:
			left += 1
			Qc1+=1
		while right > first and A[right] >= pivot:
			right -= 1
			Qc1+=1
		if left <= right: # swap A[left] and A[right]
			A[left], A[right] = A[right], A[left]
			Qs1 +=1 #교환
			left += 1
			right -= 1
	# place pivot at the right place
	A[first], A[right] = A[right], A[first]
	Qs1+=1
	quick_sort(A, first, right-1)
	quick_sort(A, right+1, last)

def insertion_sort_2(A,n):
	global Qc2 # 비교
	global Qs2 # 교환횟수
	for i in range(1,n):
		j = i-1
		while j >=0 and A[j]>A[j+1]:
			Qc2 +=1
			A[j],A[j+1] = A[j+1],A[j]
			Qs2 +=1
			j = j-1

def merge_sort(A, first, last): # merge sort A[first] ~ A[last]
	global Mc # 비교
	global Ms # 이동횟수
	if first >= last: return
	middle = (first+last)//2
	merge_sort(A, first, middle)
	merge_sort(A, middle+1, last)
	B = []
	i = first
	j = middle+1
	while i <= middle and j <= last:
		if A[i] <= A[j]:
			Mc+=1
			B.append(A[i])
			Ms+=1
			i += 1
		else:
			Mc+=1
			B.append(A[j])
			Ms+=1
			j += 1
	for i in range(i, middle+1): 
		B.append(A[i])
		Ms+=1
	for j in range(j, last+1): 
		B.append(A[j])
		Ms+=1
	for k in range(first, last+1):
		A[k] = B[k-first]
		# Ms+=1
# def merge_sort_3(A,first,last):
	
def heapify_down(A, k, n): 
	global Hc # 비교
	global Hs # 교환횟수
	while 2*k+1 < n:        #  조건문이 어떤 뜻인가? 
		L, R = 2*k + 1, 2*k + 2	 #  L, R은 어떤 값?
		if L < n and A[L] > A[k]:
			Hc+=1
			m = L
		else:
			Hc+=1
			m = k
		if R < n and A[R] > A[m]: 
			m = R # m = A[k], A[L], A[R] 중 최대값의 인덱스
		if m != k:	# A[k]가 최대값이 아니라면 힙 성질 위배
			A[k], A[m] = A[m],A[k]
			Hs += 1 # 교환
			k = m
		else: break	# 왜 break할까?

def heap_sort(A):
	global Hc # 비교
	global Hs # 교환횟수
	n = len(A)
	for i in range(n//2 - 1, -1, -1):
		heapify_down(A, i, n)
	for k in range(n-1, 0, -1):
		A[0], A[k] = A[k], A[0]
		Hs += 1 #교환
		heapify_down(A, 0, k)

# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
Qc1, Qs1, Qc2, Qs2, Mc3, Ms3 = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
D = A[:]
E = A[:]
F = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

print("Quick sort 1:")
print("time =", timeit.timeit("quick_sort_1(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc1, Qs1))

# print("Quick sort2:")
# print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
# print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# print("Merge sort3:")
# print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
# print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
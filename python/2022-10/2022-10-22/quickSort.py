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


A = []

quick_sort(A, 0, 100)

quick_sort_1(B, 0, 100)
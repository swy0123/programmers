import sys

def RotatingList(A):
    l, r = 0, len(A) - 1
    while l <= r:
        if A[l] <= A[r]:
            return l
        mid = (l + r) // 2
        if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
            return len(A)-1-mid
        elif A[mid] < A[r]:
            r = mid 
        elif A[mid] > A[l]:
            l = mid

# A = list(map(int,sys.stdin.readline().split()))
A = [15, 18, 20, 31, 5, 8, 9]
print(RotatingList(A))
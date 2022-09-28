def quick_select(A,k):
    p = A[0]
    S,L,M = [],[],[]
    M.append(p)
    for x in A[1:]:
        if x < p : 
            S.append(x)
        elif x == p:
            M.append(x)
        else:
            L.append(x)
    if len(S) >=  k:
        return quick_select(S,k)
    elif len(S)+ len(M) < k :
        return quick_select(L, k-len(S)-len(M))
    else:
        return p
    
# A = list(map(int,input().split()))
A = [9, 1, 3, 2, 7, 0, -2, 4, 5]
answer = 0

for i in range(len(A)):
        m = A[:i+1]
        print(m, i//3+1)
        a = quick_select(m,i//3+1)
        print(a)
        answer += a

print(answer)

# 9 1 3 2 7 0 -2 4 5

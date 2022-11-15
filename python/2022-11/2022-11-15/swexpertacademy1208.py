# 1208. Flatten D3

for tset_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    for i in range(dump):
        m = min(arr)
        M = max(arr)
        arr[arr.index(M)] -= 1
        arr[arr.index(m)] += 1
    answer = '#' + str(tset_case)
    print(answer, max(arr)-min(arr))
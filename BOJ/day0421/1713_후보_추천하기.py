N = int(input())
cnt = int(input())

recommends = list(map(int,input().split()))
arr = []

def check(arr, x):
    for i, a in enumerate(arr):
        if a[2] == x:
            return True, i
    return False, -1
for idx, r in enumerate(recommends):
    t, ii = check(arr,r)
    if t:
        arr[ii][0]+=1

    else:
        if len(arr) < N:
            arr.append([1,idx,r])
        else:
            arr.pop()
            arr.append([1,idx,r])
    arr.sort(key=lambda x:(x[0],x[1]),reverse=True)

ans = sorted(arr, key=lambda x:x[2])
for aa in ans:
    print(aa[2],end =' ')

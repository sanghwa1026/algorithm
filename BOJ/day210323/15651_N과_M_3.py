global N, M, visited, nums
N, M = map(int, input().split())

nums = [i for i in range(1,N+1)]
visited = [False]*N

def perm(r, s):
    global N, M, visited, nums

    if r == M:
        print(s[:len(s)-1])
        return
    elif r > M:
        return

    for i in range(0, N):
        perm(r+1,s+str(nums[i])+' ')

perm(0, '')
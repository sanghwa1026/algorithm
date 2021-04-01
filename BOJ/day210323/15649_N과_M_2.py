global nums, visited, M

N, M = map(int,input().split())

nums = [i for i in range(1,N+1)]
visited = [False]*len(nums)

def comb(c,target):
    global M, nums, visited
    if target == M:
        s = ''
        for i in range(len(nums)):
            if visited[i]:
                s+=str(nums[i])
                s+=' '

        print(s[:len(s)-1])
        return

    for i in range(c,len(nums)):
        if not visited[i]:
            visited[i] = True
            comb(i,target+1)
            visited[i] = False

comb(0,0)
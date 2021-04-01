global N, M, nums, visited
N,M = map(int,input().split())

nums = list(map(int,input().split()))

visited = [False]*N
nums.sort()
def solve(c, r):
    global N,M, nums, visited

    if r==M:
        s = ''
        for i in range(N):
            if visited[i]:
                s+=str(nums[i])
                s+=' '

        print(s[:len(s)-1])
        return

    for i in range(c, N):
        if not visited[i]:
            visited[i] = True
            solve(i,r+1)
            visited[i] = False

solve(0,0)

global N, M, nums, visited
N, M = map(int, input().split())

nums = list(map(int, input().split()))
visited = [False]*N
nums.sort()
def solve(c, s):
    global N,M, nums, visited
    if c == M:
        print(s[:-1])
        return

    for i in range(N):
        solve(c+1,s+str(nums[i])+' ')

solve(0,'')
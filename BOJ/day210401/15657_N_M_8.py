global N, M, nums
N,M = map(int,input().split())

nums = list(map(int,input().split()))
nums.sort()
def solve(c,s,idx):
    global N,M,nums

    if c == M:
        print(s[:len(s)-1])
        return

    for i in range(N):
        if nums[i] >= nums[idx]:
            solve(c+1,s+str(nums[i])+' ',i)

solve(0,'',0)
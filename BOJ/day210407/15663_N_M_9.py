N, M = map(int, input().split())

visited = [False]*N
nums = list(map(int, input().split()))
nums.sort()

s = set([])
def solve(t,ss):
    global N,M, nums, visited, s
    if t == M:
        if not ss in s:
            s.add(ss)
            print(ss)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            solve(t+1, ss+str(nums[i])+' ')
            visited[i] = False

solve(0,'')
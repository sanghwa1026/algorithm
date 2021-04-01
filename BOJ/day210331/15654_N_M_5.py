global nums, ans

N, M = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
ans = []
visited = [False] * N

def comb(t, r, s):
    global nums, ans
    if t == r:
        ans.append(s[1:])
        return

    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            comb(t+1, r, s+' '+str(nums[i]))
            visited[i] = False

comb(0,M,'')


for i in ans:
    print(i)
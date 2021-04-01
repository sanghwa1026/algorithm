global nums, visited, M

N, M = map(int,input().split())

nums = [i for i in range(1,N+1)]

visited = [False]*len(nums)
ans = []
def swap(i,j):
    global nums
    nums[i], nums[j] = nums[j], nums[i]

def perm(c):
    global nums,visited, M

    if c == M:
        s = ''
        for i in range(len(nums)):
            if visited[i]:
                s+=str(nums[i])
                s+=' '
        ans.append(s[:len(s)-1])
        return

    for i in range(c, len(nums)):
        if not visited[i]:
            visited[c] = True
            swap(i,c)
            perm(c+1)
            swap(i,c)
            visited[c] = False


perm(0)
ans.sort()
for a in ans:
    print(a)
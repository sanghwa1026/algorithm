N = int(input())

nums = []*N
ans = 0

for i in range(N):
    t,p = map(int,input().split())
    nums.append([t,p])

for i,n in enumerate(nums):
    if i+n[0] >= N-1:
        continue

    temp = n[1]
    j = i
    while j+nums[j][0] < N-1:

        j = j+nums[j][0]
        temp += nums[j][1]
    ans = max(ans,temp)
print(ans)
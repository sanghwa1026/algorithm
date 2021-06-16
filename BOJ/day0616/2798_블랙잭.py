N,M = map(int,input().split())
nums = list(map(int, input().split()))

ans = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        for k in range(len(nums)):
            if j == k or i == k:
                continue
            if nums[i]+nums[j]+nums[k] <= M:
                ans = max(ans, nums[i]+nums[j]+nums[k])

print(ans)
N = int(input())

nums = list(map(int,input().split()))
dp = [1]*len(nums)

print(dp)
for i in range(len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j])
            dp[i]+=1

print(dp)
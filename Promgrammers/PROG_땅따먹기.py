nums = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

dp = [[0]*len(nums[0]) for i in range(len(nums))]
for i in range(len(nums)):
    for j in range(len(nums[0])):
        dp[i][j] = nums[i][j]

for i in range(1,len(nums)):
    for j in range( len(nums[0])):
        for k in range(len(nums[0])):
            if j == k:
                continue

            if dp[i-1][k]+nums[i][j] > dp[i][j]:
                dp[i][j] = dp[i-1][k]+nums[i][j]
print(max(dp[len(dp)-1]))
N = int(input())

nums = list(map(int,input().split()))
ans = 0

for cur in range(N):
    first = nums[cur]
    prev = nums[cur]
    for i in range(cur+1,N):
        if prev >= nums[i]:
            ans = max(ans, abs(first - prev))
            cur = i
            break
        elif i == len(nums)-1:
            ans = max(ans, abs(first-nums[i]))
        prev = nums[i]

print(ans)


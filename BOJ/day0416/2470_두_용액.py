N = int(input())

nums = list(map(int,input().split()))

def lower_bound(s,e,t,arr):
    while s < e:
        m = (s+e)//2
        if arr[m] < t:
            s=m+1
        else:
            e=m
    return e

nums.sort()
ans = int(2e9)
for i in range(len(nums)):
    temp = lower_bound(0, len(nums)-1, -nums[i], nums)
    if nums[i]+nums[temp] == 0:
        a, b = nums[i], nums[temp]
        break
    elif nums[i]+nums[temp] < ans:
        ans = nums[i]+nums[temp]
        a, b = nums[i], nums[temp]

if a > b:
    a, b = b, a

print(a, b)
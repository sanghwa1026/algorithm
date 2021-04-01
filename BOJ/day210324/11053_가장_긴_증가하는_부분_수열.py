import bisect
N = int(input())
nums = list(map(int,input().split()))

ans = []
ans.append(nums[0])

def lower(arr,value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return left

for i in range(1, len(nums)):
    if ans[len(ans) - 1] < nums[i]:
        ans.append(nums[i])
    else:
        ans[lower(ans, nums[i])] = nums[i]
        #ans[bisect.bisect_left(ans,nums[i])] = nums[i]

print(len(ans))
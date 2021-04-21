def binary(arr,x):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start+end)//2

        if arr[mid] == x:
            return 1
        elif arr[mid] < x:
            start = mid+1
        else:
            end = mid

    return 0
n = int(input())
nums = list(map(int,input().split()))
m = int(input())
values = list(map(int, input().split()))

nums.sort()

for v in values:
    print(binary(nums, v))
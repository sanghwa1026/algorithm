nums = list(map(int, input().split()))

incre = True
decre = True

for i in range(1,len(nums)):
    if nums[i-1] > nums[i]:
        incre = False
    else:
        decre = False

if incre:
    print("ascending")
elif decre:
    print("descending")
else:
    print("mixed")
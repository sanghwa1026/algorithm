from itertools import permutations
N = int(input())

nums = list(permutations([1,2,3,4,5,6,7,8,9],3))

for _ in range(N):
    num, s, b = map(int,input().split())
    remove_cnt = 0
    num = list(str(num))

    for i in range(len(nums)):
        ns, nb = 0, 0
        i-=remove_cnt
        for j in range(3):
            if int(num[j]) in nums[i]:
                if nums[i][j] == int(num[j]):
                    ns+=1
                else:
                    nb+=1

        if not ns == s or not nb == b:
            nums.remove(nums[i])
            remove_cnt+=1

print(len(nums))


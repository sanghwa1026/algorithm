global N, M, nums
N, M = map(int, input().split())

nums = [i for i in range(1,N+1)]


def comb(c, r, s):
    global N, M, nums

    if r == M:
        print(s[:len(s)-1])
        return

    for i in range(c,N):
        comb(i,r+1,s+str(nums[i])+' ')

comb(0,0, '')
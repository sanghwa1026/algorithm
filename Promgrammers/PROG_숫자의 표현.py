def solution(n):
    ans,idx,total = 0, 1, 0
    nums = [i for i in range(n+1)]

    for i in range(1,n+1):
        total+=i

        if total == n:
            ans+=1
        elif total > n:
            while total > n:
                total-=nums[idx]
                idx+=1
            if total == n:
                ans+=1

    return ans
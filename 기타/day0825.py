import sys
from typing import List
from pprint import pprint as pp

sys.setrecursionlimit(10**8)

nums = []
nums = [2, 7, 11, 15]

ans = []



def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i,x in enumerate(nums):
        n = target - x
        if n not in d:
            d[x] = i
        else:
            return [d[n], i]

'''    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if i == j: continue
                
            if nums[i] + nums[j] == target:
                left = i
                rigt = j
                result = [left, rigt]
                    
                return result
'''



ans = twoSum(nums, 9)

for i in ans:
    print(i)

import sys
from collections import deque

numbers = [1,1,1,1,1]

target = 3

qu = deque()
ans = 0

for i in range(0,len(numbers)):
    visit = [False] * len(numbers) 
    qu.append(-i)
    visit[i] = True
    
    tempSum = -i
    while len(qu) > 0:
        temp = qu.popleft()
        
        if tempSum == target:
            qu.clear()
            ans+=1
            break

        for j in range(0,len(numbers)):
            if i == j: continue
            if not visit[j]:
                qu.append(j)
                visit[j] = True
                tempSum+=numbers[j]
                print(tempSum)
                if tempSum == target:
                    qu.clear()
                    ans+=1
                    break


print(ans)
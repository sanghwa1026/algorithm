from collections import deque
from itertools import combinations

N = int(input())

nums = []
for i in range(N):
    num = list(map(int,input().split()))
    nums.append(num)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#1. 5자리 덧셈 비용 및 x, y 저장
q = deque()
for i in range(1, N-1):
    for j in range(1, N-1):
        temp = nums[i][j]
        for d in range(len(dx)):
            temp+=nums[i+dx[d]][j+dy[d]]
        q.append([i, j, temp])

ans = int(1e9)
#2. 조합을 이용해 3개씩 뽑아
for c in list(combinations(list(q),3)):

    if( ans > c[0][2]+c[1][2]+c[2][2] ):

        visited = [[False for _ in range(N)] for _ in range(N)]
        flag = False
        for cc in c:
            visited[cc[0]][cc[1]] = True

            for d in range(len(dx)):
                if visited[cc[0]+dx[d]][cc[1]+dy[d]]:
                    flag = True
                    break
                visited[cc[0]+dx[d]][cc[1]+dy[d]] = True
            if flag:
                break
        if not flag:
            #print(c)
            ans = c[0][2]+c[1][2]+c[2][2]

print(ans)
'''
6
1 0 2 3 3 4
1 1 1 1 1 1
0 0 1 1 1 1
3 9 9 0 1 99
9 11 3 1 0 3
12 3 0 0 0 1
'''
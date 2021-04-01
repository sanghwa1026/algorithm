import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N = int(sys.stdin.readline().strip())

lt = [list(sys.stdin.readline()) for _ in range(N)]

def bfs(x, y):
    qu = deque()
    qu.append([x,y])
    cnt = 1
    lt[x][y] = '0'
    while len(qu):
        tempX, tempY = qu.popleft()
        #lt[tempX][tempY] = 0
        for i in range(0, len(dx)):
            nx = tempX+dx[i]
            ny = tempY+dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(lt) or ny >= len(lt): continue

            if lt[nx][ny] == '1':
                qu.append([nx,ny])
                lt[nx][ny] = '0'
                cnt+=1
    return cnt
cnt = list()

for i in range(0,len(lt)):
    for j in range(0,len(lt)):
        if lt[i][j] == '1':
            cnt.append(bfs(i,j))
cnt.sort()
print(len(cnt))
print("\n".join(str(j) for j in cnt))
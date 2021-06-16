from sys import stdin
from collections import deque

def bfs():
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[rx][ry][bx][by] = True
    ret = -1
    while que:
        cur_rx, cur_ry, cur_bx, cur_by, cur_count = que.popleft()

        if cur_count > 10:
            break
        if graph[cur_rx][cur_ry] == 'O' and graph[cur_bx][cur_by] != 'O':
            ret = cur_count
            break

        for d in range(len(dx)):
            nrx = cur_rx
            nry = cur_ry
            nbx = cur_bx
            nby = cur_by

            while True:
                if not graph[nrx][nry] == '#' and not graph[nrx][nry] == 'O':
                    nrx+=dx[d]
                    nry+=dy[d]
                else:
                    if graph[nrx][nry] == '#':
                        nrx-=dx[d]
                        nry-=dy[d]
                    break

            while True:
                if not graph[nbx][nby] == '#' and not graph[nbx][nby] == 'O':
                    nbx += dx[d]
                    nby += dy[d]
                else:
                    if graph[nbx][nby] == '#':
                        nbx -= dx[d]
                        nby -= dy[d]
                    break

            if nrx == nbx and nry == nby:
                if not graph[nrx][nry] == 'O':
                    red_dist = abs(nrx - cur_rx) + abs(nry - cur_ry)
                    blue_dist = abs(nbx - cur_bx) + abs(nby - cur_by)
                    if red_dist > blue_dist:
                        nrx-=dx[d]
                        nry-=dy[d]
                    else:
                        nbx-=dx[d]
                        nby-=dy[d]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                que.append([nrx,nry,nbx,nby,cur_count+1])
    return ret
N, M = map(int, stdin.readline().split())
que = deque([])
graph = []
ans = 0

rx, ry, bx, by = [0]*4
for i in range(N):
    s = stdin.readline().rstrip()
    if 'R' in s:
        rx, ry = i,s.index('R')

    if 'B' in s:
        bx, by = i, s.index('B')
    graph.append(list(s))

que.append([rx,ry,bx,by,0])
ans = bfs()
print(ans)
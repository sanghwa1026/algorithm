from collections import deque
import copy
global N, graph, visited, dx, dy, copyGraph
N = int(input())

graph = []
visited = [[False for _ in range(N)] for i in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

copyGraph = []

#print(visited[0][0])
for i in range(N):
    s = str(input())
    graph.append(s)
    copyGraph.append(s.replace('R','G'))

#빨강, 초록, 파랑

def bfs(x, y, ch, gh):
    global visited, N, dx, dy

    q = deque()
    q.append([x, y])

    while q:
        temp = q.popleft()

        for d in range(len(dx)):
            nx = temp[0]+dx[d]
            ny = temp[1]+dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if not visited[nx][ny] and gh[nx][ny] == ch:
                visited[nx][ny] = True
                q.append([nx, ny])

#R, G, B = 0, 0, 0
rgb, rg = 0, 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, graph[i][j], graph)
            rgb+=1

visited = [[False for _ in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, copyGraph[i][j], copyGraph)
            rg += 1
print(rgb,rg) #정상
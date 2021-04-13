global visited,N, prob, result
nums = list(map(int,input().split()))
N = nums[0]

visited = [[False]*(N*2+1) for _ in range(N*2+1)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

prob = [0]*4

for i in range(1, len(nums)):
    prob[i-1] = nums[i]*0.01
result = 0

def dfs(c, x, y, chance):
    global N, visited, prob, result
    if c == N:
        result+=chance
        return

    if x < 0 or x >= (N*2+1) or y < 0 or y >= (N*2+1):
        return

    visited[x][y] = True

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or nx >= (N*2+1) or ny < 0 or ny >= (N*2+1):
            continue

        if not visited[nx][ny]:
            dfs(c+1, nx,ny,chance*prob[i])
            visited[nx][ny] = False

dfs(0, N, N, 1.0)

print(result)
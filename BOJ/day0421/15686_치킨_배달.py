from itertools import combinations
N,M = map(int,input().split())
homes,g, chi = [],[],[]

def bfs(arr, x,y):
    min_dist = int(1e9)

    for a in arr:
        dist = abs(x-a[0]) + abs(y-a[1])
        min_dist = min(min_dist, dist)

    return min_dist

for i in range(N):
    g.append(list(map(int,input().split())))
    for j in range(len(g[i])):
        if g[i][j] == 1:
            homes.append([i,j])
        elif g[i][j] == 2:
            chi.append([i,j])

ans = int(1e9)

for idx,c in enumerate(list(combinations(chi,M))):
    temp = 0

    for h in homes:
        temp+=bfs(c, h[0], h[1])

    if temp > 0:
        ans = min(temp, ans)

print(ans)
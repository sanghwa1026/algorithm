from collections import deque

N, K = map(int,input().split())

dx = [1,-1,2]

q = deque([N])
ans = 0
visited = [0]*100001

while q:
    temp = q.popleft()
    #print(temp)

    if temp == K:
        ans = visited[temp]
        break

    for next in (temp-1, temp+1, temp*2):
        if 0 <= next < 100001 and not visited[next]:
            visited[next] = visited[temp] + 1
            q.append(next)

print(ans)
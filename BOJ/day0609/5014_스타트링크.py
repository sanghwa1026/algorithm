from collections import deque

F, S, G, U, D = map(int,input().split())

move = [U, D]

que = deque([])
que.append([S,0])
ans = -1
visited = [False]*(F+1)
visited[S] = True
while que:
    cur,cur_move = que.popleft()
    if cur == G:
        ans = cur_move
        break

    for m in range(len(move)):
        if m:
            next = cur+U
            if next <= F and not visited[next]:
                visited[next] = True
                que.append([next, cur_move + 1])
        else:
            next = cur - D
            if 0 < next and not visited[next]:
                visited[next] = True
                que.append([next, cur_move + 1])
if ans < 0:
    print("use the stairs")
else:
    print(ans)
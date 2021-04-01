from collections import deque

init = "123456780"
dx = [1,-1,0,0]
dy = [0,0,1,-1]

N = 3
visited = {}

q = deque()
ss = ""

for i in range(N):
    nums = list(map(int, input().split()))
    ss+= ''.join(map(str,nums))

cost = 0
q.append([ss,cost])
visited[ss] = cost
ans = int(1e9)

def swap(ss, i, j):
    ss[i], ss[j] = ss[j], ss[i]
    return ''.join(ss)

while q:
    s, c = q.popleft()
    zero_index = s.index('0')

    if s == init:
        ans = visited[s]
        break

    for d in range(len(dx)):
        nx = zero_index//N +dx[d]
        ny = zero_index%N +dy[d]

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        ss = swap(list(s), zero_index, nx*N+ny)
        if not ss in visited:
            visited[ss] = c+1
            q.append([ss, c + 1])

if ans == int(1e9):
    print(-1)
else:
    print(ans)
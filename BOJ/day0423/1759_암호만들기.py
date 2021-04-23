L, C = map(int, input().split())
ch = list(map(str,input().split()))

visited = [False]*C
ss = []
def solve(c, t, m, j,s):
    global L, C, mo, visited, ch, ss
    if t == L and m >= 1 and j >= 2:
        ss.append(''.join(sorted(s)))
        return

    for i in range(c, C):
        if not visited[i]:
            visited[i] = True
            if ch[i] in ['a','e','i','o','u']:
                m+=1
                solve(i, t + 1, m, j, s + ch[i])
                m-=1
            else:
                j+=1
                solve(i, t + 1, m, j, s + ch[i])
                j-=1

            visited[i] = False

solve(0,0,0,0,'')

ss.sort()
for ans in ss:
    print(ans)
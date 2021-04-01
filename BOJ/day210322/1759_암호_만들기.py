global chars, visited, L, ans, m

L, C = map(int,input().split())

chars = list(map(str,input().split()))

chars.sort()
visited = [False]*C
ans = []

m = ['a','e','i','o','u']

def dfs(cur, target):
    global visited, chars, L, ans, m
    if target == L:
        s = ''
        mm = 0
        jj = 0
        for i in range(len(chars)):
            if visited[i]:
                if chars[i] in m:
                    mm+=1
                else:
                    jj+=1

                s+=chars[i]
                #print(chars[i],end=' ')
        if mm >= 1 and jj >= 2:
            ans.append(s)
        return

    for i in range(cur, len(chars)):
        if visited[i]:
            continue

        visited[i] = True
        dfs(i, target+1)
        visited[i] = False


dfs(0,0)

[print(a) for a in ans]

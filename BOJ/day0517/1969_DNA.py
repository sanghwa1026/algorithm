N,M = map(int,input().split())

s = []
cnt = [[0]*26 for _ in range(M)]
ans = ''
hammingDist = 0

for n in range(N):
    s.append(str(input()))

    for j in range(M):
        cnt[j][int(ord(s[n][j])-65)]+=1

for i in range(M):
    m = max(cnt[i])
    idx = cnt[i].index(m)
    ans+=chr(idx+65)
    hammingDist+=N-m

print(ans)
print(hammingDist)
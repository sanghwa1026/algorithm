N, M = map(int, input().split())

m = [[-int(1e9)]*(M+3) for _ in range(N+3)]

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        print(data)
        m[i][j] = data[j]


print(m)
N = int(input())
lines = list(map(int,input().split()))
costs = list(map(int,input().split()))

ans = 0
pre = int(1e9)
prev = [int(1e9)]*len(costs)
for i in range(len(costs)):
    if costs[i] < pre:
        pre = costs[i]

    prev[i] = pre

for i,v in enumerate(lines):
    ans+=(v*prev[i])

print(ans)

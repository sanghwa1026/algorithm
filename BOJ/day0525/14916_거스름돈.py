n = int(input())

#5원, 2원
ans = int(1e9)

idx = 0
while True:
    if idx*5 > n:
        break

    i = 0
    if n == idx*5:
        ans = idx
        break
    temp = n - idx*5
    if temp%2 == 0:
        ans = min(ans, temp//2 + idx)
    idx+=1

if ans == int(1e9):
    print(-1)
else:
    print(ans)
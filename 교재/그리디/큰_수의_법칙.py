N, M, K = map(int, input().split())

lt = list(map(int, input().split()))

lt = sorted(lt, reverse=True)

sum = 0
for i in range(M):
  if i%(K+1) == 0:
    sum+=lt[1]
    print(lt[1], end=' ')
  else:
    sum+=lt[0]
    print(lt[0], end=' ')

print(sum)
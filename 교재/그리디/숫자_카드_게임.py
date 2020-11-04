N, M = map(int, input().split())

data = [[0]*N for _ in range(M)]

answer = []

for n in range(N):
  data[n] = list(map(int, input().split()))
  answer.append(min(data[n]))
  
print(max(answer))
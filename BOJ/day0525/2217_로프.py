import sys
N = int(sys.stdin.readline())
w = []

for _ in range(N):
    w.append(int(sys.stdin.readline()))

w.sort(reverse=True)

for i in range(len(w)):
    w[i] = w[i]*(i+1)

print(max(w))
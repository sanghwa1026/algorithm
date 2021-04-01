import sys
from collections import Counter

n = int(sys.stdin.readline().strip())

a = list()
for i in range(0, n):
    input = int(sys.stdin.readline().strip())
    a.append(input)

b = sorted(Counter(a).items(), key=lambda x: x[0])

for k, v in b:
    for i in range(0,v):
        sys.stdout.write(str(k) + '\n')
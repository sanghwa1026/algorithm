import sys
n = int(sys.stdin.readline().strip())

ls = list()

for i in range(0, n):
    input = int(sys.stdin.readline().strip())
    ls.append(input)

ls.sort()

for i in ls:
    print(i)

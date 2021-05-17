from sys import stdin

T = int(stdin.readline())

for t in range(T):
    n, m = map(int,stdin.readline().split())
    ans = 0
    for i in range(1,n):
        for j in range(1,i):
            tmp = (pow(i,2)+pow(j,2)+m)/(i*j)
            if tmp - int(tmp) == 0:
                ans+=1
    print(ans)
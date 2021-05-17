N,K = map(int,input().split())
ans = 0

def findPrime():
    global N,K
    prime = [False] * 1001
    cnt = 1

    for i in range(2,N+1):
        j=i
        for j in range(j,N+1,i):
            if prime[j] == False:
                if cnt == K:
                    return j
                prime[j] = True
                cnt+=1

print(findPrime())
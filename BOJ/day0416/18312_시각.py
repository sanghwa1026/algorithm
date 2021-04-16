N, K = map(int,input().split())

ans = 0

for i in range(0, N+1):
    for j in range(0, 60):
        for k in range(0, 60):
            s = ''
            if len(str(i)) == 1:
                s+='0'+str(i)
            else:
                s+=str(i)

            if len(str(j)) == 1:
                s+='0'+str(j)
            else:
                s+=str(j)

            if len(str(k)) == 1:
                s+='0'+str(k)
            else:
                s+=str(k)

            if str(K) in s:
                ans+=1

print(ans)
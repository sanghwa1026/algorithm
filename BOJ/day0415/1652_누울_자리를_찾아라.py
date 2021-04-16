N = int(input())

ch = [input()+'X' for _ in range(N)]+['X'*(N+1)]
w, h = 0, 0
for i in range(N):
    cnt = 0
    for j in range(N+1):
        if ch[i][j] == '.':
            cnt+=1
        else:
            if cnt >= 2:
                w+=1
            cnt=0

for j in range(N):
    cnt = 0
    for i in range(N+1):
        if ch[i][j] == '.':
            cnt+=1
        else:
            if cnt >= 2:
                h+=1
            cnt=0

print(str(w)+" "+str(h))
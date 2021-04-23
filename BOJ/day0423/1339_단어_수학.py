N = int(input())
arr = []
alpha = [0 for _ in range(26)]
size = 0
for i in range(N):
    tmp = str(input())
    s=0
    for t in reversed(tmp):
        if alpha[ord(t)-ord('A')] == 0:
            size+=1
        alpha[ord(t)-ord('A')]+=pow(10,s)
        s+=1

alpha.sort(reverse=True)
idx,ans = 0, 0

for i in range(9, 9-size, -1):
    ans+=alpha[idx]*i
    idx+=1

print(ans)
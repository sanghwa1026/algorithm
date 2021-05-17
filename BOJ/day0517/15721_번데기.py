A = int(input())
T = int(input())
findStr = int(input()) #뻔 = 0, 데기 = 1
#bundegi = [0,1,0,1,0,1]

n = 1

s = '010101'
idx,cnt = 0, 0
ans = -1
flag = False
while True:
    for i in range(len(s)):
        if s[i] == str(findStr):
            cnt+=1

        if T == cnt:
            ans = i%A
            flag = True
            break
    if flag:
        break
    n+=1
    s='0'+('1'*n)+('0'*n)+'101'

print(ans)
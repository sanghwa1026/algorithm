#지구 = E 1 ~ 15
#태양 = S 1 ~ 28
#달 = M 1 ~ 19

E, S, M = map(int, input().split())

EAX = 15
SAX = 28
MAX = 19

e = 1
s = 1
m = 1

ans = 1

while True:
  #print(e, s, m)

  if e == E and s == S and m == M:
    break

  e%=EAX
  s%=SAX
  m%=MAX

  e+=1
  s+=1
  m+=1

  ans+=1
  #print(ans)

print(ans)


#printf("%d", ["abcde"]);

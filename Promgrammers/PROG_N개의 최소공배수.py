def gcd(n,m):
    if n < m:
        n,m = m,n

    if m == 0:
        return n
    elif n%m == 0:
        return m
    else:
        return gcd(n%m,m)

arr = [2,6,8,14]

ans = 1
for i in arr:
    ans = (ans*i) // (gcd(ans,i))

print(ans)
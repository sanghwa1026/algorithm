import string
N = int(input())

tmp = string.digits+string.ascii_lowercase
def convert(num, base):
    q,r = divmod(num,base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]
print(tmp)
print(convert(int(str(N),8),2))
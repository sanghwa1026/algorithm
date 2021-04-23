while True:
    try:X, Y = map(int,input().split())
    except EOFError: break
    Z = int(Y*100/X)

    s = 1
    e = int(1e9)

    while s < e:
        mid = (s+e)//2
        n = int(((mid+Y)*100/(mid+X)))
        if n <= Z:
            s = mid+1
        else:
            e = mid

    print(e if int((Y+e)/(X+e)*100) > Z else -1)


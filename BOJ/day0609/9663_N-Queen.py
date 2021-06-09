def check(row, col):
    global N, chk_col, chk_dig, chk_dig2
    if chk_col[col] == 1:
        return False
    elif chk_dig[row+col] == 1:
        return False
    elif chk_dig2[row-col+N-1] == 1:
        return False
    return True

def dfs(row):
    global N, chk_col, chk_dig, chk_dig2
    if row == N:
        return 1
    result = 0
    for col in range(N):
        if check(row,col):
            D[row][col] = 1
            chk_col[col] = 1
            chk_dig[row+col] = 1
            chk_dig2[row-col+N-1] = 1
            result+=dfs(row+1)
            D[row][col] = 0
            chk_col[col] = 0
            chk_dig[row + col] = 0
            chk_dig2[row - col + N - 1] = 0
    return result

N = int(input())
D = [[0]*N for _ in range(N)]
chk_col = [0] * N
chk_dig = [0] * (2*N-1)
chk_dig2 = [0] * (2*N-1)
print(dfs(0))
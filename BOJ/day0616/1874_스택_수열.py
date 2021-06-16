N = int(input())

ans = []
stack = []
count = 1

for i in range(1, N+1):
    data = int(input())
    while count<=data:
        stack.append(count)
        count+=1
        ans.append('+')

    if stack[-1] == data:
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        exit(0)

print('\n'.join(ans))
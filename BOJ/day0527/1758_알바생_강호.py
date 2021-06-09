N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)
tip = 0

for i in range(len(arr)):
    if arr[i]-i > 0:
        tip+=arr[i]-i

print(tip)
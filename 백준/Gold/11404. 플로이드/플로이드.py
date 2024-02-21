import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(m):
    i, j, c = map(int, input().split())
    if arr[i-1][j-1]:
        arr[i-1][j-1] = min(arr[i-1][j-1], c)
    else:
        arr[i-1][j-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if arr[i][k] and arr[k][j]:
                if arr[i][j]:
                    arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])
                else:
                    arr[i][j] = arr[i][k] + arr[k][j]
for i in range(n):
    print(*arr[i])
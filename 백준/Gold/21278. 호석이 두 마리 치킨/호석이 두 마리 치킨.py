import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        if i == k: continue
        for j in range(n):
            if i == j or j == k: continue
            if arr[i][k] <= 0 or arr[k][j] <= 0: continue
            if arr[i][j] <= 0:
                arr[i][j] = arr[i][k] + arr[k][j]
            else:
                arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])

a = -1
b = -1
ssum = 10000
for i in range(n):
    for j in range(i+1, n):
        if i == j: continue
        tmp = 0
        for home in range(n):
            tmp += min(arr[home][i], arr[home][j])
        if tmp < ssum:
            a = i
            b = j
            ssum = tmp
print(a + 1, b + 1, ssum * 2)
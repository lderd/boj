n = int(input())
m = int(input())
arr = [[9876543210] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)
for i in range(n):
    arr[i][i] = 0
for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(n):
                if i != k:
                    arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])
for i in range(n):
    for j in range(n):
        if arr[i][j] >= 9876543210:
            print(0, end=' ')
        else:
            print(arr[i][j], end=' ')
    print()
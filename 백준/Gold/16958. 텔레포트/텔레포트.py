import sys
input = sys.stdin.readline
n, t = map(int, input().split())
arr = dict()
for i in range(n):
    s, x, y = map(int, input().split())
    arr[i] = (s, x, y)

dist = [[10000000] * n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if i == j: continue
        si, xi, yi = arr[i]
        sj, xj, yj = arr[j]
        dist[i][j] = abs(xi-xj) + abs(yi-yj)
        if si and sj and t < dist[i][j]:
            dist[i][j] = t
        dist[j][i] = dist[i][j]

for k in range(n):
    for i in range(n):
        if i == k: continue
        for j in range(i+1, n):
            if j == k: continue
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
            dist[j][i] = dist[i][j]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(dist[a-1][b-1])
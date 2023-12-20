import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
checked = [[0] * m for _ in range(n)]
d = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
answer = 0
tmp = 1
for i in range(n):
    for j in range(m):
        if not checked[i][j]:
            ci, cj = i, j
            while not checked[ci][cj]:
                checked[ci][cj] = tmp
                di, dj = d[arr[ci][cj]]
                ci += di
                cj += dj
            if checked[ci][cj] == tmp:
                answer += 1
            tmp += 1
print(answer)
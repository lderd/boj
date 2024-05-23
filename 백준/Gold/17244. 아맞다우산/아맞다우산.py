from collections import deque
n, m = map(int, input().split())
home = [input() for _ in range(m)]
s = tuple
t = 0
things = {}
e = tuple
for i in range(m):
    for j in range(n):
        if home[i][j] == 'S':
            s = (i, j)
        elif home[i][j] == 'X':
            t += 1
            things[(i, j)] = t
        elif home[i][j] == 'E':
            e = (i, j)
check = [[[9876543210] * (1 << t + 1) for _ in range(n)] for _ in range(m)]
check[s[0]][s[1]][0] = 0
q = deque([(*s, 1 << 0, 0)])
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    ci, cj, c, cnt = q.popleft()
    for di, dj in d:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < m and 0 <= nj < n and home[ni][nj] != '#':
            if home[ni][nj] == 'E':
                if check[ni][nj][c] > cnt + 1:
                    check[ni][nj][c] = cnt + 1
            elif home[ni][nj] == '.' or home[ni][nj] == 'S':
                if check[ni][nj][c] > cnt + 1:
                    check[ni][nj][c] = cnt + 1
                    q.append((ni, nj, c, cnt + 1))
            elif home[ni][nj] == 'X':
                if check[ni][nj][c | (1 << things[(ni, nj)])] > cnt + 1:
                    check[ni][nj][c | (1 << things[(ni, nj)])] = cnt + 1
                    q.append((ni, nj, c | (1 << things[(ni, nj)]), cnt + 1))
print(check[e[0]][e[1]][(1 << (t + 1)) - 1])
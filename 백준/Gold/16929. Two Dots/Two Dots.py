import sys
n, m = map(int, input().split())
board = [input() for _ in range(n)]
checked = [[False] * m for _ in range(n)]
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for i in range(n):
    for j in range(m):
        if not checked[i][j]:
            checked[i][j] = True
            color = board[i][j]
            l = 1
            q = [(i, j, 0)]
            route = {(i, j)}
            while q:
                ci, cj, dd = q.pop()
                li, lj = -1, -1
                if q:
                    li, lj, ld = q[-1]
                if dd >= 4:
                    l -= 1
                    route.remove((ci, cj))
                    continue
                else:
                    q.append((ci, cj, dd+1))
                di, dj = d[dd]
                ni, nj = ci+di, cj+dj
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == color:
                    if not (ni == li and nj == lj) and l >= 4 and  (ni, nj) in route:
                        print('Yes')
                        sys.exit()
                    if (ni, nj) not in route:
                        checked[ni][nj] = True
                        q.append((ni, nj, 0))
                        route.add((ni, nj))
                        l += 1
print('No')
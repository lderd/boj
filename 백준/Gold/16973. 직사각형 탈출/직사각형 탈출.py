import sys
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
h, w, sr, sc, fr, fc = map(int, input().split())
sr -= 1
sc -= 1
fr -= 1
fc -= 1
if sr == fr and sc == fc:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                for di in range(h):
                    for dj in range(w):
                        ni, nj = i-di, j-dj
                        if 0 <= ni and 0 <= nj and board[ni][nj] == 0:
                            board[ni][nj] = 2
    d = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    q = deque([(sr, sc, 0)])
    checked = [[False] * m for _ in range(n)]
    checked[sr][sc] = True
    while q:
        ci, cj, cnt = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n - h + 1 and 0 <= nj < m - w + 1 and not checked[ni][nj] and board[ni][nj] == 0:
                checked[ni][nj] = True
                if ni == fr and nj == fc:
                    print(cnt + 1)
                    sys.exit()
                q.append((ni, nj, cnt + 1))
    print(-1)
from itertools import combinations
from collections import deque
n, m, g, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
hubo = set()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            hubo.add((i, j))
answer = 0
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for green in combinations(hubo, g):
    for red in combinations(hubo - set(green), r):
        checked = [[[0] * 2 for _ in range(m)] for _ in range(n)]
        greens = []
        reds = []
        for i, j in green:
            checked[i][j][0] = -1
            greens.append((i, j, 0, 'g'))
        for i, j in red:
            checked[i][j][1] = -1
            reds.append((i, j, 0, 'r'))
        tmp = 0
        q = deque(greens + reds)
        while q:
            ci, cj, cnt, rg = q.popleft()
            if checked[ci][cj][0] == checked[ci][cj][1]:
                tmp += 1
                continue
            for di, dj in d:
                ni, nj = ci+di, cj+dj
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != 0:
                    if rg == 'g' and checked[ni][nj][0] == 0 and checked[ni][nj][1] == 0:
                        checked[ni][nj][0] = cnt + 1
                        q.append((ni, nj, cnt+1, rg))
                    elif rg == 'r' and checked[ni][nj][1] == 0:
                        if checked[ni][nj][0] == cnt + 1:
                            checked[ni][nj][1] = cnt + 1
                        elif checked[ni][nj][0] == 0:
                            checked[ni][nj][1] = cnt + 1
                            q.append((ni, nj, cnt+1, rg))
        if tmp > answer:
            answer = tmp
print(answer)

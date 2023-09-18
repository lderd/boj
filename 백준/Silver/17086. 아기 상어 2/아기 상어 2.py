from collections import deque
n, m = map(int, input().split())
space = [input().split() for _ in range(n)]
d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
answer = 0
for i in range(n):
    for j in range(m):
        if space[i][j] == '1': continue
        q = deque([(i, j, 0)])
        checked = [[False] * m for _ in range(n)]
        checked[i][j] = True
        flag = False
        while q:
            ci, cj, cnt = q.popleft()
            for di, dj in d:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < m and not checked[ni][nj]:
                    if space[ni][nj] == '1':
                        space[i][j] = cnt + 1
                        if answer <= cnt:
                            answer = cnt + 1
                        flag = True
                        break
                    else:
                        q.append((ni, nj, cnt + 1))
                        checked[ni][nj] = True
            if flag:
                break
print(answer)
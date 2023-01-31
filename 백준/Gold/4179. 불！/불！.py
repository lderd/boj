from collections import deque
r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]
jihun = tuple()
q = deque()
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            jihun = (i, j, 1, 0)
        elif maze[i][j] == 'F':
            q.append((i, j, 0, 0))
q.append(jihun)
answer = 'IMPOSSIBLE'
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while q:
    ci, cj, jihun, cnt = q.popleft()
    if jihun:
        if ci == 0 or ci == r - 1 or cj == 0 or cj == c - 1:
            answer = cnt + 1
            break
    for di, dj in d:
        ni, nj = ci+di, cj+dj
        if 0 <= ni < r and 0 <= nj < c:
            if jihun:
                if maze[ni][nj] == '.':
                    maze[ni][nj] = 'J'
                    q.append((ni, nj, jihun, cnt+1))
            else:
                if maze[ni][nj] == 'J' or maze[ni][nj] == '.':
                    maze[ni][nj] = 'F'
                    q.append((ni, nj, jihun, cnt))
    if type(answer) == int:
        break
print(answer)
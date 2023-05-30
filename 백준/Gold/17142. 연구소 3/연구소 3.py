from itertools import combinations
from collections import deque
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
virus = []
answer = -1
binkan = 0
for i in range(n):
    for j in range(n):
        if maze[i][j] == 2:
            virus.append((i, j, 0))
        elif maze[i][j] == 0:
            binkan += 1
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
if binkan > 0:
    for combi in combinations(virus, m):
        checked = [[True] * n for _ in range(n)]
        cnt = binkan
        for i, j, time in combi:
            checked[i][j] = False
        q = deque(combi)
        flag = 0
        while q:
            i, j, time = q.popleft()
            if answer > -1 and time >= answer:
                break
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and checked[ni][nj]:
                    q.append((ni, nj, time + 1))
                    checked[ni][nj] = False
                    if maze[ni][nj] == 0:
                        cnt -= 1
                        if cnt == 0:
                            if answer == -1 or answer > time + 1:
                                answer = time + 1
                                flag = 1
                            break
            if flag == 1:
                break
    print(answer)
else:
    print(0)
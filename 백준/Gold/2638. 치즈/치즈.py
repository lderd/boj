from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
while True:
    checked = [[0] * m for _ in range(n)]
    q = deque([(0, 0)])
    melt = set()
    while q:
        ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 0 and checked[ni][nj] == 0:
                    checked[ni][nj] = 1
                    q.append((ni, nj))
                elif arr[ni][nj] == 1:
                    if checked[ni][nj] == 0:
                        checked[ni][nj] = 2
                    elif checked[ni][nj] == 2:
                        checked[ni][nj] = 3
                        melt.add((ni, nj))
    if melt:
        for i, j in melt:
            arr[i][j] = 0
        answer += 1
    else:
        break
print(answer)
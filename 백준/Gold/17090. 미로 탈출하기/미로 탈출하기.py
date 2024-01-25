n, m = map(int, input().split())
arr = [input() for _ in range(n)]
checked = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if checked[i][j] == 0:
            q = [(i, j)]
            setq = {(i, j)}
            can = False
            while True:
                ci, cj = q[-1]
                if arr[ci][cj] == 'U':
                    ni, nj = ci-1, cj
                elif arr[ci][cj] == 'R':
                    ni, nj = ci, cj+1
                elif arr[ci][cj] == 'D':
                    ni, nj = ci+1, cj
                else:
                    ni, nj = ci, cj-1
                if ni < 0 or ni >= n or nj < 0 or nj >= m or checked[ni][nj] > 0:
                    can = True
                    break
                if (ni, nj) in setq or checked[ni][nj] < 0:
                    break
                q.append((ni, nj))
                setq.add((ni, nj))
            if can:
                for ci, cj in q:
                    checked[ci][cj] = 1
            else:
                for ci, cj in q:
                    checked[ci][cj] = -1
answer = 0
for i in range(n):
    for j in range(m):
        if checked[i][j] > 0:
            answer += 1
print(answer)
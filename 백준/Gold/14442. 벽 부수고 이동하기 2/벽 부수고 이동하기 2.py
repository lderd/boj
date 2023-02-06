from collections import deque
n, m, k = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
checked = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
q = deque([(0, 0, 0)])
checked[0][0][0] = 1
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = -1
if n == m == 1:
    answer = 1
while q:
    ci, cj, cnt = q.popleft()
    for di, dj in d:
        ni, nj = ci+di, cj+dj
        if 0 <= ni < n and 0 <= nj < m:
            if ni == n-1 and nj == m-1:
                answer = checked[ci][cj][cnt] + 1
                break
            if arr[ni][nj] == 0:
                if checked[ni][nj][cnt] == 0:
                    checked[ni][nj][cnt] = checked[ci][cj][cnt] + 1
                    q.append((ni, nj, cnt))
            else:
                if cnt < k:
                    if checked[ni][nj][cnt+1] == 0:
                        checked[ni][nj][cnt+1] = checked[ci][cj][cnt] + 1
                        q.append((ni, nj, cnt+1))
    if answer > -1:
        break
print(answer)
from collections import deque
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
x -= 1
y -= 1
birus = []
checked = [[False] * n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            birus.append((arr[i][j], i, j, 0))
            checked[i][j] = True
            if i == x and j == y:
                answer = arr[i][j]
                break
    if answer > 0:
        break
birus.sort()
q = deque(birus)
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q and answer <= 0:
    num, ci, cj, cnt = q.popleft()
    if cnt >= s: continue
    for di, dj in d:
        ni, nj = ci+di, cj+dj
        if 0 <= ni < n and 0 <= nj < n and not checked[ni][nj]:
            if ni == x and nj == y:
                answer = num
                break
            q.append((num, ni, nj, cnt+1))
            checked[ni][nj] = True
    if answer > 0:
        break
print(answer)
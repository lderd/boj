import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
P = list(map(lambda x:int(x)-1, input().split()))
arr = [[-1] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    if arr[u-1][v-1] == -1 or arr[u-1][v-1] > w:
        arr[u-1][v-1] = w
checked = [[200000] * (1<<n) for _ in range(n+1)]
q = deque()
for i in range(n):
    if P[i] == i and arr[n][i] > 0:
        q.append((arr[n][i], i, 1<<i))
        checked[i][1<<i] = arr[n][i]
while q:
    now_dist, now_town, now_checked = q.popleft()
    if now_dist > checked[now_town][now_checked]: continue
    if now_checked == (1 << n) - 1:
        if arr[now_town][n] > 0:
            checked[n][-1] = min(now_dist + arr[now_town][n], checked[n][-1])
        continue
    for j in range(n):
        if arr[now_town][j] > 0 and (now_checked & (1<<P[j]) or j == P[j]) and not now_checked & (1<<j):
            if checked[j][now_checked | (1<<j)] > now_dist + arr[now_town][j]:
                checked[j][now_checked | (1<<j)] = now_dist + arr[now_town][j]
                q.append((now_dist+arr[now_town][j], j, now_checked | (1<<j)))
if checked[n][-1] == 200000:
    print(-1)
else:
    print(checked[n][-1])
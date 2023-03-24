from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * m for _ in range(n)]
q = deque()
if n > 1:
    q.append((1, 0))
if m > 1:
    q.append((0, 1))
memo[0][0] = 1
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while q:
    ci, cj = q.popleft()
    tmp = 0
    tmp_list = []
    for di, dj in d:
        ni, nj = ci + di, cj+dj
        if 0 <= ni < n and 0 <= nj < m:
            if arr[ni][nj] > arr[ci][cj]:
                tmp += memo[ni][nj]
            elif arr[ni][nj] < arr[ci][cj]:
                tmp_list.append((ni, nj))
    if tmp > memo[ci][cj]:
        memo[ci][cj] = tmp
        q.extend(tmp_list)
print(memo[n-1][m-1])
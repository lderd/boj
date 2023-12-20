from collections import deque
n = int(input())
arr = [[0] * (2*n) for _ in range(n)]
for i in range(n):
    for j in range(n-i%2):
        a, b = map(int, input().split())
        arr[i][j*2+i%2] = a
        arr[i][j*2+1+i%2] = b
q = deque([(0, 0, 1)])
checked = [-1] * (n*n-n//2+1)
checked[1] = 1
d = [(0, -1), (-1, 0), (1, 0), (0, 1)]
answer = []
while q:
    li, lj, rj = q.popleft()
    c_idx = (2 * n - 1) * (li // 2) + (li % 2) * n + (lj - li % 2) // 2 + 1
    for dd in range(3):
        di, dj = d[dd]
        ni, nj = li+di, lj+dj
        if 0 <= ni < n and 0 <= nj < 2*n and arr[li][lj] == arr[ni][nj]:
            n_idx = (2 * n - 1) * (ni // 2) + (ni % 2) * n + (nj-1 - ni % 2) // 2 + 1
            if checked[n_idx] == -1:
                q.append((ni, nj-1, nj))
                checked[n_idx] = c_idx
    for dd in range(1, 4):
        di, dj = d[dd]
        ni, nj = li+di, rj+dj
        if 0 <= ni < n and 0 <= nj < 2*n and arr[li][rj] == arr[ni][nj]:
            n_idx = (2 * n - 1) * (ni // 2) + (ni % 2) * n + (nj - ni % 2) // 2 + 1
            if checked[n_idx] == -1:
                q.append((ni, nj, nj+1))
                checked[n_idx] = c_idx
answer = []
for i in range(n*n-n//2, 1, -1):
    if checked[i] > 0:
        tmp = i
        while True:
            answer.append(tmp)
            tmp = checked[tmp]
            if tmp == checked[tmp]:
                break
        if answer[-1] > 1:
            answer.append(tmp)
        break
if len(answer) == 0:
    print(1)
    print(1)
else:
    answer.reverse()
    print(len(answer))
    print(*answer)
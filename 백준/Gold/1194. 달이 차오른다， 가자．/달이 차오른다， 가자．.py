from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
si = sj = 0
flag = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            si = i
            sj = j
            flag = 1
            break
    if flag:
        break
ky = 'abcdef'
door = 'ABCDEF'
q = deque([(si, sj, 0, 0)])
checked = [[set() for _ in range(m)] for _ in range(n)]
checked[si][sj].add(0)
d = [(0, -1), (0, 1), (1, 0), (-1, 0)]
answer = -1
while q:
    ci, cj, cnt, k = q.popleft()
    for di, dj in d:
        ni, nj = ci+di, cj+dj
        if 0 <= ni < n and 0 <= nj < m:
            # 빈칸이면
            if arr[ni][nj] == '.' or arr[ni][nj] == '0':
                if k not in checked[ni][nj]:
                    checked[ni][nj].add(k)
                    q.append((ni, nj, cnt + 1, k))
            # 열쇠면
            elif arr[ni][nj].islower():
                if k not in checked[ni][nj]:
                    checked[ni][nj].add(k)
                    q.append((ni, nj, cnt + 1, k | 1 << ky.index(arr[ni][nj])))
            # 문이면
            elif arr[ni][nj].isupper():
                if k & 1 << door.index(arr[ni][nj]) and k not in checked[ni][nj]:
                    checked[ni][nj].add(k)
                    q.append((ni, nj, cnt + 1, k))
            # 출구면
            elif arr[ni][nj] == '1':
                answer = cnt + 1
                break
    if answer > 0:
        break
print(answer)
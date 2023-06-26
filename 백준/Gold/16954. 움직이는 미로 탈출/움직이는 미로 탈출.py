from collections import deque
arr = [list(input()) for _ in range(8)]
d = [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
q = deque()
q.append((7, 0))
answer = 0
while q:
    qq = deque()
    checked = [[True] * 8 for _ in range(8)]
    while q:
        ci, cj = q.pop()
        if arr[ci][cj] == '#':
            continue
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 8 and 0 <= nj < 8 and checked[ni][nj] and arr[ni][nj] == '.':
                if ni == 0 and nj == 7:
                    answer = 1
                    break
                qq.append((ni, nj))
                checked[ni][nj] = False
        if answer:
            break
    if answer:
        break
    for i in range(7, -1, -1):
        for j in range(8):
            if arr[i][j] == '#':
                arr[i][j] = '.'
                if i < 7:
                    arr[i + 1][j] = '#'
    q = qq
print(answer)
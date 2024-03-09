import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
position = [(-1, -1) for _ in range(m+1)]
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            position[arr[i][j]] = (i, j)
            arr[i][j] = (arr[i][j], k)
        else:
            arr[i][j] = (0, 0)

direction = [0] + list(map(int, input().split()))
priority = [[]] + [[] for _ in range(m)]
for i in range(1, m+1):
    priority[i].append(())
    for _ in range(4):
        priority[i].append(tuple(map(int, input().split())))
d = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]
shark = m
for answer in range(1, 1001):
    new = [[(0, 0) for _ in range(n)] for _ in range(n)]
    # 상어 이동
    for shark_number in range(1, m+1):
        ci, cj = position[shark_number]
        if ci == cj == -1: continue
        # 상어의 현재 방향
        now_d = direction[shark_number]
        next_d = -1
        # 상어의 다음 방향을 찾아서
        for n_d in priority[shark_number][now_d]:
            di, dj = d[n_d]
            ni, nj = ci+di, cj+dj
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj][0] == 0:
                    next_d = n_d
                    break
        # 냄새가 없는 곳이 없다면
        if next_d == -1:
            for n_d in priority[shark_number][now_d]:
                di, dj = d[n_d]
                ni, nj = ci+di, cj+dj
                if 0 <= ni < n and 0 <= nj < n:
                    if arr[ni][nj][0] == shark_number:
                        next_d = n_d
                        break
        di, dj = d[next_d]
        ni, nj = ci + di, cj + dj
        # 그 위치에 상어가 없다면 이동
        if new[ni][nj][0] == 0:
            new[ni][nj] = (shark_number, k)
            direction[shark_number] = next_d
            position[shark_number] = (ni, nj)
        else:
            position[shark_number] = (-1, -1)
            direction[shark_number] = 0
            shark -= 1
    if shark <= 1:
        print(answer)
        sys.exit()
    for i in range(n):
        for j in range(n):
            if arr[i][j][1] > 1 and new[i][j][0] == 0:
                new[i][j] = (arr[i][j][0], arr[i][j][1] - 1)
    arr = new
print(-1)
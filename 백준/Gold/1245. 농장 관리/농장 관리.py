from collections import deque
N, M = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
checked = [[0] * M for _ in range(N)]
d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
answer = 0
for i in range(N):
    for j in range(M):
        if checked[i][j] == 0:
            q = deque([(i, j)])
            checked[i][j] = 1
            flag = 0
            while q:
                ci, cj = q.popleft()
                for di, dj in d:
                    ni, nj = ci+di, cj+dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if farm[ni][nj] == farm[ci][cj] and checked[ni][nj] == 0:
                            checked[ni][nj] = 1
                            q.append((ni, nj))
                        elif farm[ni][nj] > farm[ci][cj]:
                            flag = 1
            if flag == 0:
                answer += 1
print(answer)
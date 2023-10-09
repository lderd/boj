def solve(camera_number, camera_idx, sagak):
    global answer
    if camera_idx >= len(camera[camera_number]):
        if camera_number >= 4:
            tmp = max_office - len(sagak)
            if answer > tmp:
                answer = tmp
            return
        return solve(camera_number + 1, 0, sagak)
    ci, cj = camera[camera_number][camera_idx]
    for camera_d in d[camera_number]:
        now = set()
        for di, dj in camera_d:
            cnt = 1
            while True:
                ni, nj = ci + di * cnt, cj + dj * cnt
                if 0 <= ni < n and 0 <= nj < m and office[ni][nj] < 6:
                    now.add((ni, nj))
                    cnt += 1
                else:
                    break
        solve(camera_number, camera_idx + 1, sagak | now)


n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
camera = [[] for _ in range(5)]
d = [[[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]], [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]], [[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(1, 0), (0, -1)], [(1, 0), (0, 1)]], [[(0, -1), (1, 0), (0, 1)], [(-1, 0), (1, 0), (0, 1)], [(-1, 0), (0, -1), (0, 1)], [(-1, 0), (0, -1), (1, 0)]], [[(-1, 0), (0, -1), (1, 0), (0, 1)]]]
max_office = n * m
sagak = set()
for i in range(n):
    for j in range(m):
        if 0 < office[i][j] < 6:
            camera[office[i][j] - 1].append((i, j))
            sagak.add((i, j))
        elif office[i][j] == 6:
            sagak.add((i, j))
answer = max_office
solve(0, 0, sagak)
print(answer)
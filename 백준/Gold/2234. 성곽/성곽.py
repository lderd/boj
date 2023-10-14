m, n = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
room_num = [[-1] * m for _ in range(n)]
cnt = 0
room_size = []
delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]
for i in range(n):
    for j in range(m):
        if room_num[i][j] == -1:
            tmp = 1
            q = [(i, j)]
            room_num[i][j] = cnt
            while q:
                ci, cj = q.pop()
                for d in range(4):
                    if castle[ci][cj] & 1 << d: continue
                    di, dj = delta[d]
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < n and 0 <= nj < m and room_num[ni][nj] == -1:
                        q.append((ni, nj))
                        room_num[ni][nj] = cnt
                        tmp += 1
            room_size.append(tmp)
            cnt += 1
print(cnt)
print(max(room_size))
checked = [[True] * m for _ in range(n)]
max_sum = 0
for i in range(n):
    for j in range(m):
        if checked[i][j]:
            number = room_num[i][j]
            q = [(i, j)]
            compare_checked = set()
            while q:
                ci, cj = q.pop()
                for di, dj in delta:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < n and 0 <= nj < m and checked[ni][nj]:
                        if room_num[ni][nj] == number:
                            q.append((ni, nj))
                            checked[ni][nj] = False
                        elif room_num[ni][nj] not in compare_checked:
                            compare_checked.add(room_num[ni][nj])
                            max_sum = max(max_sum, room_size[number] + room_size[room_num[ni][nj]])
print(max_sum)
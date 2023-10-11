r, c, k = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
check_list = []
heater = []
for i in range(r):
    for j in range(c):
        if room[i][j] == 5:
            check_list.append((i, j))
            room[i][j] = 0
        elif room[i][j] > 0:
            heater.append((i, j, room[i][j]-1))
            room[i][j] = 0
wall = set()
for _ in range(int(input())):
    x, y, t = map(int, input().split())
    wall.add((x-1, y-1, t))
chocolate = 0
dlt = [(0, 1), (0, -1), (-1, 0), (1, 0)]
ddlt = [[(-1, 0), (0, 0), (1, 0)], [(0, -1), (0, 0), (0, 1)]]
wind = [[0] * c for _ in range(r)]
for x, y, d in heater:
    dx, dy = dlt[d]
    checked = set()
    wind[x + dx][y + dy] += 5
    q = [(x + dx, y + dy)]
    for h in range(4, 0, -1):
        nq = []
        while q:
            cx, cy = q.pop()
            for dd in range(3):
                ddx, ddy = ddlt[d // 2][dd]
                nx, ny = cx + dx + ddx, cy + dy + ddy
                if (nx, ny) in checked: continue
                if 0 <= nx < r and 0 <= ny < c:
                    if d == 0:
                        if (cx + ddx, cy + ddy, 1) not in wall:
                            if dd == 0:
                                if (cx, cy, 0) not in wall:
                                    checked.add((nx, ny))
                                    wind[nx][ny] += h
                                    nq.append((nx, ny))
                            elif dd == 2:
                                if (cx + 1, cy, 0) not in wall:
                                    checked.add((nx, ny))
                                    wind[nx][ny] += h
                                    nq.append((nx, ny))
                            else:
                                checked.add((nx, ny))
                                wind[nx][ny] += h
                                nq.append((nx, ny))
                    elif d == 1:
                        if (cx + dx + ddx, cy + dy + ddy, 1) not in wall:
                            if dd == 0:
                                if (cx, cy, 0) not in wall:
                                    checked.add((nx, ny))
                                    wind[nx][ny] += h
                                    nq.append((nx, ny))
                            elif dd == 2:
                                if (cx + 1, cy, 0) not in wall:
                                    checked.add((nx, ny))
                                    wind[nx][ny] += h
                                    nq.append((nx, ny))
                            else:
                                checked.add((nx, ny))
                                wind[nx][ny] += h
                                nq.append((nx, ny))
                    elif d == 2:
                        if (cx + ddx, cy + ddy, 0) not in wall:
                            if dd == 0:
                                if (cx, cy - 1, 1) not in wall:
                                    checked.add((nx, ny))
                                    wind[nx][ny] += h
                                    nq.append((nx, ny))
                            elif dd == 2:
                                if (cx, cy, 1) not in wall:
                                    checked.add((nx, ny))
                                    wind[nx][ny] += h
                                    nq.append((nx, ny))
                            else:
                                checked.add((nx, ny))
                                wind[nx][ny] += h
                                nq.append((nx, ny))
                    else:
                        if (cx + dx + ddx, cy + dy + ddy, 0) not in wall:
                            if dd == 0:
                                if (cx, cy - 1, 1) not in wall:
                                    checked.add((nx, ny))
                                    wind[nx][ny] += h
                                    nq.append((nx, ny))
                            elif dd == 2:
                                if (cx, cy, 1) not in wall:
                                    checked.add((nx, ny))
                                    wind[nx][ny] += h
                                    nq.append((nx, ny))
                            else:
                                checked.add((nx, ny))
                                wind[nx][ny] += h
                                nq.append((nx, ny))
        q = nq
while chocolate <= 100:
    chocolate += 1
    for i in range(r):
        for j in range(c):
            room[i][j] += wind[i][j]
    operator = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if i < r-1 and (i+1, j, 0) not in wall:
                if room[i][j] < room[i+1][j]:
                    gap = (room[i+1][j] - room[i][j]) // 4
                    operator[i+1][j] -= gap
                    operator[i][j] += gap
                elif room[i][j] > room[i+1][j]:
                    gap = (room[i][j] - room[i+1][j]) // 4
                    operator[i+1][j] += gap
                    operator[i][j] -= gap
            if j < c-1 and (i, j, 1) not in wall:
                if room[i][j] < room[i][j+1]:
                    gap = (room[i][j+1] - room[i][j]) // 4
                    operator[i][j+1] -= gap
                    operator[i][j] += gap
                elif room[i][j] > room[i][j+1]:
                    gap = (room[i][j] - room[i][j+1]) // 4
                    operator[i][j+1] += gap
                    operator[i][j] -= gap
    for i in range(r):
        for j in range(c):
            room[i][j] += operator[i][j]
            if (i == 0 or j == 0 or i == r-1 or j == c-1) and room[i][j]:
                room[i][j] -= 1
    flag = 1
    for i, j in check_list:
        if room[i][j] < k:
            flag = 0
            break
    if flag:
        break
print(chocolate)
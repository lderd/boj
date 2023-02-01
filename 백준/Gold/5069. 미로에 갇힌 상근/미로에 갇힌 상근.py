T = int(input())
d1 = [(-1, -1), (-1, 0), (0, 1), (0, -1), (1, 1), (1, 0)]
d2 = [(-1, -1), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 0)]
d3 = [(-1, 0), (-1, 1), (0, 1), (0, -1), (1, 0), (1, -1)]
for _ in range(T):
    n = int(input())
    half = n // 2
    maze = []
    for i in range(half + 1, half * 2 + 2):
        maze.append([0] * i + [-1] * (half * 2 + 1 - i))
    for i in range(half * 2, half, -1):
        maze.append([0] * i + [-1] * (half * 2 + 1 - i))
    maze[half][half] = 1
    cnt = 0
    while cnt < n:
        tmp_maze = [[0] * (half * 2 + 1) for _ in range(half * 2 + 1)]
        for i in range(half * 2 + 1):
            for j in range(half * 2 + 1):
                if maze[i][j] >= 0:
                    tmp = 0
                    if i < half:
                        d = d1
                    elif i == half:
                        d = d2
                    else:
                        d = d3
                    for di, dj in d:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < half * 2 + 1 and 0 <= nj < half * 2 + 1 and maze[ni][nj] >= 0:
                            tmp += maze[ni][nj]
                    tmp_maze[i][j] = tmp
                else:
                    tmp_maze[i][j] = maze[i][j]
        cnt += 1
        maze = tmp_maze
    print(maze[half][half])
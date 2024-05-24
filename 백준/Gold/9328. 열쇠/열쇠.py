from collections import deque
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for _ in range(int(input())):
    h, w = map(int, input().split())
    building = [input() for _ in range(h)]
    start = []
    checked = [[False] * w for _ in range(h)]
    has = set()
    answer = 0
    for i in range(h):
        if building[i][0] != '*':
            start.append((i, 0))
            checked[i][0] = True
            if building[i][0].islower():
                has.add(building[i][0])
            if building[i][0] == '$':
                answer += 1
        if building[i][w - 1] != '*':
            start.append((i, w - 1))
            checked[i][w - 1] = True
            if building[i][w - 1].islower():
                has.add(building[i][w - 1])
            if building[i][w - 1] == '$':
                answer += 1
    for j in range(1, w - 1):
        if building[0][j] != '*':
            start.append((0, j))
            checked[0][j] = True
            if building[0][j].islower():
                has.add(building[0][j])
            if building[0][j] == '$':
                answer += 1
        if building[h - 1][j] != '*':
            start.append((h - 1, j))
            checked[h - 1][j] = True
            if building[h - 1][j].islower():
                has.add(building[h - 1][j])
            if building[h - 1][j] == '$':
                answer += 1
    tmp = input()
    if tmp != '0':
        has = has.union(tmp)
    flag = True
    new_q = start
    while flag:
        q = deque(new_q)
        new_q = []
        flag = False
        while q:
            ci, cj = q.popleft()
            if building[ci][cj].isupper():
                if building[ci][cj].lower() not in has:
                    new_q.append((ci, cj))
                    continue
            for di, dj in d:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < h and 0 <= nj < w and not checked[ni][nj]:
                    checked[ni][nj] = True
                    if building[ni][nj] == '*':
                        continue
                    elif building[ni][nj] == '$':
                        q.append((ni, nj))
                        answer += 1
                    elif building[ni][nj] == '.':
                        q.append((ni, nj))
                    elif building[ni][nj].islower():
                        if building[ni][nj] not in has:
                            has.add(building[ni][nj])
                            flag = True
                        q.append((ni, nj))
                    elif building[ni][nj].isupper():
                        q.append((ni, nj))
    print(answer)
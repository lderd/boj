def down():
    if direction == 0:
        for j in range(n):
            cnt = 0
            for i in range(n-1, -1, -1):
                if board[i][j] >= 0:
                    board[i][j], board[i+cnt][j] = board[i+cnt][j], board[i][j]
                elif board[i][j] == -2:
                    cnt += 1
                elif board[i][j] == -1:
                    cnt = 0
    elif direction == 1:
        for i in range(n):
            cnt = 0
            for j in range(n):
                if board[i][j] >= 0:
                    board[i][j], board[i][j-cnt] = board[i][j-cnt], board[i][j]
                elif board[i][j] == -2:
                    cnt += 1
                elif board[i][j] == -1:
                    cnt = 0
    elif direction == 2:
        for j in range(n):
            cnt = 0
            for i in range(n):
                if board[i][j] >= 0:
                    board[i][j], board[i-cnt][j] = board[i-cnt][j], board[i][j]
                elif board[i][j] == -2:
                    cnt += 1
                elif board[i][j] == -1:
                    cnt = 0
    elif direction == 3:
        for i in range(n):
            cnt = 0
            for j in range(n-1, -1, -1):
                if board[i][j] >= 0:
                    board[i][j], board[i][j+cnt] = board[i][j+cnt], board[i][j]
                elif board[i][j] == -2:
                    cnt += 1
                elif board[i][j] == -1:
                    cnt = 0


def score():
    global answer
    checked = [[False] * n for _ in range(n)]
    cnt_color = 0
    cnt_rainbow = 0
    max_group = {}
    if direction == 0:
        for i in range(n):
            for j in range(n):
                if board[i][j] > 0 and not checked[i][j]:
                    checked[i][j] = True
                    q = [(i, j)]
                    now_color = board[i][j]
                    tmp_color = 1
                    tmp_rainbow = 0
                    tmp = {(i, j)}
                    while q:
                        ci, cj = q.pop()
                        for di, dj in d:
                            ni, nj = ci+di, cj+dj
                            if 0 <= ni < n and 0 <= nj < n:
                                if board[ni][nj] == now_color and not checked[ni][nj]:
                                    checked[ni][nj] = True
                                    tmp_color += 1
                                    q.append((ni, nj))
                                    tmp.add((ni, nj))
                                elif board[ni][nj] == 0 and (ni, nj) not in tmp:
                                    tmp_rainbow += 1
                                    q.append((ni, nj))
                                    tmp.add((ni, nj))
                    if tmp_color + tmp_rainbow < 2:
                        continue
                    if cnt_color + cnt_rainbow < tmp_color + tmp_rainbow:
                        cnt_color = tmp_color
                        cnt_rainbow = tmp_rainbow
                        max_group = tmp
                    elif cnt_color + cnt_rainbow == tmp_color + tmp_rainbow:
                        if cnt_rainbow <= tmp_rainbow:
                            cnt_color = tmp_color
                            cnt_rainbow = tmp_rainbow
                            max_group = tmp
    elif direction == 1:
        for j in range(n-1, -1, -1):
            for i in range(n):
                if board[i][j] > 0 and not checked[i][j]:
                    checked[i][j] = True
                    q = [(i, j)]
                    now_color = board[i][j]
                    tmp_color = 1
                    tmp_rainbow = 0
                    tmp = {(i, j)}
                    while q:
                        ci, cj = q.pop()
                        for di, dj in d:
                            ni, nj = ci+di, cj+dj
                            if 0 <= ni < n and 0 <= nj < n:
                                if board[ni][nj] == now_color and not checked[ni][nj]:
                                    checked[ni][nj] = True
                                    tmp_color += 1
                                    q.append((ni, nj))
                                    tmp.add((ni, nj))
                                elif board[ni][nj] == 0 and (ni, nj) not in tmp:
                                    tmp_rainbow += 1
                                    q.append((ni, nj))
                                    tmp.add((ni, nj))
                    if tmp_color + tmp_rainbow < 2:
                        continue
                    if cnt_color + cnt_rainbow < tmp_color + tmp_rainbow:
                        cnt_color = tmp_color
                        cnt_rainbow = tmp_rainbow
                        max_group = tmp
                    elif cnt_color + cnt_rainbow == tmp_color + tmp_rainbow:
                        if cnt_rainbow <= tmp_rainbow:
                            cnt_color = tmp_color
                            cnt_rainbow = tmp_rainbow
                            max_group = tmp
    elif direction == 2:
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] > 0 and not checked[i][j]:
                    checked[i][j] = True
                    q = [(i, j)]
                    now_color = board[i][j]
                    tmp_color = 1
                    tmp_rainbow = 0
                    tmp = {(i, j)}
                    while q:
                        ci, cj = q.pop()
                        for di, dj in d:
                            ni, nj = ci+di, cj+dj
                            if 0 <= ni < n and 0 <= nj < n:
                                if board[ni][nj] == now_color and not checked[ni][nj]:
                                    checked[ni][nj] = True
                                    tmp_color += 1
                                    q.append((ni, nj))
                                    tmp.add((ni, nj))
                                elif board[ni][nj] == 0 and (ni, nj) not in tmp:
                                    tmp_rainbow += 1
                                    q.append((ni, nj))
                                    tmp.add((ni, nj))
                    if tmp_color + tmp_rainbow < 2:
                        continue
                    if cnt_color + cnt_rainbow < tmp_color + tmp_rainbow:
                        cnt_color = tmp_color
                        cnt_rainbow = tmp_rainbow
                        max_group = tmp
                    elif cnt_color + cnt_rainbow == tmp_color + tmp_rainbow:
                        if cnt_rainbow <= tmp_rainbow:
                            cnt_color = tmp_color
                            cnt_rainbow = tmp_rainbow
                            max_group = tmp
    elif direction == 3:
        for j in range(n):
            for i in range(n-1, -1, -1):
                if board[i][j] > 0 and not checked[i][j]:
                    checked[i][j] = True
                    q = [(i, j)]
                    now_color = board[i][j]
                    tmp_color = 1
                    tmp_rainbow = 0
                    tmp = {(i, j)}
                    while q:
                        ci, cj = q.pop()
                        for di, dj in d:
                            ni, nj = ci+di, cj+dj
                            if 0 <= ni < n and 0 <= nj < n:
                                if board[ni][nj] == now_color and not checked[ni][nj]:
                                    checked[ni][nj] = True
                                    tmp_color += 1
                                    q.append((ni, nj))
                                    tmp.add((ni, nj))
                                elif board[ni][nj] == 0 and (ni, nj) not in tmp:
                                    tmp_rainbow += 1
                                    q.append((ni, nj))
                                    tmp.add((ni, nj))
                    if tmp_color + tmp_rainbow < 2:
                        continue
                    if cnt_color + cnt_rainbow < tmp_color + tmp_rainbow:
                        cnt_color = tmp_color
                        cnt_rainbow = tmp_rainbow
                        max_group = tmp
                    elif cnt_color + cnt_rainbow == tmp_color + tmp_rainbow:
                        if cnt_rainbow <= tmp_rainbow:
                            cnt_color = tmp_color
                            cnt_rainbow = tmp_rainbow
                            max_group = tmp
    if cnt_color + cnt_rainbow > 1:
        answer += (cnt_color + cnt_rainbow) ** 2
        for i, j in max_group:
            board[i][j] = -2
        return False
    else:
        return True


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 어디로 떨어지냐
# 0하, 1좌, 2상, 3우
direction = 0
d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
answer = 0
while True:
    if score(): break
    down()
    direction = (direction + 1) % 4
    down()
print(answer)

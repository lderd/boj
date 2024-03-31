from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# 0흰색, 1빨강, 2파랑
# 뒤집기, 그대로, 방향반대
color = [list(map(int, input().split())) for _ in range(n)]
mal = [()] * k
mal_d = [0] * k
board = [[deque() for _ in range(n)] for _ in range(n)]
for idx in range(k):
    i, j, dr = map(int, input().split())
    mal[idx] = (i-1, j-1)
    if dr == 2:
        dr = 3
    elif dr == 3:
        dr = 2
    mal_d[idx] = dr-1
    board[i-1][j-1].append(idx)
for answer in range(1, 1001):
    for idx in range(k):
        ci, cj= mal[idx]
        cd = mal_d[idx]
        ni, nj = ci+d[cd][0], cj+d[cd][1]
        if 0 <= ni < n and 0 <= nj < n and color[ni][nj] == 1:
            tmp = []
            while board[ci][cj][-1] != idx:
                tmp_idx = board[ci][cj].pop()
                mal[tmp_idx] = (ni, nj)
                tmp.append(tmp_idx)
            tmp.append(board[ci][cj].pop())
            mal[idx] = (ni, nj)
            board[ni][nj].extend(tmp)
            if len(board[ni][nj]) >= 4:
                print(answer)
                sys.exit()
        elif 0 <= ni < n and 0 <= nj < n and color[ni][nj] == 0:
            tmp = deque()
            while board[ci][cj][-1] != idx:
                tmp_idx = board[ci][cj].pop()
                mal[tmp_idx] = (ni, nj)
                tmp.appendleft(tmp_idx)
            tmp.appendleft(board[ci][cj].pop())
            board[ni][nj].extend(tmp)
            mal[idx] = (ni, nj)
            if len(board[ni][nj]) >= 4:
                print(answer)
                sys.exit()
        else:
            cd = (cd + 2) % 4
            ni, nj = ci+d[cd][0], cj+d[cd][1]
            mal_d[idx] = cd
            if 0 <= ni < n and 0 <= nj < n and color[ni][nj] == 1:
                tmp = []
                while board[ci][cj][-1] != idx:
                    tmp_idx = board[ci][cj].pop()
                    mal[tmp_idx] = (ni, nj)
                    tmp.append(tmp_idx)
                tmp.append(board[ci][cj].pop())
                board[ni][nj].extend(tmp)
                mal[idx] = (ni, nj)
                if len(board[ni][nj]) >= 4:
                    print(answer)
                    sys.exit()
            elif 0 <= ni < n and 0 <= nj < n and color[ni][nj] == 0:
                tmp = deque()
                while board[ci][cj][-1] != idx:
                    tmp_idx = board[ci][cj].pop()
                    mal[tmp_idx] = (ni, nj)
                    tmp.appendleft(tmp_idx)
                tmp.appendleft(board[ci][cj].pop())
                board[ni][nj].extend(tmp)
                mal[idx] = (ni, nj)
                if len(board[ni][nj]) >= 4:
                    print(answer)
                    sys.exit()
print(-1)

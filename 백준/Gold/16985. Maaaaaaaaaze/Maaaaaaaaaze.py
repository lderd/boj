from collections import deque
from copy import deepcopy
def dfs():
    def bfs():
        global answer
        if board[0][0][0] == 0 or board[4][4][4] == 0: return
        checked = [[[False] * 5 for _ in range(5)] for _ in range(5)]
        q = deque([(0, 0, 0, 0)])
        checked[0][0][0] = True
        while q:
            ci, cj, ck, cnt = q.popleft()
            if cnt >= answer - 1: return
            for di, dj, dk in d:
                ni, nj, nk = ci+di, cj+dj, ck+dk
                if 0 <= ni < 5 and 0 <= nj < 5 and 0 <= nk < 5 and not checked[nk][ni][nj] and board[nk][ni][nj]:
                    if ni == nj == nk == 4:
                        answer = cnt + 1
                        return
                    else:
                        checked[nk][ni][nj] = True
                        q.append((ni, nj, nk, cnt+1))
    def rotate(k):
        tmp = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                tmp[j][4-i] = board[k][i][j]
        board[k] = tmp
    board = [deepcopy(new_board[0]), deepcopy(new_board[1]), deepcopy(new_board[2]), deepcopy(new_board[3]), deepcopy(new_board[4])]
    for _ in range(4):
        for _ in range(4):
            for _ in range(4):
                for _ in range(4):
                    for _ in range(4):
                        bfs()
                        rotate(4)
                    rotate(3)
                rotate(2)
            rotate(1)
        rotate(0)


origin_board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
answer = 200
d = [(0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
for i in range(5):
    index = [i]
    for j in range(5):
        if j not in index:
            index.append(j)
            for k in range(5):
                if k not in index:
                    index.append(k)
                    for l in range(5):
                        if l not in index:
                            index.append(l)
                            for m in range(5):
                                if m not in index:
                                    index.append(m)
                                    new_board = [deepcopy(origin_board[index[0]]), deepcopy(origin_board[index[1]]), deepcopy(origin_board[index[2]]), deepcopy(origin_board[index[3]]), deepcopy(origin_board[index[4]])]
                                    dfs()
                                    index.pop()
                            index.pop()
                    index.pop()
            index.pop()
if answer == 200:
    print(-1)
else:
    print(answer)
def solve(ci, cj, cnt):
    global answer
    for di, dj in d:
        if answer < 0:
            return
        ni, nj = ci + di * board[ci][cj], cj + dj * board[ci][cj]
        if 0 <= ni < n and 0 <= nj < m:
            if checked[ni][nj][0]:
                answer = -1
                return
            else:
                if board[ni][nj] == 'H':
                    if cnt > answer:
                        answer = cnt
                else:
                    if checked[ni][nj][1] < cnt:
                        checked[ni][nj][1] = cnt
                        checked[ni][nj][0] = cnt
                        solve(ni, nj, cnt + 1)
                        checked[ni][nj][0] = 0
        else:
            if cnt > answer:
                answer = cnt


n, m = map(int, input().split())
board = [list(map(lambda x: int(x) if x.isdigit() else x, input())) for _ in range(n)]
checked = [[[0] * 2 for _ in range(m)] for _ in range(n)]
checked[0][0][0] = 1
answer = 0
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
solve(0, 0, 1)
print(answer)
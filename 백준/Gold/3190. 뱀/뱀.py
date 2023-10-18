from collections import deque
n = int(input())
apple = set()
for _ in range(int(input())):
    i, j = map(int, input().split())
    apple.add((i-1, j-1))
board = [[False] * n for _ in range(n)]
board[0][0] = True
snake = deque([(0, 0)])
l = int(input())
rotate = []
for _ in range(l):
    t, c = input().split()
    rotate.append([int(t), c])
answer = 0
dlt = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
rotate_idx = 0
flag = 0
while True:
    answer += 1
    ci, cj = snake[-1]
    di, dj = dlt[d]
    ni, nj = ci + di, cj + dj
    if ni < 0 or ni >= n or nj < 0 or nj >= n or board[ni][nj]:
        break
    if (ni, nj) in apple:
        apple.remove((ni, nj))
    else:
        ri, rj = snake.popleft()
        board[ri][rj] = False
    snake.append((ni, nj))
    board[ni][nj] = True
    if rotate_idx < l and answer == rotate[rotate_idx][0]:
        if rotate[rotate_idx][1] == 'D':
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4
        rotate_idx += 1
print(answer)
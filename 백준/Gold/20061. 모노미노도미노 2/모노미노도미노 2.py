import sys
input = sys.stdin.readline
def block_g(t, y):
    for i in range(2, 6):
        if t == 1:
            if green[i][y] == 1:
                green[i-1][y] = 1
                break
        elif t == 2:
            if green[i][y] == 1 or green[i][y+1] == 1:
                green[i-1][y] = 1
                green[i-1][y+1] = 1
                break
        else:
            if green[i][y] == 1:
                green[i-1][y] = 1
                green[i-2][y] = 1
                break
    else:
        if t == 1:
            green[5][y] = 1
        elif t == 2:
            green[5][y] = 1
            green[5][y+1] = 1
        else:
            green[5][y] = 1
            green[4][y] = 1


def block_b(t, x):
    for i in range(2, 6):
        if t == 1:
            if blue[i][x] == 1:
                blue[i-1][x] = 1
                break
        elif t == 2:
            if blue[i][x] == 1:
                blue[i-1][x] = 1
                blue[i-2][x] = 1
                break
        else:
            if blue[i][x] == 1 or blue[i][x+1] == 1:
                blue[i-1][x] = 1
                blue[i-1][x+1] = 1
                break
    else:
        if t == 1:
            blue[5][x] = 1
        elif t == 2:
            blue[5][x] = 1
            blue[4][x] = 1
        else:
            blue[5][x] = 1
            blue[5][x+1] = 1



def boom():
    cnt_g = 0
    cnt_b = 0
    for i in range(2, 6):
        if sum(green[i]) == 4:
            green[i] = [0, 0, 0, 0]
            cnt_g += 1
        if sum(blue[i]) == 4:
            blue[i] = [0, 0, 0, 0]
            cnt_b += 1
    return (cnt_g, cnt_b)


def drop():
    cnt_g = 0
    cnt_b = 0
    for i in range(5, -1, -1):
        if sum(green[i]) == 0:
            cnt_g += 1
        else:
            if cnt_g:
                for j in range(4):
                    green[i + cnt_g][j] = green[i][j]
                    green[i][j] = 0
        if sum(blue[i]) == 0:
            cnt_b += 1
        else:
            if cnt_b:
                for j in range(4):
                    blue[i + cnt_b][j] = blue[i][j]
                    blue[i][j] = 0


def spill():
    cnt_g = 0
    cnt_b = 0
    for i in range(2):
        if sum(green[i]) > 0:
            cnt_g += 1
        if sum(blue[i]) > 0:
            cnt_b += 1
    for _ in range(cnt_g):
        green.pop()
        green.insert(0, [0] * 4)
    for _ in range(cnt_b):
        blue.pop()
        blue.insert(0, [0] * 4)


n = int(input())
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]
answer = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    block_g(t, y)
    block_b(t, x)
    cnt_g, cnt_b = boom()
    answer += cnt_g + cnt_b
    if cnt_g or cnt_b:
        drop()
    spill()
print(answer)
cnt = 0
for i in range(6):
    cnt += sum(green[i]) + sum(blue[i])
print(cnt)
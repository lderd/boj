r, s = map(int, input().split())
picture = [input() for _ in range(r)]
dist = r
for j in range(s):
    ground = r
    for i in range(r-1, -1, -1):
        if picture[i][j] == '#':
            ground = i
        if picture[i][j] == 'X':
            dist = min(ground - i - 1, dist)
            break
answer = [['.'] * s for _ in range(r)]
for i in range(r):
    for j in range(s):
        if picture[i][j] == 'X':
            answer[i+dist][j] = 'X'
        elif picture[i][j] == '#':
            answer[i][j] = '#'
for i in range(r):
    print(''.join(answer[i]))
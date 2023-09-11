import sys
r, c, n = map(int, input().split())
if n % 4 == 2 or n % 4 == 0:
    for _ in range(r):
        print('O' * c)
    sys.exit()
first = set()
for i in range(r):
    row = input()
    for j in range(c):
        if row[j] == 'O':
            first.add((i, j))
unable = set()
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i, j in first:
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c and (ni, nj) not in first:
            unable.add((ni, nj))
three = set()
for i in range(r):
    for j in range(c):
        if (i, j) not in first and (i, j) not in unable:
            three.add((i, j))
unable.clear()
for i, j in three:
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c and (ni, nj) not in three:
            unable.add((ni, nj))
one = set()
for i in range(r):
    for j in range(c):
        if (i, j) not in three and (i, j) not in unable:
            one.add((i, j))
answer = [['.'] * c for _ in range(r)]
if n == 1:
    for i, j in first:
        answer[i][j] = 'O'
    for i in range(r):
        print(''.join(answer[i]))
elif n % 4 == 1:
    for i, j in one:
        answer[i][j] = 'O'
    for i in range(r):
        print(''.join(answer[i]))
else:
    for i, j in three:
        answer[i][j] = 'O'
    for i in range(r):
        print(''.join(answer[i]))
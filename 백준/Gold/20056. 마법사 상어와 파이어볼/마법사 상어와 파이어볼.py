from pprint import pprint
def move():
    global arr
    n_arr = [[[0, 0, []] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mass, s, directions = arr[i][j]
            if mass:
                for direction in directions:
                    ni, nj = (i + s * d[direction][0]) % n, (j + s * d[direction][1]) % n
                    n_arr[ni][nj][0] += mass
                    n_arr[ni][nj][1] += s
                    n_arr[ni][nj][2].append(direction)
    arr = n_arr


def divide():
    global arr
    n_arr = [[[0, 0, []] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mass, s, directions = arr[i][j]
            if len(directions) >= 2:
                mass //= 5
                if mass:
                    s //= len(directions)
                    same = -1
                    for direction in directions:
                        if same == -1:
                            same = direction % 2
                        else:
                            if same != direction % 2:
                                directions = [1, 3, 5, 7]
                                break
                    else:
                        directions = [0, 2, 4, 6]
                    n_arr[i][j] = [mass, s, directions]
            elif len(directions) == 1:
                n_arr[i][j] = [mass, s, directions]
    arr = n_arr


n, m, k = map(int, input().split())
#       질량, 속력, [방향]
arr = [[[0, 0, []] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    # r, c, 질량, 속력, 방향
    r, c, mass, s, d = map(int, input().split())
    arr[r-1][c-1][0] += mass
    arr[r-1][c-1][1] += s
    arr[r-1][c-1][2].append(d)
cnt = 0
d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
while cnt < k:
    cnt += 1
    move()
    divide()
answer = 0
for i in range(n):
    for j in range(n):
        mass, s, directions = arr[i][j]
        if mass:
            answer += mass * len(directions)
print(answer)
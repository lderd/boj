def cross_area(i, j):
    cnt = 1
    flag = 0
    while True:
        for di, dj in d:
            ni, nj = i + di * cnt, j + dj * cnt
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == '#' and checked[ni][nj] == 0:
                continue
            else:
                flag = 1
                break
        else:
            cnt += 1
        if flag:
            break
    return (cnt - 1) * 4 + 1


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
answer = 0
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
checked1 = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == '#':
            checked1[i][j] = 1
            checked = [[0] * m for _ in range(n)]
            cnt = 1
            checked[i][j] = 1
            flag = 0
            area1 = (cnt - 1) * 4 + 1
            for ci in range(n):
                for cj in range(m):
                    if arr[ci][cj] == '#' and checked[ci][cj] == 0 and checked1[ci][cj] == 0:
                        area2 = cross_area(ci, cj)
                        if area1 * area2 > answer:
                            answer = area1 * area2
            while True:
                check = []
                for di, dj in d:
                    ni, nj = i + di * cnt, j + dj * cnt
                    if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == '#':
                        check.append((ni, nj))
                    else:
                        flag = 1
                        break
                else:
                    cnt += 1
                    area1 = (cnt - 1) * 4 + 1
                    for ni, nj in check:
                        checked[ni][nj] = 1
                    for ci in range(n):
                        for cj in range(m):
                            if arr[ci][cj] == '#' and checked[ci][cj] == 0 and checked1[ci][cj] == 0:
                                area2 = cross_area(ci, cj)
                                if area1 * area2 > answer:
                                    answer = area1 * area2
                if flag:
                    break
print(answer)
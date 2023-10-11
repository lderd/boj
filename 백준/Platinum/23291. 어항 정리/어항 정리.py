n, k = map(int, input().split())
arr = list(map(int, input().split()))
h = 0
w = 0
tmp = 0
for i in range(1, 11):
    for j in range(2):
        if n - (tmp + i) >= i + j:
            tmp += i
        else:
            h = i - 1 + j
            w = i
            break
    if w > 0:
        break
answer = 0
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while max(arr) - min(arr) > k:
    plus = min(arr)
    for i in range(n):
        if arr[i] == plus:
            arr[i] += 1
    new_arr = [[-1] * w for _ in range(h)] + [arr[tmp:]]
    i = h
    j = 0
    d = 0
    for idx in range(tmp-1, -1, -1):
        while True:
            di, dj = delta[d]
            ni, nj = i + di, j + dj
            if 0 <= ni < h and 0 <= nj < w and new_arr[ni][nj] == -1:
                i, j = ni, nj
                break
            else:
                d = (d + 1) % 4
        new_arr[i][j] = arr[idx]

    operator = [[0] * w for _ in range(h)] + [[0] * (n - tmp)]
    for i in range(h):
        for j in range(w):
            if j + 1 < w:
                if new_arr[i][j+1] > new_arr[i][j]:
                    gap = (new_arr[i][j+1] - new_arr[i][j]) // 5
                    operator[i][j] += gap
                    operator[i][j+1] -= gap
                elif new_arr[i][j+1] < new_arr[i][j]:
                    gap = (new_arr[i][j] - new_arr[i][j+1]) // 5
                    operator[i][j] -= gap
                    operator[i][j+1] += gap
            if i + 1 <= h:
                if new_arr[i+1][j] > new_arr[i][j]:
                    gap = (new_arr[i+1][j] - new_arr[i][j]) // 5
                    operator[i][j] += gap
                    operator[i+1][j] -= gap
                elif new_arr[i+1][j] < new_arr[i][j]:
                    gap = (new_arr[i][j] - new_arr[i+1][j]) // 5
                    operator[i][j] -= gap
                    operator[i+1][j] += gap
    for j in range(n - tmp - 1):
        if new_arr[h][j+1] > new_arr[h][j]:
            gap = (new_arr[h][j+1] - new_arr[h][j]) // 5
            operator[h][j] += gap
            operator[h][j+1] -= gap
        elif new_arr[h][j+1] < new_arr[h][j]:
            gap = (new_arr[h][j] - new_arr[h][j+1]) // 5
            operator[h][j] -= gap
            operator[h][j+1] += gap
    for i in range(h):
        for j in range(w):
            new_arr[i][j] += operator[i][j]
    for j in range(n - tmp):
        new_arr[h][j] += operator[h][j]
    new_new_arr = [[0] * (n // 4) for _ in range(4)]
    i = h
    j = 0
    for new_new_i in [2, 1, 0, 3]:
        for new_new_j in range(n//4):
            if new_new_i % 2:
                new_new_arr[new_new_i][new_new_j] = new_arr[i][j]
            else:
                new_new_arr[new_new_i][-new_new_j-1] = new_arr[i][j]
            if i - 1 < 0:
                j += 1
                i = h
            elif j >= w:
                j += 1
            else:
                i -= 1
    operator = [[0] * (n//4) for _ in range(4)]
    for i in range(4):
        for j in range(n//4):
            if j + 1 < n // 4:
                if new_new_arr[i][j+1] > new_new_arr[i][j]:
                    gap = (new_new_arr[i][j+1] - new_new_arr[i][j]) // 5
                    operator[i][j] += gap
                    operator[i][j+1] -= gap
                elif new_new_arr[i][j+1] < new_new_arr[i][j]:
                    gap = (new_new_arr[i][j] - new_new_arr[i][j+1]) // 5
                    operator[i][j] -= gap
                    operator[i][j+1] += gap
            if i + 1 < 4:
                if new_new_arr[i+1][j] > new_new_arr[i][j]:
                    gap = (new_new_arr[i+1][j] - new_new_arr[i][j]) // 5
                    operator[i][j] += gap
                    operator[i+1][j] -= gap
                elif new_new_arr[i+1][j] < new_new_arr[i][j]:
                    gap = (new_new_arr[i][j] - new_new_arr[i+1][j]) // 5
                    operator[i][j] -= gap
                    operator[i+1][j] += gap
    new_tmp = 0
    for j in range(n//4):
        for i in range(3, -1, -1):
            arr[new_tmp] = new_new_arr[i][j] + operator[i][j]
            new_tmp += 1
    answer += 1
print(answer)

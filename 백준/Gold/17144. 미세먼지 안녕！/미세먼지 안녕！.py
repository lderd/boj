from collections import deque
def check_dust():
    global answer
    answer = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                answer += arr[i][j]
                q.append((i, j, arr[i][j]))


r, c, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
q = deque()
cleaner = []
cleaner_ = 0
upper_cleaner = 0
lower_cleaner = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            cleaner_ += -1
            if cleaner_ == -1:
                upper_cleaner = i
            else:
                lower_cleaner = i
            cleaner.append((i, j, cleaner_))
        elif arr[i][j] > 0:
            q.append((i, j, arr[i][j]))
t = 0
q.extend(cleaner)
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0
while q and t < T:
    i, j, dust = q.popleft()
    if dust <= -2:
        t += 1
        check_dust()
        q.extend(cleaner)
    elif dust > -1:
        cnt = 0
        for di, dj in d:
            ni, nj = i+di, j+dj
            if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] > -1:
                cnt += 1
                if nj == 0:
                    if ni < upper_cleaner - 1:
                        arr[ni + 1][nj] += dust // 5
                    elif ni > lower_cleaner + 1:
                        arr[ni - 1][nj] += dust // 5

                elif nj == c - 1:
                    if ni == 0 or ni == r - 1:
                        arr[ni][nj - 1] += dust // 5
                    elif ni <= upper_cleaner:
                        arr[ni - 1][nj] += dust // 5
                    elif ni >= lower_cleaner:
                        arr[ni + 1][nj] += dust // 5

                elif ni == upper_cleaner or ni == lower_cleaner:
                    arr[ni][nj+1] += dust // 5

                elif ni == 0 or ni == r - 1:
                    arr[ni][nj - 1] += dust // 5

                else:
                    arr[ni][nj] += dust // 5
        arr[i][j] -= dust

        if j == 0:
            if i < upper_cleaner - 1:
                arr[i + 1][j] += dust - dust // 5 * cnt
            elif i > lower_cleaner + 1:
                arr[i - 1][j] += dust - dust // 5 * cnt

        elif j == c - 1:
            if i == 0 or i == r - 1:
                arr[i][j - 1] += dust - dust // 5 * cnt
            elif i <= upper_cleaner:
                arr[i - 1][j] += dust - dust // 5 * cnt
            elif i >= lower_cleaner:
                arr[i + 1][j] += dust - dust // 5 * cnt

        elif i == upper_cleaner or i == lower_cleaner:
            arr[i][j + 1] += dust - dust // 5 * cnt

        elif i == 0 or i == r - 1:
            arr[i][j - 1] += dust - dust // 5 * cnt

        else:
            arr[i][j] += dust - dust // 5 * cnt

print(answer)
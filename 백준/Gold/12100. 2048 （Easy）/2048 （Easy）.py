def up(arr):
    tmp = [[0] * n for _ in range(n)]
    rows = [0] * n
    for j in range(n):
        for i in range(n):
            if arr[i][j]:
                if tmp[rows[j]][j] == 0:
                    tmp[rows[j]][j] += arr[i][j]
                elif tmp[rows[j]][j] == arr[i][j]:
                    tmp[rows[j]][j] += arr[i][j]
                    rows[j] += 1
                else:
                    rows[j] += 1
                    tmp[rows[j]][j] += arr[i][j]
    return tmp


def down(arr):
    tmp = [[0] * n for _ in range(n)]
    rows = [n-1] * n
    for j in range(n):
        for i in range(n-1, -1, -1):
            if arr[i][j]:
                if tmp[rows[j]][j] == 0:
                    tmp[rows[j]][j] += arr[i][j]
                elif tmp[rows[j]][j] == arr[i][j]:
                    tmp[rows[j]][j] += arr[i][j]
                    rows[j] -= 1
                else:
                    rows[j] -= 1
                    tmp[rows[j]][j] += arr[i][j]
    return tmp


def left(arr):
    tmp = [[0] * n for _ in range(n)]
    cols = [0] * n
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                if tmp[i][cols[i]] == 0:
                    tmp[i][cols[i]] += arr[i][j]
                elif tmp[i][cols[i]] == arr[i][j]:
                    tmp[i][cols[i]] += arr[i][j]
                    cols[i] += 1
                else:
                    cols[i] += 1
                    tmp[i][cols[i]] += arr[i][j]
    return tmp


def right(arr):
    tmp = [[0] * n for _ in range(n)]
    cols = [n-1] * n
    for i in range(n):
        for j in range(n-1, -1, -1):
            if arr[i][j]:
                if tmp[i][cols[i]] == 0:
                    tmp[i][cols[i]] += arr[i][j]
                elif tmp[i][cols[i]] == arr[i][j]:
                    tmp[i][cols[i]] += arr[i][j]
                    cols[i] -= 1
                else:
                    cols[i] -= 1
                    tmp[i][cols[i]] += arr[i][j]
    return tmp


def max_check(arr):
    global answer
    for i in range(n):
        for j in range(n):
            if arr[i][j] > answer:
                answer = arr[i][j]


def solve(arr, cnt):
    max_check(arr)
    if cnt < 5:
        solve(up(arr), cnt+1)
        solve(down(arr), cnt+1)
        solve(right(arr), cnt+1)
        solve(left(arr), cnt+1)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
solve(arr, 0)
print(answer)
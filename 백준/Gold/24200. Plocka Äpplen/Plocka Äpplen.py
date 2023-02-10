def solve(i, j, tmp, cnt):
    global answer
    if tmp > answer:
        answer = tmp
    if cnt >= k:
        return
    for di, dj in d:
        ni, nj = i+di, j+dj
        if 0 <= ni < 2 and 0 <= nj < n and checked[ni][nj] == 0:
            checked[ni][nj] = 1
            solve(ni, nj, tmp+arr[ni][nj], cnt + 1)
            checked[ni][nj] = 0


n, k = map(int, input().split())
answer = 0
arr = [list(map(int, input().split())) for _ in range(2)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
checked = [[0] * n for _ in range(2)]
checked[1][0] = 1
solve(1, 0, arr[1][0], 1)
print(answer)
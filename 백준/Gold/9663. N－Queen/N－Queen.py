def solve(a, b, checked):
    global answer
    for di, dj in d:
        ci, cj = a + di, b + dj
        while 0 <= ci < n and 0 <= cj < n:
            if (ci, cj) in checked:
                return
            ci += di
            cj += dj
    if sum(col) >= n:
        answer += 1
        return
    for j in range(n):
        if col[j] == 0:
            col[j] = 1
            solve(a+1, j, checked | {(a+1, j)})
            col[j] = 0


n = int(input())
answer = 0
d = [(-1, 1), (-1, -1)]
for j in range(n//2):
    check = set()
    check.add((0, j))
    col = [0] * n
    col[j] = 1
    solve(0, j, check)
answer *= 2
if n % 2:
    check = set()
    check.add((0, n//2))
    col = [0] * n
    col[n//2] = 1
    solve(0, n//2, check)
print(answer)
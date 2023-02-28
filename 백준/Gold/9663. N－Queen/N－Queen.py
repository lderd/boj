def solve(cnt):
    global answer
    if cnt >= n:
        answer += 1
        return
    for i in range(n):
        if col[i] == 0:
            if checked[i+n-cnt][0]:
                continue
            if checked[i+n+cnt][1]:
                continue
            col[i] = 1
            checked[i+n-cnt][0] = 1
            checked[i+n+cnt][1] = 1

            solve(cnt+1)

            col[i] = 0
            checked[i+n-cnt][0] = 0
            checked[i+n+cnt][1] = 0


n = int(input())
answer = 0
for i in range(n):
    col = [0] * n
    checked = [[0, 0] for _ in range(n*3)]
    checked[i+n] = [1, 1]
    col[i] = 1
    solve(1)
print(answer)
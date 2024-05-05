n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
answer = 1
checked = [[-1] * (1 << n + 1) for _ in range(n)]
checked[0][1<<0] = 0
for ans in range(2, n+1):
    flag = False
    tmp = [[-1] * (1 << n + 1) for _ in range(n)]
    for i in range(n):
        for j in range(1, 1<<n+1):
            if checked[i][j] >= 0:
                for k in range(n):
                    if j & (1 << k): continue
                    if arr[i][k] >= checked[i][j]:
                        if tmp[k][j+(1<<k)] == -1 or tmp[k][j+(1<<k)] > arr[i][k]:
                            tmp[k][j+(1<<k)] = arr[i][k]
                        flag = True
    if flag:
        checked = tmp
        answer = ans
    else:
        break
print(answer)
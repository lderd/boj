n = int(input())
arr = [float(input()) for _ in range(n)]
tmp = arr[0]
answer = tmp
for i in range(1, n):
    tmp = max(tmp * arr[i], arr[i])
    answer = max(answer, tmp)
print('%.3f'%answer)
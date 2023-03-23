n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[9876543210] * (1 << n) for _ in range(n)]
for i in range(n):
    if arr[0][i]:
        memo[i][1 << i] = arr[0][i]
for i in range(1 << n):
    for j in range(n):
        if memo[j][i] < 9876543210:
            for k in range(n):
                if 1 << k & i == 0 and arr[j][k]:
                    memo[k][i | 1 << k] = min(memo[j][i] + arr[j][k], memo[k][i | 1 << k])
print(memo[0][(1 << n) - 1])
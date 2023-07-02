n, d = map(int, input().split())
dp = [10001] * (d+1)
dp[0] = 0
short = sorted([list(map(int, input().split())) for _ in range(n)])
for j in range(n):
    s, e, dist = short[j]
    tmp = [10001] * (d+1)
    tmp[0] = 0
    for i in range(1, d+1):
        if i == e:
            tmp[e] = min(dp[e], tmp[s] + dist, tmp[e-1] + 1)
        else:
            tmp[i] = min(dp[i], tmp[i-1] + 1)
    dp = tmp
print(dp[d])
n = int(input())
dp = [[0]*1024 for _ in range(10)]
for i in range(1, 10):
    dp[i][1<<i] = 1
for _ in range(n-1):
    tmp = [[0]*1024 for _ in range(10)]
    for i in range(10):
        for j in range(1, 1024):
            if (1 << i) & j and dp[i][j]:
                if i < 9:
                    tmp[i+1][j|(1<<(i+1))] += dp[i][j]
                    tmp[i+1][j|(1<<(i+1))] %= 1000000000
                if i > 0:
                    tmp[i-1][j|(1<<(i-1))] += dp[i][j]
                    tmp[i-1][j|(1<<(i-1))] %= 1000000000
    dp = tmp
print(sum(dp[i][1023] for i in range(10)) % 1000000000)
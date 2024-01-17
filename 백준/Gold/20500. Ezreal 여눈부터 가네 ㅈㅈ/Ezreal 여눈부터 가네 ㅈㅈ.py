n = int(input())
dp = [[0] * 10 for _ in range(2)]
dp[0][1] = 1
dp[1][5] = 1
for _ in range(n-1):
    tmp = [[0] * 10 for _ in range(2)]
    for i in range(2):
        for j in range(10):
            if dp[i][j]:
                ssum = j + 1
                while ssum >= 10:
                    ssum -= 10
                    ssum += 1
                tmp[0][ssum] += dp[i][j]
                tmp[0][ssum] %= 1000000007
                ssum = j + 5
                while ssum >= 10:
                    ssum -= 10
                    ssum += 1
                tmp[1][ssum] += dp[i][j]
                tmp[1][ssum] %= 1000000007
    dp = tmp
print((dp[1][0] + dp[1][3] + dp[1][6] + dp[1][9]) % 1000000007)
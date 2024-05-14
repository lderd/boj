for _ in range(int(input())):
    n, m = map(int, input().split())
    dp = [1] * m
    for cnt in range(1, n):
        tmp = [0] * m
        for i in range(m):
            for j in range(i+1, m):
                tmp[j] += dp[i]
        dp = tmp
    print(sum(dp))
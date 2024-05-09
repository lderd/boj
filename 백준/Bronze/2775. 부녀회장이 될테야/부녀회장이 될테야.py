T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    dp = list(range(n+1))
    for _ in range(k):
        tmp = [0]
        for i in range(1, n+1):
            tmp.append(tmp[-1] + dp[i])
        dp = tmp
    print(dp[-1])
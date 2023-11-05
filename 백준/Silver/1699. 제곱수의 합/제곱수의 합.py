n = int(input())
number = 2
dp = list(range(n+1))
while True:
    sq = number * number
    if sq > n:
        break
    tmp = [0] * (n+1)
    for i in range(1, n+1):
        if i >= sq:
            tmp[i] = min(dp[i], tmp[i-sq]+1, dp[i-sq]+1)
        else:
            tmp[i] = dp[i]
    number += 1
    dp = tmp
print(dp[n])
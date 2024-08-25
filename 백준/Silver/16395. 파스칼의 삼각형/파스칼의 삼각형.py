def find(a, b):
    if dp[a][b]:
        return dp[a][b]
    if a == b:
        dp[a][b] = 1
        return dp[a][b]
    dp[a][b] = find(a-1, b - 1) + find(a-1, b)
    return dp[a][b]

n, k = map(int, input().split())
dp = [[1] + [0] * i for i in range(n)]
print(find(n-1, k-1))
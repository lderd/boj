n = int(input())
dp = [int(input())]
for i in range(1, n):
    a = list(map(int, input().split()))
    tmp = [0] * (i + 1)
    for j in range(i):
        tmp[j] = max(dp[j] + a[j], tmp[j])
        tmp[j+1] = max(dp[j] + a[j+1], tmp[j+1])
    dp = tmp
print(max(dp))
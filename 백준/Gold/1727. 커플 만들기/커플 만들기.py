n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
if n < m :
    n, m = m, n
    arr1, arr2 = arr2, arr1
arr1.sort()
arr2.sort()
dp = [[0, 0] for _ in range(n)]
for j in range(m):
    tmp = [[0, 0] for _ in range(n)]
    tmp[0] = [1, abs(arr1[0] - arr2[j])]
    for i in range(1, n):
        if tmp[i-1][0] < dp[i-1][0] + 1:
            tmp[i] = [dp[i-1][0] + 1, dp[i-1][1] + abs(arr1[i] - arr2[j])]
        elif tmp[i-1][0] == dp[i-1][0] + 1:
            tmp[i] = [dp[i-1][0] + 1, min(dp[i-1][1] + abs(arr1[i] - arr2[j]), tmp[i-1][1])]
    dp = tmp
print(dp[-1][1])
n = int(input())
A = list(map(int, input().split()))
answer = 0
dp = [A[0]]
for i in range(1, n):
    tmp = A[i]
    for j in range(i):
        if A[i] > A[j] and tmp < dp[j] + A[i]:
            tmp = dp[j] + A[i]
    dp.append(tmp)
print(max(dp))
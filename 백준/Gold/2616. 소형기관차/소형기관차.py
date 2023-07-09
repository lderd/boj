n = int(input())
arr = list(map(int, input().split()))
cnt = int(input())
ssum = [0] * n
for i in range(n):
    if i < cnt:
        ssum[i] = sum(arr[0:i+1])
    else:
        ssum[i] = sum(arr[i-cnt+1:i+1])
dp = [0] * n
for _ in range(3):
    tmp = [0] * n
    for i in range(n):
        if i < cnt:
            tmp[i] = sum(arr[0:i+1])
        else:
            tmp[i] = max(dp[i], dp[i-cnt] + ssum[i], tmp[i-1])
    dp = tmp
print(dp[n-1])
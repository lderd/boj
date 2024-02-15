from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))
answer = 0
dp = []
for num in arr:
    i = bisect_left(dp, num)
    if i >= answer:
        dp.append(num)
        answer += 1
    else:
        dp[i] = num
print(answer)
from collections import defaultdict
n, m = map(int, input().split())
nums = defaultdict(int)
if m:
    numlist = list(map(int, input().split()))
    for i in range(m):
        nums[numlist[i]] = i + 1
    numset = set(numlist)
dp = [[0] * (1 << (m + 1)) for _ in range(10)]
for i in range(10):
    dp[i][1 << nums[i]] += 1
for _ in range(n - 1):
    tmp = [[0] * (1 << (m + 1)) for _ in range(10)]
    for i in range(10):
        for j in range(1 << (m + 1)):
            if dp[i][j]:
                for k in range(10):
                    tmp[k][j | (1 << nums[k])] += dp[i][j]
    dp = tmp
answer = 0
for i in range(10):
    for tmp in range(2):
        answer += dp[i][-1 - tmp]
print(answer)
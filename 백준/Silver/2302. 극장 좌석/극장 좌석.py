def solve(i):
    if dp[i]:
        return dp[i]
    else:
        dp[i] = solve(i-1) + solve(i-2)
        return dp[i]


n = int(input())
dp = [1, 1, 2] + [0] * (n - 2)
m = int(input())
gojung = [0] + [int(input()) for _ in range(m)] + [n+1]
cnt = []
for i in range(1, m+2):
    cnt.append(solve(gojung[i]-gojung[i-1]-1))
answer = 1
for tmp in cnt:
    answer *= tmp
print(answer)
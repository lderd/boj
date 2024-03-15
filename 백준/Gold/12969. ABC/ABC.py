import sys
n, k = map(int, input().split())
# dp[점수][A갯수][B갯수] = 만들어지는 문자열
# C갯수는 n-A갯수-B갯수
dp = [[[''] * (n+1) for _ in range(n+1)] for _ in range(k+1)]
dp[0][1][0] = 'A'
dp[0][0][1] = 'B'
dp[0][0][0] = 'C'
for i in range(2, n+1):
    tmp = [[[''] * (n+1) for _ in range(n+1)] for _ in range(k+1)]
    for s in range(k+1):
        for a in range(n+1):
            for b in range(n+1):
                now = dp[s][a][b]
                if now:
                    if s + a + b <= k and not tmp[s+a+b][a][b]:
                        tmp[s+a+b][a][b] = now + 'C'
                    if s + a <= k and b < n and not tmp[s+a][a][b+1]:
                        tmp[s+a][a][b+1] = now + 'B'
                    if a < n and not tmp[s][a+1][b]:
                        tmp[s][a+1][b] = now + 'A'
    dp = tmp
for a in range(n+1):
    for b in range(n+1):
        if dp[k][a][b]:
            print(dp[k][a][b])
            sys.exit()
print(-1)
'''
     빨         초         파     - 현재 색깔
  빨 초 파    빨 초 파     빨 초 파  - 시작 색깔
[[0, 89, 132], [86, 0, 143], [83, 97, 0]]

[[0, 110, 156], [16~, 0, 0], [0, 0, 0]]
'''
n = int(input())
dp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(n):
    a, b, c = map(int, input().split())
    tmp = [[0] * 3 for _ in range(3)]
    if i == 0:
        tmp = [[a, a, a], [b, b, b], [c, c, c]]
    elif i == 1:
        tmp = [[1000001, dp[1][1] + a, dp[2][2] + a], [dp[0][0] + b, 1000001, dp[2][2] + b], [dp[0][0] + c, dp[1][1] + c, 1000001]]
    else:
        tmp = [[min(dp[1][0], dp[2][0]) + a, min(dp[1][1], dp[2][1]) + a, min(dp[1][2], dp[2][2]) + a],
               [min(dp[0][0], dp[2][0]) + b, min(dp[0][1], dp[2][1]) + b, min(dp[0][2], dp[2][2]) + b],
               [min(dp[0][0], dp[1][0]) + c, min(dp[0][1], dp[1][1]) + c, min(dp[0][2], dp[1][2]) + c]]
    dp = tmp
answer = min(dp[0][1], dp[0][2], dp[1][0], dp[1][2], dp[2][0], dp[2][1])
print(answer)
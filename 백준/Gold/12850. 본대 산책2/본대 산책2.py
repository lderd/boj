d = int(input())
route = [[1, 2], [0, 2, 3], [0, 1, 3, 5], [1, 2, 4, 5], [3, 5, 6], [2, 3, 4, 7], [4, 7], [5, 6]]

tmp = [[0] * 8 for _ in range(8)]
for i in range(8):
    tmp[i][i] = 1
for _ in range(1000):
    ttmp = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for n in route[i]:
                ttmp[n][j] = (ttmp[n][j] + tmp[i][j]) % 1000000007
    tmp = ttmp

dp = [0] * 8
dp[0] = 1
time = 0
while time + 1000 <= d:
    time += 1000
    ttmp = [0] * 8
    for i in range(8):
        for j in range(8):
            ttmp[i] = (ttmp[i] + (dp[j] * tmp[i][j]) % 1000000007) % 1000000007
    dp = ttmp

for _ in range(time, d):
    ttmp = [0] * 8
    for i in range(8):
        for n in route[i]:
            ttmp[n] = (ttmp[n] + dp[i]) % 1000000007
    dp = ttmp
print(dp[0])
n = int(input())
scale = sorted(map(int, input().split()))
mod = 1000000007
answer = 0
ss = 0
m = 0
for i in range(n-2, -1, -1):
    ssum = ((ss*2) % mod + scale[i+1] % mod) % mod
    mul = ((m+1)*2-1) % mod
    answer += (ssum - mul * scale[i] + mod) % mod
    answer %= mod
    ss = ssum
    m = mul
print(answer)
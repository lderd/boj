n, k = map(int, input().split())
cnt = [1] * (n + 1)
for _ in range(k - 1):
    tmp = [1] + [0] * n
    for i in range(1, n + 1):
        tmp[i] = (tmp[i-1] + cnt[i]) % 1000000000
    cnt = tmp
print(cnt[n])
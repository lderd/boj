n, k = map(int, input().split())
cnt = [1] * (n + 1)
for _ in range(k - 1):
    tmp = [0] * (n + 1)
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j > n:
                break
            tmp[i + j] += cnt[i]
            tmp[i + j] %= 1000000000
    cnt = tmp
print(cnt[n])
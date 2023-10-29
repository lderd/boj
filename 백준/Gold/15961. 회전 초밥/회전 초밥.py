import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
sushi = [int(input()) - 1 for _ in range(n)]
sushi.extend(sushi[:k])
s = e = 0
cnt = [0] * d
cnt[c-1] += 1
answer = 1
tmp = 1
while e < n + k:
    plus = sushi[e]
    if cnt[plus] <= 0:
        tmp += 1
    cnt[plus] += 1
    if e - s + 1 > k:
        cnt[sushi[s]] -= 1
        if cnt[sushi[s]] <= 0:
            tmp -= 1
        s += 1
    if tmp > answer:
        answer = tmp
    e += 1
print(answer)
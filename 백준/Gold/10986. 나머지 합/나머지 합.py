n, m = map(int, input().split())
cnt = [0] * m
A = list(map(int, input().split()))
ssum = 0
answer = 0
for a in A:
    rest = a % m
    ssum = (ssum + rest) % m
    answer += cnt[ssum]
    cnt[ssum] += 1
    if ssum == 0:
        answer += 1
print(answer)
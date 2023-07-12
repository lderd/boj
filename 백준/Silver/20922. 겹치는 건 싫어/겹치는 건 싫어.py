n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * 100001
s = 0
e = 0
answer = 0
while e < n:
    cnt[arr[e]] += 1
    while cnt[arr[e]] > k:
        cnt[arr[s]] -= 1
        s += 1
    if e - s + 1 > answer:
        answer = e - s + 1
    e += 1
print(answer)
n, k = map(int, input().split())
a = list(map(int, input().split()))
answer = sum(a[:k])
s = 0
e = k
tmp = sum(a[:k])
while e < n:
    tmp += a[e]
    tmp -= a[s]
    s += 1
    e += 1
    if tmp > answer:
        answer = tmp
print(answer)
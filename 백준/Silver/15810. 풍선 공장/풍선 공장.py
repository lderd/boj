n, m = map(int, input().split())
staff = list(map(int, input().split()))
s = 0
e = m * max(staff)
while s <= e:
    mid = (s + e) // 2
    tmp = 0
    for i in staff:
        tmp += mid // i
    if tmp >= m:
        e = mid - 1
    else:
        s = mid + 1
print(s)
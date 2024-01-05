n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()
s = 0
e = 1000000000
while s <= e:
    mid = (s + e) // 2
    i = 0
    cnt = 1
    tmp = 1
    while i + tmp < n:
        if home[i+tmp] - home[i] >= mid:
            i += tmp
            tmp = 1
            cnt += 1
        else:
            tmp += 1
        if cnt >= c:
            break
    if cnt >= c:
        s = mid + 1
    else:
        e = mid - 1
print(e)
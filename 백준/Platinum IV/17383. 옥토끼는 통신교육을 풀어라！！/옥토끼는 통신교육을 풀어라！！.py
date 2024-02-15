n = int(input())
T = sorted(map(int, input().split()))
s = 1
e = 1000000000
while s < e:
    q = 0
    mid = (s + e) // 2
    flag = True
    for t in T:
        tmp = (t + mid - 1) // mid
        if q >= tmp - 1:
            q -= tmp - 1
            q += 1
        else:
            flag = False
            break
    if flag:
        if e == mid:
            break
        e = mid
    else:
        if s == mid:
            break
        s = mid
print(e)
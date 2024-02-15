n, l, w, h = map(int, input().split())
s = 0
e = min(l, w, h)
while s < e:
    a = (s + e) / 2
    cnt = (l // a) * (w // a) * (h // a)
    if cnt >= n:
        if s == a:
            break
        s = a
    else:
        if e == a:
            break
        e = a
print(s)
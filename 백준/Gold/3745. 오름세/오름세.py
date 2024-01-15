from bisect import bisect_left
while True:
    try:
        n = int(input())
        ps = list(map(int, input().split()))
        tmp = []
        l = 0
        for p in ps:
            i = bisect_left(tmp, p)
            if i >= l:
                tmp.append(p)
                l += 1
            else:
                tmp[i] = p
        print(l)
    except:
        break
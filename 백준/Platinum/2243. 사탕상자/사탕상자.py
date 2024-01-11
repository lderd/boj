import sys
input = sys.stdin.readline
n = int(input())
cnt = [0] * 1000001
for _ in range(n):
    a, *bc = map(int, input().split())
    if a == 1:
        b = bc[0]
        s = 1
        e = 1000000
        while s <= e:
            mid = (s + e) // 2
            idx = mid
            tmp = 0
            while mid > 0:
                tmp += cnt[mid]
                mid -= mid & -mid
            if tmp < b:
                s = idx + 1
            else:
                e = idx - 1
        print(s)
        while s <= 1000000:
            cnt[s] -= 1
            s += s & -s
    else:
        b, c = bc
        while b <= 1000000:
            cnt[b] += c
            b += b & -b
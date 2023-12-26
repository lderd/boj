import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
tree = [0] * (n + 1)
for _ in range(m):
    t, *abc = map(int, input().split())
    if t == 1:
        a, b, c = abc
        a += 1
        b += 2
        while a <= n:
            tree[a] ^= c
            a += a & (-a)
        while b <= n:
            tree[b] ^= c
            b += b & (-b)
    else:
        c, *_ = abc
        answer = arr[c]
        c += 1
        while c > 0:
            answer ^= tree[c]
            c -= c & (-c)
        print(answer)
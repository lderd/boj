import sys
from bisect import bisect_left
input = sys.stdin.readline
def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        p[b] = a
    else:
        p[a] = b


def find(a):
    if p[a] == a:
        return p[a]
    p[a] = find(p[a])
    return p[a]


n, k = map(int, input().split())
jewerly = list(list(map(int, input().split())) for _ in range(n))
bags = sorted(int(input()) for _ in range(k))
jewerly.sort(key=lambda x:[-x[1]])
p = list(range(k+1))
answer = 0
for i in range(n):
    m, v = jewerly[i]
    idx = bisect_left(bags, m)
    pidx = find(idx)
    if pidx == k:
        continue
    else:
        answer += v
        union(idx, pidx+1)
print(answer)